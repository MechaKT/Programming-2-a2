# Quiz Game

points = 0

print("What's the best game?")
answer = input().strip("!?,.() ").upper()
if answer == "ONESHOT":
    print("NICE. YOU'RE RIGHT.")
    points+=1
else:
    print("Nice try, but there's a much better game called Oneshot out there :sunglasses:")
print("Objectively, what is the *coolest* color?")
answer = input().strip("!?,.()").upper()
if answer == "BLUE":
    print("Yes! Everyone knows blue is the best color!")
    points+=1
else:
    print("Nope, good choice, but it's not blue.")

print("Math question! What's 6^3*9(0-2) ?")
answer = int(input().strip("!?.,()"))
if answer == -3888:
    print("Yessir! You know your maths!")
    points+=1
else:
    print("Nope. Check your order of operatiopns a bit better! It should be -3888.")

print("Which of the following describes the Mitochondria?")
print("(A) Powerhouse of cell (B) Housecleaner of cell (C) Dishwasher of cell")
answer = input().strip("!?,.()").upper()
if answer == "A":
    print("Good job! We all love a little bit of energy!")
    points+=1
else:
    print("Nope. The mitochondria is a powerhouse! You should know this!")

print("Final question! What is the best school subject?")
print("(A) Math (B) Science (C) Programming (D) Sleep")
answer = input().strip("!?.,()").upper()
if answer == "C":
    print("Without a doubt! the best and most fun course!")
    points+=1
elif answer == "D":
    print("I wish that was a school subject too kid. Have a half mark for that.")
    points+=0.5
else:
    print("Nope, try a more... beep boop... subject.")

print(f"And now the quiz is done! It looks like you got {points}")
percent = (points / 5)*100
print(f"Total percentage... {percent} percent!")

