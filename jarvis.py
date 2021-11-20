from platform import system  # to use system files(inbuilt)
from time import struct_time 
import pyttsx3 #module to convert text to speech
import datetime
import speech_recognition as sr 
import wikipedia
import webbrowser
import os 
import smtplib
import pyjokes
engine =pyttsx3.init('sapi5') #speech API
voices = engine.getProperty('voices')
# print(voices[0].id)

engine.setProperty('voice',voices[0].id)

def sendemail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('sushantky00@gmail.com','9608076661')
    server.sendmail('sushantky00@gmail.com',to,content)
    server.close()



def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour <12:
        speak("Good morning") 

    elif hour>=12 and hour<18:
        speak("good afternoon")
    else:
        speak("good evening Sir")
    speak("I am Jarvis . Please tell me how may I help You.")




def takeCommand():
    #   it takes microsphone input and return string output
    r =sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening..")
        r.pause_threshold = 1
        audio=r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language='en-in')
        print(f"User said:{query}\n")
    except Exception as e:
        # print(e)

        print("Say that again,please")
        speak("anything else sir ?")
        return "None"
    return query

    


def main():

    wishme()
    while True:
        query =takeCommand().lower()
        if 'wikipedia' in query :
            speak('searching Wikipedia...')
            query = query.replace('wikipedia',"")
            results = wikipedia.summary(query,sentences=2)
            speak("according to wikipedia")
            print(results)
            speak(results)
        
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open('google.com')
        elif 'open stackoverflow' in query:
            webbrowser.open('stackoverflow.com')
        elif 'play music' in query:
            music_dir ="D:\\songs"
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))
        elif 'the time' in query:
            strTime=datetime.datetime.now().strftime("%H hrs %M mins %S seconds")
            speak(f"The time is{strTime}")
        elif 'open vs code' in query:
            codePath ="C://Users//sushant//AppData//Local//Programs//Microsoft VS Code//Code.exe"
            os.startfile(codePath)
        elif 'send email' in query:
            try:
                speak("what should I send ,sir?")
                content =takeCommand()
                speak("whom should i send ")
                to = input()
                sendemail(to,content)
            except Exception as e:
                print(e)
                speak("i am not able to send this mail sir")
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("% H:% M:% S")   
            speak(f"Sir, the time is {strTime}")
        elif 'how are you' in query:
            speak("I am fine, Thank you")
            speak("How are you, Sir")
 
        elif 'fine' in query or "good" in query:
            speak("It's good to know that your fine")   
        elif 'joke' in query:
            speak(pyjokes.get_joke())
        elif 'exit' in query:
            speak("bye sir take care and love you")
            exit()
        elif 'thank you' in query:
            speak("its my pleasure sir")
        elif 'bye' in query:
            speak('i never want you to leave me but i know u are busy, bye sir')
            exit()
        else:
            continue


if __name__=='__main__':
    main()