#  Write a program to count vowels and consonants in a given string.
def countVowelsConsonants(str):
    if str.isalpha():
        str = str.lower()
        vowel = 0
        consonant = 0
        vowelList = ["a", "e", "i", "o", "u"]
        for i in str:
            if (i in vowelList):
                vowel += 1
            else:
                consonant += 1
        return vowel, consonant
    else:
        return False   
    
str = input("string = ")
result = countVowelsConsonants(str)
if (result == False):
    print("Enter valid inputs")
else:
    print("Number of Vowels = ", result[0])
    print("Number of Consonants = ", result[1])
    