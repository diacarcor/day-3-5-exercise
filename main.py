# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
#Combine both lower names
names = name1.lower() + name2.lower()

#Calculate digit one
digit_one = 0
digit_one += names.count("t") + names.count("r") + names.count("u") + names.count("e")

#Calculate digit two
digit_two = 0
digit_two += names.count("l") + names.count("o") + names.count("v") + names.count("e")

#Get score
score = digit_one * 10 + digit_two

#Check compatibility
message = f"Your score is {score}"

if (score < 10) or (score > 90):
  message = message + ", you go together like coke and mentos."
elif (score >= 40) and (score <= 50):
  message = message + ", you are alright together."
else:
  message = message + "."
  
print(message)