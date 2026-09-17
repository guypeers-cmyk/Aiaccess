# DE SITE ONLINE ZETTEN — JOUW STAPPEN

```text
Jouw repo:      github.com/guypeers-cmyk/Aiaccess   (bestaat al, is nu nog leeg)
Jouw adres:     https://guypeers-cmyk.github.io/Aiaccess/
Wat er nog moet: de bestanden erin zetten, en Pages één keer aanzetten.
```

Ik heb je repo nagekeken: hij bestaat, hij staat op openbaar, en er zit nog niets in.
De site is nog niet aan — dat moet één keer in de website zelf. Hieronder staat alles, in volgorde.

---

## WEG 1 — DE BESTANDEN ERIN ZETTEN (zonder slepen)

De regel van dit systeem is: **één korte klik, nooit slepen of vasthouden**. Daarom staat hier
vooraan de weg zonder slepen. Slepen mag ook — maar het hoeft niet.

```text
1.  Log in op GitHub en open:  https://github.com/guypeers-cmyk/Aiaccess/upload/main

2.  Klik op de knop "choose your files" (er staat ook een sleepvak, dat mag je negeren).

3.  Het venster van je computer opent. Ga naar de map die je uit deploy.zip hebt uitgepakt,
    druk op Ctrl+A (alles selecteren), en klik Openen.

4.  De bestanden staan nu in de lijst op de pagina. Klik onderaan op Commit changes.
    Wacht tien seconden.

5.  De keuring erbij zetten — dat is één bestand in een verborgen map, en daarom één klik:
    klik op de link hieronder. De pagina opent met de naam en de hele inhoud al ingevuld.
    Je hoeft alleen nog onderaan op Commit changes te klikken.

       [de link staat in deploy/KEURING-LINK.txt — open dat bestand en klik hem aan]

6.  Ga daarna naar Settings → Pages → Source: Deploy from a branch → main → / (root) → Save.

7.  Wacht één minuut en open:  https://guypeers-cmyk.github.io/Aiaccess/
```

**Waarom die link in een apart bestand staat.** De link is ruim 2000 tekens: daarin zit het hele
keuringsbestand, klaar om te plakken. Zo hoeft er niets getypt of gesleept te worden — ook de map
`.github` niet, die je computer normaal verstopt. Open `deploy/KEURING-LINK.txt`, en klik of plak
de link in je browser.

**Zie je die map `.github` wel?** Dan mag je hem ook gewoon meeslepen of met de rest mee kiezen
(Windows: Beeld → Verborgen items · Mac: Cmd+Shift+punt). Dan is de link niet nodig.

## DE KEURING AANZETTEN — DIT IS JOUW WEBHOOK

Je koos route 1: de keuring die zichzelf draait. Die heeft **geen adres** nodig en kan niet uitvallen,
want GitHub draait hem zelf na elke push. Hij zit al in de zip.

**Wat je daarna ziet**

```text
· Op github.com/guypeers-cmyk/Aiaccess/actions staat bij elke push een keuring.
· Groen vinkje = alles in orde. Rood kruis = je krijgt een mailtje van GitHub.
· Klik op de keuring → onderaan de pagina staat het volledige verslag, in gewone taal.
· Wat hij narekent: nooit typen · niets van buiten · knoppen 64 px en letters 24 px ·
  geen persoonsgegevens · geen {{ die GitHub kan aanpassen · elke keuze zegt wat ze doet ·
  taal en titel · geen dode link.
```

**Hoe je hem mee-uploadt — twee manieren. Eén ervan lukt altijd.**

```text
WEG A · SLEPEN (als je verborgen bestanden kan zien)
  In de zip zit een map ".github". Die begint met een punt, dus je computer verstopt hem.
  · Windows: open de map, klik bovenin op Beeld → vink "Verborgen items" aan.
  · Mac: druk in de map op  Cmd + Shift + punt.
  Nu zie je .github. Sleep hem mee met de rest van de bestanden. GitHub maakt de mappen zelf aan.

WEG B · TWEE KEER PLAKKEN (als je hem niet ziet, of als slepen niet lukt)
  1. Open je lege repo en klik op "creating a new file" (of Add file → Create new file).
  2. In het vak voor de bestandsnaam plak je deze hele regel:
         .github/workflows/keuring.yml
     (de schuine strepen maken vanzelf de mappen aan)
  3. Plak in het grote vak de inhoud van keuring.yml die in de zip zit (map .github/workflows).
  4. Klik onderaan op Commit changes.

LUKT GEEN VAN BEIDE? Sla de keuring over. De site werkt ook zonder. Zeg het tegen mij en ik loop
het met je door, of ik kijk het voor je na zodra de site online staat.
```

## WEG 2 — MET GIT, IN ÉÉN OPDRACHT (voor een helper)

```text
1.  Pak deploy.zip uit en open een terminal in die map.

2.  Typ:  bash push.sh

    Het script gebruikt automatisch jouw repo: git@github.com:guypeers-cmyk/Aiaccess.git
    Het maakt de repo klaar in de map, legt alles vast, en verstuurt het.
    Git vraagt de eerste keer om een naam en een e-mailadres: invullen, daarna nooit meer.

3.  Weigert SSH met "Permission denied (publickey)"? Dan heeft deze computer nog geen sleutel.
    Maak een token: github.com/settings/tokens → Generate new token (classic) → vinkje bij "repo".
    Draai daarna:  bash push.sh https://github.com/guypeers-cmyk/Aiaccess.git
    en plak de token waar om een wachtwoord gevraagd wordt.

4.  Daarna nog één keer in de website: Settings → Pages → Deploy from a branch → main → / (root) → Save.
    Het script kijkt op het einde zelf of de site al leeft en zegt het je.
```

**Het script forceert nooit.** Staat er al iets in de repo, dan stopt het en zet het twee keuzes op het
scherm. Dat is met een namaak-GitHub getest: nieuw werk erbij gaat goed, en een botsing wordt netjes
geweigerd in plaats van overschreven.

---

## ALS HET NIET WERKT — DE VIJF DINGEN DIE HET VAAKST MISGAAN

```text
1. "404 — There isn't a GitHub Pages site here."
   Je bent nog niet klaar met stap 5 tot 9 van WEG 1. Soms duurt het twee minuten; ververs één keer.

2. De pagina is leeg, of ik zie alleen een lijst met bestanden.
   Kijk in de LIJST van je repo: staat index.html daar direct tussen, of zit hij in een mapje?
   Zit alles in een mapje, klik dan in die map op "Add file" → "Upload files" en sleep de
   bestanden nog één keer — nu naar de hoofdmap.

3. Ik zie nog de oude versie.
   Ctrl+F5, of een nieuw tabblad. GitHub bouwt de site elke keer opnieuw; dat duurt ongeveer een minuut.

4. De opmaak is weg, het is één lap tekst.
   Dan zijn de bestanden zonder hun volledige naam geüpload. De naam moet eindigen op
   .html of .css (index.html, dashboard.html, chat-demo.html, kaartje_stadhuis_waregem.html,
   chat-accessibility.css).

5. Ik zie geen .nojekyll in de lijst.
   Niet erg. Dat bestand is een extraatje voor GitHub; de site werkt er ook zonder. Ik heb
   gecontroleerd dat er niets in de pagina's staat dat GitHub zou aanpassen.
```

---

## WAT ER ONLINE GAAT, EN WAT NIET

```text
MAG WEL MEE:    index.html · dashboard.html · chat-demo.html · kaartje_stadhuis_waregem.html ·
                chat-accessibility.css · README.md · dit stappenplan · push.sh

BLIJFT PRIVÉ:   profiel_kern.json · profiel_log_mijn_kliks.jsonl · sessies.jsonl ·
                beslissingslog.jsonl · PT_RUN · TEGENSPRAAK · PROFIEL_GRADING ·
                AAS_EVALUATIE_EN_STAPPEN · de twintig regelbestanden
                (00_START_HIER.md, T01–T12, 60_PROFILER.md, …)

WAAROM:         daar staat wat jij klikte, wat het systeem besloot en hoe jouw profiel eruitziet.
                Een openbare site is voor iedereen leesbaar, en GitHub Pages blijft openbaar —
                ook als je de repo later op privé zet.

CONTROLE:       ik heb de vier pagina's die online gaan nagekeken op de verboden woorden
                (ziekte, diagnose, medicijn, adres, telefoon, inkomen, gezin, werkgever).
                Ze komen alleen voor in de regels die ze juist VERBIEDEN — nergens als iets
                over jou. Er staat geen naam, geen leeftijd, geen ziekte in.
```

---

## LATER IETS AANPASSEN

```text
1.  Open op GitHub het bestand dat je wil wijzigen (bijvoorbeeld index.html).
2.  Klik rechtsboven in dat bestand op het potlood.
3.  Pas aan. Klik daarna op Commit changes.
4.  Ongeveer één minuut later staat het op de site.
```

---

## EN DAN?

```text
Zeg het als je klaar bent met slepen. Dan kijk ik of je site echt leeft, of alle vier de
pagina's het doen, en of de speelvloer online net zo werkt als hier. Dat kost jou niets:
ik kijk gewoon naar het adres.
```
