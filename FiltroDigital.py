import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

# Definir la frecuencia de muestreo y las frecuencias de corte
fs = 2000 # Hz
fc = 250 # Hz

# Crear un filtro FIR pasa alto
numtaps = 101
taps = signal.firwin(numtaps, fc, pass_zero=False, fs=fs)

# Generar una señal de prueba
t = np.linspace(0, 1, fs, endpoint=False)
x = np.sin(2*np.pi*100*t) + np.sin(2*np.pi*200*t) + np.sin(2*np.pi*300*t)

# Aplicar el filtro a la señal
y = signal.lfilter (taps, 1.0, x)

# Graficar la señal original y la señal filtrada
plt. figure (figsize= (20, 6))
plt.xlim (0.2,0.3)
plt.plot(t, x, label= 'Señal original')
#plt.plot(t, y, label= 'Señal filtrada')
plt.legend
plt.show
