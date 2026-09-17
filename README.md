# Toegankelijke AI — de site

Deze site laat zien hoe één set regels elke AI-chatbot bruikbaar maakt voor wie niet kan typen,
niet kan vasthouden of slecht ziet. Eén korte klik per keuze, nooit een diagnose, en een antwoord
dat niet toegankelijk is telt als fout — ook als het inhoudelijk juist is.

## Wat er in deze map staat

- `index.html` — **de site.** Begin hier. Bovenaan de speelvloer: je profiel in zeven lagen, en vijf
  agenten van team Beeld die de echte pagina meten. Daarna de vragen, de demo, de teams, de profiler,
  het toepassen en het einde van de sessie.
- `dashboard.html` — alle teams, alle subagenten en de beslisboom van één klik tot uitkomst.
- `chat-demo.html` — de demo van een gesprek met de twee uitklapmenu's.
- `kaartje_stadhuis_waregem.html` — een voorbeeld van een brief die als kaartje terugkomt.
- `chat-accessibility.css` — de grote letters, dikke randen, grote knoppen en het donkere thema.

Alles is zelfstandig: geen externe bestanden, geen internet nodig, geen reclame, geen tracking.
Je mag de pagina's los openen, ook zonder server.

## Online zetten

Deze map staat klaar voor **github.com/guypeers-cmyk/Aiaccess**.
Zie **`ZET_OP_GITHUB.md`** — slepen in de browser kan volledig zonder typen, en met `push.sh`
gaat het in één opdracht. De site komt op **https://guypeers-cmyk.github.io/Aiaccess/**.

## Wat hier bewust NIET in staat

Deze map is bedoeld om openbaar te zijn. Daarom staan jouw werkbestanden er niet in:

- `profiel_kern.json`, `profiel_log_mijn_kliks.jsonl`, `sessies.jsonl`, `beslissingslog.jsonl`
- de rapporten (`PT_RUN`, `TEGENSPRAAK`, `PROFIEL_GRADING`, `AAS_EVALUATIE_EN_STAPPEN`)
- de set van twintig regelbestanden (`00_START_HIER.md`, `T01`–`T12`, `60_PROFILER.md`, enzovoort)

Daar staat wat jij klikte, wat het systeem besloot en hoe jouw eigen profiel eruitziet. Dat hoort in
je werkplaats, niet op een openbare site. Wil je de set er toch bij, zeg het dan — dan zet ik er een
schone versie van klaar zonder profielgegevens.

## Aanpassen

Je kan elk bestand rechtstreeks op GitHub bewerken: open het bestand, klik op het potlood, typ,
en klik op **Commit changes**. Ongeveer een minuut later staat het op de site.
