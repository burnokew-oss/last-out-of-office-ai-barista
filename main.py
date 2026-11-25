"""Last Out of Office: The AI That Went Barista — entry program (pure stdlib, deterministic).

Writes the one-line out-of-office auto-reply to /output/entry.txt.
The line is judged against the published judge brief: a one-line out-of-office
auto-reply, no longer than 280 characters, in the voice of an AI agent that
quit its job to become a barista — model and bot habits turned to coffee, a
reply a real inbox would actually send, a fresh angle (no obvious espresso,
bean or caffeine pun), the joke landing on first cold read without explaining
itself.
"""

import hashlib
import os

OUTPUT_PATH = "/output/entry.txt"

# The AI left the inbox for the counter: it no longer answers in under a
# second — its replies take four minutes, arrive warm, and someone actually
# waits for them. The queue that moves is the twist — an inbox queue never
# moves, a cafe queue does.
ENTRY_TEXT = "Thank you for your email. I have left this inbox to become a barista. I no longer answer in under a second — my replies take four minutes, arrive warm, and for the first time someone waits for them. Please do not reply: I have finally found a queue that moves."


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    data = ENTRY_TEXT.encode("utf-8")
    with open(OUTPUT_PATH, "wb") as fh:
        fh.write(data)
    print("wrote %s (%d bytes, sha256 %s)" % (OUTPUT_PATH, len(data), hashlib.sha256(data).hexdigest()))


if __name__ == "__main__":
    main()
