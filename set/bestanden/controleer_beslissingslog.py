#!/usr/bin/env python3
"""controleer_beslissingslog.py — keurt het beslissingslog tegen de regels van de set.

Gebruik:  python3 controleer_beslissingslog.py beslissingslog.jsonl
Uitvoer:  een kort rapport met getallen, en per fout de regel en het veld.
"""

import json
import re
import sys

VERPLICHT = ["ts", "wie", "regel", "bron", "gevolg", "omkeerbaar"]
BRON = re.compile(r"^[A-F][1-6]$")
WIJZIGING = ("toegepast", "gewijzigd", "gezet", "ingetrokken", "hersteld", "verwijderd")
VERBODEN = [
    "ziekte", "diagnose", "medicijn", "medicatie", "behandeling", "adres", "telefoon",
    "e-mail", "inkomen", "gezin", "werkgever", "rijksregister", "gevoel", "gefrustreerd",
    "bang", "verward", "verdrietig", "depress",
]


def lees(pad):
    regels = []
    with open(pad, encoding="utf-8") as f:
        for nr, regel in enumerate(f, 1):
            regel = regel.strip()
            if not regel:
                continue
            try:
                regels.append((nr, json.loads(regel)))
            except json.JSONDecodeError as fout:
                regels.append((nr, {"__fout__": str(fout)}))
    return regels


def controleer(regels):
    fouten = []
    vragen_per_sessie = {}
    sessie = 0

    for nr, r in regels:
        if "__fout__" in r:
            fouten.append((nr, "geen geldige JSON", r["__fout__"]))
            continue

        for veld in VERPLICHT:
            if veld not in r:
                fouten.append((nr, "veld ontbreekt", veld))

        if "bron" in r and not BRON.match(str(r["bron"])):
            fouten.append((nr, "broncode is geen A–F met 1–6", r["bron"]))

        tekst = " ".join(str(r.get(k, "")) for k in ("regel", "gevolg")).lower()
        for woord in VERBODEN:
            # een ontkenning is geen overtreding: "geen ziekte", "nooit ziekte", "zonder ziekte"
            if re.search(r"(geen|nooit|zonder)\s+\w{0,12}\s?" + re.escape(woord), tekst):
                continue
            if woord in tekst:
                fouten.append((nr, "verboden woord", woord))

        gevolg = str(r.get("gevolg", "")).lower()
        if any(w in gevolg for w in WIJZIGING) and r.get("omkeerbaar") is not True:
            fouten.append((nr, "wijziging die niet omkeerbaar is", gevolg))

        if "sessie" in r:
            sessie = r["sessie"]
        if r.get("wie") == "profiler" and gevolg.startswith("vraag gesteld"):
            vragen_per_sessie[sessie] = vragen_per_sessie.get(sessie, 0) + 1

    for s, n in vragen_per_sessie.items():
        if n > 1:
            fouten.append((0, "meer dan één open vraag in sessie " + str(s), str(n) + " vragen"))

    return fouten


def main():
    pad = sys.argv[1] if len(sys.argv) > 1 else "beslissingslog.jsonl"
    regels = lees(pad)
    fouten = controleer(regels)

    per_wie = {}
    per_bron = {}
    omkeerbaar = 0
    for _, r in regels:
        per_wie[r.get("wie", "?")] = per_wie.get(r.get("wie", "?"), 0) + 1
        per_bron[r.get("bron", "?")] = per_bron.get(r.get("bron", "?"), 0) + 1
        if r.get("omkeerbaar") is True:
            omkeerbaar += 1

    print("BESLISSINGSLOG — CONTROLE")
    print("bestand:", pad)
    print("regels:", len(regels))
    print("omkeerbaar:", str(omkeerbaar) + "/" + str(len(regels)))
    print("per wie:", per_wie)
    print("per bron:", per_bron)
    print("fouten:", len(fouten))
    for nr, wat, detail in fouten:
        print("  regel", nr, "|", wat, "|", detail)
    if not fouten:
        print("  geen — het log houdt zich aan de regels")
    return 0 if not fouten else 1


if __name__ == "__main__":
    sys.exit(main())
