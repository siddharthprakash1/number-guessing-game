'''enemies=5
def increase_enemies():
    enemies=2
    print(f"enemies inside the function :{enemies}")
increase_enemies()
print(f"enemies outside function:{enemies} ")
def i_e():
    global enemies
    enemies+=1
    print(f"enemies inside the function :{enemies}")
i_e()
print(f"enemies outside function:{enemies} ")
  '''  
#always put the constants in upper case and variables in lower case
#EXAMPLE1:09(do all the examples on your own )
'''def a_function(a_parameter):
    a_variable = 15
    return a_parameter
 
a_function(10)
print(a_variable)'''
#EXAMPLE2:
'''i = 50
def foo():
    i = 100
    return i
 
foo()
print(i)'''
#EXAMPLE3:
'''def bar():
    my_variable = 9
 
    if 16 > 9:
      my_variable = 16
 
    print(my_variable)
 
bar()'''
import random 
l=[]
for i in range(100):
    l.append(i)
print("welcome to the number guessing game")
print("I'm thinkin of a number between 1 and 100:")
number_choosen=random.choice(l)
print(number_choosen)
def difficult():
    for i in range(5):
        n=int(input("Make a Guess:"))
        if number_choosen>n:
            print("Too low")
            print("Guess again")
            print("you have ",5-i,"tries remaning")
        elif number_choosen<n:
            print("Too High")
            print("Guess again")
            print("you have ",5-i,"tries remaning")
        elif number_choosen==n:
            print("You win ")
def easy():
    for i in range(10):
        n=int(input("Make a Guess:"))
        if number_choosen>n:
            print("Too low")
            print("Guess again")
            print("you have ",10-i,"tries remaning")
        elif number_choosen<n:
            print("Too High")
            print("Guess again")
            print("you have ",10-i,"tries remaning")
        elif number_choosen==n:
            print("You win ")

choice=input("Choose a difficulty. Type 'easy' or 'hard' :")
if choice=="hard":
    difficult()
elif choice=="easy":
    easy()
