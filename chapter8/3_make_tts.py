from gtts import gTTS
from playsound import playsound

filename ='justpython.mp3'
text = "파이썬 재미있쥬?"
tts = gTTS(text=text, lang='ko')
tts.save(filename)
playsound(filename)

"""
from AppKit     import NSSound
ImportError: No module named 'AppKit'
위와 같은 에러가 나는 경우 pip install -U PyObjC 해줘야함 
"""

