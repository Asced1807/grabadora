import sounddevice
from scipy.io.wavfile import write
fs=44100 #taza_de_muestra
second=int(input("Ingrese la duración del tiempo en segundos:")) #ingrese el tiempo requerido..
print("Recording....\n")
record_voice=sounddevice.rec(int(second * fs),samplerate=fs,channels=2)
sounddevice.wait()
write("out.wav",fs,record_voice)
print("Terminado... \n Por favor revíselo...")