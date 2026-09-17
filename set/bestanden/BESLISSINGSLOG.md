# BESLISSINGSLOG — één regel per beslissing

**Wat het is:** het logboek van het systeem, niet van de gebruiker. Elke beslissing die een agent
neemt of voorstelt komt er in één regel in. Zo is een fout terug te vinden bij de regel die hem
veroorzaakte.

**Wie schrijft erin:** de **beslissingslogger** (rol 7 in `60_PROFILER.md`). Alleen die.
**Wie leest het:** de maker, de helper, en het onderzoeksteam. Nooit de gebruiker als verrassing —
bij het sessie-einde hoort het in het rapport te staan.

---

## 1. Het formaat — precies zes velden

```json
{"ts":"2026-09-17T14:20:03","wie":"gebruiker","regel":"§F sluis 2 — de gebruiker beslist","bron":"A1","gevolg":"letters op 28 px toegepast","omkeerbaar":true}
```

```text
VELD        WAT ER IN KOMT                                    VOORBEELD
ts          tijd, ISO, tot op de seconde                      2026-09-17T14:20:03
wie         wie nam of voorstelde: gebruiker · profiler ·      gebruiker
            teamleider T03 · onderzoeksteam · sessieteller
regel       welke regel uit de set dit veroorzaakte            §F sluis 2 — de gebruiker beslist
            (met § erbij, zodat je hem kan opzoeken)
bron        betrouwbaarheid van de bron, A–F + 1–6             A1 · B2 · C3 · F6
gevolg       wat er gebeurde, in één regel, in gewone taal     letters op 28 px toegepast
omkeerbaar  ja of nee — kan de gebruiker dit terugdraaien?     true
```

**Zes velden. Niet zeven, niet vijf.** Mist er één, dan is de regel onbruikbaar en telt hij niet.

---

## 2. De regels van dit log

```text
1. ÉÉN REGEL PER BESLISSING. Ook als er niets gebeurde: "geen voorstel" is ook een beslissing.
2. GEEN PERSOONSGEGEVENS. Geen naam, geen adres, geen telefoon, geen inkomen, geen gezin.
   Geen ziekte, geen diagnose, geen medicijn, geen lichaamsdeel.
3. GEEN GEVOEL. Nooit "is gefrustreerd", "is bang", "is verward". Alleen gedrag en gevolg.
4. DE BRON IS VERPLICHT. Zonder broncode weet je niet of een regel iets mocht veranderen.
5. ELKE WIJZIGING IS OMKEERBAAR. Staat er "false", dan had de wijziging niet mogen doorgaan.
6. WAT NIET IN HET LOG MAG, BESTAAT NIET — ook niet als gedachte. (Dat is dezelfde regel als in
   het profiel_log.)
7. HET LOG IS VAN DE GEBRUIKER. "Wat heb je besloten?" geeft drie regels. "Vergeet het" wist het.
8. MAXIMAAL ÉÉN OPEN VRAAG PER SESSIE. Staat er een tweede, dan is er iets fout gegaan — en dat
   zie je terug in de controle.
```

---

## 3. De controleur — `controleer_beslissingslog.py`

```text
Draai:   python3 controleer_beslissingslog.py beslissingslog.jsonl
Doet:    leest elke regel en meldt wat er fout is
Meldt:   · ontbrekende velden
         · een broncode die geen A–F met 1–6 is
         · een wijziging die niet omkeerbaar is
         · verboden woorden (ziekte, diagnose, adres, telefoon, inkomen, gevoel)
         · meer dan één open vraag in dezelfde sessie
```

Zo weet je met één commando of het systeem zich aan zijn eigen regels houdt — zonder dat iemand
het log hoeft te lezen. De uitkomst is een getal, geen mening.

---

## 3b. In de site schrijft het zichzelf — getest op 17-09-2026

```text
TIEN MOMENTEN WAAROP DE SITE EEN REGEL SCHRIJFT
 1 de analyse van de profiler          wie: profiler · welke regel: §5 en §21
 2 de vraag die gesteld wordt          wie: profiler · "vraag gesteld: …"
 3 het antwoord van de gebruiker       wie: gebruiker · bron A1
 4 een aanname die ingetrokken wordt   wie: gebruiker · "wordt niet opnieuw geprobeerd"
 5 een toegepaste instelling           wie: gebruiker · bron A1
 6 het terugdraaien van een wijziging  wie: gebruiker · "vorige stand hersteld"
 7 de teamkeuze                        wie: gebruiker · §8 één team tegelijk
 8 elke ronde van de ?-knop            wie: profiler · ook als het geweigerd wordt (rondes op)
 9 elk antwoord uit de wie-vragen      wie: gebruiker · overslaan wordt ook gelogd
10 elke keuze uit de instellingen      wie: gebruiker · deel B van de wizard
```

**De keuring zit ook in het scherm.** De knop "Keur het beslissingslog" doet hetzelfde als het
Python-script: ontbrekende velden · een broncode die geen A–F met 1–6 is · een wijziging die niet
omkeerbaar is · een verboden woord · meer dan één open vraag in dezelfde sessie.

**Getest met vijf opzettelijke fouten — alle vijf gevonden:**

```text
regel 1  wijziging die niet omkeerbaar was          → gemeld
regel 2  broncode Z9 (bestaat niet)                 → gemeld
regel 3  het woord "bang" in een gevolg             → gemeld
regel 4  een veld dat ontbrak (ts)                   → gemeld
regel 5  twee open vragen in dezelfde sessie         → gemeld
En de ontkenning werd niet vals gemeld: "geen ziekte, geen gevoel" passeert terecht.
```

## 4. Waarom dit bestaat, in drie zinnen

```text
1. Zonder dit log is een fout niet terug te vinden: zat het in de profiler, in de teamleider,
   in het onderzoeksteam of in de regel zelf?
2. Onderzoek naar systemen met meerdere agenten noemt observability vanaf dag één als vereiste,
   juist omdat een fout in de overdracht kan zitten en niet in het antwoord.
3. Het log maakt van "wij denken dat het goed gaat" een uitspraak die je kan controleren:
   hoeveel beslissingen, welke bron, hoeveel omkeerbaar, en hoeveel vragen per sessie.
```

---

## 5. Wat er nooit in komt — dezelfde verboden lijst als overal

```text
geen naam · geen adres · geen telefoon · geen e-mail · geen inkomen · geen gezin · geen werkgever
geen ziekte · geen diagnose · geen medicijn · geen behandeling · geen lichaamsdeel · geen foto
geen gevoel · geen score over een persoon · geen cijfer dat iemand beoordeelt
```

*Onderdeel van de set. Zie `60_PROFILER.md` §24 voor de rol die dit log schrijft.*
