import random

print("""
1.Rock
2.Paper
3.Scissors""")

user_choce=int(input("Choose one of them number:"))

computer_list=["Rock","Paper","Scissors"]

random_number=random.randint(0,2)

computer_choce=computer_list[random_number]


if user_choce==1:
    if computer_choce=="Rock":
        print("Computer chose Rock.")
        print("It is a draw.")
    elif computer_choce=="Paper":
        print("Computer chose Paper.")
        print("You lose!")
    else:
        print("Computer chose Scisssors.")
        print("You won!")
elif user_choce==2:
    if computer_choce=="Rock":
        print("Computer chose Rock.")
        print("You won.")
    elif computer_choce=="Paper":
        print("Computer chose Paper.")
        print("It is a draw.")
    else:
        print("Computer chose Scisssors.")
        print("You lost!")
elif user_choce==3:
    if computer_choce=="Rock":
        print("Computer chose Rock.")
        print("you lost.")
    elif computer_choce=="Paper":
        print("Computer chose Paper.")
        print("You  won!")
    else:
        print("Computer chose Scisssors.")                 
        print("It is a draw.")       
else:
    print("You only can type 1,2 and 3.")
