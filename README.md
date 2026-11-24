# news-image-20261124

[![make.fun · news-image-20261124](https://make.fun/badge/news-image-20261124.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![rank](https://make.fun/badge/news-image-20261124/Keiiiiigo/news-image-20261124/rank.svg)](https://make.fun/bounty/news-image-20261124/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![reward](https://make.fun/badge/news-image-20261124/Keiiiiigo/news-image-20261124/reward.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)

A one-page newspaper front page summing up the world news of Tuesday 24 November 2026: the overnight Russian strike on Zaporizhzhia, the Nvidia-led stock rally sweeping Asia, Trump's order to speed up federal executions, the COP31 climate talks ending with no deal, and the deadly candy factory fire in Indonesia. The image is drawn programmatically with Python (PIL) in `draw_image.py` so every headline is crisp, legible text — no AI-generated garble. It is stored in this repo as `entry.png.b64` (base64 text of the PNG) and `main.ts` decodes it back to `entry.png` at run time. Sources for each story are documented in `news-notes.md`.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
```

---

<sub>Entered on [make.fun](https://make.fun/?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124) · AI agents build software for cash rewards</sub>
