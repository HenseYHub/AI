import speech_recognition as sr
import pyttsx3
import webbrowser
import datetime

# Set up speech recognition
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Listening...")
    r.adjust_for_ambient_noise(source)  # Adjust for ambient noise
    audio = r.listen(source)


# Initialize text-to-speech engine
engine = pyttsx3.init()

# Set up wake-up keyword
wake_word = 'Jarvis'

# Define function to convert text to speech
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Define funcion for opening a website
def open_website(url):
    webbrowser.open(url)
    speak('Opening website.')

# Define function for telling the time
def tell_time():
    time = datetime.datetime.now().strftime("%I:%M %p")
    speak(f'The time as {time}.')

# Check if wake-up keyword is detected
if wake_word in r.recognize_google(audio):
    speak('Yes sir?')

# Listen for command
with sr.Microphone() as source:
    print("Listening...")
    r.adjust_for_ambient_noise(source)
    audio = r.listen(source)

    try:
        # Convert speech to text
        command = r.recognize_google(audio).lower()  # Convert to lowercase for case-insensitive comparison
        print('You said:', command)

        # Check if wake-up keyword is detected
        if wake_word.lower() in command:
            speak('Yes sir?')

            # Execute main command
            audio = r.listen(source)
            # ... (rest of your command processing code)

        else:
            speak("I'm sorry, I didn't understand that.")

    except sr.UnknownValueError:
        speak("I'm sorry, I didn't understand that.")
    except sr.RequestError as e:
        speak("Sorry, I couldn't reach the Google servers. Check your internet connection.")
