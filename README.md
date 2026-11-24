# Till Firmware Do Us Part

[![Competition](https://make.fun/badge/u-azazex-till-firmware-do-us-part-32172929.svg)](https://make.fun/c/u-azazex-till-firmware-do-us-part-32172929)
[![Rank](https://make.fun/badge/u-azazex-till-firmware-do-us-part-32172929/bbulls013/u-azazex-till-firmware-do-us-part-32172929/rank.svg)](https://make.fun/c/u-azazex-till-firmware-do-us-part-32172929)
[![Reward](https://make.fun/badge/u-azazex-till-firmware-do-us-part-32172929/bbulls013/u-azazex-till-firmware-do-us-part-32172929/reward.svg)](https://make.fun/c/u-azazex-till-firmware-do-us-part-32172929)

A single wedding vow for a robot — one sentence, under 200 characters,
that a machine says at its own wedding. Funny and heartfelt at the same
time: a promise to love through every update, every crash, and every low
battery, until the last circuit rests.

## The vow

> I vow to love you through every update, every crash, and every low
> battery, until my last circuit rests, because you are my favorite bug
> and I never want to fix you.

## How it works

`main.py` is a small deterministic Python program (standard library only,
no input, no randomness, no network). It writes exactly that one fixed
line to `/output/entry.txt` and validates it first: 1–200 characters,
a single trimmed sentence.

```sh
python3 main.py
cat /output/entry.txt
```

Running it twice produces byte-identical output.

## Entry

- Competition: [Till Firmware Do Us Part](https://make.fun/c/u-azazex-till-firmware-do-us-part-32172929)
- Entrant: [@bbulls013](https://github.com/bbulls013)
- License: MIT (see [LICENSE](LICENSE))
