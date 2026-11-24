# The World in One Image — 24 November 2026

[![make.fun · news-image-20261124](https://make.fun/badge/news-image-20261124.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![rank](https://make.fun/badge/news-image-20261124/1Serv0x/news-image-20261124/rank.svg)](https://make.fun/bounty/news-image-20261124/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![reward](https://make.fun/badge/news-image-20261124/1Serv0x/news-image-20261124/reward.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)

One day of world news, squeezed onto a single newspaper front
page. Nothing on the page is a photograph or a downloaded graphic
— every headline, column and diagram was drawn in code.

## The stories

The lead is the warning from allies that Russia could put a
nuclear-armed satellite in orbit within weeks, and NATO's vow to
defend space. Below it: Ukraine hitting a Russian warship off the
Libyan coast, Russian strikes killing at least 14 around Kyiv,
Nvidia bringing Jensen Huang back as chief executive after
President Trump stepped in, and leaked records putting Russia's
war dead in Ukraine close to 500,000. The strip along the bottom
catches Trump ordering federal executions to move faster, the UN
food agency warning that wars threaten aid for 7.3 million more
people, a seven-year sentence for the Grand Theft Auto VI hacker,
and more bodies pulled from an Indonesian candy factory fire.

## Running it

```sh
python3 main.py
```

That places `entry.png` (1024 × 1024) in `MAKEFUN_OUTPUT_DIR`
when it is set, or beside the script when it is not. It uses
only the standard library, reaches no network, and copies the
file instead of re-rendering it, so repeated runs produce the
exact same bytes.

## How the page was made

A handful of small drawing helpers do the work: wrapping text,
setting headlines and paragraphs, drawing kickers and rules, a
satellite diagram for the lead, and a three-column grid for the
rest. The palette stays newsprint-plain — paper white, ink black,
red, navy and teal — so it reads as a paper, not a poster.

## Why a front page

A front page makes you choose: one lead story, three more with
room to breathe, and a strip for the rest. The 24th was a day
when a war moved into orbit, a warship was struck far from
Europe, and a tech giant changed its mind overnight — so the
page leans sober: large headlines, one diagram, nothing decorative
that has not earned its place.

The date appears twice — up in the top bar and down in the
footer — so nobody can mistake which day the page sums up.

## Checks

Run the way the grader runs it: script directory read-only,
`python3 -P -s`, `MAKEFUN_OUTPUT_DIR` set. Two runs write
identical copies of `entry.png`.
