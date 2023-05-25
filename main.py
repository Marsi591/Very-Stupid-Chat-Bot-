import nltk
from nltk.corpus import wordnet
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')

import spacy
from tkinter import *

nlp = spacy.load('en_core_web_sm')

def process_input(user_input):
    tokens = nltk.word_tokenize(user_input)
    tagged_tokens = nltk.pos_tag(tokens)

    doc = nlp(user_input)
    entities = doc.ents

    return tagged_tokens, entities

def generate_response(user_input):
    tagged_tokens, entities = process_input(user_input)

    # Example logic for generating appropriate response based on user input and entities
    if 'how are you' in user_input.lower():
        response = "I'm doing well, thank you!"
    elif 'what' in user_input.lower() and 'up' in user_input.lower():
        response = "Not much, just chatting with you!"
    elif entities:
        response = f"I see that you mentioned {entities}. That's interesting!"
    else:
        response = "I'm sorry, I didn't understand. Can you please rephrase?"

    return response

def send_message():
    user_input = input_entry.get()
    response = generate_response(user_input)
    message_list.insert(END, "User: " + user_input)
    message_list.insert(END, "Chatbot: " + response)
    input_entry.delete(0, END)

root = Tk()
root.title("Chatbot")
root.geometry("400x500")

message_list = Listbox(root, width=50, height=25)
message_list.pack(pady=10)

input_frame = Frame(root)
input_frame.pack(pady=10)

input_entry = Entry(input_frame, font=("Helvetica", 14))
input_entry.pack(side=LEFT, padx=10)
send_button = Button(input_frame, text="Send", command=send_message)
send_button.pack(side=LEFT)

root.mainloop()
