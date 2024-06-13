import sys
import os
import string

cwd = os.getcwd()
path_file = os.path.join(cwd, 'dictionary.txt')

dict_file = {}

word_list_clean = []

 # Define the range of single-letter alphabets from 'a' to 'z'
permissable = list(string.ascii_lowercase)

def dict_clean(file):
    try:
        with open(file) as in_file:
            loaded_text = in_file.read().strip().split('\n')
            loaded_text = [x.lower() for x in loaded_text]
            # return loaded_text
            # print(type(loaded_text))
            for word in loaded_text:
                if len(word) > 1:
                    word_list_clean.append(word)
                    print("No Single letter found in the dictionary")
                    break
                elif len(word) ==1 and word in permissable:
                    word_list_clean.append(word)
                    print("Single letter found, there you go !!!")
                else:
                    continue
            # print("{}".format(word_list_clean))
    except IOError as e:
        print(f"\nError Opening. Terminating program {e, file}", file=sys.stderr)
        sys.exit(1)


dict_clean(path_file)
