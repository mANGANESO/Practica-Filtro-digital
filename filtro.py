import scipy.io.wavfile as wavfile
import scipy.signal as signal
import numpy as np
import matplotlib.pyplot as plt

# Cargar el archivo de audio WAV
fs, data = wavfile.read('audio_ruido.wav')

# Normalizar los datos de audio entre -1 y 1
data = data / np.max(np.abs(data))

# Definir los parámetros del filtro pasa banda
f1 = 900.0  # Frecuencia de corte inferior en Hz
f2 = 1000.0  # Frecuencia de corte superior en Hz
order = 4  # Orden del filtro

# Calcular los coeficientes del filtro
b, a = signal.butter(order, [f1/(fs/2), f2/(fs/2)], btype='band')

# Aplicar el filtro al audio
filtered_data = signal.lfilter(b, a, data)

# Guardar el audio filtrado en un archivo WAV
wavfile.write('audio_filtrado.wav', fs, np.int16(filtered_data * 32767.0))

# Graficar el espectrograma del audio original
plt.specgram(data, Fs=fs)
plt.title('Espectrograma del audio original')
plt.xlabel('Tiempo (s)')
plt.ylabel('Frecuencia (Hz)')
plt.show()

# Graficar el espectrograma del audio filtrado
plt.specgram(filtered_data, Fs=fs)
plt.title('Espectrograma del audio filtrado')
plt.xlabel('Tiempo (s)')
plt.ylabel('Frecuencia (Hz)')
plt.show()

# Escuchar el audio original
plt.figure()
plt.plot(data)
plt.title('Audio original')
plt.xlabel('Muestras')
plt.ylabel('Amplitud')
plt.show()

# Escuchar el audio filtrado
plt.figure()
plt.plot(filtered_data)
plt.title('Audio filtrado')
plt.xlabel('Muestras')
plt.ylabel('Amplitud')
plt.show()
