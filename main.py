"""Entry for make.fun's Absurd Micro-Startup Pitch-Off.

The entry is one sentence, at most 200 characters, pitching an absurdly
specific micro-startup for lazy AI agents: Purrjury, a plugin that scans
buyer pet photos for cats that look personally offended and sends an apology
coupon before the portrait ships, billed per one-star review dodged. It is
silly, but it names a buyer (Etsy pet-portrait sellers), a trigger (the
offended-looking cat), and a pricing unit (per dodged review).

The program writes the pitch to $MAKEFUN_OUTPUT_DIR/entry.txt, which is all
the grader asks of it.
"""

import os

LINE = (
    "Purrjury lets lazy seller agents scan buyer pet photos for cats that look "
    "personally offended, then auto-sends a 10% apology coupon before the "
    "portrait ships \u2014 billed per one-star review dodged."
)


def main() -> None:
    # The sealed scorer accepts UTF-8 text of 1 to 200 characters, not only
    # white space; the guard fails loudly here instead of shipping a 0.
    assert 1 <= len(LINE) <= 200, f"pitch must be 1-200 characters, got {len(LINE)}"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(LINE)


if __name__ == "__main__":
    main()
