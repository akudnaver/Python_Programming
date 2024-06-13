"""
    Load  a text file as a list

    Arguments:
    -text file name( and directory path, if needed)

    Returns:
    - A list of all words in a text file in lower case

    Requires-import sys

"""

import sys
import os

# path = 'D:/Desktop/Personal/Machine_Learning/Python_Programming/python_oops/12dicts-6.0.2/dictionary.txt'
cwd = os.getcwd()
# # print(cwd)
# file_path = os.path.basename(path)
# print(file_path)

# file_path = os.path.basename(cwd)
# print(file_path)
file_path = os.path.join(cwd, '2of4brif.txt')

print(file_path)

def load(file):
    """ Open a text file & return a list of lowercase strings"""
    try:
        with open(file) as in_file:
            loaded_text = in_file.read().strip().split('\n')
            loaded_text = [x.lower() for x in loaded_text]
            return loaded_text
            # print(type(loaded_text))
    except IOError as e:
        print(f"\nError Opening. Terminating program {e, file}", file=sys.stderr)
        sys.exit(1)

dict_file = load(file_path)

palindromes = []

for word in dict_file:
    if word[:] == word[::-1]:
        palindromes.append(word)
print(palindromes)

# load(file_path)
