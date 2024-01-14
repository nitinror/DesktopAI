import speech_recognition as sr
import os
import webbrowser
import openai
from config import apikey  # Assuming you have a config file with your OpenAI API key
import datetime
import random
import pyttsx3  # Add this import for text-to-speech on Windows
import numpy as np

chatStr = ""

def chat(query):
    global chatStr
    print(chatStr)
    openai.api_key = apikey
    chatStr += f"Nitin: {query}\n Nitin's Assistant: "
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt= chatStr,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    say(response["choices"][0]["text"])
    chatStr += f"{response['choices'][0]['text']}\n"
    return response["choices"][0]["text"]

def ai(prompt):
    openai.api_key = apikey
    text = f"OpenAI response for Prompt: {prompt} \n --------********------**---\n\n"
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    text += response["choices"][0]["text"]
    if not os.path.exists("Openai"):
        os.mkdir("Openai")
    with open(f"Openai/{''.join(prompt.split('intelligence')[1:]).strip()}.txt", "w") as f:
        f.write(text)

def say(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query
        except Exception as e:
            return "Some Error Occurred. Sorry from Nitin's Assistant "

if __name__ == '__main__':
    print('Welcome to Nitin_Assist A.I')
    say("I am Nitin's A.I")
    while True:
        print("Listening...")
        query = takeCommand()
        sites = [
            ["youtube", "https://www.youtube.com"],
            ["wikipedia", "https://www.wikipedia.com"],
            ["google", "https://www.google.com"],
            ["chat GPT", "https://chat.openai.com/"]
        ]
        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                say(f"Opening {site[0]} sir...")
                webbrowser.open(site[1])
        if "open music" in query:
            # Adjust the musicPath for Windows
            musicPath = r"C:\Path\To\Your\mysong.mp3"
            os.system(f"start {musicPath}")
        elif "the time" in query:
            hour = datetime.datetime.now().strftime("%H")
            min = datetime.datetime.now().strftime("%M")
            say(f"Sir time is {hour} hours {min} minutes")
        elif "open facetime".lower() in query.lower():
            # Adjust the path for Windows
            os.system(r"start C:\Path\To\FaceTime.exe")
        elif "open app".lower() in query.lower():
            # Adjust the path for Windows
            os.system(r"start C:\Path\To\app.exe")
        elif "Using artificial intelligence".lower() in query.lower():
            ai(prompt=query)
        elif "Nitin's A.I. Quit".lower() in query.lower():
            exit()
        elif "reset chat".lower() in query.lower():
            chatStr = ""
        else:
            print("Chatting...")
            chat(query)

