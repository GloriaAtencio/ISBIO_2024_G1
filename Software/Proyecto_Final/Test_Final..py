import pandas as pd
import numpy as np
import os
import glob
import matplotlib.pyplot as plt
import pywt
from scipy.signal import find_peaks
from Heart_rate_BPM import calculate_bpm  # Import calculate_bpm function from Heart_rate_BPM.py

# Set Matplotlib backend
plt.switch_backend('Agg')

# Base directory where VP folders are located
base_dir = r'C:\Proyecto final\ECG'  # Usar r'' para raw strings para evitar problemas con las barras invertidas
output_dir = r'C:\Proyecto final\Final Results'

# Get all VP folders
vp_folders = glob.glob(os.path.join(base_dir, 'VP*'))

# Function to classify based on HR and HRV
def classify_fobia(hr, hrv, clip_id, thresholds):
    high_threshold_hr = 80
    low_threshold_hr = 75
    high_threshold_hrv = thresholds['high_threshold_hrv']
    low_threshold_hrv = thresholds['low_threshold_hrv']
    
    if clip_id == 'BIOFEEDBACK-REST':
        return 'fobia nula detectada'
    elif hr > high_threshold_hr and hrv < low_threshold_hrv:
        return 'alta fobia detectada'
    elif hr < low_threshold_hr and hrv > high_threshold_hrv:
        return 'baja fobia detectada'
    else:
        return 'fobia moderada detectada'

# Function to calculate HRV metrics
def calculate_hrv_metrics(rr_intervals):
    rr_intervals = np.array(rr_intervals)
    
    # Filter out zero or negative RR intervals
    rr_intervals = rr_intervals[rr_intervals > 0]
    
    if len(rr_intervals) == 0:
        raise ValueError("RR intervals contain zero or negative values only.")
    
    # NN (Normal-to-Normal) intervals
    nn_intervals = rr_intervals
    
    # Mean of RR intervals
    rr_mean = np.mean(rr_intervals)
    
    # Standard deviation of RR intervals
    rr_std = np.std(rr_intervals)
    
    # Heart rate mean (HR mean)
    hr_mean = 60 / rr_mean if rr_mean != 0 else np.nan  # HR mean in beats per minute (1/min)
    
    # Heart rate standard deviation (HR std)
    hr_values = 60 / rr_intervals
    hr_std = np.std(hr_values)
    
    # RMSSD (Root Mean Square of Successive Differences)
    diff_intervals = np.diff(rr_intervals)
    rmssd = np.sqrt(np.mean(diff_intervals ** 2))

    # Convert RMSSD to milliseconds
    rmssd_ms = rmssd * 1000

    return {
        'NN': nn_intervals,
        'RR mean': rr_mean,
        'RR std': rr_std,
        'HR mean': hr_mean,
        'HR std': hr_std,
        'RMSSD': rmssd_ms,  # RMSSD in milliseconds
    }

# Iterate over each VP folder
for vp_folder in vp_folders:
    output_excel = os.path.join(output_dir, f'ECG_Clips_{os.path.basename(vp_folder)}.xlsx')

    # Create ExcelWriter object for this VP
    with pd.ExcelWriter(output_excel, engine='xlsxwriter') as writer:
        ecg_file = os.path.join(vp_folder, 'BitalinoECG.txt')
        triggers_file = os.path.join(vp_folder, 'Triggers.txt')
        
        if os.path.exists(ecg_file) and os.path.exists(triggers_file):
            # Read ECG signal file
            ecg_data = pd.read_csv(ecg_file, sep='\t', header=None, names=['ECG', 'Timestamp', 'Type'])
            ecg_data['Timestamp'] = ecg_data['Timestamp'].astype(str)
            
            # Read triggers file
            triggers = pd.read_csv(triggers_file, sep='\t', header=None, names=['ClipID', 'Start', 'End'])
            triggers = triggers[~triggers['ClipID'].isin(['BIOFEEDBACK-OXYGEN-TRAININGS'])]

            # Filter out clips with ClipID 'BIOFEEDBACK-REST'
            filtered_triggers = triggers[triggers['ClipID'] != 'BIOFEEDBACK-REST']

            # Create output directory for VP if it doesn't exist
            vp_id = os.path.basename(vp_folder)
            vp_output_dir = os.path.join(output_dir, vp_id)
            os.makedirs(vp_output_dir, exist_ok=True)

            # List to store all BPMs and HRV metrics
            bpm_list = []
            hrv_list = []

            # Calculate thresholds excluding 'BIOFEEDBACK-REST' clips
            if not filtered_triggers.empty:
                hr_values = []
                rmssd_values = []

                for idx, row in filtered_triggers.iterrows():
                    clip_id = row['ClipID']
                    start_time = row['Start']
                    end_time = row['End']

                    # Filter ECG data within clip interval
                    clip_data = ecg_data[(ecg_data['Timestamp'] >= str(start_time)) & (ecg_data['Timestamp'] <= str(end_time))].copy()
                    clip_data['Seconds'] = np.arange(0, len(clip_data)) / 100.0

                    # Apply wavelet filtering with db5
                    signal = clip_data['ECG'].values
                    max_level = pywt.dwt_max_level(len(signal), 'db5')
                    level = min(5, max_level)
                    if len(signal) > 0:
                        coeffs = pywt.wavedec(signal, 'db5', level=level)
                        reconstructed_signal = pywt.waverec(coeffs, 'db5')
                        clip_data['Filtered_ECG'] = reconstructed_signal[:len(signal)]

                        # Calculate BPM using calculate_bpm function
                        bpm, rr_intervals = calculate_bpm(clip_data['Filtered_ECG'].values, fs=100)

                        # Calculate HRV metrics using the rr_intervals from calculate_bpm
                        hrv_metrics = calculate_hrv_metrics(rr_intervals)

                        # Separate NN intervals from other HRV metrics
                        nn_intervals = hrv_metrics.pop('NN')

                        # Add HR mean and RMSSD to lists for threshold calculation
                        hr_values.append(hrv_metrics['HR mean'])
                        rmssd_values.append(hrv_metrics['RMSSD'])

                        # Classify fobia level
                        thresholds = {
                            'high_threshold_hr': np.percentile(hr_values, 75),
                            'low_threshold_hr': np.percentile(hr_values, 25),
                            'high_threshold_hrv': np.percentile(rmssd_values, 75),
                            'low_threshold_hrv': np.percentile(rmssd_values, 25)
                        }
                        fobia_level = classify_fobia(hrv_metrics['HR mean'], hrv_metrics['RMSSD'], clip_id, thresholds)

                        # Plot data with BPM value
                        plt.figure(figsize=(10, 4))
                        plt.plot(clip_data['Seconds'], clip_data['Filtered_ECG'], label='Filtered ECG (db5)')
                        plt.xlabel('Time (s)')
                        plt.ylabel('ECG (mV)')
                        plt.title(f'ECG Signal with db5 Wavelet Filter for {clip_id}')
                        plt.legend()
                        plt.grid(True)
                        plt.text(0.95, 0.95, f'BPM: {float(bpm):.2f}\nFobia Level: {fobia_level}', transform=plt.gca().transAxes, fontsize=12, ha='right', va='top',
                                bbox=dict(facecolor='white', edgecolor='black', boxstyle='round,pad=0.5'))
                        output_file = os.path.join(vp_output_dir, f'{clip_id}_ecg_plot_with_db5_filter.png')
                        plt.savefig(output_file)
                        plt.close()

                        # Save data in Excel sheet
                        sheet_name = f'{clip_id}_filtered'
                        clip_data[['Filtered_ECG', 'Seconds']].to_excel(writer, sheet_name=sheet_name[:31], index=False)

                        # Add HRV metrics to a new sheet in Excel
                        hrv_df = pd.DataFrame(hrv_metrics, index=[0])
                        hrv_df.to_excel(writer, sheet_name=f'HRV-Metrics-{clip_id[:31]}', index=False)

                        # Add NN intervals to a separate sheet
                        nn_df = pd.DataFrame({'NN intervals': nn_intervals})
                        nn_df.to_excel(writer, sheet_name=f'NN-Intervals-{clip_id[:31]}', index=False)

                        # Append BPM and HRV metrics to lists
                        bpm_list.append({'ClipID': clip_id, 'BPM': bpm})
                        hrv_metrics['ClipID'] = clip_id
                        hrv_list.append(hrv_metrics)

                # Save thresholds in Excel for each VP
                thresholds_df = pd.DataFrame(thresholds, index=[0])
                thresholds_df.to_excel(writer, sheet_name='Thresholds', index=False)

                # Write all BPMs in BPM-CLIPS sheet
                if bpm_list:
                    bpm_df = pd.DataFrame(bpm_list)
                    bpm_df.to_excel(writer, sheet_name='BPM-CLIPS', index=False)

                # Write all HRV metrics in HRV-CLIPS sheet
                if hrv_list:
                    hrv_df = pd.DataFrame(hrv_list)
                    hrv_df.to_excel(writer, sheet_name='HRV-CLIPS', index=False)

                # Write classification of fobia in a new sheet
                if not filtered_triggers.empty:
                    classification_df = pd.DataFrame({
                        'ClipID': filtered_triggers['ClipID'],
                        'Fobia Level': filtered_triggers['ClipID'].apply(lambda clip_id: classify_fobia(hrv_metrics['HR mean'], hrv_metrics['RMSSD'], clip_id, thresholds))
                    })
                    classification_df.to_excel(writer, sheet_name='Fobia-Classification', index=False)

            print(f"Procesamiento completo para {vp_id}.")

print("Todos los VP procesados correctamente.")
