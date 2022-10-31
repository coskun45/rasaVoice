import subprocess
from gtts import gTTS

import playsound

mytext='hello world my name is james'
language='en'
myobj=gTTS(text=mytext,lang=language)
myobj.save("welcome.mp3")
playsound.playsound("welcome.mp3")
#subprocess.call(['mpg321', "welcome.mp3", '--play-and-exit'])

#subprocess.call(['mpg321',"welcome.mp3",'--play-and-exit'])