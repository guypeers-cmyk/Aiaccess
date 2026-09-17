# WAT JE DEELT — EN WAARMEE

Je site en je set staan in de repo `guypeers-cmyk/Aiaccess`. Hieronder staat wat waarvoor dient.

## Kort, als de site eenmaal online is

```text
DE SITE        https://guypeers-cmyk.github.io/Aiaccess/
HET DASHBOARD  https://guypeers-cmyk.github.io/Aiaccess/dashboard.html
DE SET         https://guypeers-cmyk.github.io/Aiaccess/set/
ALLE BESTANDEN https://guypeers-cmyk.github.io/Aiaccess/set/aas.zip
```

## Nu al, zonder dat je iets aanzet

```text
DE BESTANDEN INZIEN   github.com/guypeers-cmyk/Aiaccess
DE SET OP GITHUB      github.com/guypeers-cmyk/Aiaccess/tree/main/set
WAT JE IEMAND STUURT   het bestand set/aas.zip uit die map (rechtsboven: Download raw file)
                       of: deploy.zip, dat in je werkplaats klaarstaat
```

## Vijf seconden testen zonder instellingen — en waarom het niet je deel-link is

```text
Werkt wel:  https://rawcdn.githack.com/guypeers-cmyk/Aiaccess/main/index.html
Maar:       een bezoeker krijgt EERST een waarschuwingspagina van die dienst te zien
            ("One more step … avoid entering passwords"). Voor deze doelgroep is dat
            precies verkeerd: een extra klik en een bange boodschap.
Dus:        alleen om zelf even te kijken, niet om te delen.
```

## Twee dingen die jij nog moet doen (elk twee minuten)

```text
A. PAGES AANZETTEN in de website
   github.com/guypeers-cmyk/Aiaccess/settings/pages
   → Source: Deploy from a branch → Branch: main → / (root) → Save
   Daarna publiceert de workflow de site bij elke push, zonder dat je nog iets klikt.

B. OF: EEN KLASSIEK TOKEN, DAN DOE IK HET
   github.com/settings/tokens/new  (dat is de klassieke soort, niet de fijnmazige)
   → Note: aiaccess deploy · Expiration: 7 days · vink aan: repo en workflow
   → Generate token → plak hem hier
   Let op: een klassiek token is breder dan een fijnmazig token. Trek hem direct in
   als ik klaar ben: github.com/settings/tokens → Delete.

C. OF: ZONDER GITHUB PAGES, BIJ NETLIFY (werkt vandaag, met wachtwoord op de proefversie)
   app.netlify.com/drop → knop "file" → kies deploy.zip → na ±7 seconden staat er een link
   → "Claim this site" → "Sign up with GitHub" → je site blijft, met https
```

## Wat er in de set zit, en wat niet

```text
WEL:   de site (speelvloer, wizard, demo, dashboard, kaartje) · 23 leesbare pagina's
       alle regelbestanden om te downloaden · een LEEG profielsjabloon · licentie (CC BY 4.0)
NIET:  jouw profiel (kern, logboek, sessies, beslissingslog) · je werkdossier
       (onderhoud, evaluatie, grading, tegenspraak, PT-run) · je naam, gemeente of token
```
