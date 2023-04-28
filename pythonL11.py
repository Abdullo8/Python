print("Welcome to this game!")

playing = input("Do you want to play this game? : ")

if playing.lower() != "yes":
    quit()

print("Lets play it! ")
score = 0

answer = input("What is the capital of Tajikistan? : ")
if answer.lower() == "dushanbe":
    print("Answer is correct!)")
    score += 1
else:
    print("Your answer is wrong.(")

answer = input("What is the population of Tajikistan? : ")
if answer.lower() == "11m":
    print("Answer is correct!)")
    score += 1
else:
    print("Your answer is wrong.(")

answer = input("Who is the best player in the world? : ")
if answer.lower() == "ronaldo":
    print("Your answer is correct! ")
    score += 1
else:
    print("Your answer is WRONG !)")

answer = input("Who is the GOAT? : ")
if answer.lower() == "ronaldo":
    print("Your answer is correct")
    score += 1
else:
    print("Wrong answer! ")

answer = input("How many countries in the world? : ")
if answer.lower() == "196":
    print("Correct answer! ")
    score += 1

else:
    print("Wrong answer! ")

answer = input("Who was Elizabeth 2? : ")
if answer.lower() == "queen":
    print("Correct answer! Good job! ")
    score += 1
else:
    print("Wrong answer! Why you don't know her? ")

answer = input("Who won the Balloon d'or in 2022? : ")
if answer.lower() == "benzema":
    print("Correct answer! Execellent! ")
    score += 1
else:
    print("Wrong answer! Search from internet NOW! You should know this!")

answer = input("When was the last World War? : ")
if answer.lower() == "1945":
    print("Correct answer!")
    score += 1
else:
    print("Wrong answer")

answer = input("Who is Messi? : ")
if answer.lower() == "football player":
    print("Yes that is true! ")
    score += 1
else:
    print("WRONG ANSWER! Why you don't know him? ")

answer = input("Which team won the 2022 WORLD CUP ? : ")
if answer.lower() == "argentina":
    print("Correct answer! ")
    score += 1
else:
    print("WRONG ANSWER! Why you didn't watch that match?")

answer = input("Did you watch that match ? : ")
if answer.lower() == "yes":
    print("Good job! i've watched too.)")
    score += 1
else:
    print("Why you didn't watch it? Go and watch it NOW! " )


print("Your score : " + str(score) )
print("Your percentage : " + str((score / 11) * 100))