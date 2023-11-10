print("The Love Calculator is calculating your score...")
name1 = input("What is your name? ")
name2 = input("What is their name? ")
name = name1+name2
lower_name = name.lower()
t = lower_name.count("t")
r = lower_name.count("r")
u = lower_name.count("u")
e = lower_name.count("e")
ll = lower_name.count("l")
o = lower_name.count("o")
v = lower_name.count("v")
ee = lower_name.count("e")
first_digit = t + r + u + e
second_digit = ll + o + v + ee
percent_love = int((str(first_digit) + str(second_digit)))
if percent_love <= 10 or percent_love >= 90:
    print(f"Your score is {percent_love}, you go together like coke and mentos.")
elif percent_love >= 40 and percent_love <= 50:
    print(f"Your score is {percent_love}, you are alright together.")
else:
    print(f"Your score is {percent_love}.")