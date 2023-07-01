import pyttsx3

speech = pyttsx3.init()
print("\n!!!!!!!!!!    Welcome to Robo Speaker    !!!!!!!!!! \n")
text_bye = "Bye "
while True:
    # speech = pyttsx3.init()
    text = input("what you want to say : ")
    if text=='q':
        speech.say(text_bye)
        break
    speech.say(text)    
    speech.runAndWait()  
