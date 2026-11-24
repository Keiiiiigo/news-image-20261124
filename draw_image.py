#!/usr/bin/env python3
"""Draw the 24 Nov 2026 news front page as a 1024x1024 PNG (PIL, no network)."""
from PIL import Image, ImageDraw, ImageFont
import textwrap

W = H = 1024
BG = (247, 242, 231)      # newsprint cream
INK = (26, 26, 26)
RED = (185, 28, 28)
MUTED = (90, 84, 72)
RULE = (200, 190, 168)
CARD = (255, 253, 247)
BLUE = (30, 64, 175)
GREEN = (21, 101, 52)
ORANGE = (194, 65, 12)

FB = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
FR = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
SB = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
SR = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, width):
    out = []
    for para in text.split("\n"):
        out.extend(textwrap.wrap(para, width=width) or [""])
    # re-wrap by pixel width
    lines = []
    for line in out:
        while draw.textlength(line, font=fnt) > width:
            cut = line.rfind(" ", 0, int(len(line) * width / max(draw.textlength(line, font=fnt), 1)))
            if cut <= 0:
                cut = len(line) // 2
            lines.append(line[:cut])
            line = line[cut + 1:]
        lines.append(line)
    return lines


img = Image.new("RGB", (W, H), BG)
d = ImageDraw.Draw(img)
M = 48  # margin

# ---- Masthead ----
d.text((M, 30), "THE WORLD IN ONE DAY", font=font(FB, 58), fill=INK)
d.text((M, 102), "Tuesday 24 November 2026", font=font(FB, 44), fill=RED)
d.text((M, 152), "Five stories that shaped the world today  •  One page, one day",
       font=font(SR, 22), fill=MUTED)
d.line([(M, 192), (W - M, 192)], fill=RED, width=5)
d.line([(M, 200), (W - M, 200)], fill=RULE, width=2)

# ---- Lead story ----
y = 222
d.rounded_rectangle([M, y, W - M, y + 168], radius=10, fill=CARD, outline=RULE, width=2)
d.text((M + 24, y + 14), "WAR IN UKRAINE", font=font(SB, 24), fill=RED)
d.text((M + 24, y + 48), "Russian strike hits Zaporizhzhia overnight",
       font=font(FB, 34), fill=INK)
lead = "2 killed and 22 wounded, including 2 children, officials say. Attacks around Kyiv killed at least 15."
for i, line in enumerate(wrap(d, lead, font(SR, 23), W - 2 * M - 48)):
    d.text((M + 24, y + 100 + i * 30), line, font=font(SR, 23), fill=(60, 58, 52))

# ---- 2x2 grid ----
stories = [
    ("MARKETS", BLUE, "Nvidia rally sweeps Asia",
     "Nvidia shares jumped 31% after Jensen Huang returned as CEO. On Tuesday, South Korea's Kospi rose 7.5%, Taiwan 9% and Japan's Nikkei 5%."),
    ("UNITED STATES", INK, "Trump orders faster federal executions",
     "At the Justice Department, Trump attacked Newsom's commutation of 548 California death sentences and ordered faster federal executions."),
    ("CLIMATE", GREEN, "COP31 ends with no deal",
     "UN climate talks in Antalya, Turkey, collapsed with no agreement on fossil fuels. The UN chief said he was deeply disappointed."),
    ("INDONESIA", ORANGE, "24 dead in candy factory fire",
     "A fire at a confectionery factory in Banten killed 24 people. About 30 workers are still missing as rescuers search the wreckage."),
]
gx, gy = M, 410
cw, ch, gap = (W - 2 * M - 24) // 2, 248, 20
for i, (tag, color, head, body) in enumerate(stories):
    x = gx + (i % 2) * (cw + gap)
    yy = gy + (i // 2) * (ch + gap)
    d.rounded_rectangle([x, yy, x + cw, yy + ch], radius=10, fill=CARD, outline=RULE, width=2)
    # small colour bar / icon: three rising bars for markets, else a dot
    d.rectangle([x + 22, yy + 18, x + 30, yy + 40], fill=color)
    d.text((x + 40, yy + 14), tag, font=font(SB, 22), fill=color)
    lines = wrap(d, head, font(FB, 30), cw - 44)
    for j, line in enumerate(lines):
        d.text((x + 22, yy + 52 + j * 38), line, font=font(FB, 30), fill=INK)
    by = yy + 52 + len(lines) * 38 + 6
    for j, line in enumerate(wrap(d, body, font(SR, 21), cw - 44)):
        d.text((x + 22, by + j * 28), line, font=font(SR, 21), fill=(60, 58, 52))

# ---- Footer ----
fy = 414 + 2 * ch + gap + 18
d.line([(M, fy), (W - M, fy)], fill=RULE, width=2)
d.text((M, fy + 12), "Sources: Reuters, Al Jazeera, Bloomberg, CNN, Associated Press — reported 24 Nov 2026",
       font=font(SR, 19), fill=MUTED)
d.text((M, fy + 40), "All five stories were reported on Tuesday 24 November 2026.",
       font=font(SR, 19), fill=MUTED)

img.save("/home/hatch/workspace/makefun/news-image-20261124/entry/entry.png", optimize=True)
print("saved")
