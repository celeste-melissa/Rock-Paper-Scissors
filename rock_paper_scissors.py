import random
print("====================")
print("Rock Paper Scissors")
print("====================")

print("1) ✊")
print("2) ✋")
print("3) ✌️")

player = int(input("Pick a number: "))
computer = random.randint(1,3)

print("You chose:", player)
print("CPU chose:", computer)

if player not in [1,2,3]:
    print("Invalid choice! Please pick 1, 2, or 3.")
    exit()
if player > computer:
    print("The player won!")
elif player < computer:
    print("The computer won!")
else:
    print("Tie!")
    