# Question 3: Modify the previous program such that only the users Alice and Bob are greeted with their names.

# taken from: https://adriann.github.io/programming_problems.html


name = input("What is your name?")

if (name == "ALice") or (name == "Bob"):
    print("Hello %s, How are you?" %(name))

else:
    print("Hello stranger!")




name = input("What is your name?")

if (name=="Bob") or (name=="Alice"):
    print("Hello %s, How are you?" %(name))
else:
    print("Hello lowly peasant!")