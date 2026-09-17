#!/usr/bin/env python3
"""
CONTROLEER_SITE — de keuring die na elke push automatisch draait.
===============================================================
Draait zonder internet, zonder browser, zonder extra pakketten: alleen Python 3.

Wat het narekent op de pagina's die online staan:
  1. nooit typen            geen tekstvak, geen tekstgebied, geen keuzelijst
  2. zelfstandig            geen enkel bestand van buiten (geen cdn, geen font, geen plaatje van het web)
  3. raakvlak               de knopmaat staat op 64 px of meer
  4. geen gegevens          geen verboden woord, en geen woord in een verbod
  5. geen verrassing        geen {{ of {% die GitHub Pages kan aanpassen
  6. een keuze zegt wat ze doet   elke optie in de wizard heeft haar gevolg erbij
  7. de basis               taal, titel en scherminstelling op elke pagina
  8. geen dode link         elke #sprong op de pagina bestaat echt

Uitkomst: per keuring PASS of FAIL, en één totaalregel. Exitcode 1 als er iets faalt,
zodat GitHub de push rood maakt en jou een mailtje stuurt.
"""
import re
import sys
import pathlib

PAGINAS = ["index.html", "dashboard.html", "chat-demo.html", "kaartje_stadhuis_waregem.html"]
CSS = "chat-accessibility.css"
DOEL_PX = 64
VERBODEN = [
    "ziekte", "diagnose", "medicijn", "medicatie", "behandeling", "adres", "telefoon",
    "e-mail", "inkomen", "gezin", "werkgever", "rijksregister", "depress",
]
ONTKENNING = re.compile(r"(geen|nooit|zonder|verbied\w*)\s+(\w+\s+){0,3}%s")


def lees(naam):
    return pathlib.Path(naam).read_text(encoding="utf-8")


def keur_geen_typen(naam, html):
    fouten = []
    for m in re.finditer(r"<input\b[^>]*>", html, re.I):
        tag = m.group(0)
        soort = (re.search(r'type=["\']([^"\']+)', tag, re.I) or [None, "text"])[1]
        if soort.lower() not in ("checkbox", "radio", "button", "submit", "hidden"):
            fouten.append("%s: een tekstvak (%s) — de gebruiker mag nooit typen" % (naam, soort))
    for tag in ("textarea", "select"):
        if re.search(r"<%s\b" % tag, html, re.I):
            fouten.append("%s: een <%s> gevonden — dat vraagt typen of kiezen in een lijst" % (naam, tag))
    return fouten


def keur_zelfstandig(naam, html):
    fouten = []
    for m in re.finditer(r"<(?:script|img|iframe|link|source)\b[^>]*>", html, re.I):
        tag = m.group(0)
        if re.search(r'\b(?:src|href)\s*=\s*["\']https?://', tag, re.I):
            fouten.append("%s: haalt iets van buiten op — %s" % (naam, tag[:90]))
    for m in re.finditer(r"url\(\s*[\"']?(https?://[^)\"']+)", html, re.I):
        fouten.append("%s: een plaatje of font van buiten — %s" % (naam, m.group(1)[:60]))
    return fouten


def keur_raakvlak(css, html):
    """De knopmaat en de lettergrootte, in beide bestanden."""
    fouten = []
    gevonden = []
    for naam, tekst in (("chat-accessibility.css", css), ("index.html", html)):
        m = re.search(r"--(?:a11y-)?target\s*:\s*(\d+)px", tekst)
        if m:
            px = int(m.group(1))
            gevonden.append(px)
            if px < DOEL_PX:
                fouten.append("%s: de knopmaat is %d px, onder de grens van %d px" % (naam, px, DOEL_PX))
    if not gevonden:
        fouten.append("ik vind nergens een knopmaat (--target of --a11y-target)")
    maten = []
    for naam, tekst in (("chat-accessibility.css", css), ("index.html", html)):
        for var in ("--a11y-font-size", "--grootte"):
            m = re.search(re.escape(var) + r"\s*:\s*(\d+)px", tekst)
            if m:
                px = int(m.group(1))
                maten.append(px)
                if px < 24:
                    fouten.append("%s: %s staat op %d px, onder de grens van 24 px" % (naam, var, px))
    if not maten:
        fouten.append("ik vind nergens een lettergrootte")
    return fouten, (gevonden[0] if gevonden else 0)


PATRONEN = [
    ("een e-mailadres", re.compile(r"[\w.+-]+@[\w-]+\.[a-zA-Z]{2,}")),
    ("een telefoonnummer", re.compile(r"\+32[\s\d().-]{6,}|\b0\d{2}[\s/.-]?\d{2}[\s/.-]?\d{2}[\s/.-]?\d{2}\b")),
    ("een rekeningnummer", re.compile(r"\bBE\d{2}[\s]?\d{4}[\s]?\d{4}[\s]?\d{4}\b")),
    ("een rijksregisternummer", re.compile(r"\b\d{2}[.\s-]?\d{2}[.\s-]?\d{2}[.\s-]?\d{3}[.\s-]?\d{2}\b")),
    ("een geboortedatum", re.compile(r"geboorte\w*|geboren op", re.I)),
]
WOORDEN = [
    ("de naam van de gebruiker", re.compile(r"mijn naam is|gebruikersnaam\s*[:=]", re.I)),
    ("een patiënt- of cliëntaanduiding", re.compile(r"\bpati[eë]nt\w*|\bcli[eë]nt\w*", re.I)),
]


# Wat expliciet MAG, met de reden erbij. Alles wat hier niet in staat, is een fout.
TOEGESTAAN = {
    "056621211": "het publieke nummer van het stadhuis van Waregem, in een openbaar voorbeeld",
    "0566212 11": "het publieke nummer van het stadhuis van Waregem, in een openbaar voorbeeld",
}


def keur_geen_gegevens(naam, html):
    """Zoekt echte gegevens, geen woordenlijst: een e-mailadres, een nummer, een aanduiding."""
    fouten = []
    for uitleg, patroon in PATRONEN + WOORDEN:
        for m in patroon.finditer(html):
            gevonden = m.group(0)
            schoon = re.sub(r"[\s().-]", "", gevonden)
            if schoon in TOEGESTAAN or gevonden.strip() in TOEGESTAAN:
                continue
            stuk = html[max(0, m.start() - 45):m.end() + 25].replace("\n", " ").strip()
            fouten.append("%s: %s gevonden — ...%s..." % (naam, uitleg, stuk[:80]))
            break
    return fouten


def keur_geen_verrassing(naam, html):
    fouten = []
    if "{{" in html or "{%" in html:
        fouten.append("%s: er staat {{ of {% in de pagina — GitHub kan dat aanpassen" % naam)
    return fouten


def keur_gevolgen(html):
    """Elke optie van de wizard moet zeggen wat ze doet."""
    fouten = []
    blokken = re.findall(r"opties:\s*\[(.*?)\]\s*\}", html, re.S)
    if not blokken:
        return ["ik vind de opties van de wizard niet terug in index.html"]
    aantal = 0
    for blok in blokken:
        for stuk in re.split(r"\],\s*\[", blok):
            aantal += 1
            velden = re.findall(r"'([^']*)'|\bnull\b", stuk)
            if len(velden) < 3:
                fouten.append("een optie zonder gevolg-regel: %s" % stuk.strip()[:70])
    if aantal < 12:
        fouten.append("ik tel maar %d opties; de wizard hoort er minstens 12 te hebben" % aantal)
    return fouten, aantal


def keur_basis(naam, html):
    fouten = []
    if not re.search(r'<html[^>]*lang="nl"', html, re.I):
        fouten.append("%s: de taal (lang=nl) staat er niet in" % naam)
    if not re.search(r"<title>[^<]+</title>", html, re.I):
        fouten.append("%s: er is geen titel" % naam)
    if "name=\"viewport\"" not in html and "name='viewport'" not in html:
        fouten.append("%s: de scherminstelling (viewport) staat er niet in" % naam)
    return fouten


def keur_sprongen(naam, html):
    fouten = []
    doelen = set(re.findall(r'href="#([^"]+)"', html))
    hebben = set(re.findall(r'id="([^"]+)"', html))
    for d in sorted(doelen):
        if d and d not in hebben:
            fouten.append('%s: de link #%s wijst naar niets' % (naam, d))
    return fouten


def main():
    hier = pathlib.Path(__file__).resolve().parent
    import os
    os.chdir(hier)

    alles = {}
    for naam in PAGINAS:
        if not pathlib.Path(naam).exists():
            print("FAIL  %s ontbreekt" % naam)
            return 1
        alles[naam] = lees(naam)
    css = lees(CSS)

    uitslagen = []

    fouten = []
    for naam, html in alles.items():
        fouten += keur_geen_typen(naam, html)
    uitslagen.append(("nooit typen", fouten))

    fouten = []
    for naam, html in alles.items():
        fouten += keur_zelfstandig(naam, html)
    uitslagen.append(("zelfstandig (niets van buiten)", fouten))

    fouten, px = keur_raakvlak(css, alles['index.html'])
    uitslagen.append(("raakvlak %d px en letters vanaf 24 px" % px, fouten))

    fouten = []
    for naam, html in alles.items():
        fouten += keur_geen_gegevens(naam, html)
    uitslagen.append(("geen persoonsgegevens in de pagina", fouten))

    fouten = []
    for naam, html in alles.items():
        fouten += keur_geen_verrassing(naam, html)
    uitslagen.append(("geen verrassing voor GitHub", fouten))

    fouten, aantal = keur_gevolgen(alles["index.html"])
    uitslagen.append(("elke keuze zegt wat ze doet (%d opties)" % aantal, fouten))

    fouten = []
    for naam, html in alles.items():
        fouten += keur_basis(naam, html)
    uitslagen.append(("taal, titel en scherminstelling", fouten))

    fouten = []
    for naam, html in alles.items():
        fouten += keur_sprongen(naam, html)
    uitslagen.append(("geen dode link", fouten))

    print("=" * 66)
    print("KEURING VAN DE SITE — %s" % ", ".join(PAGINAS))
    print("=" * 66)
    totaal = 0
    for naam, fouten in uitslagen:
        totaal += len(fouten)
        print("%-6s %s" % ("PASS" if not fouten else "FAIL", naam))
        for f in fouten:
            print("       · %s" % f)
    print("-" * 66)
    if totaal == 0:
        print("UITKOMST: %d keuringen, 0 fouten. De site mag online." % len(uitslagen))
        return 0
    print("UITKOMST: %d keuringen, %d fouten. De site mag zo niet online." % (len(uitslagen), totaal))
    return 1


if __name__ == "__main__":
    sys.exit(main())
