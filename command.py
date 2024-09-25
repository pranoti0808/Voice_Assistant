import pyttsx3
import speech_recognition as sr
import eel
import time


def speak(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices') 
    engine.setProperty('voice', voices[1].id)
    engine.setProperty('rate', 175)
    eel.DisplayMessage(text)
    engine.say(text)
    engine.runAndWait()




def takeCommand():
    r = sr.Recognizer()

    with sr. Microphone() as source:
        print('Listening...')
        eel.DisplayMessage("Listening...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)

        audio = r.listen(source,10,6)

    try:
        print('recognizing')
        eel.DisplayMessage("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}")
        eel.DisplayMessage(query)
        time.sleep(2)
        
        
        
    except Exception as e:
        return ""
    
    return query.lower()

# text = takeCommand()
# speak(text)

@eel.expose
def allCommands():
    
    query = takeCommand()
    print(query)

    if "open" in query:
        from engine.features import openCommand
        openCommand(query)
    elif "On youtube":
        from engine.features import playYoutube
        playYoutube(query)
    else:
        print("Not run")
    eel.ShowHood()