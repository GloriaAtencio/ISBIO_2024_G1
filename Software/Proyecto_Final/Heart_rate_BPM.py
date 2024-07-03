import numpy as np
from scipy.signal import find_peaks
from scipy.fftpack import fft

def calculate_bpm(ecg_signal, fs):
    # Normalización de la señal ECG (opcional)
    ecg_signal_norm = (ecg_signal - np.mean(ecg_signal)) / np.std(ecg_signal)

    # Detección de picos R usando find_peaks
    peaks, _ = find_peaks(ecg_signal_norm, distance=int(fs * 0.6))

    # Calcular intervalos RR (en segundos)
    rr_intervals = np.diff(peaks) / fs

    # Calcular el promedio de los intervalos RR
    mean_rr_interval = np.mean(rr_intervals)

    # Calcular el BPM
    bpm = 60 / mean_rr_interval

    return bpm, rr_intervals
