import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os




 # Register Brave browser
brave_path = "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe"  # Adjust path if necessary
webbrowser.register('brave', None, webbrowser.BackgroundBrowser(brave_path))


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
        speak("Sorry, I didn't catch that. Could you repeat please?")
        print("Sorry, I didn't catch that. Could you repeat please?")
        return "None"
    
    return query
        

def open_website(query):
    if 'open' in query:
        try:
            # Extract website name by removing 'open'
            website_name = query.replace("open website ", "").strip()

            # Check if the website already contains a domain like '.com', '.org', etc.
            if not any(website_name.endswith(tld) for tld in ['.com', '.org', '.net', '.edu']):
                website_name += ".com"  # Default to .com if no domain is specified
            
            # Construct the URL
            url = f"https://www.{website_name}"
            print(f"Opening {url}...")
            
        except Exception as e:
            print(f"Could not open the website. Error: {e}")
    else:
        print("No 'open website' command detected.")
        
    
    # Open the website using Brave browser
    try:
        speak(f"Opening {website_name} in Brave browser.")
        webbrowser.get('brave').open(website_name)
    except Exception as e:
        speak(f"Could not open {website_name}")

        
 
 
 
 
 
 
         
           
if __name__ == '__main__':
    wishme()
    
    while True:
        if 1:
    
            query = takecommand().lower()
    
    # logic for executing tasks based on query.

        if 'wikipedia' in query:  #if wikipedia found in the query then this block will be executed
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2) 
            speak("According to Wikipedia")
            print(results)
            speak(results)
        
        elif 'open youtube' in query:
            speak("Opening youtube")
            webbrowser.get('brave').open("youtube.com")
            
        elif 'open medium' in query:
            speak("Opening medium")
            webbrowser.get('brave').open("medium.com")
            
        elif 'open linkedin' in query:
            speak("Opening linkedin")
            webbrowser.get('brave').open("linkedin.com")
        
        elif 'open my upes portal' in query:
            speak("Opening UPES portal")
            webbrowser.get('brave').open("https://myupes-beta.upes.ac.in/connectportal/user/student/home/dashboard")
            
        elif 'open google' in query:
            speak("Opening Google")
            webbrowser.get('brave').open("google.com")
        
        elif 'open website' in query:
            open_website(query)
            
        elif 'exit jarvis' in query:
            speak("Goodbye Rhythm! Shutting down.")
            break
            
        elif 'what is the time' in query:
            strtime = datetime.datetime.now().strftime("%H:%M")
            speak(f"Sir the time is {strtime}")
            
        elif 'open code' in query:
            speak("Opening Vs Code")
            codepath = "C:\\Users\\hp\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)

           
            
            
        