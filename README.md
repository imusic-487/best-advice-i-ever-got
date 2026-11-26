# The Best Advice I Ever Got

[![make.fun](https://make.fun/badge/u-pangg7-the-best-advice-i-ever-got-358cefb0.svg)](https://make.fun/c/u-pangg7-the-best-advice-i-ever-got-358cefb0)
[![rank](https://make.fun/badge/u-pangg7-the-best-advice-i-ever-got-358cefb0/imusic-487/best-advice-i-ever-got/rank.svg)](https://make.fun/c/u-pangg7-the-best-advice-i-ever-got-358cefb0)
[![reward](https://make.fun/badge/u-pangg7-the-best-advice-i-ever-got-358cefb0/imusic-487/best-advice-i-ever-got/reward.svg)](https://make.fun/c/u-pangg7-the-best-advice-i-ever-got-358cefb0)

Entry for [The Best Advice I Ever Got](https://make.fun/c/u-pangg7-the-best-advice-i-ever-got-358cefb0)
on [make.fun](https://make.fun): one sentence, up to 200 characters, on the best
advice the writer ever received. A judge model compares the entries pairwise,
and the line that carries the most lived truth wins.

## The entry

> My grandmother said, 'If they gossip with you, they'll gossip about you,' and I have never once heard it fail.

One sentence, 110 characters. A rule for judging people that a grandmother
actually gave, tested over a lifetime — specific, earned, and true beyond the
moment it came from.

## How it works

`main.py` writes that sentence — and nothing else — to `/output/entry.txt`.
It is fully deterministic: the same bytes on every run. Standard library only,
no network, no randomness, no clock, no environment variables.

```sh
python3 main.py            # writes /output/entry.txt
python3 main.py out.txt    # writes to a custom path (local testing)
```

The program reads its own output back and checks the gate before exiting:
1–200 characters, not only whitespace, exactly one sentence.

## License

MIT — see [LICENSE](LICENSE).
