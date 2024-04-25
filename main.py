import speech_recognition as sr
import pyttsx3
import os
import webbrowser
import wikipedia
import pywhatkit
import datetime





def say(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold =  0.6
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language="en-bn")
            print(f"User said: {query}")
            return query
        except Exception as e:
            return "Some Error Occurred. Sorry from Jarvis"


if __name__ == '__main__':
    print('PyCharm')
    say("Hello I am Jarvis AI")
    while True:
      print("Listening...")
      query = takeCommand().lower()
      # todo: Add more sites
      sites = [["Facebook", "https://www.facebook.com"], ["wikipedia", "https://www.wikipedia.com"],
               ["google", "https://www.google.com"],["ndb", "https://www.ndub.edu.bd/"] ]
      for site in sites:
          if f"Open {site[0]}".lower() in query.lower():
              say(f"Opening {site[0]} sir...")
              webbrowser.open(site[1])

      # todo: Add a feature to play a specific songG

      if "open music" in query:
         musicPath = "E:\songs\downfall-21371.mp3"
         os.startfile(musicPath)

      elif "time" in query:
          musicPath = "E:\songs"
          hour = datetime.datetime.now().strftime("%H")
          min = datetime.datetime.now().strftime("%M")
          say(f"Sir time is {hour} and {min} minutes")


      elif 'who is' in query:
          person = query.replace('who is', '').strip()
          try:
              info = wikipedia.summary(person, 3)
              print(info)
              say(info)
          except:
              say("I couldn't find information about that, sir.")





      if 'play' in query:
          song = query.replace('play', '').strip()  # Remove the 'play' keyword and strip any extra spaces
          say('playing your song ' + song)
          pywhatkit.playonyt(song)

      if 'what is' in query:
          person = query.replace('what is', '').strip()
          try:
              info = wikipedia.summary(person, 3)
              print(info)
              say(info)
          except:
              say("I couldn't find information about that, sir.")
      if 'how can i be a' in query:
          person = query.replace('how can i be a', '').strip()
          try:
              info = wikipedia.summary(person, 3)
              print(info)
              say(info)
          except:
              say("I couldn't find information about that, sir.")

      if 'open visual studio code' in query:
          path_to_vscode = "C:\\Users\\acer\\AppData\\Local\\Programs\\Microsoft VS Code\\code.exe"


          os.startfile(path_to_vscode)

      elif 'open powerpoint' in query:
          path_to_powerpoint = "C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.EXE"

          os.startfile(path_to_powerpoint)




