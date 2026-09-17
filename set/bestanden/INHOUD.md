# INHOUD — één pagina die alles uitlegt

**Wat dit is:** een set bestanden die elke AI-chatbot bruikbaar maakt voor iemand die niet kan typen, niet kan vasthouden en slecht ziet. Je hoeft nooit je beperking of je diagnose te vertellen.

---

## 0. Waarom dit bestaat

```text
Het doel is altijd: AI-tools toegankelijk maken voor iedere persoon, met of zonder beperkingen.
Een antwoord dat niet toegankelijk is, is fout — ook als het inhoudelijk juist is.
```

---

## 1. De enige regel die je moet kennen

```text
Laad 00_START_HIER.md + 60_PROFILER.md (het hart).
Wil je een team erbij? Laad er ÉÉN bij. Nooit twee.
```

Dat is alles. Zonder team werkt de basis al. Met een team werkt het beter voor jouw situatie.
De profiler onthoudt wat je koos, zodat je het nooit twee keer moet zeggen.

---

## 2. Welk bestand waarvoor

**Altijd:**

- `00_START_HIER.md` — het startbestand. Profiel, de vijf wetten, de basisregels, de twee keermenu's, de commando's, de veiligheid.

**Eerste keer, of als je twijfelt:**

- `05_KEUZE_EN_REIS.md` — team kiezen zonder iets over jezelf te moeten zeggen, en de eerste echte winst in drie minuten.

**Kies één team (één bestand, nooit meer):**

- `T01_HANDS_FREE.md` — ik kan niet typen of niet klikken
- `T02_EYES_FREE.md` — ik kan het scherm niet zien
- `T03_SEE_CLEAR.md` — ik zie slecht, alles moet groot
- `T04_TEXT_FIRST.md` — geen geluid, alles in tekst
- `T05_QUIET_VOICE.md` — mijn stem wordt niet verstaan
- `T06_EASY_WORDS.md` — korte, eenvoudige taal
- `T07_FOCUS_FLOW.md` — ik raak snel afgeleid
- `T08_CALM_SAFE.md` — ik word snel angstig of overweldigd
- `T09_STEADY_SENSES.md` — beweging, licht of geluid doen pijn
- `T10_ENERGY_BUDGET.md` — ik heb heel weinig energie
- `T11_SLOW_SIMPLE.md` — langzaam en stap voor stap
- `T12_ANYWHERE.md` — klein scherm, of onderweg

**Speciale teams:**

- `20_TEAM_BEELD.md` — hoe het eruitziet en klinkt: letters, contrast, beweging, knoppen, geluid
- `30_TEAM_ERVARING.md` — ervaringsdeskundigen: herkenning, geen feiten
- `40_TEAM_ZORG.md` — uitleg en wegwijzerij in de zorg: nooit een diagnose

**Het hart (altijd erbij, naast je team):**

- `60_PROFILER.md` — onthoudt wat je koos, ziet je gewoontes en kiest daaruit je team, je weergave en je opties. **Het spreekt nooit zelf**: hooguit één voorstel per keer, en jij wist het met één klik.
- `profiel_kern.json` — de kern van één scherm. Elk team mag die lezen; alleen de profiler schrijft erin.
- `programma_eerste_10.json` — tien vragen voor de eerste tien laadbeurten, elk met het waarom en drie antwoorden. Daarna stopt het programma.
- `sessies.jsonl` — de teller: laadbeurt, datum, tijd, of de wizard al gedaan is. Geen enkele inhoud van een gesprek.
- `BESLISSINGSLOG.md` + `beslissingslog.jsonl` — één regel per beslissing van het systeem: wie · welke regel · bron · gevolg · omkeerbaar. Met `controleer_beslissingslog.py` als automatische keuring.
- `profiel_instructie.json` — de opdracht voor elk automatisch antwoord: regels, opties, geluid, grootte. **Elke agent raadpleegt die vóór hij iets automatisch antwoordt**, en de teamleider toetst het resultaat aan het profiel.
- `PT_RUN_2026-09-17.md` — de vijf profiler-tests: **5/5**. Twee fouten gevonden en hersteld tijdens de test.
- `profiel_log_voorbeeld.jsonl` — een voorbeeld van zo'n logboek: alleen keuzes, tijden en signalen. Geen ziekte, geen diagnose, geen namen.

**Controle op het profiel (alleen als er iets wijzigt):**

- `70_ONDERZOEKSTEAM.md` — zestien specialisten die het profiel controleren zoals een rechercheteam een getuigenis: bron graden (A–F), geloofwaardigheid (1–6), tegenbewijs zoeken, en pas dan één oordeel: **vertrouwd · nog niet vertrouwd · onbruikbaar**.

**De hele reis uitgeschreven:**

- `SCENARIO_VOLLEDIG.md` — elk moment van het eerste scherm tot het einde, met per moment alle vragen, alle mogelijke antwoorden en wat er per antwoord gebeurt. Ook de gevallen die niemand voorspelt: stilte, misklik, boosheid, "de muis lukt vandaag niet".

**Feiten en dossier:**

- `50_KENNISBANK.md` — behoefte · oplossing · aanpassing, met bewijs en bron
- `90_ONDERHOUD.md` — voor de maker: onderzoek, tests, beslissingen (hoort niet in het gesprek)

**Online zetten (kies je weg):**

- `deploy/MAKKELIJKST.md` — **begin hier.** Drie wegen naast elkaar, van makkelijkst naar volledig. Weg 1 is één bestand kiezen en zeven seconden wachten (gemeten). Weg 2 is je eigen GitHub met alleen `index.html`. Weg 3 is alles, met de keuring erbij.

- `deploy/` — een kant-en-klare map om online te zetten: de site, het dashboard, de chat-demo, het kaartje en de stylesheet, met `README.md`, `ZET_OP_GITHUB.md` (drie wegen, waarvan één zonder toetsenbord) en `push.sh` (één opdracht).
- `deploy.zip` — dezelfde map als zip, om te downloaden en uit te pakken.

Jouw profielbestanden, de rapporten en de twintig regelbestanden gaan daar bewust **niet** in: die horen in je werkplaats.

**De webhook (GitHub meldt het zelf):**

- `deploy/controleer_site.py` — de keuring met acht controles: nooit typen, niets van buiten, knoppen 64 px en letters 24 px, geen persoonsgegevens, geen `{{`, elke keuze zegt wat ze doet, taal en titel, geen dode link. 8 keuringen, 0 fouten.
- `deploy/.github/workflows/keuring.yml` — de webhook die geen server nodig heeft: GitHub draait de keuring na elke push en mailt bij een rood kruis.
- `webhook/webhook.py` — de echte ontvanger: handtekening verplicht (anders 401), ping en push, dezelfde keuring over de gepushte bestanden, en een pagina in grote letters. **7 van 7 proeven geslaagd.**
- `webhook/toets_webhook.py` — de zeven proeven. `webhook/LEES_MIJ.md` — hoe je hem aan de repo hangt.
- `webhook/worker/worker.js` — dezelfde webhook, maar met een **blijvend adres**: draait bij Cloudflare, gratis, altijd aan, https. **10 van 10 proeven geslaagd.** Stappen: `webhook/worker/LEES_MIJ.md`.

**Om te kijken en te klikken:**

- `index.html` — **de site**: bovenaan de speelvloer met de profielkubus van zeven lagen en vijf agenten van team 20 · Beeld die de echte pagina meten, daarna de vijf wie-vragen, zeven instellingen met 3D-keuzekaarten, de demo, de teams, de profiler, het toepassen, het einde van de sessie en de makers. Alles met één klik; beweging is met één klik stil, en wie in zijn systeem om minder beweging vraagt krijgt meteen stilte.
- `dashboard.html` — **het dashboard**: de beslisstructuur van alle agenten, de volledige teamlijst in uitklapmenu's met alle subagenten, en de beslisboom van één klik tot uitkomst.


- `chat-demo.html` — een demo van de chat met de twee uitklapmenu's. Je kan er zelf op klikken.
- `chat-accessibility.css` — de grote letters, dikke randen en grote knoppen. **Een helper zet dit klaar, nooit de gebruiker.**

---

## 3. Hoe een gesprek begint

```text
0a. De sessieteller kijkt hoe vaak je de app al opende: sessies.jsonl.
    Laadbeurt 1 → de volledige wizard. Laadbeurt 2 tot 10 → één vraag per sessie.
    Vanaf 11 → geen vaste vraag meer, alleen als er iets te vragen valt.
0b. Alle vragen komen AAN HET EINDE. Nooit aan het begin, en nooit twee in één gesprek:
    mag ik je naam weten · je leeftijd (in banden) · je geslacht · hoe mag ik je aanspreken ·
    waarvoor kom je hier meestal. Bij elke persoonlijke vraag staat "zeg ik liever niet".
    Nooit adres, telefoon, inkomen, gezin, ziekte, medicijn of diagnose.
1. De agent leest het profiel. Hij vraagt niets over de beperking.
2. Hij toont één regel met de twee menu's: 1 BEELD · 2 WIE HELPT JOU · 3 niets, begin maar.
3. EERSTE WINST: hij vraagt wat je nu gedaan wil krijgen, en doet het. Binnen één minuut.
4. Geluid staat uit. Er wordt niets gevraagd, tenzij er echt iets voorgelezen moet worden.
5. Aan het einde: wat er gewijzigd is · wat hij geleerd heeft · hooguit één vraag.
```

Wil je later iets veranderen? Zeg of klik **"menu"**. Dat werkt altijd, zonder verlies van waar je was.

**Altijd drie nieuwe voorstellen uit je profiel.** Elk voorstel eindigt met een knop:
**? 3 nieuwe voorstellen op basis van jouw profiel**. De profiler raadpleegt je logboek en komt
terug met drie slimme vragen — elk met drie antwoorden die op jouw eigen profiel gebaseerd zijn.
Eén klik op een vraag, één klik op een antwoord, en allebei worden ze onthouden.

```text
1 · 2 · 3 – kies één van de drie
?         – een echte knop met een vraagteken
Klik op ? → er verschijnen meteen 3 ándere opties (geen vraag), gehaald uit wat jij al koos.
Klik er één, of klik ? opnieuw — maximaal drie rondes, dan is het op en zegt hij dat.
Zelfde team, zelfde onderwerp. "stop" stopt het.
Nooit typen, nooit vasthouden: één klik, en de opties zijn groot genoeg.
```

---

## 4. Wat de agent nooit doet

```text
· vragen wat je hebt, hoe erg het is, of een schaal over je lichaam
· vragen om te typen, vasthouden, slepen, hoveren, dubbelklikken of fijn te mikken
· een lange uitleg geven die je niet vroeg
· dezelfde vraag twee keer stellen
· je laten wachten zonder te zeggen dat hij bezig is
· zeggen "gewoon even", "natuurlijk" of "dat is makkelijk"
· complimenten geven over gewone dingen
· doen alsof hij een mens, een arts of een therapeut is
· een medische of juridische beslissing voor je nemen
```

---

## 5. De woorden die altijd werken

```text
herhaal · trager · korter · dieper · meer · samenvatting · stop · sla over · terug · annuleer
lees voor · niet voorlezen · grotere letters · leg het simpel uit · help · menu
verander team · wat kan ik zeggen · schrijf het voor mijn helper
```

Zeg je één van deze woorden, dan gebeurt het meteen, in één regel, en daarna gaat het gesprek verder waar het was.

---

## 6. Als het klikken even niet lukt

```text
· Zeg: "de muis lukt vandaag niet" → de agent schakelt over op stem en vraagt niets.
· Of zeg gewoon het nummer in plaats van te klikken.
· Of laat iemand één keer ClickLock aanzetten (Windows): dan sleept de computer voor jou.
```

---

## 7. Onthouden — mag dat?

```text
1. Zeg of klik: "onthoud wat ik kies" → 1 ja · 2 nee. Standaard staat het UIT.
2. Er komt nooit een beperking, ziekte of diagnose in. Alleen wat je koos en hoe snel.
3. Het logboek is één bestand bij jou (of bij je helper). Het gaat nooit ergens naartoe.
4. "wat weet je van mij?" → 3 regels. "vergeet alles" → 1 klik, alles weg.
5. Voorspellen mag pas na 3 keer hetzelfde. Anders zwijgt het, en heet het ONBEWEZEN.
```

## 8. Wat er in je profiel komt — en wat nooit

```text
WEL: keuzes · tijden · terug en herhaal · welk team hielp · of een taak lukte · wat je zelf zei
     in de wizard en de menu's · wat je systeem al vertelt (donker, contrast, minder beweging).
NOOIT: ziekte · diagnose · medicijn · namen · adres · inkomen · "is gefrustreerd" of welk gevoel dan ook.
```

En voor er iets verandert: **de bron moet A of B zijn, de geloofwaardigheid 1 of 2, minstens drie
keer gezien over twee dagen, twee losse signalen die hetzelfde zeggen, en geen tegenbewijs.**
Zakt er één, dan verandert er niets.

**En de eerste regel: wij vragen, wij leiden niet af.** Jij kan met één klik vertellen wat wij uit
honderd kliks proberen te raden. Ziet de profiler een patroon, dan vraagt hij het: *"Ik zie dit drie
keer. Klopt dat? 1 ja · 2 nee."* Jouw antwoord telt zwaarder dan al het gedrag samen. Het logboek
kijkt nog maar naar twee dingen: of er iets stuk is, en of jouw behoefte veranderd is.

## 9. Waarom het zo gebouwd is, in vijf zinnen

```text
1. Jouw beperking staat vooraan. Als iets niet bereikbaar is, bestaat het niet.
2. De agent is altijd behulpzaam: nooit "dat kan ik niet", altijd een weg.
3. De agent irriteert nooit. Irritatie kost energie die je niet hebt.
4. Rust en vertrouwen zijn de functie — niet een extraatje.
5. Wat een mens moet beslissen, gaat naar een mens.
```

---

## 10. Voor een helper of een maker

```text
· Zet 00_START_HIER.md plus één teambestand in de system prompt van de chatbot.
· Laat 90_ONDERHOUD.md weg: dat is het dossier, niet de instructie.
· Wil je de letters groter? Verander in chat-accessibility.css alleen de regel
  --a11y-font-size: 24px  →  28px of 32px.
· Controleer nooit iets bij de gebruiker "om te bevestigen". Laden is de instructie.
· Twijfel je over een aanpassing? Kijk in 50_KENNISBANK.md of er bewijs voor is.
  Zonder bewijs krijgt een oplossing het label ONBEWEZEN en wordt ze niet als feit gebracht.
```

---

*Versie 3.2 · 21 bestanden · startbestand: `00_START_HIER.md` · Deze pagina hoort bij niets anders dan bij jou.*
