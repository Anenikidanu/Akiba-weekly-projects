import string


def clean_text(text):
    text = text.lower()

    for punctuation in string.punctuation:
        text = text.replace(punctuation, "")

    return text


def count_words(text):
    words = clean_text(text).split()
    return len(words)


def count_characters(text):
    return sum(1 for char in text if not char.isspace())


def count_vowels_consonants(text):
    vowels = 0
    consonants = 0

    for char in text.lower():
        if char in "aeiou":
            vowels += 1
        elif char.isalpha():
            consonants += 1

    return vowels, consonants


def find_longest_word(text):
    words = clean_text(text).split()

    if not words:
        return None

    longest = words[0]

    for word in words:
        if len(word) > len(longest):
            longest = word

    return longest


def count_word_frequency(text):
    words = clean_text(text).split()
    frequency = {}

    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1

    return frequency


def find_repeated_words(text):
    frequency = count_word_frequency(text)
    repeated = []

    for word, count in frequency.items():
        if count > 1:
            repeated.append(word)

    return repeated


def five_most_frequent_words(text):
    frequency = count_word_frequency(text)
    sorted_words = sorted(
        frequency.items(),
        key=lambda item: item[1],
        reverse=True
    )

    return sorted_words[:5]


def analyze_text(text):
    vowels, consonants = count_vowels_consonants(text)

    print("\n--- TEXT ANALYSIS ---")
    print("Words:", count_words(text))
    print("Characters excluding spaces:", count_characters(text))
    print("Vowels:", vowels)
    print("Consonants:", consonants)
    print("Longest word:", find_longest_word(text))
    print("Word frequency:", count_word_frequency(text))
    print("Repeated words:", find_repeated_words(text))
    print("Top five words:", five_most_frequent_words(text))


paragraph = input("Enter a paragraph: ")
analyze_text(paragraph)