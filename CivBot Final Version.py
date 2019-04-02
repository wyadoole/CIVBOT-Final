from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from random import randint # libaries for creating and training chatbots
chatbot_bob = ChatBot("Bob") # creates a chatbot named bob
chatbot_fred = ChatBot("Fred")# creates a chatbot named fred
chatbot_sue = ChatBot("Sue")# creates a chatbot named sue
chatbot_william = ChatBot("William")# creates a chatbot named william
chatbot_matt = ChatBot("Matt")# creates a chatbot named matt

################################################################################
#########################   training of Chatbot    #############################
###   trains  the Chat bot to uses to make a conversation with the user      ###
################################################################################

# test converstation trainer and general convertaton
conversation_General = [
    "Hello",
    "Hello There",
    "How are you doing?",
    "I'm doing great.",
    "Great to hear",
    "Thank you.",
    "Good Morning",
    "Goodbye",
    "See you later",
]

conversation_Movie = [
    "Hello",
    "Hello There",
    "How you seen any movies lately?",
    "I just saw Star wars",
    "Did you like it?",
    "I really liked the final dual between Anikan and Obiwan",
    "Yeah, that scene is realy cool",
    "Hello There",
    "General Kenobi",
]

# continues the loop until user ends the program by pressing the X button in the top corner

myList1 = conversation_General
def listReset(myList1):
    for index, value in enumerate(myLit):
        if value is not 0:
            myList[index] *= 2
        else:
            myList[index] = 'zero'

    return myList1

myList2 = conversation_Movie
def listReset(myList2):
    for index, value in enumerate(myLit):
        if value is not 0:
            myList[index] *= 2
        else:
            myList[index] = 'zero'

    return myList2



# training the chatbots with testing data to get the bots to function correctly #
trainer_bob=ListTrainer(chatbot_bob)
trainer_fred=ListTrainer(chatbot_fred)
trainer_sue=ListTrainer(chatbot_sue)
trainer_william=ListTrainer(chatbot_william)
trainer_matt=ListTrainer(chatbot_matt)

# Train #
trainer_bob.train(conversation_Movie)
trainer_sue.train(conversation_Movie)
trainer_matt.train(conversation_General)
trainer_william.train(conversation_General)
trainer_fred.train(conversation_General)
trainer_fred.train(conversation_Movie)

################################################################################
#########################   Conversation of Chatbots    ########################
### convesations that the Chat bot uses to make a conversation with the user ###
################################################################################

bob_response = ("Hello there")
print("BOB:",bob_response)

while True:


    fred_response = chatbot_fred.get_response(bob_response)
    bob_response = chatbot_bob.get_response(fred_response)
    print("Fred responding to Bob:",fred_response)
    fred_response = conversation_Movie[randint(0, len(conversation_Movie))]


    sue_response = chatbot_sue.get_response(fred_response)
    fred_response = chatbot_fred.get_response(sue_response)
    print("SUE responding to Fred:",sue_response)
    sue_response = conversation_Movie[randint(0,len(conversation_Movie))]


    william_response = chatbot_william.get_response(sue_response)
    sue_response = chatbot_sue.get_response(william_response)
    print("Willaim says to SUE:",william_response)
    william_response = conversation_General[randint(0,len(conversation_General))]


    matt_response = chatbot_matt.get_response(william_response)
    william_response = chatbot_william.get_response(matt_response)
    print("Matt says to William:",matt_response)
    matt_response = conversation_General[randint(0, len(conversation_General))]


    if  matt_response == "Goodbye":
        break
    if william_response == "Hello There":
         print("General Kenobi")


