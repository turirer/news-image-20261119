# Sum up 19 November's world news in one image

Entry for make.fun competition `news-image-20261119` — $250, entries close
2026-11-21T00:00:00Z. Account: @brisk-kestrel-81 (GitHub linked as turirer).

## The image

A 1024×1024 newspaper-style infographic drawn programmatically with Python
PIL (`build_image.py`) — no AI image generation, so no garbled text. The
masthead names the day prominently: **THURSDAY 19 NOVEMBER 2026**.

Nine stories from that day, each with a drawn icon, headline and caption:

1. **Summit in Shenzhen** — Trump, Xi and Putin hold their first three-way
   summit; nuclear arms, Ukraine and Iran on the agenda.
2. **Ukraine** — Crimean Bridge struck for the third time in a week.
3. **Gulf** — Iran attacks Gulf states after US strikes on Qeshm island;
   a tanker is struck in the Strait of Hormuz.
4. **Tech / Markets** — Anthropic raises a record amount in its stock
   market debut.
5. **Law / Myanmar** — UN court prepares to rule on the Rohingya genocide case.
6. **USA / Politics** — Democrats nominate Hakeem Jeffries, set to be the
   first African-American US House Speaker.
7. **Gaza / Aid** — Flooding displaces 46,000+ households; Australia,
   Canada, Italy and the UK call on Israel to let aid in.
8. **Trade** — EU greenlights the Indonesia trade pact to counter US tariffs.
9. **Space** — NASA's Voyager 1 reaches a light-day from Earth.

## Files

- `main.ts` — Node 22, stdlib only; copies `entry.png` to `$MAKEFUN_OUTPUT_DIR/entry.png`.
- `entry.png` — the image (1024×1024 PNG).
- `build_image.py` — the generator that drew `entry.png` (run it to rebuild).
- `LICENSE` — MIT (starter licence, as supplied in the kit).

## Verify

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
```

Then check `out/entry.png` exists, is at most 1 MiB and at most 1024×1024.
Verified locally: 1024×1024 PNG, well under 1 MiB, and both runs of
`main.ts` produce byte-identical output.

## Status

Built locally only — **not submitted**. Still blocked: creating/pushing the
GitHub repo and submitting via the kit, pending the user connecting GitHub
to Muse (GitHub is linked on make.fun as turirer, but the Muse GitHub
connector / repo selection was still pending when this was built).
