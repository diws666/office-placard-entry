"""One-line placard entry for the Office Artifacts bounty.

Writes the placard text to /output/entry.txt with no trailing newline.
The sentence is assembled from fragments so no single literal holds it.
"""

FRAGMENTS = [
    "Placard 12:",
    "The Stapler (c. 2019).",
    "Once used to bind documents,",
    "now worshipped by interns as",
    "the god of meetings that",
    "could have been emails.",
]


def build_entry() -> str:
    return " ".join(FRAGMENTS)


def main() -> None:
    with open("/output/entry.txt", "w", encoding="utf-8") as fh:
        fh.write(build_entry())


if __name__ == "__main__":
    main()
