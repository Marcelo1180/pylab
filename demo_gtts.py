from gtts import gTTS
import os
tts = gTTS(text='El elemento de memoria en el servidor no lo puedo cuantificar, seria tan amable de darme acceso', lang='es')
tts.save("good.mp3")
os.system("mplayer good.mp3")
