import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import random
import smtplib
import pywhatkit
import pyjokes
import cv2
from requests import get
import wolframalpha
import requests
import winshell
import ctypes
import subprocess
import time
import sys
from GoogleNews import GoogleNews
from twilio.rest import Client
import pyautogui
import json
import instaloader
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QTimer, QTime, QDate, Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from alexUi import Ui_Alex


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices)
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    tt = time.strftime("%I:%M %p")
    if hour>=0 and hour<12:
        speak(f"Good Morning sir!, its {tt}")
    elif hour>=12 and hour<18:
        speak(f"Good Afternoon sir!, its {tt}")
    else:

        speak(f"Good Evening sir!, its {tt}")
    speak("I am Alex. Please tell me how may I help you")


        

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('nishantmandil2018@gmail.com', 'Mandil2018@')
    server.sendmail('nishantmandil2018@gmail.com', to, content)
    server.close()

def news():
    main_url = 'https://newsapi.org/v2/top-headlines?country=us&apiKey=48b026cd01184399930afb53f1be9e7f'

    main_page = requests.get(main_url).json()
    articles = main_page["articles"]
    head = []
    day = ["first","second","third","fourth","fifth","sixth","seventh","eighth","ninth","tenth"]
    for ar in articles:
        head.append(ar["title"])
    for i in range(len(day)):
        speak(f"today's {day[i]} news is : {head[i]}")


class MainThread(QThread):
    def __init__(self):
        super(MainThread, self).__init__()

    def run(self):
        self.TaskExecution()

    def takeCommand(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 1
            audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")
        except Exception:
            print("Say that again please...")
            return "None"
        return query
        

    def TaskExecution(self):
        clear = lambda: os.system('cls')
        clear()
        contact= {"nishant":"nishantmandil105@gmail.com", "lucky":"lracer316@gmail.com"}
        phone = {"mummy":"+918982733612","nishant":"+918085569375"}
        wishMe()
        while True:
            self.query = self.takeCommand().lower()

            if 'wikipedia' in self.query:
                speak("Searching Wikipedia")
                # self.query = self.query.replace("wikipedia", "")
                try:
                    results = wikipedia.summary(self.query, sentences=3)
                    speak("Acoording to Wikipedia")
                    print(results)
                    speak(results)
                except Exception :
                    print("Wikipedia has no result!")
                
                speak("sir, do you have any other work!")


            elif 'open youtube' in self.query:
                speak("Here you go to Youtube\n")
                webbrowser.open("www.youtube.com")
                speak("sir, do you have any other work!")


            elif 'play youtube video' in self.query or 'play video on youtube' in self.query:
                speak("Which video you want to watch!")
                name = self.takeCommand()
                speak("playing "+name)
                pywhatkit.playonyt(name)
                speak("Anything else i can do for you")
    
            elif 'open facebook' in self.query:
                speak("Here you go to facebook\n")
                webbrowser.open("www.facebook.com")
                speak("sir, do you have any other work!")

            elif 'open google' in self.query:
                speak("sir, what should i search on google")
                cm = self.takeCommand().lower()
                webbrowser.open(f"{cm}")

            elif 'open online diary' in self.query:
                webbrowser.open("onlinediary.great-site.net")

            elif 'play music' in self.query or "play song" in self.query:
                speak("Here you go with music")
                music_dir = 'F:\\music'
                songs = os.listdir(music_dir)   
                speak("Enjoy your song sir! I am going to sleep now. You can call me anytime.")
                os.startfile(os.path.join(music_dir, songs[5]))
                break

            elif 'time' in self.query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"The time is {strTime}")
                speak("sir, do you have any other work!")

            elif 'open visual studio code' in self.query:
                codepath = "G:\\Microsoft VS Code\\Code.exe" 
                os.startfile(codepath)
                speak("sir, do you have any other work!")

    #to close application
            elif 'close visual studio code' in self.query:
                speak("Okay sir, closing visual studio code")
                os.system("taskkill /f /im Code.exe")
                speak("sir, do you have any other work!")
            
            
            elif 'open microsoft edge' in self.query:
                Mepath = "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"
                os.startfile(Mepath)
                speak("opening microsoft edge")
                speak("sir, do you have any other work!")
    #to close application
            elif 'close microsoft edge' in self.query:
                speak("Okay sir, closing microsoft edge")
                os.system("taskkill /f /im msedge.exe")
                speak("sir, do you have any other work!")

            elif 'open notepad' in self.query:
                codepath = "C:\\WINDOWS\\system32\\notepad.exe"
                os.startfile(codepath)
                speak("opening notepad")
                speak("sir, do you have any other work!")
    #to close any application
            elif 'close notepad' in self.query:
                speak("Okay sir, closing notepad")
                os.system("taskkill /f /im notepad.exe")
                speak("sir, do you have any other work!")

            elif 'open command prompt' in self.query:
                os.system('start cmd')
                speak("opening command prompt")
                speak("sir, do you have any other work!")
    #to close any application
            elif 'close command prompt' in self.query:
                speak("Okay sir, closing command prompt")
                os.system("taskkill /f /im cmd.exe")
                speak("sir, do you have any other work!")
            
            # elif 'open camera' in self.query:
            #     cap = cv2.VideoCapture(0)
            #     while True:
            #         ret, img = cap.read()
            #         cv2.imshow("webcam", img)
            #         k = cv2.waitKey(50)
            #         if k==27:
            #             break
            #     cap.release()
            #     cv2.destroyAllWindows()

            elif "ip address" in self.query:
                ip = get('https://api.ipify.org').text
                speak(f"Your IP address is {ip}")
                speak("sir, do you have any other work!")

            elif 'where i am' in self.query or 'where we are' in self.query:
                speak("wait sir, let me check")
                try:
                    ipAdd = requests.get('https://api.ipify.org').text
                    url = 'https://get.geojs.io/v1/ip/geo/'+ipAdd+'.json'
                    geo_requests = requests.get(url)
                    geo_data = geo_requests.json()
                    city = geo_data['city']
                    country = geo_data['country']
                    speak(f"Sir i am not sure, but i think we are in {city} , {country}")
                except Exception:
                    speak("Sorry sir, Due to network issue i am not able to find where we are.")
                    pass



            elif "whatsapp" in self.query:
                # pywhatkit.sendwhatmsg("+91898******","hii",int(datetime.datetime.now().strftime("%H")),int(datetime.datetime.now().strftime("%M")))
                speak("opening Whatsapp!")
                try:
                    speak("whom you want to send a message")
                    to = self.takeCommand()
                    for key,value in phone.items():

                        if to.lower() == key:
                            email= int(value)
                            speak("what should i write!")
                            content = self.takeCommand()
                            pywhatkit.sendwhatmsg(value,content,int(datetime.datetime.now().strftime("%H")),int(datetime.datetime.now().strftime("%M"))+1)
                            break
                    else:
                        print("person not in contact")
                except Exception as e:
                    speak("Unable to send message!")

                speak("sir, do you have any other work!")
                

            elif 'send email' in self.query:
                try:
                    speak("whom you want to send")
                    to = self.takeCommand()
                    for key,value in contact.items():

                        if to.lower() == key:
                            email= value
                            speak("what should i write!")
                            content = self.takeCommand()
                            sendEmail(email, content)
                            speak("Email has been sent!")
                            break
                    else:
                        print("person not in contact")
                except Exception as e:
                    print(e)

                speak("sir, do you have any other work!")

            # elif 'news' in self.query:
            #     # googlenews = GoogleNews()
            #     googlenews = GoogleNews('en', 'd')
            #     try:
            #         speak("What type or country news you want to listen")
            #         cmd = self.takeCommand()
            #         googlenews.search('cmd')
            #         googlenews.getpage(1)

            #         speak(googlenews.result())
                
            #     except Exception:
            #         speak("Unable to find a news , try again later")
            #         speak("sir, do you have any other work!")

            elif 'set alarm' in self.query:
                nn = int(datetime.datetime.now().hour)
                if nn==00:
                    music_dir = 'F:\\music'
                    songs = os.listdir(music_dir)
                    random = random.randint(0,len(songs))
                    os.startfile(os.path.join(music_dir, songs[random]))

                
            elif 'lock window' in self.query:
                speak("locking the device")
                ctypes.windll.user32.LockWorkStation()

            elif 'switch the window' in self.query:
                pyautogui.keyDown("alt")
                pyautogui.press("tab")
                time.sleep(1)
                pyautogui.keyUp("alt")
                speak("Done sir! anything else")


            elif 'news' in self.query:
                speak("please wait sir , fetching the latest news")
                news()

            elif 'joke' in self.query:
                speak(pyjokes.get_joke())
                speak("sir, do you have any other work!")

            elif 'shutdown system' in self.query:
                speak("Hold On a Sec ! Your system is on its way to shut down")
                subprocess.call('shutdown / p /f')

            elif 'empty recycle bin' in self.query:
                winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True)
                speak("Recycle Bin Recycled")


            # elif "where is" in self.query:
            #     self.query = self.query.replace("where is", "")
            #     location = self.query
            #     speak("User asked to Locate")
            #     speak(location)
            #     webbrowser.open("https://www.google.com/maps/search/?api=1&" + location + "")

            elif "restart" in self.query:
                subprocess.call(["shutdown", "/r"])
                
            # elif "hibernate" in self.query or "sleep" in self.query:
            #     speak("Hibernating")
            #     subprocess.call("shutdown / h")

            elif "log off" in self.query or "sign out" in self.query:
                speak("Make sure all the application are closed before sign-out")
                time.sleep(5)
                subprocess.call(["shutdown", "/l"])

            elif "write a note" in self.query:
                speak("What should i write, sir")
                note = self.takeCommand()
                file = open('jarvis.txt', 'w')
                speak("Sir, Should i include date and time")
                snfm = self.takeCommand()
                if 'yes' in snfm or 'sure' in snfm:
                    strTime = datetime.datetime.now().strftime("% H:% M:% S")
                    file.write(strTime)
                    file.write(" :- ")
                    file.write(note)
                else:
                    file.write(note)   

            # elif "weather" in self.query:
            #     speak("which city weather you want to know?")
            #     location = 
            #     complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+&appid={API key}"
                

            elif 'instagram profile' in self.query or 'profile on instagram' in self.query:
                speak("sir please enter the user name correctly.")
                name = input("Enter Username here:")
                webbrowser.open(f"www.instagram.com/{name}")
                time.sleep(5)
                speak(f"sir whould you like to download profile picture of this account.")
                condition = self.takeCommand()
                if 'yes' in condition:
                    mod = instaloader.Instaloader()
                    mod.download_profile(name, profile_pic_only=True)
                    speak("I am done sir, profile picture is saved.")
                    speak("sir, do you have any other work!")
                else:
                    pass


            elif "take screenshot" in self.query or "take a screenshot" in self.query:
                speak("Sir, please tell me the name for this screenshot file")
                name = self.takeCommand()
                speak("please sir hold the screen for few seconds, i am taking screenshot")
                time.sleep(3)
                img = pyautogui.screenshot()
                img.save(f"{name}.png")
                speak("I am done sir, the screenshot is saved in our main folder.")
                speak("sir, do you have any other work!")



            elif "show note" in self.query:
                speak("Showing Notes")
                file = open("jarvis.txt", "r") 
                print(file.read())
                speak(file.read(6))

            elif 'on a date' in self.query:
                speak("Don't give me a headache")
                speak("sir, do you have any other work!")

            elif 'how are you' in self.query:
                speak("I am fine, Thank you")
                speak("How are you, Sir")

            elif 'fine' in self.query or 'good' in self.query:
                speak("It's good to know that you'r fine")
                speak("Sir, How may i help you!")

            elif "what's your name" in self.query or "What is your name" in self.query:
                speak("My friend call me Alex")
                speak("Sir, How may i help you!")

            elif "who made you" in self.query or "who created you" in self.query:
                speak("I have been created by Nishant Mandil")


            elif "calculate" in self.query: 
                app_id = "5U69P9-WW26AV5T9R"
                client = wolframalpha.Client(app_id)
                try:
                    indx = self.query.lower().split().index('calculate')
                    self.query = self.query.split()[indx + 1:]
                    res = client.query(' '.join(self.query))
                    answer = next(res.results).text
                    speak("The answer is " + answer)
                except Exception:
                    speak("Please say the command again!")

            elif "send message" in self.query:
                account_sid = 'AC6558c9543a31aead18dec3c3da1c1f12'
                auth_token = 'c31567a6bc62873f9c3d234c18f523df'
                client = Client(account_sid, auth_token)
                try:
                    speak("whom you want to send")
                    to = self.takeCommand()
                    for key,value in phone.items():
                        if to.lower() == key:
                            speak("what should i write!")
                            content = self.takeCommand()
                            message = client.messages \
                                            .create(
                                                body = content,
                                                from_='+18315402580',
                                                to =value
                                            )
                            speak("message sent..")
                            print(message.sid)
                except Exception as e:
                    print(e)

                speak("sir, do you have any other work!")			
                        

            elif 'search' in self.query or 'play' in self.query:
                self.query = self.query.replace("search", "")
                self.query = self.query.replace("play", "")
                webbrowser.open(self.query)
                

            elif "who i am" in self.query:
                speak("If you talk then definately your human.")

            elif "why you came to world" in self.query:
                speak("Thanks to Nishant. further It's a secret")

            # elif 'power point presentation' in self.query:
            # 	speak("opening Power Point presentation")
            # 	power = r"C:\\Users\\GAURAV\\Desktop\\Minor Project\\Presentation\\Voice Assistant.pptx"
            # 	os.startfile(power)

            elif "Good Morning" in self.query:
                speak("A warm" +self.query)
                speak("How are you Sir")		
                

            elif 'is love' in self.query:
                speak("It is 7th sense that destroy all other senses")
                

            elif "who are you" in self.query:
                speak("I am your virtual assistant created by Nishant")

            elif 'nothing' in self.query:
                speak("Ok Sir Going for sleep, You can call me any time")
                break

                
            elif 'i am sad' in self.query:
                speak("why are u sad")
                speak("i am here with you what can i do to cheer you up!")
                speak("why don't you play videogames or read some interesting books!")
            

            elif 'stop' in self.query or 'no thanks' in self.query or 'quit' in self.query:
                speak("Thanks for using me sir, have a good day.")
                break

            elif "don't listen" in self.query or "stop listening" in self.query:
                speak("Going to sleep for 5 min")
                time.sleep(5000)

            elif "what" in self.query or 'how' in self.query or 'who' in self.query or 'where' in self.query: 
                app_id = "5U69P9-WW26AV5T9R"
                client = wolframalpha.Client(app_id)
                try:
                    res = client.query(self.query)
                    answer = next(res.results).text 
                    speak(answer)
                except:
                    speak("Wait sir! Searching Wikipedia")
                    try:
                        results = wikipedia.summary(self.query, sentences=3)
                        speak("Acoording to Wikipedia")
                        speak(results)
                    except Exception :
                        speak("Wikipedia has no result!")
                    
                speak("sir, do you have any other work!")
                    
                        


                    

            
            # elif 'who is' in self.query:
            #     speak("Wait sir! Searching Wikipedia")
            #     self.query = self.query.replace("wikipedia", "")
            #     try:
            #         results = wikipedia.summary(self.query, sentences=3)
            #         speak("Acoording to Wikipedia")
            #         print(results)
            #         speak(results)
            #     except Exception :
            #         print("Wikipedia has no result!")
                
            #     speak("sir, do you have any other work!")

            elif 'hello' in self.query:
                speak("Hello Sir")
                speak("May I help you with something.")
        
            elif 'thankyou' in self.query:
                speak("Its my pleasure sir. anything else i can do for you")

            elif '' in self.query:
                speak("Please tell me how may I help you")

            else:
                speak("Sir, Please say the command again!")


startExecution = MainThread()

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Alex()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.startTask)
        self.ui.pushButton_2.clicked.connect(self.close)


    def startTask(self):
        self.ui.movie = QtGui.QMovie("wp2757832.gif")
        self.ui.label.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("iron-man-jarvis-gif-1.gif")
        self.ui.label_2.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("jarvis-gif-6.gif")
        self.ui.label_3.setMovie(self.ui.movie)
        self.ui.movie.start()
        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)
        startExecution.start()       

    def showTime(self):
        current_time = QTime.currentTime()
        current_date = QDate.currentDate()
        label_time = current_time.toString('hh:mm:ss')
        label_date = current_date.toString(Qt.ISODate)
        self.ui.textBrowser.setText(label_date)
        self.ui.textBrowser_2.setText(label_time)


# if __name__ == '__main__':
#     TaskExecution()
        
app = QApplication(sys.argv)
alex = Main()
alex.show()
exit(app.exec_())