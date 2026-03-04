vw = "aeiou"
def analyze_word(word):
    count = 0
    w_len = len(word)
    for c in word:
        if c.lower() in vw:
            count += 1
    w_upp = word.upper()

    print(f" Length: {w_len} \n Vowels: {count}\n Uppercase: {w_upp}")

w = input("Enter a word: ")
analyze_word(w)
