import os
import numpy as np
import soundfile as sf

folder = "."

# audio, sr = sf.read("loud_test.wav")
# print(np.max(np.abs(audio)))


for name in os.listdir(folder):
    if name.endswith(".wav"):
        audio, sr = sf.read(name)
        peak = np.max(np.abs(audio))
        rms = np.sqrt(np.mean(audio ** 2))
        if peak >= 0.99:
            verdict = "FLAG: clipping"
        elif rms < 0.05:
            verdict = "FLAG: too quiet"
        elif rms > 0.5:
            verdict = "FLAG: too loud"
        else:
            verdict = "PASS"
        print(f"{name} - peak {peak:.2f} - rms {rms:.2f} - {verdict}")