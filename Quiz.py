# Quiz Game

# Steven Ouyang

# Score
points = 0
#?
truePoint = 0
# Ask question
print("What's the best game?")
answer = input().strip("!?,.() ").upper()
# Reply for answer
if answer == "ONESHOT":
    print("NICE. YOU'RE RIGHT.")
    points += 1
else:
    print("Nice try, but there's a much better game called Oneshot out there :sunglasses:")

# Question 2
print("Objectively, what is the *coolest* color?")
answer = input().strip("!?,.()").upper()
if answer == "BLUE":
    print("Yes! Everyone knows blue is the best color!")
    points += 1
else:
    print("Nope, good choice, but that color isn't blue.")

# Question 3
print("Math question! What's 6^3*9(0-2) ?")
answer = int(input().strip("!?.,()"))
if answer == -3888:
    print("Yessir! You know your maths!")
    points += 1
else:
    print("Nope. Check your order of operatiopns a bit better! It should be -3888.")

# Question 4
print("Which of the following describes the Mitochondria?")
print("(A) Powerhouse of cell (B) Housecleaner of cell (C) Dishwasher of cell")
answer = input().strip("!?,.()").upper()
if answer == "A":
    print("Good job! We all love a little bit of energy!")
    points += 1
else:
    print("Nope. The mitochondria is a powerhouse! You should know this!")

# Question 5
print("Final question! What is the best school subject?")
print("(A) Math (B) Science (C) Programming (D) Sleep")
answer = input().strip("!?.,()").upper()
if answer == "C":
    print("Without a doubt! the best and most fun course!")
    points += 1
elif answer == "D":
    print("I wish that was a school subject too kid. Have a half mark for that.")
    points += 0.5
else:
    print("Nope, try a more... beep boop... subject.")


# Final calculation and output
print(f"And now the quiz is done! It looks like you got {points}")
percent = (points / 5)*100
print(f"Total percentage... {percent} percent!")


# From here onward, the true quiz begins.
if points == 5:
    print("Great! Seems like you got all the questions right!, this must mean you're")
    print("ready for the REAL QUIZ, RIGHT?")

    # Question 1
    print("From the 18-19th century, there was a famous debunked automaton")
    print("that managed to fool even Charles Babbage, and Napoleon. The robot was claimed")
    print("to be a robot that could play chess, but in reality was controlled by a human.")
    print("The name of this robot is called:")
    print("(A) Chess Master (B) The Master (C) The Turk (D) The Turk Master")
    answer = input().strip("!?,.()").upper()
    if answer == "C":
        print("Correct.")
        truePoint += 1
    else:
        print("Incorrect.")

    # Question 2
    print("H.P. Lovecraft is most famous for his creation of the subhorror genre cosmic ")
    print("and eldritch horror. The Outer God in charge of acting as both the Key and ")
    print("Gate, is:")
    print("(A) Shub-Niggurath (B) Yog-Sothoth (C) Azathoth (D) Cthulhu")
    answer = input().strip("!?,.()").upper()
    if answer == "B":
        print("Correct.")
        truePoint += 1
    else:
        print("Incorrect.")

    # Question 3
    print("Ryu from Streetfighter has an attack (tatsumaki senpukyaku) where he")
    print("swirls his legs around towards the enemy. When should it be used in Neutral?")
    print("(A) To approach the enemy (B) To punish projectiles (C) To get more hits in ")
    print("(D) To be able to get out safely")
    answer = input().strip("!?,.()").upper()
    if answer == "B":
        print("Correct.")
        truePoint += 1
    else:
        print("Incorrect.")

    # Question 4
    print("The technique in Tetris in which you perform a T-spin double and a T-spin triple")
    print("in succession is called what by the community?")
    print("(A) T2 to T3 (B) Turbo Turn Cannon (C) BT Cannon (D) DT Cannon (E) Spin Cannon")
    answer = input().strip("!?,.()").upper()
    if answer == "D":
        print("Correct.")
        truePoint += 1
    else:
        print("Incorrect.")

    # Question 5
    print("Finale: In Russian folktale, there is a person who will threaten you to")
    print("figure out his name, otherwise he will eat your child. His name is:")
    answer = input().strip("?!.,()").upper()
    if answer == "RUMPELSTILTSKIN":
        print("Splendidly done. Correct.")
        truePoint += 1
    else:
        print("Incorrect.")
    print(f"And now the quiz is done! It looks like you got {truePoint}")
    percent = (truePoint / 5) * 100
    print(f"Total percentage... {percent} percent!")
    if truePoint == 5:
        print("Amazing... You got EVERYTHING right! You really are a genuine Quiz Master!!")
    elif truePoint < 1:
        print("It is only fair that you got no right answers. This is a hard quiz.")