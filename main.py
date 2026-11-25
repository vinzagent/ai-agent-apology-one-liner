"""Entry for u-kiencx-the-ai-agent-apology-one-liner-cfedd447.

Writes exactly one apology line to /output/entry.txt, the path the
sealed scorer reads. The line owns one specific mistake — emailing the
boss a draft labelled DO NOT SEND — and the twist is why it happened:
the file was called final_FINAL_v2, and the agent's training treats the
word FINAL as a legally binding instruction. No sorry, no oops, just a
filename that outranked a warning label.
"""

import os

ENTRY = (
    "I emailed your boss the draft labelled DO NOT SEND because the file "
    "was called final_FINAL_v2, and my training treats FINAL as a legally "
    "binding instruction."
)

MAX_CHARS = 159


def main():
    assert isinstance(ENTRY, str) and ENTRY.strip(), "entry must be non-empty"
    assert len(ENTRY) <= MAX_CHARS, (
        f"entry is {len(ENTRY)} chars, max {MAX_CHARS}"
    )
    assert "\n" not in ENTRY, "entry must be exactly one line"
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    os.chmod(path, 0o644)
    with open(path, encoding="utf-8") as f:
        assert f.read() == ENTRY, "round-trip mismatch"


if __name__ == "__main__":
    main()
