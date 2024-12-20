import sounddevice as sd
from scipy.io.wavfile import write
import wavio as wv


freq = 44100
duration = 5

recording = sd.rec(int(freq * duration), samplerate = freq, channels=1)
sd.wait()

# scipy
write("recording1.wav",freq, recording)

# wavio
wv.write("recording2.wav", recording, freq, sampwidth=1)