import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import smtplib
import webbrowser as wb
import os
import pyautogui
import psutil
import pyjokes


engine=pyttsx3.init()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("The Current Time is : ")
    speak(Time)

def screenshot():
    img = pyautogui.screenshot()
    img.save('D:\Python\ss.jpg')

def cpu():
    usage = str(psutil.cpu_percent())
    speak("Cpu is at "+usage)
    battery = psutil.sensors_battery()
    speak("Battery is at ")
    speak(battery.percent)

def date():
    year = int(datetime.datetime.now().year)
    mon = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak(date)
    speak(mon)
    speak(year)
    
def wishMe():
    speak("Welcome back Mam!")
    speak("The Current Time is : ")
    time()
    speak("The Current Date is : ")
    date()
    hour = datetime.datetime.now().hour
    if hour>=6 and hour <12:
        speak("Good Morning Maam")
    elif hour>=12 and hour <17:
        speak("Good Afternoon Maam")
    elif hour>=17 and hour <22:
        speak("Good Evening Maam")
    else:
        speak("Good Night Maam")
    speak("Hello, This is Jarvis AI Assistant at your service. Please tell me how can I help you ?? ")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing.....")
        query = r.recognize_google(audio, language = 'en-in')
        print(query)
    except Exception as e:
        print(e)
        speak("Say that again please....")
        return "None"
    return query

def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('abcz@gmail.com','123')
    server.sendmail('abcz@gmail.com',to,content)
    server.close()

if __name__ == "__main__":
    #wishMe()
    while True:
        query = takeCommand().lower()
        if 'time' in query:
            time()
        elif 'date' in query:
            date()
        elif 'wikipedia' in query:
            speak("Searching.......")
            query = query.replace("wikipedia","")
            result = wikipedia.summary(query,sentences = 2)
            print(result)
            speak(result)
        elif 'send email' in query:
            try:
                speak("What should I say??")
                content = takeCommand().lower()
                to = "xyz@gmail.com"
                sendEmail(to,content)
                speak("Email has been sent!")
            except Exception as ex:
                print(ex)
                speak("Unable to send Email")
        elif 'search in chrome' in query:
            speak("What should I search??")
            chromepath = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe %s"
            search = takeCommand().lower()
            wb.get(chromepath).open_new_tab(search+".com")
        elif "logout" in query:
            os.system("shutdown -1")
        elif "shutdown" in query:
            os.system("shutdown /s /t 1")
        elif "restart" in query:
            os.system("shutdown /r /t 1")
        elif "play song" in query:
            songs = ""
            song = os.listdir(songs)
            os.startfile(os.path.join(songs,song[0]))
        elif "remember" in query:
            speak("What should I remember...")
            data = takeCommand().lower()
            speak("You said me to remember about "+data)
            remember = open('data.txt','w')
            remember.write(data)
            remember.close()
        elif "do you know anything" in query:
            remember = open('data.txt','r')
            speak("Yes you told me to remember about "+remember.read())
        elif "screenshot" in query:
            screenshot()
            speak("Done")
        elif "cpu" in query:
            cpu()
        elif "jokes" in query:
            speak(pyjokes.get_jokes())
        elif 'offline' in query:
            quit()
        

