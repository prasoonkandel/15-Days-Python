

import emoji
import pyttsx3
import time
e = emoji.emojize
print(e('I will speak what you write!:wave::heart: ',  language='alias'))
time.sleep(1)
text = input("\n Enter text :")
engine = pyttsx3.init()
engine.say(text)
engine.runAndWait()