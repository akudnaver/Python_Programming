
# import sys

# vowel = 'aeiouAEIOU'

# while True:
#     words = input("Please enter a word:\n")
#     consonant = ["blend", "java", "cpp", "cobol", "pascal", "react"]
    
#     append_way = "way"
#     append_ay = "ay"
#     new_words = []

#     if words == consonant:
#         new_words.append(words)

#         if new_words[0] in vowel:
#             pig_latin = new_words + append_way

#         else:
#             pig_latin = new_words[1:] + new_words[0] + append_ay
#         print()
#         print(f'{pig_latin}', file=sys.stderr)

#         try_again = input("\n\nTry again> (Press Enter eles n to stop)\n")

#         if try_again.lower() == "n":
#             sys.exit()


import sys


def convert_to_pig_latin(words):
    """
     Function to check the consonant and convert them to latin words
    """
    vowel = "aeiouwAEIOU"

    while True:
            # words = input("Plase enter a word to translate to its Pig Latin:\n")
        append_way = "way"
        append_ay = "ay"

        if words[0] in vowel:
            pig_latin = words +  append_way

        else:
            pig_latin = words[1:] + words[0] + append_ay

            # try_again = input("To Try again Hit Enter? Else hit n for No\n")

            # if try_again.lower() == "n":
            #     sys.exit()

        return pig_latin
                # print()
                # print(f'{pig_latin}', file = sys.stderr)


def main():
    """
    checking pig latin words from a given list 
    """
    words_to_test = ["hello", "apple", "banana", "umbrella", "grape"]

    pig_latin = [convert_to_pig_latin(word) for word in words_to_test]

    print(f'{pig_latin}', file=sys.stderr)

if __name__ == "__main__":
    main()
