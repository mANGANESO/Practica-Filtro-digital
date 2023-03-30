import numpy as np
from scipy.io import wavfile
from scipy.signal import butter, lfilter
import numpy as np
from scipy.io import wavfile
from scipy.signal import iirnotch, lfilter
import scipy.io.wavfile as wavfile
import scipy.signal as signal
import numpy as np
import matplotlib.pyplot as plt


# Cargar el archivo de audio WAV
sample_rate, audio = wavfile.read('audio_ruido.wav')

# Definir las características del filtro de paso bajo
cutoff_freq = 600  # Frecuencia de corte en Hz
order = 7  # Orden del filtro

# Calcular los coeficientes del filtro utilizando la función butter de SciPy
nyquist_freq = 0.5 * sample_rate  # Frecuencia de Nyquist
normalized_cutoff_freq = cutoff_freq / nyquist_freq
b, a = butter(order, normalized_cutoff_freq, btype='low', analog=False)

# Aplicar el filtro a la señal de audio
filtered_audio = lfilter(b, a, audio)

# Guardar la señal filtrada en un archivo WAV
wavfile.write('filtered_audio.wav', sample_rate, np.int16(filtered_audio))

# Escuchar el audio original
plt.figure()
plt.plot(audio)
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