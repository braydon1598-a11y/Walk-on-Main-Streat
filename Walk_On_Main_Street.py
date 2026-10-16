import os
import random


def make_pizza():

    os.system("cls")
    repeat = True
    list_of_toppings = []
    
    print('Welcome to the pizzeria!!')
    print('what would you like on your pizza?')
    print("ingredients:\npepperoni\ncheese\nolives\nonions\nchicken\n\n")
    print("enter the ingredients one at a time. when you're done say 'done'\n\n")

    while repeat:
        topping = input("=>")
        list_of_toppings.append(topping)

        if topping == "done":
            os.system("cls")
            repeat = False

    for topping in list_of_toppings:
        if topping != "done":
            print(f"adding {topping} to your pizza!\n")
    
    print("\n\nyour pizza is ready!!")
    input("redo?")
    os.system("cls")

def icecream():
    os.system("cls")

    print("welcome to the ice cream shop!!")
    print("what flavor would you like?")
    print("\nflavors:\nstrawberry\nchocolate\nvanilla\nmint\n")
    icecream = input("=>")
    os.system("cls")

    print(f"here's your {icecream} flavored ice cream!!")
    input("redo?")
    os.system("cls")

def store():
    os.system("cls")

    print("hello, there\nCan I get you anything?")
    input("do you have any? ")
    os.system("cls")

    print(f"I think we do, check row {random.randint(1, 10)} for it!!")
    input("redo?")
    os.system("cls")

while True:
    print("you are going on a walk on Main Street and you feel hungry.\n\ndo you want to go to the pizza shop, ice cream shop, or the store?\n")
    print("say 'stop' to end the program\n\n")
    answer = input("=>")
    answer = answer.lower()

    if answer == "pizza shop": 
        make_pizza()
    elif answer == "ice cream shop":
        icecream()
    elif answer == "the store":
        store()
    elif answer == "stop":
        break
    else:
        os.system("cls")
        print("sorry. please type exactly 'pizza shop' 'ice cream shop' or 'the store' or say 'stop' to stop the program\n")
        
print("program ended")
