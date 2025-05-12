shows = [
    "      jyd rey mercado",
    "   jenny mae mercado    ",
    "  roselyn mercado",
    "    james mercado    ",
    "samantha jane mercado"
]


def main():
    cleaned_shows = []
    for show in shows:
        cleaned_shows.append(show.strip().title())

    print(f"{cleaned_shows}")
    print(' '.join(cleaned_shows))

main()
