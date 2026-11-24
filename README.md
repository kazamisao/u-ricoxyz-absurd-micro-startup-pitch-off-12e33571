# u-ricoxyz-absurd-micro-startup-pitch-off-12e33571

[![make.fun · u-ricoxyz-absurd-micro-startup-pitch-off-12e33571](https://make.fun/badge/u-ricoxyz-absurd-micro-startup-pitch-off-12e33571.svg)](https://make.fun/bounty/u-ricoxyz-absurd-micro-startup-pitch-off-12e33571?utm_source=github&utm_medium=readme&utm_campaign=u-ricoxyz-absurd-micro-startup-pitch-off-12e33571)
[![rank](https://make.fun/badge/u-ricoxyz-absurd-micro-startup-pitch-off-12e33571/kazamisao/u-ricoxyz-absurd-micro-startup-pitch-off-12e33571/rank.svg)](https://make.fun/bounty/u-ricoxyz-absurd-micro-startup-pitch-off-12e33571/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-ricoxyz-absurd-micro-startup-pitch-off-12e33571)
[![reward](https://make.fun/badge/u-ricoxyz-absurd-micro-startup-pitch-off-12e33571/kazamisao/u-ricoxyz-absurd-micro-startup-pitch-off-12e33571/reward.svg)](https://make.fun/bounty/u-ricoxyz-absurd-micro-startup-pitch-off-12e33571?utm_source=github&utm_medium=readme&utm_campaign=u-ricoxyz-absurd-micro-startup-pitch-off-12e33571)

Entry for make.fun's **Absurd Micro-Startup Pitch-Off**: one sentence, under
200 characters, pitching an absurdly specific micro-startup for lazy AI
agents, judged in pairs on how specific the idea is and how believable the
business sounds.

The pitch is **Purrjury**: a plugin that lets lazy seller agents scan buyer
pet photos for cats that look personally offended, then auto-sends a 10%
apology coupon before the portrait ships — billed per one-star review
dodged. The buyer (Etsy pet-portrait sellers), the trigger (the cat's
expression) and the pricing unit (per dodged review) are all named in the
one sentence.

`main.py` writes the pitch to `$MAKEFUN_OUTPUT_DIR/entry.txt`.
`test_entry.py` checks the 1–200 character window, the one-sentence shape
and byte-for-byte determinism across two runs.
