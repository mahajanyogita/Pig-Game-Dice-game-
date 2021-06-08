import random

print("Let's Play PIG!\n")
print("* See how many turns it takes you to get to 20.",
      "* Turn ends when you hold or roll a 1.",
      "* If you roll a 1, you lose all points for the turn.",
      "* If you hold, you save all points for the turn.",sep="\n")
max_score = 20
total_score = 0
Turn = 0
while total_score < max_score:
    Turn += 1
    turn_score = 0
    print("\nTURN ", Turn)
    while True:
        choice = input("Roll or Hold?(r/h):\t")
        if choice == 'r':
            num = random.randint(1, 6)
            print("Die :", num)
            if num == 1:
                turn_score = 0
                print("Turn Over ,No score")
                break
            else:
                turn_score += num
        elif choice == 'h':
            print("Score for the Turn", Turn, "is", turn_score)
            break
        else:
            print("Enter valid character")
    total_score = total_score + turn_score
    print("Total Score :", total_score)

print("Congratulations! , You Finished it in", Turn, "Turns")

