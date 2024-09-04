import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia


# Speak Function (Giving Our program Power to speak) 

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

# print(voices[1].id)
# To set voices by id 
engine.setProperty('voice', voices[0].id)


# Speak Function

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# Wish me function to greet at any time of day with date time module 

def wishme():
    
    speak("All Systems Online.")
    
            
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Rhythm!")
    
    elif hour>=12 and hour<18:
        speak("Good Afternoon Rhythm!")
        
    else:
        speak("Good Evening Rhythm!")
    
    speak("How may i help you.")        
    

def takecommand():
    # it takes mic input and returns string output
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1 
        audio = r.listen(source)
        
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User Said: {query}\n")
    
    except Exception as e:
        # print(e)
        print("Please Try Again.")
        return "None"
    
    return query
        
            
if __name__ == '__main__':
    wishme()
    while True:
        query = takecommand().lower()
    
    # logic for executing tasks based on query.

    if 'wikipedia' in query:
        speak('Searching on wikipedia')
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=3)
        speak("According to wikipedia")
        speak(results)
        print(results)
        
        
        
        
        