import random

computer_choice=random.choice(['rock', 'paper', 'scissors'])
user_choice=input("Do you pick rock, paper, or scissors?\n")

if computer_choice == user_choice:
    print("How could we have picked the same thing? Ah... I'm not feeling wellnhBSAIO8qy2982hUHIDiy82heiIH2IEwgwuYEHvvvvvvvvvvvv")
elif computer_choice == 'scissors' and user_choice == 'rock':
    print("Ugh... let's have a rematch.")
elif computer_choice == 'scissors' and user_choice == "paper":
    print("Hah! You've been bested by AI.")
elif computer_choice == 'rock' and user_choice == 'paper':
    print('You went late, cheater!')
elif computer_choice == 'rock' and user_choice == "scissors":
    print("You'll never beat me.")
elif computer_choice == 'paper' and user_choice == 'rock':
    print("You've been suffocated inside a white bag")
elif computer_choice == "paper" and user_choice == "scissors":
    print("Ugh... cut into pieces...")
