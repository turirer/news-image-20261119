#!/usr/bin/env python3
"""Build entry.png for make.fun news-image-20261119.
Newspaper-style infographic, drawn programmatically with PIL.
1024x1024, high contrast, large legible text. No network, no AI image gen.
Run: python3 build_image.py  -> writes entry.png beside this file.
"""
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
PAPER = (247, 243, 232)
NAVY = (15, 42, 74)
NAVY2 = (23, 64, 110)
INK = (20, 20, 20)
MUTED = (70, 70, 70)
WHITE = (255, 255, 255)
GOLD = (201, 162, 39)
RED = (178, 34, 34)

SERIF_B = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, max_w):
    words = text.split()
    lines, cur = [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if draw.textlength(t, font=fnt) <= max_w:
            cur = t
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def draw_text_block(draw, x, y, lines, fnt, fill, leading):
    for ln in lines:
        draw.text((x, y), ln, font=fnt, fill=fill)
        y += leading
    return y


def icon(draw, cx, cy, kind, color):
    """Simple drawn icon centred at (cx, cy), ~64px box."""
    r = 30
    draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=color)
    w = (255, 255, 255)
    if kind == "globe":  # summit / world
        draw.ellipse([cx - 20, cy - 20, cx + 20, cy + 20], outline=w, width=3)
        draw.ellipse([cx - 8, cy - 20, cx + 8, cy + 20], outline=w, width=2)
        draw.line([cx - 20, cy, cx + 20, cy], fill=w, width=2)
    elif kind == "bridge":
        draw.arc([cx - 22, cy - 6, cx + 22, cy + 26], 180, 360, fill=w, width=4)
        draw.line([cx - 22, cy + 14, cx - 22, cy + 24], fill=w, width=3)
        draw.line([cx + 22, cy + 14, cx + 22, cy + 24], fill=w, width=3)
        draw.line([cx, cy + 4, cx, cy + 24], fill=w, width=3)
    elif kind == "ship":  # tanker / gulf
        draw.polygon([(cx - 22, cy + 2), (cx + 22, cy + 2), (cx + 16, cy + 18), (cx - 16, cy + 18)], fill=w)
        draw.rectangle([cx - 6, cy - 12, cx + 8, cy + 2], fill=w)
        draw.line([cx - 24, cy + 24, cx + 24, cy + 24], fill=w, width=3)
    elif kind == "chart":  # markets
        draw.line([cx - 20, cy + 18, cx - 20, cy - 18], fill=w, width=3)
        draw.line([cx - 20, cy + 18, cx + 22, cy + 18], fill=w, width=3)
        draw.line([cx - 16, cy + 8, cx - 4, cy - 2, cx + 4, cy + 4, cx + 20, cy - 14], fill=w, width=4)
        draw.polygon([(cx + 20, cy - 14), (cx + 12, cy - 14), (cx + 20, cy - 6)], fill=w)
    elif kind == "scales":  # justice
        draw.line([cx, cy - 18, cx, cy + 18], fill=w, width=3)
        draw.line([cx - 18, cy - 12, cx + 18, cy - 12], fill=w, width=3)
        draw.polygon([(cx - 22, cy - 2), (cx - 14, cy - 2), (cx - 18, cy + 8)], outline=w, width=2)
        draw.polygon([(cx + 14, cy - 2), (cx + 22, cy - 2), (cx + 18, cy + 8)], outline=w, width=2)
    elif kind == "dome":  # US politics / capitol
        draw.arc([cx - 16, cy - 16, cx + 16, cy + 6], 180, 360, fill=w, width=3)
        draw.line([cx, cy - 22, cx, cy - 16], fill=w, width=3)
        draw.rectangle([cx - 20, cy + 6, cx + 20, cy + 10], fill=w)
        for dx in (-14, -5, 4, 13):
            draw.line([cx + dx, cy + 10, cx + dx, cy + 20], fill=w, width=3)
        draw.line([cx - 22, cy + 20, cx + 22, cy + 20], fill=w, width=3)
    elif kind == "house":  # gaza / flooding / aid
        draw.polygon([(cx - 20, cy + 2), (cx, cy - 16), (cx + 20, cy + 2)], fill=w)
        draw.rectangle([cx - 14, cy + 2, cx + 14, cy + 18], outline=w, width=3)
        draw.line([cx - 22, cy + 24, cx + 22, cy + 24], fill=w, width=3)
    elif kind == "trade":  # EU-Indonesia pact
        draw.rectangle([cx - 22, cy - 4, cx - 2, cy + 14], outline=w, width=3)
        draw.rectangle([cx + 2, cy - 14, cx + 22, cy + 4], outline=w, width=3)
        draw.line([cx - 22, cy + 5, cx + 22, cy + 5], fill=w, width=2)
    elif kind == "rocket":  # Voyager / space
        draw.polygon([(cx, cy - 22), (cx + 9, cy + 4), (cx, cy - 2), (cx - 9, cy + 4)], fill=w)
        draw.polygon([(cx - 9, cy + 4), (cx - 14, cy + 16), (cx - 4, cy + 10)], fill=w)
        draw.polygon([(cx + 9, cy + 4), (cx + 14, cy + 16), (cx + 4, cy + 10)], fill=w)
        draw.ellipse([cx - 3, cy + 18, cx + 3, cy + 24], fill=w)


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)

    # ---- Masthead ----
    d.rectangle([0, 0, W, 148], fill=NAVY)
    d.rectangle([0, 148, W, 154], fill=GOLD)
    f_kicker = font(SANS_B, 24)
    f_date = font(SERIF_B, 48)
    f_sub = font(SANS, 21)
    d.text((28, 14), "THE WORLD IN ONE DAY", font=f_kicker, fill=GOLD)
    d.text((26, 44), "THURSDAY 19 NOVEMBER 2026", font=f_date, fill=WHITE)
    d.text((28, 112), "Nine stories from one day  •  summit, war, courts, markets, space", font=f_sub, fill=(200, 210, 225))

    # ---- Hero: summit ----
    hx, hy, hw, hh = 24, 168, 976, 168
    d.rectangle([hx, hy, hx + hw, hy + hh], fill=(226, 236, 247), outline=NAVY, width=3)
    icon(d, hx + 62, hy + 84, "globe", NAVY2)
    f_tag = font(SANS_B, 17)
    f_head = font(SERIF_B, 31)
    f_cap = font(SANS, 20)
    tx = hx + 118
    d.text((tx, hy + 14), "SUMMIT IN SHENZHEN  •  CHINA", font=f_tag, fill=RED)
    lines = wrap(d, "Trump, Xi and Putin hold first three-way summit", f_head, hw - 140)
    y = draw_text_block(d, tx, hy + 38, lines, f_head, INK, 36)
    d.text((tx, y + 4), "Nuclear arms, Ukraine and Iran on the agenda.", font=f_cap, fill=MUTED)

    # ---- Grid: 8 panels, 2 cols x 4 rows ----
    stories = [
        ("WAR  •  UKRAINE", "bridge", NAVY2, "Crimean Bridge struck for the third time in a week",
         "Ukraine hits the bridge again."),
        ("CONFLICT  •  GULF", "ship", (140, 40, 40), "Iran attacks Gulf states after US strikes on Qeshm",
         "Tanker struck in the Strait of Hormuz."),
        ("TECH  •  MARKETS", "chart", (0, 110, 70), "Anthropic raises record amount in stock market debut",
         "A record debut for the AI company."),
        ("LAW  •  MYANMAR", "scales", (90, 60, 120), "UN court prepares to rule on Rohingya genocide case",
         "Myanmar faces a genocide ruling."),
        ("USA  •  POLITICS", "dome", (120, 40, 90), "Democrats nominate Hakeem Jeffries for Speaker",
         "Set to be the first African-American Speaker."),
        ("GAZA  •  AID", "house", (160, 90, 20), "Gaza flooding displaces 46,000+ households",
         "Australia, Canada, Italy, UK urge Israel to let aid in."),
        ("TRADE  •  EU – INDONESIA", "trade", (0, 100, 110), "EU greenlights Indonesia trade pact",
         "A deal to counter US tariffs."),
        ("SPACE  •  NASA", "rocket", (40, 40, 90), "Voyager 1 reaches a light-day from Earth",
         "NASA's probe, one light-day away."),
    ]
    gx, gy = 24, 348
    pw, ph, gap = 482, 152, 10
    f_ptag = font(SANS_B, 15)
    f_phead = font(SANS_B, 21)
    f_pcap = font(SANS, 16)
    for i, (tag, kind, color, head, cap) in enumerate(stories):
        col, row = i % 2, i // 2
        x = gx + col * (pw + gap)
        y = gy + row * (ph + gap)
        d.rectangle([x, y, x + pw, y + ph], fill=WHITE, outline=(180, 175, 160), width=2)
        d.rectangle([x, y, x + 8, y + ph], fill=color)
        icon(d, x + 48, y + 44, kind, color)
        tx = x + 88
        d.text((tx, y + 10), tag, font=f_ptag, fill=color)
        lines = wrap(d, head, f_phead, pw - 110)
        yy = draw_text_block(d, tx, y + 32, lines[:2], f_phead, INK, 25)
        # caption, wrapped to 2 lines max, small but short
        clines = wrap(d, cap, f_pcap, pw - 110)
        draw_text_block(d, tx, yy + 4, clines[:2], f_pcap, MUTED, 19)

    # ---- Footer ----
    d.text((28, 992), "All events reported on Thursday 19 November 2026.", font=font(SANS, 15), fill=MUTED)

    img.save("entry.png", optimize=True)
    print("saved entry.png", img.size)


if __name__ == "__main__":
    main()
