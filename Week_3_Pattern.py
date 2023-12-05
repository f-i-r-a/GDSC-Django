def pattern():
    b=0
    e=3
    for i in range(49):
        if i==b:
            print(letter)
            b=i+e
            e+=2
        else:
            print(letter,end='')
letter=input('enter the pattern to be printed: ')
while 1:
    vowels='a i e o u'
    if len(letter)==1:
        if letter in vowels:
            letter=input('letter cannot be a vowel enter again: ')
        else:
            pattern()
            break
    else:
        letter=input('length of character has to be 1  enter again: ')