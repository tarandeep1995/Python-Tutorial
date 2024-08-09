import pyttsx3

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Get input from the user
text = input("Enter the text you want me to speak: ")

# Pass the text to the engine to be spoken
engine.say(text)

# Wait for the speech to finish
engine.runAndWait()
