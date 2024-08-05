import speech_recognition as sr
import pyttsx3
import webbrowser
from datetime import datetime

# Initialize the recognizer and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Function to make the computer speak
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to greet the user based on the time of day
def wish_me():
    hour = datetime.now().hour
    if 0 <= hour < 12:
        speak("Good Morning Boss...")
    elif 12 <= hour < 17:
        speak("Good Afternoon Master...")
    else:
        speak("Good Evening Sir...")

# Function to process commands
def take_command(command):
    command = command.lower()
    if 'hey' in command or 'hello' in command:
        speak("Hello Sir, How May I Help You?")
    elif "open google" in command:
        webbrowser.open("https://google.com")
        speak("Opening Google...")
    elif "open youtube" in command:
        webbrowser.open("https://youtube.com")
        speak("Opening YouTube...")
    elif "open facebook" in command:
        webbrowser.open("https://facebook.com")
        speak("Opening Facebook...")
    elif 'what is' in command or 'who is' in command or 'what are' in command:
        query = command.replace(" ", "+")
        webbrowser.open(f"https://www.google.com/search?q={query}")
        speak(f"This is what I found on the internet regarding {command}")
    elif 'wikipedia' in command:
        query = command.replace("wikipedia", "").strip()
        webbrowser.open(f"https://en.wikipedia.org/wiki/{query}")
        speak(f"This is what I found on Wikipedia regarding {command}")
    elif 'time' in command:
        time = datetime.now().strftime("%H:%M")
        speak(f"The current time is {time}")
    elif 'date' in command:
        date = datetime.now().strftime("%b %d")
        speak(f"Today's date is {date}")
    elif 'calculator' in command:
        webbrowser.open('Calculator:///')
        speak("Opening Calculator")
    elif 'weather' in command:
        webbrowser.open("https://www.accuweather.com/")
        speak("Opening Weather")
    else:
        query = command.replace(" ", "+")
        webbrowser.open(f"https://www.google.com/search?q={query}")
        speak(f"I found some information for {command} on Google")

# Main function to handle the voice assistant
def main():
    speak("Initializing FRIDAY...")
    wish_me()

    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        speak("Listening...")
        print("Listening...")

        while True:
            try:
                audio = recognizer.listen(source)
                command = recognizer.recognize_google(audio)
                print(f"You said: {command}")
                take_command(command)
            except sr.UnknownValueError:
                speak("Sorry, I did not get that.")
            except sr.RequestError:
                speak("Sorry, my speech service is down.")

if __name__ == "__main__":
    main()
