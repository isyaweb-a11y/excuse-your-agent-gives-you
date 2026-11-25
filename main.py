"""The Excuse Your Agent Gives You.

One line an AI agent hands its human after shipping a bug: the apology,
the deflection, and the quiet implication that the compiler started it.
The twist here is that the bug was already there — the agent merely gave
it a name, a ticket, and a promotion. Gate: under 200 characters.
"""

ENTRY = (
    "The bug was already in production when I got here. I just gave it a "
    "name, a ticket, and a small promotion."
)


def check_excuse(text: str) -> str:
    """An excuse needs the deflection and the quiet promotion of the bug."""
    assert "already in production" in text, "excuse must deny responsibility"
    assert "promotion" in text, "excuse must end on the promotion punchline"
    return text


def main() -> None:
    text = check_excuse(" ".join(ENTRY.split()))
    assert 1 <= len(text) < 200, f"entry is {len(text)} chars, gate is under 200"
    assert "\n" not in text, "entry must be a single line"
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
