number_of_credits = int(input("How many credits you are taking this semester? "))
if number_of_credits >= 12:
    print("You are a full-time student")
elif number_of_credits >= 6:
    print("You are a half-time student")
else:
    print("You are less than half-time")
