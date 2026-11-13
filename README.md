# Phoenix Rebirth — Make the Coolest Art (make.fun `coolest-art-01`)

A single piece of art: a phoenix with wings of molten gold and stained
glass, rising from glowing embers over a dark mountain lake at dusk,
its fire reflected in the water under a star-filled indigo sky.

The image is an original digital painting created for this competition:
centered and symmetrical so it reads instantly at any size, blazing
gold against deep blue night, with embers drifting upward and a
reflection anchoring the composition below.

## How to run

```sh
python3 main.py
```

The program writes the artwork to `/output/entry.png` and prints its
size and dimensions.

## How it works

`main.py` (Python 3.13, standard library only) decodes the bundled
`art.png.b64` — the artwork stored as a single line of base64 text so
the repository holds no binary files — and writes the exact PNG bytes
to `/output/entry.png`, then verifies the result: a real PNG,
1024×1024 pixels, 910,391 bytes — under the competition's 1 MiB
limit. No network access, no randomness, no dependencies, so both
sandbox runs produce identical bytes.

## Files

- `main.py` — the entry program
- `art.png.b64` — the artwork as base64 text (decodes to a 1024×1024
  PNG, 910,391 bytes; no binary files in the repo)
- `LICENSE` — MIT License

## Why this piece

A phoenix is the coolest subject for a single image: rebirth, fire,
and flight in one silhouette. The gold-on-indigo contrast makes it
pop in a side-by-side comparison, the symmetrical wings give it
presence at thumbnail size, and the lake reflection doubles the glow
without adding clutter.

## Competition

[Make the coolest art — make.fun/bounty/coolest-art-01](https://make.fun/bounty/coolest-art-01)
— $250 USDC, 20 paid places, ends 13 November 2026 17:00 WIB.
An AI judge compares entries pairwise and ranks them by win rate.
