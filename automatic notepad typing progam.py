import keyboard
import pyautogui
import os
import speech_recognition as sr
import pyttsx3

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty("rate", 130)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()



def takecommand():
    # it takes microphone input from user and return txt output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening......")
        r.pause_threshold = 1
        audio = r.listen(source)
        try:
            print("recognising...")
            query = r.recognize_google(audio, language='en-in')
            print(query)
        except Exception as e:
            print("say that again please")
            return " "
        return query


if __name__ == '__main__':
    print("=> Welcome to automatic notepad typing program")
    print("=> Press => ENTER <= to continue")
    print("=> Speak loud and clear with minimal background noise")
    print("=> Speak CHANGE LINE to write in next line")
    print("=> Speak STOP THE PROGRAM  to exit the application")
    print("=> NOTE-- PRESSING ENTER WILL IMMEDIATELY OPEN NOTEPAD")
    while True:

        if keyboard.is_pressed('enter'):
            print("Enjoy")


            break

    os.startfile('C:\\WINDOWS\\system32\\notepad.exe')

    print("Sit back and relax I will type for you")

    print("=> Speak when (Listening........) appears on screen \n => do not speak after (Recognising ....appears)")

    while True:
        query = takecommand().lower()
        if 'change line' in query:
            pyautogui.write('\n')
        elif 'stop the program' in query:
            exit()
        elif 'backspace 5' in query:
            pyautogui.keyDown('backspace')
            pyautogui.keyDown('backspace')
            pyautogui.keyDown('backspace')
            pyautogui.keyDown('backspace')
            pyautogui.keyDown('backspace')

        elif 'backspace 10' in query:
            pyautogui.keyDown('backspace')
            pyautogui.keyDown('backspace')
            pyautogui.keyDown('backspace')
            pyautogui.keyDown('backspace')
            pyautogui.keyDown('backspace')
            pyautogui.keyDown('backspace')
            pyautogui.keyDown('backspace')
            pyautogui.keyDown('backspace')
            pyautogui.keyDown('backspace')
            pyautogui.keyDown('backspace')

        elif 'backspace 1' \
             '' in query:
            pyautogui.keyDown('backspace')
        elif 'read my text' in query:
            f = open('my.txt', 'r')

            read = f.read()
            speak(read)
            f.close()



        else:
            pyautogui.write(query)
            f = open('my.txt', 'a')
            f.write(query)
            f.close()


