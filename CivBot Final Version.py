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
# a  differant topic for the AI chatbot to use
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




# training the chatbots with testing data to get the bots to function correctly #
trainer_bob=ListTrainer(chatbot_bob) # trainer for bob
trainer_fred=ListTrainer(chatbot_fred) # trainer for fred
trainer_sue=ListTrainer(chatbot_sue) #trainer
trainer_william=ListTrainer(chatbot_william)
trainer_matt=ListTrainer(chatbot_matt)

# Train #
trainer_bob.train(conversation_Movie)# calls the movie converstation for bob -> to train
trainer_sue.train(conversation_Movie)# calls the movie converstation for sue -> to train
trainer_matt.train(conversation_General) # calls the general converstation for matt -> to train
trainer_william.train(conversation_General)# calls the general conversation for willaim -> to train
trainer_fred.train(conversation_General)#  calls the general conversation for fred -> to train
trainer_fred.train(conversation_Movie)# calls the movie conversation for fred -> to train

################################################################################
#########################   Conversation of Chatbots    ########################
### convesations that the Chat bot uses to make a conversation with the user ###
################################################################################

bob_response = ("Hello there") # greattings for chatbot application
print("BOB:",bob_response)# prints bob response

while True: # if true run loop until no responses are left


    fred_response = chatbot_fred.get_response(bob_response)# fred bots having converstation with bob about
    bob_response = chatbot_bob.get_response(fred_response) #gets bobs response so that fred can respond to it
    print("Fred responding to Bob:",fred_response)
    fred_response = conversation_Movie[randint(0, len(conversation_Movie))]


    sue_response = chatbot_sue.get_response(fred_response)# sues bots having converstation with fred about
    fred_response = chatbot_fred.get_response(sue_response)# gets freds response so that sue can respond to fred
    print("SUE responding to Fred:",sue_response) #prints sues response
    sue_response = conversation_Movie[randint(0,len(conversation_Movie))] # calls the list movie at the top of script for the chat bot to use as random response


    william_response = chatbot_william.get_response(sue_response)# william bot having a conversation with william  using movie  topic
    sue_response = chatbot_sue.get_response(william_response) # gets sues response so that willaim can responed to sue
    print("Willaim says to SUE:",william_response) # prints willaims response
    william_response = conversation_General[randint(0,len(conversation_General))]# calls the list general at the top of script for the chat bot to use as random response


    matt_response = chatbot_matt.get_response(william_response) # matt bot having a conversation with william  using general   topic
    william_response = chatbot_william.get_response(matt_response)# gets william pervious response so that matt can respond to
    print("Matt says to William:",matt_response)#prints matts response
    matt_response = conversation_General[randint(0, len(conversation_General))] # calls the list general at the top of script for the chat bot to use as random response


    if  matt_response == "Goodbye": # ends the program if user inputs  goodbye
        break
    if william_response == "Hello There": # ends the program if user inputs  goodbye
         print("General Kenobi")


