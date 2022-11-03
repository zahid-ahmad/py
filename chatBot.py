user = input("What's your name?")
print("Hello {}!".format(user))
user = input("Do you like ice cream?")
if user.lower() == "yes":
  user = input("Me too! What's your favorite ice cream?")
elif user.lower() == "no":
  user = input("Aw too bad. Do you like pizza?")
  if user.lower() == "yes":
    user = input("Me too! What's your favorite pizza?")

    print("Yes")
  else:
    print("Who doesn't like pizza?!")