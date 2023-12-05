sum=0
count=0
for i in range(51):
    if i%2==0:
        sum+=i
        if i%3==0:
            print('Three')
            count+=1
        elif i%5==0:
            print('Five')
            count+=1
        else:print(i)
print('The sum of the even numbers is: ',sum)
print('The count of the numbers replaced by "Three" and "Five" are: ',count)
        