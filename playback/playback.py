# ProblemSet0:Playback of jeoydori (Jyd Rey Mercado)

def strip(words):
    #stripped_words = []
    stripped_words = words.strip().rsplit()
    return stripped_words

def main():
    words = str(input("Type a message: "))
    stripped_words = strip(words)

    print('...'.join(stripped_words))

main()

