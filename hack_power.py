def hack_calculator(hack: str, _letters={'a': 1, 'b': 2, 'c': 3}, _phrases={'ba': 10, 'baa': 20}):
    letters = _letters
    phrases = _phrases
    letters_occurrences = {}
    letter_error = False

    for letter in letters:
        letters_occurrences[letter] = 0
    points = 0

    for letter in hack:
        if letter in letters:
            letters_occurrences[letter] += 1
            points += letters[letter] * letters_occurrences[letter]
        else:
            letter_error = True
            points = 0
            break

    if letter_error:
        return points

    for phrase, point in sorted(phrases.items(), key=lambda x: x[1], reverse=True):
        index = hack.find(phrase)
        while index >= 0:
            points += point
            hack = hack.replace(phrase, '_', 1)
            index = hack.find(phrase)
    return points


if __name__ == '__main__':
    import sys
    print(hack_calculator(sys.argv[1]))
