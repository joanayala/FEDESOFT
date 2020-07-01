#My first basic calc: This calc lets you operate 2 numbers. 
#Developer: Joan C. Ayala.
#Create date: 01 jul 2020

#Get first number
print("First number: ")
n1 = int(input())
#Get second number
n2 = int(input("Second number: "))
#Show menu options
print("::: Operations Menu :::")
print("[1]. Add \n [2]. Subs \n [3]. Mult \n [4]. Div \n")
#Get option
op = input("Please press a number option: ")

if op == "1" :
    ans = n1 + n2
    print("The add is: ", ans)
elif op == "2" :
    ans = n1 - n2
    print("The subst is: ", ans)
elif op == "3" :
    ans = n1 * n2
    print("The mult is: ", ans)
elif op == "4" :
    ans = n1 / n2
    print("The div is: ", ans)
else :
    print("Invalid option")


