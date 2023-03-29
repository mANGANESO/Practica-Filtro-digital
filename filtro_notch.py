import numpy as np
from scipy.io import wavfile
from scipy.signal import iirnotch, lfilter
import scipy.io.wavfile as wavfile
import scipy.signal as signal
import numpy as np
import matplotlib.pyplot as plt

# Cargar el archivo de audio
sample_rate, audio_data = wavfile.read("audio_ruido.wav")

# Frecuencia a la que se desea eliminar la señal
notch_freq = 100  # Hz

# Frecuencia de corte del filtro notch
bandwidth = 10000  # Hz

# Calcular los coeficientes del filtro notch
f0 = notch_freq / sample_rate
Q = notch_freq / bandwidth
b, a = iirnotch(f0, Q)

# Filtrar la señal de audio utilizando los coeficientes del filtro
filtered_audio = lfilter(b, a, audio_data)

# Convertir la señal de audio a un tipo de datos adecuado para guardarla en un archivo
filtered_audio = np.int16(filtered_audio / np.max(np.abs(filtered_audio)) * 32767)

# Guardar la señal de audio filtrada en un archivo
wavfile.write("filtered_audio.wav", sample_rate, filtered_audio)

# Escuchar el audio original
plt.figure()
plt.plot(audio_data)
plt.title('Audio original')
plt.xlabel('Muestras')
plt.ylabel('Amplitud')
plt.show()

# Escuchar el audio filtrado
plt.figure()
plt.plot(filtered_audio)
plt.title('Audio filtrado')
plt.xlabel('Muestras')
plt.ylabel('Amplitud')
plt.show()