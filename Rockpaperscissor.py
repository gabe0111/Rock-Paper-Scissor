import random

rock = "✊"
paper = "✋"
scissors = "✌"

print("___________________")
print("Rock Paper Scissors")
print("___________________")
print("1. ✊")
print("2. ✋")
print("3. ✌")

print("Pick a number: ")
player = int(input())
computer = random.randint(1,3)

playerSign = 0
computerSign = 0

if player == 1:
    playerSign = "✊"
elif player == 2:
    playerSign = "✋"
elif player == 3:
    playerSign = "✌"
else:
    print("Tf did u type?")

if computer == 1:
    computerSign = "✊"
elif computer == 2:
    computerSign = "✋"
elif computer == 3:
    computerSign = "✌"
    

print(f"You chose: {playerSign}")
print(f"CPU chose: {computerSign}")

if player == computer:
    print("It is a tie!")
elif (player == 1 and computer == 3) or (player == 2 and computer == 1) or (player == 3 and computer == 2):
    print("You won! The computer lost")
else:
    print("The computer won! You lost")
