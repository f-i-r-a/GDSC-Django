word=input('please enter a word to check: ')
string=''
for i in range(len(word)-1,-1,-1):
        string+=word[i]
if string==word: print(f"the word {word} is palindrome")
else: print(f"the word {word} is not palodrone, because {word} is not equal to {string}")