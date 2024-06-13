import sys
import os
import time
start_time = time.time()
# import enchant 
# import load_dictionary
cwd = os.getcwd()
file_path = os.path.join(cwd, '2of4brif.txt')
print(file_path)

def load_dictionary_file(file):
    """
    this fucntion is to load the dictionary file
    """
    try:
        with open(file) as in_file:
            load_dict = in_file.read().strip().split('\n')
            load_dict = [x.lower() for x in load_dict]
            return load_dict
    except IOError as e:
            print(f"\nError Opening. Terminating program {e, file}", file=sys.stderr)
            sys.exit(1)

    
word_list = load_dictionary_file(file_path)
# print(word_list)


# word_list = load_dictionary(file_path)

def palingram():
    """
    checking paligrams function
    """
    pali_words = []
    words = set(word_list)
    for word in words:
        word_len = len(word)
#  The word’s length determines the indexes the program uses to slice
# through the word, looking for every possible reversed word-palindromic
# sequence combination

        rev_word = word[::1]
        if word_len > 1:
            for i in range(word_len):
                if word[i:] == rev_word[:word_len-i] and rev_word[word_len-i:] in words:
                    pali_words.append((word, rev_word[word_len-i:]))
                if word[:i] == rev_word[word_len-i:] and rev_word[:word_len-i] in words:
                    pali_words.append((rev_word[:word_len-i], word))       
    return pali_words

palingrams = palingram()
palingrams_sorted = sorted(palingrams)

print("\nNumber of palingrams = {}\n".format(len(palingrams_sorted)))

for first, second in palingrams_sorted:
    print('{} {}'.format(first, second))

end_time = time.time()

print("Runtime for this program was {} seconds.".format(end_time - start_time))























# """
#     Load  a text file as a list

#     Arguments:
#     -text file name( and directory path, if needed)

#     Returns:
#     - A list of all words in a text file in lower case

#     Requires-import sys

# """

# import sys
# import os
# import time


# start_time = time.time()

# end_time = time.time()

# # path = 'D:/Desktop/Personal/Machine_Learning/Python_Programming/python_oops/12dicts-6.0.2/dictionary.txt'
# cwd = os.getcwd()
# # # print(cwd)
# # file_path = os.path.basename(path)
# # print(file_path)

# # file_path = os.path.basename(cwd)
# # print(file_path)
# file_path = os.path.join(cwd, 'dictionary.txt')

# print(file_path)

# def load(file):
#     """ Open a text file & return a list of lowercase strings"""
#     try:
#         with open(file) as in_file:
#             loaded_text = in_file.read().strip().split('\n')
#             loaded_text = [x.lower() for x in loaded_text]
#             return loaded_text
#             # print(type(loaded_text))
#     except IOError as e:
#         print(f"\nError Opening. Terminating program {e, file}", file=sys.stderr)
#         sys.exit(1)

# # """
# # Load digital dictionary file as list of words 
# # Create a empty list to hold palindromes
# # Loop through each word in the word_list:
# #     if word sliced if forward is the same as the slice backward:
# #        append word to palindrome list

# # print palindrome lists  

# dict_file = load(file_path)

# def find_palingrams():
#     """
#     Find dictionary palingrams
#     """
#     pali_list = []
#     words = set(dict_file)
#     for word in words:
#         end = len(word)
#         rev_word = word[::1]
#         if end > 1:
#             for i in range(end):
#                 if word[i:] == rev_word[:end-i] and rev_word[end-i:] in dict_file:
#                     pali_list.append((word, rev_word[end -i]))
                
#                 if word[:i] == rev_word[end-i:] and rev_word[:end-i] in dict_file:
#                     pali_list.append((rev_word[:end-i], word))
#             return pali_list
        
# print(start_time)
# palingrams = find_palingrams()
# # sort palingrams on first word 
# palingrams_sorted = sorted(palingrams)

# #display the list of palingrams
# print("\nNumber of palingrams = {}\n".format(len(palingrams_sorted)))

# for first, second in palingrams_sorted:
#     print("{} {}".format(first, second))
# print(end_time)
