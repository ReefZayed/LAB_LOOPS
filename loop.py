for n in range(45 ,210):
    if n == 100:
        continue
    print(n)
    if n == 205:
     break

print("_"*20)

mltuNum= input("what is the product of 7 * 24 ?")

while int(mltuNum)!=168:
    print("Your Answer is wrong try again..") 
    print(input("what is the product of 7 * 24 ?"))
else:
    print("You answered this Question correctly")  