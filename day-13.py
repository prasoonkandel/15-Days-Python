import speech_recognition as sr
import webbrowser as brave
import pyttsx3
import time
gap = time.sleep
bot = pyttsx3.init()
recognise = sr.Recognizer()
commands = {
    #social media
    "open tiktok": ["https://www.tiktok.com", "Opening TikTok"],
    "open youtube": ["https://www.youtube.com", "Opening YouTube"],
    "open google": ["https://www.google.com", "Opening Google"],
    "open chatgpt": ["https://chatgpt.com", "Opening ChatGPT"],
    "open my website": ["https://prasoonkandel.netlify.app", "Opening your website"],
    "open facebook": ["https://facebook.com", "Opening Facebook"],
    "open instagram": ["https://www.instagram.com", "Opening Instagram"],
    "open twitter": ["https://twitter.com", "Opening Twitter"],
    "open reddit": ["https://www.reddit.com", "Opening Reddit"],
    "open linkedin": ["https://www.linkedin.com", "Opening LinkedIn"],
    "open github": ["https://github.com", "Opening GitHub"],

    # Greetings 
    "hello": [None, "Hello, I am a simple Voice assistant."],
    "hi": [None, "Hello, I am a simple Voice assistant."],
    "how are you": [None, "I am fine and ready to talk with you."],
    "how r u": [None, "I am fine and ready to talk with you."],
    "how r you": [None, "I am fine and ready to talk with you."],
    "what's up": [None, "I am fine and ready to talk with you."],
    
    # Identity 
    "your name": [None, "I am a simple Voice assistant made by Prasoon Kandel."],
    "who are you": [None, "I am a simple Voice assistant made by Prasoon Kandel."],
    "your creator": [None, "This Voice Assistant is created by Prasoon Kandel. Visit his website: https://prasoonkandel.netlify.app/"],
    
    # Exit
    "bye": ["bye", "Bye, have a nice day!"]
}



print("Hello , I am a simple voice assistant")
bot.say("Hello , I am a simple voice assistant")
bot.runAndWait()

print("Say something (bye to exit)")
running=True
while running == True:
    with sr.Microphone() as source:
        print("Listening your command")
        audio = recognise.listen(source)
        try :
            commandIn = recognise.recognize_google(audio)
            command = commandIn.lower()
            print(f"You said {command}")
            for key in commands:
                if key in command:
                    url , message = commands[key]
                    print(message)
                    bot.say(message)
                    bot.runAndWait()
                    if url == "bye" :
                        running = False
                    elif url == None:
                         running = True   
                        
                    else:
                        brave.open(url)
                    break      
                      
  
        except sr.UnknownValueError:
            print("Sorry, I can't catch that!")
            bot.say("Sorry, I can't catch that!")
            bot.runAndWait()
        except Exception as e:
            print("Oops! Something went wrong:", e)
            bot.say("Oops! Something went wrong.")
            bot.runAndWait()
