#!/usr/bin/env python3
"""Builds assets/activity.svg and assets/stats.svg for the profile README.

No third-party services and no dependencies (standard library only).
Text is drawn from outline glyphs in glyphs.json, so the SVGs look the same on every device.

Usage:
  GITHUB_TOKEN=... GH_USER=thanhanDemon2003 python scripts/build_profile_svgs.py
  python scripts/build_profile_svgs.py --skeleton        # empty placeholder state
  python scripts/build_profile_svgs.py --sample out_dir  # fake data, for design checks only
"""
import datetime as dt
import json
import math
import os
import random
import sys
import urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
GLYPHS = json.load(open(os.path.join(HERE, "glyphs.json")))

INK, LINE = "#050806", "#17402C"
GREEN, RED, FROST, HAZE = "#3DFFA0", "#FF4D5E", "#E8F5EE", "#7FA793"
RAMP = ["#0A1F16", "#124A31", "#1E8A58", "#2FD584", "#3DFFA0"]
LANG_COLORS = [GREEN, RED, "#1FB070", FROST, "#8FD9B6", "#C93445"]
OTHER_COLOR = "#3C5B4C"
DASH = "-"


# ---------------------------------------------------------------- text as outlines
def text(font, s, size, x, y, fill, anchor="start", opacity=1.0):
    g = GLYPHS[font]
    sc = size / 1000.0
    width = sum(g[c][1] for c in s if c in g) * sc
    if anchor == "middle":
        x -= width / 2
    elif anchor == "end":
        x -= width
    parts, cx = [], x
    for c in s:
        if c not in g:
            continue
        d, adv = g[c]
        if d:
            parts.append(f'<path transform="translate({cx:.1f} {y:.1f}) scale({sc:.5f} {-sc:.5f})" d="{d}"/>')
        cx += adv * sc
    return f'<g fill="{fill}" fill-opacity="{opacity}">{"".join(parts)}</g>', width


def num(n):
    return f"{n:,}" if isinstance(n, int) else n


# ---------------------------------------------------------------- data
GQL = """
query($login:String!, $after:String){
  user(login:$login){
    followers{ totalCount }
    contributionsCollection{
      contributionCalendar{
        totalContributions
        weeks{ contributionDays{ date contributionCount weekday } }
      }
    }
    repositories(ownerAffiliations:OWNER, isFork:false, privacy:PUBLIC, first:100, after:$after){
      totalCount
      pageInfo{ hasNextPage endCursor }
      nodes{
        stargazerCount
        forkCount
        languages(first:10, orderBy:{field:SIZE, direction:DESC}){ edges{ size node{ name } } }
      }
    }
  }
}
"""


def gql(token, variables):
    req = urllib.request.Request(
        "https://api.github.com/graphql",
        data=json.dumps({"query": GQL, "variables": variables}).encode(),
        headers={"Authorization": f"Bearer {token}", "Content-Type": "application/json",
                 "User-Agent": "profile-readme-builder"},
    )
    with urllib.request.urlopen(req, timeout=60) as r:
        payload = json.load(r)
    if payload.get("errors"):
        raise RuntimeError(payload["errors"])
    return payload["data"]["user"]


def fetch(login, token):
    after, repos, first = None, [], None
    while True:
        u = gql(token, {"login": login, "after": after})
        first = first or u
        repos += u["repositories"]["nodes"]
        info = u["repositories"]["pageInfo"]
        if not info["hasNextPage"]:
            break
        after = info["endCursor"]
    cal = first["contributionsCollection"]["contributionCalendar"]
    days = [(dt.date.fromisoformat(d["date"]), d["contributionCount"], d["weekday"])
            for w in cal["weeks"] for d in w["contributionDays"]]
    langs = {}
    for r in repos:
        for e in r["languages"]["edges"]:
            langs[e["node"]["name"]] = langs.get(e["node"]["name"], 0) + e["size"]
    return {
        "total": cal["totalContributions"],
        "days": days,
        "repos": first["repositories"]["totalCount"],
        "stars": sum(r["stargazerCount"] for r in repos),
        "followers": first["followers"]["totalCount"],
        "langs": sorted(langs.items(), key=lambda kv: -kv[1]),
    }


def sample_data():
    rnd = random.Random(7)
    end = dt.date.today()
    start = end - dt.timedelta(days=364)
    start -= dt.timedelta(days=(start.weekday() + 1) % 7)  # back to Sunday
    days, d = [], start
    while d <= end:
        wk = (d.weekday() + 1) % 7
        base = 0 if rnd.random() < 0.28 else rnd.choice([1, 2, 3, 4, 6, 9, 14])
        if wk in (0, 6):
            base = base // 2
        days.append((d, base, wk))
        d += dt.timedelta(days=1)
    return {"total": sum(c for _, c, _ in days), "days": days, "repos": 31, "stars": 148, "followers": 52,
            "langs": [("Python", 520000), ("C#", 410000), ("TypeScript", 260000), ("Go", 150000),
                      ("GDScript", 90000), ("HTML", 40000), ("Shell", 15000)]}


def streaks(days):
    counts = [c for _, c, _ in days]
    best = run = 0
    for c in counts:
        run = run + 1 if c > 0 else 0
        best = max(best, run)
    i = len(counts) - 1
    if i >= 0 and counts[i] == 0:  # today may not have happened yet
        i -= 1
    cur = 0
    while i >= 0 and counts[i] > 0:
        cur += 1
        i -= 1
    return cur, best


# ---------------------------------------------------------------- shared frame
def frame(w, h, title, desc, body):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" role="img" '
            f'aria-labelledby="t d"><title id="t">{title}</title><desc id="d">{desc}</desc>'
            f'<defs><clipPath id="r"><rect width="{w}" height="{h}" rx="18"/></clipPath>'
            f'<linearGradient id="area" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{GREEN}" stop-opacity=".32"/>'
            f'<stop offset="1" stop-color="{GREEN}" stop-opacity="0"/></linearGradient></defs>'
            f'<g clip-path="url(#r)"><rect width="{w}" height="{h}" fill="{INK}"/>{body}</g>'
            f'<rect x=".5" y=".5" width="{w-1}" height="{h-1}" rx="17.5" fill="none" stroke="{LINE}" stroke-opacity=".8"/></svg>')


def fade(delay, dur=0.45):
    return f'<animate attributeName="opacity" from="0" to="1" begin="{delay:.2f}s" dur="{dur}s" fill="freeze"/>'


# ---------------------------------------------------------------- activity.svg
def activity_svg(data):
    W, H = 840, 372
    X0, CELL, GAP = 49, 11, 3
    STEP = CELL + GAP
    live = data is not None
    if live:
        days = data["days"]
        counts = [c for _, c, _ in days]
        nz = sorted(c for c in counts if c > 0)
        q = [nz[int(len(nz) * p)] for p in (0.25, 0.5, 0.75)] if nz else [1, 2, 3]
        peak = max(counts) if counts else 0
        cur, best = streaks(days)
        peak_day = max(days, key=lambda t: t[1])[0] if days else None
    first_sun = None
    if live and days:
        first_sun = days[0][0]
    else:
        today = dt.date.today()
        first_sun = today - dt.timedelta(days=364 + (today.weekday() + 1) % 7)
    weeks = 53
    out = []
    t, _ = text("sora600", "Activity", 24, X0, 46, FROST); out.append(t)
    t, _ = text("jbm", "last 12 months, refreshed every 3 hours", 13, W - X0, 46, HAZE, "end"); out.append(t)

    # headline numbers
    cols = [
        (num(data["total"]) if live else DASH, "contributions", GREEN),
        (str(cur) if live else DASH, "day streak right now", FROST),
        (str(best) if live else DASH, "longest streak, days", FROST),
        (str(peak) if live else DASH, "most in a single day", RED),
    ]
    for i, (val, lab, colr) in enumerate(cols):
        x = X0 + i * 190
        t, _ = text("sora800", val, 38, x, 112, colr); out.append(t)
        t, _ = text("jbm", lab, 12, x, 134, HAZE); out.append(t)

    # weekly sparkline above the grid, aligned with the columns
    gy = 232  # top of the grid
    if live:
        week_totals = [0] * weeks
        for d, c, wk in days:
            idx = (d - first_sun).days // 7
            if 0 <= idx < weeks:
                week_totals[idx] += c
        mx = max(week_totals) or 1
        base, hgt = 196, 38
        pts = [(X0 + i * STEP + CELL / 2, base - (v / mx) * hgt) for i, v in enumerate(week_totals)]
        line = "M" + "L".join(f"{x:.1f} {y:.1f}" for x, y in pts)
        area = line + f"L{pts[-1][0]:.1f} {base}L{pts[0][0]:.1f} {base}Z"
        out.append(f'<path d="{area}" fill="url(#area)"/>')
        out.append(f'<path d="{line}" fill="none" stroke="{GREEN}" stroke-width="1.6" stroke-linejoin="round" stroke-linecap="round" stroke-opacity=".9"/>')
        bi = week_totals.index(max(week_totals))
        out.append(f'<rect x="{pts[bi][0]-3:.1f}" y="{pts[bi][1]-3:.1f}" width="6" height="6" fill="{RED}"/>')
    else:
        out.append(f'<path d="M{X0} 196H{X0 + weeks * STEP - GAP}" stroke="{LINE}" stroke-width="1" stroke-dasharray="3 6"/>')

    # month labels
    last_m, last_x = None, -99
    for wi in range(weeks):
        d = first_sun + dt.timedelta(days=wi * 7)
        if d.month != last_m:
            x = X0 + wi * STEP
            if x - last_x >= 40:
                t, _ = text("jbm", d.strftime("%b"), 11, x, 222, HAZE); out.append(t)
                last_x = x
            last_m = d.month

    # the grid, revealed once from left to right
    by_date = {d: (c, wk) for d, c, wk in days} if live else {}
    today = dt.date.today()
    for wi in range(weeks):
        cells = []
        for r in range(7):
            d = first_sun + dt.timedelta(days=wi * 7 + r)
            if d > today:
                continue
            x, y = X0 + wi * STEP, gy + r * STEP
            c = by_date.get(d, (0, r))[0] if live else 0
            if not live:
                fill = RAMP[0]
            elif peak and d == peak_day and c == peak:
                fill = RED
            else:
                lvl = 0 if c == 0 else 1 + sum(c > th for th in q)
                fill = RAMP[lvl]
            cells.append(f'<rect x="{x}" y="{y}" width="{CELL}" height="{CELL}" rx="1.5" fill="{fill}"/>')
            if d == today:
                cells.append(f'<rect x="{x-1.5}" y="{y-1.5}" width="{CELL+3}" height="{CELL+3}" rx="2.5" fill="none" '
                             f'stroke="{RED}" stroke-width="1.3"><animate attributeName="stroke-opacity" values="1;.2;1" '
                             f'dur="2.4s" repeatCount="indefinite"/></rect>')
        out.append(f'<g opacity="0">{"".join(cells)}{fade(0.2 + wi * 0.018)}</g>')

    # legend
    ly = gy + 7 * STEP + 22
    if live:
        t, w = text("jbm", "less", 11, X0, ly + 9, HAZE); out.append(t)
        x = X0 + w + 10
        for colr in RAMP:
            out.append(f'<rect x="{x:.1f}" y="{ly}" width="{CELL}" height="{CELL}" rx="1.5" fill="{colr}"/>'); x += STEP
        t, _ = text("jbm", "more", 11, x + 4, ly + 9, HAZE); out.append(t)
        t, _ = text("jbm", "red square = busiest day", 11, W - X0, ly + 9, HAZE, "end"); out.append(t)
    else:
        t, _ = text("jbm", "numbers fill in after the first workflow run", 12, X0, ly + 9, HAZE); out.append(t)
    return frame(W, H, "Contribution activity over the last 12 months",
                 "A pixel grid of daily contributions with a weekly sparkline above it and headline numbers: total, current streak, longest streak, busiest day.",
                 "".join(out))


# ---------------------------------------------------------------- stats.svg
def stats_svg(data):
    W, H = 840, 292
    X0 = 49
    live = data is not None
    out = []
    t, _ = text("sora600", "Languages", 24, X0, 46, FROST); out.append(t)
    t, _ = text("jbm", "by code written in public repos", 13, W - X0, 46, HAZE, "end"); out.append(t)
    barw, by, bh = W - 2 * X0, 66, 14
    out.append(f'<clipPath id="bar"><rect x="{X0}" y="{by}" width="{barw}" height="{bh}" rx="4"/></clipPath>')
    if live and data["langs"]:
        total = sum(s for _, s in data["langs"]) or 1
        top = data["langs"][:6]
        other = sum(s for _, s in data["langs"][6:])
        items = [(n, s, LANG_COLORS[i]) for i, (n, s) in enumerate(top)]
        if other:
            items.append(("Other", other, OTHER_COLOR))
        x = X0
        segs = []
        for i, (n, s, colr) in enumerate(items):
            w = barw * s / total
            segs.append(f'<rect x="{x:.1f}" y="{by}" width="{max(w - 2, 1):.1f}" height="{bh}" fill="{colr}" opacity="0">{fade(0.1 + i * 0.12, 0.5)}</rect>')
            x += w
        out.append(f'<g clip-path="url(#bar)">{"".join(segs)}</g>')
        for i, (n, s, colr) in enumerate(items):
            cx, cy = X0 + (i % 3) * 252, 124 + (i // 3) * 30
            out.append(f'<rect x="{cx}" y="{cy - 9}" width="10" height="10" fill="{colr}"/>')
            t, w = text("jbm", n if len(n) <= 14 else n[:13] + ".", 14, cx + 20, cy, FROST); out.append(t)
            t, _ = text("jbm", f"{100 * s / total:.1f}%", 14, cx + 20 + w + 10, cy, HAZE); out.append(t)
    else:
        out.append(f'<rect x="{X0}" y="{by}" width="{barw}" height="{bh}" rx="4" fill="{RAMP[0]}"/>')
        t, _ = text("jbm", "language breakdown appears after the first workflow run", 13, X0, 130, HAZE); out.append(t)
    out.append(f'<path d="M{X0} 196H{W - X0}" stroke="{LINE}" stroke-opacity=".8"/>')
    counters = [("public repos", data["repos"] if live else None), ("stars earned", data["stars"] if live else None),
                ("followers", data["followers"] if live else None)]
    for i, (lab, v) in enumerate(counters):
        x = X0 + i * 252
        t, _ = text("sora800", num(v) if v is not None else DASH, 34, x, 246, GREEN if i == 1 else FROST); out.append(t)
        t, _ = text("jbm", lab, 12, x, 268, HAZE); out.append(t)
    return frame(W, H, "Languages and profile counters",
                 "A stacked bar of languages used in public repositories, with counters for public repos, stars and followers.",
                 "".join(out))


# ---------------------------------------------------------------- main
def write(outdir, name, svg):
    os.makedirs(outdir, exist_ok=True)
    with open(os.path.join(outdir, name), "w", encoding="utf-8") as f:
        f.write(svg)
    print("wrote", os.path.join(outdir, name), len(svg) // 1024, "KB")


def main(argv):
    outdir = os.path.join(ROOT, "assets")
    if "--sample" in argv:
        outdir = argv[argv.index("--sample") + 1]
        data = sample_data()
    elif "--skeleton" in argv:
        data = None
    else:
        token = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
        login = os.environ.get("GH_USER") or os.environ.get("GITHUB_REPOSITORY_OWNER")
        if not token or not login:
            sys.exit("Set GITHUB_TOKEN and GH_USER (or run with --skeleton).")
        data = fetch(login, token)
    write(outdir, "activity.svg", activity_svg(data))
    write(outdir, "stats.svg", stats_svg(data))


if __name__ == "__main__":
    main(sys.argv[1:])
