n = int(input("enter any number: "))

if n < 0 :
    print("enter a postive number")
else:
    sum = 0
    while n > 0:
        sum += n
        n -= 1   
    
    print(sum)    