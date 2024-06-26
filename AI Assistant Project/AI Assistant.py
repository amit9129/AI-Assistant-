import random
import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import smtplib

# Initialize the speech recognizer and engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Function to speak the response
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to greet the user
def greet():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        return "Good morning!"
    elif 12 <= hour < 18:
        return "Good afternoon!"
    else:
        return "Good evening!"

# Function to respond to user commands
def respond(command):
    if 'who is' in command:
        person = command.replace('who is', '')
        try:
            info = wikipedia.summary(person, sentences=2)
            return info
        except wikipedia.exceptions.DisambiguationError as e:
            return f"There are multiple results for '{person}'. Can you be more specific?"
        except wikipedia.exceptions.PageError:
            return f"Sorry, I couldn't find any information on '{person}'."
    elif 'what is' in command:
        topic = command.replace('what is', '')
        try:
            info = wikipedia.summary(topic, sentences=2)
            return info
        except wikipedia.exceptions.DisambiguationError as e:
            return f"There are multiple results for '{topic}'. Can you be more specific?"
        except wikipedia.exceptions.PageError:
            return f"Sorry, I couldn't find any information on '{topic}'."
    elif 'open' in command:
        url = command.replace('open', '').strip()  # Extract the URL or search query
        webbrowser.open(url)  # Open in default web browser
        return f"Opening {url} in the browser."
    elif 'play music' in command:
        # You can specify the directory where your music files are stored and play them randomly
        music_dir = "path_to_music_directory"
        songs = os.listdir(music_dir)
        if songs:
            song = random.choice(songs)
            os.startfile(os.path.join(music_dir, song))
            return f"Now playing {song}."
        else:
            return "No music files found in the specified directory."
    elif 'send email' in command:
        # Add code to send email
        pass
    elif 'set reminder' in command:
        # Add code to set reminder
        pass
    elif 'show reminders' in command:
        # Add code to show reminders
        pass
    elif 'search' in command:
        search_query = command.replace('search', '')
        webbrowser.open(f"https://www.google.com/search?q={search_query}")
        return f"Here are the search results for {search_query}."
    elif 'locate' in command:
        location = command.replace('locate', '')
        webbrowser.open(f"https://www.google.com/maps/place/{location}")
        return f"Locating {location}."
    elif 'weather' in command:
        # You can use a weather API to get weather information based on the user's location or a specific location
        return "The weather is sunny today."
    elif 'news' in command:
        # You can use a news API to get the latest news headlines
        return "Here are the latest news headlines..."
    elif 'calculate' in command:
        try:
            expression = command.replace('calculate', '')
            result = eval(expression)
            return f"The result of {expression} is {result}."
        except Exception as e:
            return str(e)
    elif 'shutdown' in command:
        os.system("shutdown /s /t 1")
        return "Shutting down the system."
    elif 'restart' in command:
        os.system("shutdown /r /t 1")
        return "Restarting the system."
    elif 'joke' in command:
        jokes = [
            "Why don't scientists trust atoms? Because they make up everything!",
            "Parallel lines have so much in common. It’s a shame they’ll never meet.",
            "Why did the scarecrow win an award? Because he was outstanding in his field!",
            "I'm reading a book on anti-gravity. It's impossible to put down!",
            "Did you hear about the mathematician who's afraid of negative numbers? He'll stop at nothing to avoid them!"
        ]
        return random.choice(jokes)
    else:
        return "I'm sorry, I didn't understand that."

# Main loop for interacting with the AI
speak("Hello! How can I assist you today?")
while True:
    try:
        with sr.Microphone() as source:
            print("Listening...")
            audio = recognizer.listen(source)

        print("Processing...")
        user_input = recognizer.recognize_google(audio)
        print("You:", user_input)

        if user_input.lower() == 'exit':
            speak("Goodbye!")
            break

        greeting = greet()
        response = respond(user_input)
        speak(greeting)
        speak(response)

    except sr.UnknownValueError:
        speak("Sorry, I couldn't understand what you said.")
    except sr.RequestError:
        speak("My speech service is unavailable right now.")
