try:
    a = input("enter something: ")
    b = int(input("enter any number: "))

    print(a+b) 

except (TypeError,ValueError) as v:  
    print(v)

print("dhanyawaad!") 