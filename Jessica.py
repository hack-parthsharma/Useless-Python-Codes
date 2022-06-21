import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
from googlesearch import search
import random
import smtplib
import requests
from bs4 import BeautifulSoup
import html5lib
import nltk

from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize, sent_tokenize
#--------------------------------------------------------------




#initialize the pyttsx3 package for usage and (sapi5) is driver used in windows same as (nsss) used on macos 
engine=pyttsx3.init('sapi5')

#getproperty function mainly get the value of the property of enigine which you'll pass you to it as an argument
v=engine.getProperty('voices')

'''setproperty function bascially takes 2 arguments (property name , value )
to assign the particular property that value , here we are assigning (voice)
property a value of (v) the voice which we have in our system '''
engine.setProperty('voice',v[0].id)

#if you'll print execute the below statement you'll get the id of voices (v) which is of ZIRA
#print(v[0].id)

def speak(audio):
    '''speak function take audio string as an agrument and with the help of pyttsx3 which we have intialize above
       it will narrate that string .
    here {engine.say()} method is used to get computer to speak the particular
    sentence as here we passed the audio and {engine.runAndWait()} is a function
    used for execution of the above method properly . Invokes callbacks for engine notifications appropriately. '''

    engine.say(audio)
    engine.runAndWait()

def wishme():
    '''wishme function basically wishes and introduce itself whenever we start the jarvis programm it also contains 
    datetime module function to give us our for further calculating and classifying what time it is .'''

    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning sir ,Have a nice day ahead ")
    elif hour>=12 and hour <=18:
        speak('Good Afternoon sir')
    elif hour>18 and hour<=21:
        speak('Good Evening Sir')
    else:
        speak("Good Night Sir")
    speak('I am Jessica , Please tell me how may I help you sir?')

def takeQuery():
    '''takes the query of user through speech and with speech_recognition module converts it to text and then implement the task according to the query'''
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.adjust_for_ambient_noise(source)
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        print('Recognizing Please Wait..')
        recog=r.recognize_google(audio)
        print(f"user said : {recog}\n")
    except Exception as ex:
        print(ex)
        print("Say that again please..")
        return 'none'
    return recog

def sendemail(emailid,content):
    
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('Your Email','Your Password')
    server.sendmail('Your Email',emailid,content)
    server.close()
    
def contentcreator(urlsam,topic):

    def beaut(urlsample):
        url=urlsample
        
        Samplecontent=requests.get(url)

        htmlContent=Samplecontent.content

        #print(htmlContent)
        soup=BeautifulSoup(htmlContent,'html.parser')
        stn=""
        sam=soup.find_all('p')
        speak('sir can you please enter the main keyword of your topic for more accurate content')
        t=input('keyword: ')
        for i in sam:
            
            if t in i.text.lower():
                
                stn+= (i.get_text())
       
        return stn
    speak('parsing the webpage sir')
    text=beaut(urlsam)
    
    speak('analysing and creating summarized content')


    stopWords = set(stopwords.words("english")) 
    words = word_tokenize(text) 
    freqTable = dict() 

    for word in words: 
        word = word.lower() 
        if word in stopWords: 
            continue
        if word in freqTable: 
            freqTable[word] += 1
        else: 
            freqTable[word] = 1

    sentences = sent_tokenize(text) 
    sentenceValue = dict() 

    for sentence in sentences: 
        for word, freq in freqTable.items(): 
            if word in sentence.lower(): 
                if sentence in sentenceValue: 
                    sentenceValue[sentence] += freq 
                else: 
                    sentenceValue[sentence] = freq
    
    sumValues = 0
    for sentence in sentenceValue: 
        sumValues += sentenceValue[sentence] 
    average = int(sumValues / len(sentenceValue)) 

    summary = ""
    for sentence in sentences: 
        if (sentence in sentenceValue) and (sentenceValue[sentence] > (1.2 * average)): 
            summary += " " + sentence 
    speak('your content is creating please copy and adjust by your accordance sir')  
    print('YOUR CONTENT ',end='\n')
    print(summary)    



def mainfunc():
    speak("sir can you please enter the topic for more accuracy")


    query=input('enter the topic here: ')
            
            
            
    speak("please wait sir , creating your content ")
    for i in search(query,tld='co.in',num=10,start=1,stop=1,pause=2.0):
        print(f"Data Scraped from website : {i}")
        j=i
        contentcreator(j,query)
if __name__ == "__main__":
    
    
    wishme()
    while True:
        query=takeQuery().lower()
        #TASKS WHICH WE WANT TO EXECUTE
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query=query.replace('wikipedia','')#removing wikipedia from string
            queryResult=wikipedia.summary(query,sentences=3)
            speak('According to Wikipedia..')
            print(queryResult)
            speak(queryResult)
        elif 'send mail to' in query:
            try:
                query=query.replace('send mail to','')
                speak("for more accuracy , can you please type the email id sir?")
                emailid=input()
                speak("what should I write ,sir?")
                content=takeQuery().lower()
                sendemail(emailid,content)
                speak('email has been sent sir')
            except Exception as e:
                print(e)
                speak('Sorry sir , due to some unknown reasons i am unable to send the mail')
        elif 'search' in query:
            query=query.replace('search','')
            for i in search(query,tld='co.in',num=2,stop=1,pause=2):
                webbrowser.open(i)
        elif 'open youtube' in query:
            speak('Opening youtube sir')
            webbrowser.open('www.youtube.com')
        
        elif 'open google' in query:
            speak('Opening google sir')
            webbrowser.open('www.google.com')
        elif 'open github' in query:
            speak('Opening github sir')
            webbrowser.open('www.github.com')
        elif 'open hackerrank' in query:
            speak('Opening Hackrank sir')
            webbrowser.open('www.hackerrank.com')
        elif 'open amazon' in query:
            speak('Opening amazon sir')
            webbrowser.open('www.amazon.in')
        elif 'open flipkart' in query:
            speak('Opening flipkart sir')
            webbrowser.open('www.flipkart.com')
        
        elif 'play music' in query:
            music_dir='Your Songs Directory'
            songs=os.listdir(music_dir)
            os.startfile(os.path.join(music_dir,songs[random.randint(0,len(songs))]))
        elif 'the time' in query:
            strtime=datetime.datetime.now()
            speak(f'the time is {strtime}')
        elif 'open code' in query:
            path="VSCode.exe Directory in your System"
            os.startfile(path)
        elif 'open atom' in query:
            path="atom.exe Directory in your System"
            os.startfile(path)
        elif 'open notepad' in query:
            path='notepad.exe Directory in your System'
            os.startfile(path)
        
        elif 'who are you' in query:
            speak('I am your personal assistant bot sir , made with love by you , Mr.Parth')
        
        elif 'you are beautiful' in query:
            speak('I am blushing sir , please do not tease me but thank you sir')
        elif  query=='create content':
            mainfunc()
        elif 'stop jessica' or 'abort' in query:
            speak('Okay sir , Take care , bye')
            break
        elif True:
            continue