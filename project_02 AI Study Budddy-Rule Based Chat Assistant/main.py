# Rule Based AI Python chatBot

import datetime
import time

name = input("Swagat hai, Enter your name : ")
presentHour = datetime.datetime.now().hour

if 5<= presentHour <=11:
    print("Good morning, ", name)
elif 11<=presentHour<=17:
    print("Good afternoon, ", name)
elif 17<=presentHour <=20:
    print("Good evening, ", name)
else:
    print("Good night, ", name)

print("Namaste! Welcome to your Buddy ChatBot")
print("You can ask me basic question, Type 'bye' to exit from the bot")

# Chatbot Memory Creation [dictionary of responses]

responses ={
    "hello":" Hi, Welcome. How can I help you?",
    "how are you":" I am very fine. Thank you",
    "who are you":" I am smart AI chatbot ",
    "motivate me":" Keep going. Every bug of your project makes you a better coder",
    "tell me about python":" Python is powerful-it can do AI, Automation, and much more!",
    "happy":" Great to hear that",
    "bye":" Good Bye! Keep learning and Keep Smiling.",
}

# Method/Function to get responses og ChatBot

def getResponsesOfBot(userQuestion):
    userQuestion= userQuestion.lower()
    for eachkey in responses:
        if eachkey in userQuestion:
            return responses[eachkey]

    return "I am not able to tell that yet. I am still in learning mode"



# take user input
while True:
    userInput = input("Please ask your question : ")
    reply = getResponsesOfBot(userInput)
    print("Bot Response :",reply)

    if "bye" in userInput.lower():
        break