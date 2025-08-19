import pyttsx3

# Initialize the TTS engine
engine = pyttsx3.init()

# Text you want to convert to speech
text = "My name is Bharath and I am from India, I am a fascist."

# Convert text to speech
engine.say(text)

# Wait for the speech to finish
engine.runAndWait()