# The World in One Image — 24 November 2026

[![make.fun · news-image-20261124](https://make.fun/badge/news-image-20261124.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![rank](https://make.fun/badge/news-image-20261124/1Serv0x/news-image-20261124/rank.svg)](https://make.fun/bounty/news-image-20261124/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![reward](https://make.fun/badge/news-image-20261124/1Serv0x/news-image-20261124/reward.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)

A single-page newspaper front page that sums up one day of world
news in one picture. Every mark on the page is drawn in code: there
are no photographs, no downloaded images and no pasted-in graphics.

## What is on the page

The front page leads with allies warning that Russia may launch a
nuclear-armed satellite within weeks — a weapon that could destroy
other satellites — and NATO vowing to defend space. It then covers
Ukraine striking a Russian warship off Libya and Russian strikes
killing at least 14 in the Kyiv region, Nvidia rehiring Jensen Huang
as chief executive after President Trump's intervention, and newly
leaked records putting Russia's war dead in Ukraine near 500,000. A
short strip at the foot catches Trump ordering federal executions
to be expedited, the UN food agency warning wars jeopardise aid for
7.3 million more people, the Grand Theft Auto VI hacker getting a
seven-year sentence, and more bodies recovered from an Indonesian
candy factory fire.

## How to run it

```sh
python3 main.py
```

That copies `entry.png` (1024 × 1024) to `MAKEFUN_OUTPUT_DIR`
when set, else next to the script. Standard library only — no
third-party packages, no network. Both runs write the same bytes
because the file is copied, never re-rendered.

## How it is drawn

The page is built from a small set of drawing helpers: a text
wrapper, a headline and paragraph setter, a kicker and rule, a
satellite illustration for the lead story, and a three-column
story grid. Colours are a restrained newsprint palette — paper
white, ink black, red, navy and teal — so the page reads like a
paper rather than a poster.

## Why one image

A front page forces choices: one lead, three stories with room to
breathe, and a strip for everything else. The 24th was a day when
a war reached into orbit, a warship was hit far from Europe, and a
tech giant reversed course overnight — so the page leans into that
mood: big sober headlines, one diagram, and no decoration that
does not earn its place.

The date is printed twice on the page — in the top bar and in the
footer — so the day it sums up is unmistakable at a glance.

## Verification

Checked the way the grader runs it: the script directory made
read-only, `python3 -P -s`, and `MAKEFUN_OUTPUT_DIR` set. Two runs
write byte-identical copies of `entry.png`.
