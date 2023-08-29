def tables(num):
    for i in range(11):
        print(f"{num} X {i} = {num * i } ")

def repeat(num):
    for i in range(num):
        print(f"This code made me repeat {num} for {num1} times")

print("1.Tables \n2.Repeat")
Option = int(input("Choose Option: "))
num = int(input("Enter Number: "))

if Option == 1:
   tables(num)
elif Option == 2:
    repeat(num)
else:
    print("Invalid Option")
