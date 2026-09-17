# DE MAKKELIJKSTE MANIER OM JE SITE ONLINE TE ZETTEN

Ik heb drie wegen naast elkaar getest. Hier staan ze van makkelijkst naar volledig.
Kies er één. Je hoeft niets af te maken wat je niet wil.

---

## WEG 1 — ÉÉN BESTAND, ZEVEN SECONDEN, GEEN INSTELLINGEN

**Wat je doet**

```text
1. Open:   app.netlify.com/drop
2. Klik op de knop "file" op die pagina (er is ook een knop "folder"; die heb je niet nodig).
3. Het venster van je computer opent. Kies één bestand:  deploy.zip
4. Klaar. Na ongeveer zeven seconden staat je site online, met een adres erbij.
```

**Wat ik zelf gemeten heb, met de echte website:**

```text
· Ik heb een zip met één pagina erin gekozen → NA 7 SECONDEN stond hij online.
· Er verscheen een adres van de vorm https://iets-leuks.netlify.app
· De pagina zegt: "Your project is live."
· Geen account nodig om dit te doen. Geen instellingen. Geen map kiezen.
```

**Wat er daarna nog moet, en waarom**

```text
· Een niet-geclaimde site is BEVEILIGD MET EEN WACHTWOORD en verdwijnt na ÉÉN UUR.
  Dat wachtwoord staat op je scherm, bijvoorbeeld "My-Drop-Site". Om de site aan iemand
  te kunnen geven moet je hem claimen. Dat is het punt hierna.
· Klik op "Claim this site". Je komt op een pagina met grote knoppen.
· Klik op "Sign up with GitHub". Kies daarna "Authorize".
  Je hebt al een GitHub-account, dus je hoeft geen nieuw account te maken en geen
  wachtwoord te bedenken. Daarna is je site blijvend, met https.
· Wat ik niet kon testen: wat er ná dat inloggen gebeurt — daar is jouw account voor nodig.
  Tot aan dat scherm heb ik het getest, en daar staat precies wat ik hierboven schrijf.
```

**Waarom dit de makkelijkste is:** één bestand kiezen in plaats van twaalf, geen
verborgen mappen, geen instellingenpagina, en in zeven seconden zie je resultaat.

**Nadeel eerlijk gezegd:** je site woont dan bij Netlify en niet in je eigen GitHub-repo.
Je repo blijft wel bestaan als je archief; later zetten we hem daar alsnog in als je wil.

---

## WEG 2 — IN JE EIGEN GITHUB, MET ÉÉN BESTAND

**De ontdekking:** je site heeft maar **één** bestand nodig. `index.html` bevat alles:
de speelvloer, de wizard, de demo, de teams, de profiler, het toepassen, het einde.
Er staat nergens een link naar de andere bestanden. Die zijn extra, geen noodzaak.

```text
1. Open:   github.com/guypeers-cmyk/Aiaccess/upload/main
2. Klik op "choose your files".
3. Kies in het venster ALLEEN:  index.html
   (een map openen en één bestand aanwijzen kan met één klik)
4. Klik onderaan op Commit changes.
5. Settings → Pages → Source: Deploy from a branch → main → / (root) → Save.
6. Wacht één minuut en open:  https://guypeers-cmyk.github.io/Aiaccess/
```

**Wat je dan nog hebt liggen voor later** (mag ook nooit): `dashboard.html`,
`chat-demo.html`, het kaartje, de stylesheet en de keuring. Elk daarvan kan er later bij,
één per keer, via dezelfde uploadpagina.

---

## WEG 3 — ALLES ERIN, ZOALS EERST (de volledige versie)

Zoals het in `ZET_OP_GITHUB.md` staat: alle twaalf bestanden, plus de keuring die na
elke push draait via de één-klik-link in `KEURING-LINK.txt`.

Kies deze als je het dashboard, de chat-demo en het kaartje er ook meteen bij wil hebben,
en de keuring die je waarschuwt als er iets fout gaat.

---

## WELKE KIES JE

```text
WIL JE HET SNEL ZIEN?                 → WEG 1. Zeven seconden, één bestand.
WIL JE HET IN JE EIGEN REPO?          → WEG 2. Eén bestand, geen verborgen mappen.
WIL JE ALLES, MET DE KEURING ERBIJ?   → WEG 3. Twaalf bestanden, zoals eerder beschreven.
```

**Ze kunnen alle drie naast elkaar bestaan.** Je mag WEG 1 doen om te kijken, en daarna
rustig WEG 3 afmaken. Er gaat niets verloren en er wordt niets dubbel gedaan.

---

## WAT ER IN `deploy.zip` ZIT

```text
index.html                        de site zelf — dit is de enige die echt nodig is
dashboard.html                    alle teams, alle subagenten, de beslisboom
chat-demo.html                    de demo van een gesprek
kaartje_stadhuis_waregem.html     een voorbeeld van een brief als kaartje
chat-accessibility.css            de grote letters, dikke randen, het donkere thema
controleer_site.py                de keuring, 8 controles, 0 fouten
.github/workflows/keuring.yml     de keuring die GitHub zelf draait na elke push
KEURING-LINK.txt                  één klik om die keuring toe te voegen
README.md · ZET_OP_GITHUB.md      uitleg
push.sh                           voor een helper, met git
```

Geen enkel bestand erin bevat een naam, een leeftijd, een ziekte of een diagnose.
Dat heb ik met de keuring nagemeten: **8 keuringen, 0 fouten.**
