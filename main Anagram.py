# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


#def find_anagram(word, anagram):
    # [assignment] Add your code here
word = input("Enter your base word: ")
Word2 = input("Enter your comparative word: ")



if len(word) == len(Word2):
    if sorted(word) == sorted(Word2):
        print("True!", word, "and", Word2, "are", "Anagram") 
    else:
        print("False!", word, "and",  Word2, "are", "not", "Anagram") 
    #return True
else:
    print("False!", word, "and",  Word2, "are", "not", "Anagram")
