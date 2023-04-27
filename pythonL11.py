print("Welcome to this game!")

playing = input("Do you want to play this game? :")

if playing.lower() != "yes":
    quit()

print("Lets play NIGGA)")
score = 0

answer = input("What is the capital of Tajikistan? :")
if answer.lower() == "dushanbe":
    print("Answer is correct!)")
    score += 1
else:
    print("Your answer is wrong.(")

answer = input("What is the population of Tajikistan? :")
if answer.lower() == "11m":
    print("Answer is correct!)")
    score += 1
else:
    print("Your answer is wrong.(")

answer = input("Who is the best player in the world? :")
if answer.lower() == "ronaldo":
    print("Yes bro you're right ")
    score += 1
else:
    print("Your answer is WRONG !)")

answer = input("Who is the GOAT? :")
if answer.lower() == "ronaldo":
    print("You're RIGHT BRO")
    score += 1
else:
    print("The answer is WRONG boyyy.(")

print("Your score is " + str(score) )
print("Your percentage is " + str((score / 4) * 100))