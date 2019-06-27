from gtts import gTTS
import os
from playsound import playsound
file = open("data.txt", "r") 
data = file.read() 
tts = gTTS(text=data, lang='en')
tts.save("good.mp3")
os.system("mpg321 good.mp3")
path = 'good.mp3'
playsound(path)
