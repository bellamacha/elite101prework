#variables
userHelpOne = "example choice 1"
userHelpTwo = "example choice 2"
userHelpThree = "example choice 3"
userHelpFour = "example choice 4"

#welcoming the user
user_name = input("What is your name?\n")
print ("\nWelcome " + user_name + "!")
user_age = int(input("What is your age?\n"))
print("\nHow may we help today? (enter to show options)")
input("")


print("1.) " +  userHelpOne )
print("2.) " +  userHelpTwo )
print("3.) " +  userHelpThree )
print("4.) " +  userHelpFour )
print("5.) Exit")

user_help = input("\nSelect a choice\n -> ")
if user_help == "1":
  print("you chose " + userHelpOne)
elif user_help == "2":
  print("you chose " + userHelpTwo)
elif user_help == "3":
  print("you chose " + userHelpThree)
elif user_help == "4":
  print("you chose " + userHelpFour)
elif user_help == "5":
  print("Thank you for visiting our service !")
  exit(1)
  