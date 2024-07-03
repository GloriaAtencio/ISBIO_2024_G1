import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import pandas as pd
import os
import glob
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

# Set Matplotlib backend
plt.switch_backend('Agg')

# Load BPM and classification data
base_dir = r'C:\Proyecto final\ECG'
output_dir = r'C:\Proyecto final\RESULTADOS_COMPLETOS'
vp_folders = [os.path.basename(folder) for folder in glob.glob(os.path.join(base_dir, 'VP*'))]

def load_data(vp_id):
    file_path = os.path.join(output_dir, f'ECG_Clips_{vp_id}.xlsx')
    if os.path.exists(file_path):
        excel_data = pd.ExcelFile(file_path)
        return excel_data
    else:
        return None

def plot_ecg(clip_id, vp_id):
    global canvas
    excel_data = load_data(vp_id)
    if excel_data is not None:
        sheet_name = f'{clip_id}_filtered'
        if sheet_name in excel_data.sheet_names:
            data = pd.read_excel(excel_data, sheet_name=sheet_name)
            fig = Figure(figsize=(10, 4))
            ax = fig.add_subplot(111)
            ax.plot(data['Seconds'], data['Filtered_ECG'], label='Filtered ECG (db5)')
            ax.set_xlabel('Time (s)')
            ax.set_ylabel('ECG (mV)')
            ax.set_title(f'ECG Signal with db5 Wavelet Filter for {clip_id}')
            ax.legend()
            ax.grid(True)
            if canvas:
                canvas.get_tk_widget().pack_forget()
            canvas = FigureCanvasTkAgg(fig, master=root)
            canvas.draw()
            canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        else:
            messagebox.showerror("Error", f"Data for clip {clip_id} not found.")
    else:
        messagebox.showerror("Error", f"Data for VP {vp_id} not found.")

def plot_bpm(vp_id):
    global canvas
    excel_data = load_data(vp_id)
    if excel_data is not None:
        if 'BPM-CLIPS' in excel_data.sheet_names:
            bpm_data = pd.read_excel(excel_data, sheet_name='BPM-CLIPS')
            fig = Figure(figsize=(10, 6))
            ax = fig.add_subplot(111)
            bars = ax.bar(bpm_data['ClipID'], bpm_data['BPM'], color='b')
            highest_bpm_clip = bpm_data.loc[bpm_data['BPM'].idxmax()]
            highest_idx = bpm_data[bpm_data['BPM'] == highest_bpm_clip['BPM']].index[0]
            bars[highest_idx].set_color('r')  # Highlight highest BPM
            ax.text(highest_idx, highest_bpm_clip['BPM'], f'Highest BPM: {highest_bpm_clip["BPM"]:.2f}',
                    ha='center', va='bottom', fontsize=12, color='r', fontweight='bold')
            ax.set_xlabel('Clip ID')
            ax.set_ylabel('BPM')
            ax.set_title(f'BPM vs Clip ID for {vp_id}')
            ax.set_xticks(range(len(bpm_data['ClipID'])))
            ax.set_xticklabels(bpm_data['ClipID'], rotation=90)
            fig.tight_layout()
            if canvas:
                canvas.get_tk_widget().pack_forget()
            canvas = FigureCanvasTkAgg(fig, master=root)
            canvas.draw()
            canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        else:
            messagebox.showerror("Error", "BPM-CLIPS data not found.")
    else:
        messagebox.showerror("Error", f"Data for VP {vp_id} not found.")

def show_classification(vp_id, clip_id):
    excel_data = load_data(vp_id)
    if excel_data is not None:
        if 'Fobia-Categoría' in excel_data.sheet_names:
            category_data = pd.read_excel(excel_data, sheet_name='Fobia-Categoría')
            clip_category = category_data[category_data['ClipID'] == clip_id]
            if not clip_category.empty:
                category_text.delete("1.0", tk.END)
                category_text.insert(tk.END, clip_category.to_string(index=False))
            else:
                messagebox.showerror("Error", f"Classification for clip {clip_id} not found.")
        else:
            messagebox.showerror("Error", "Fobia-Categoría data not found.")
    else:
        messagebox.showerror("Error", f"Data for VP {vp_id} not found.")

def plot_hrv_metrics(vp_id):
    excel_data = load_data(vp_id)
    if excel_data is not None:
        hr_metrics_sheets = [sheet_name for sheet_name in excel_data.sheet_names if 'HRV-Metrics' in sheet_name]
        if hr_metrics_sheets:
            hr_metrics_data = pd.concat([pd.read_excel(excel_data, sheet_name) for sheet_name in hr_metrics_sheets])
            messagebox.showinfo("HRV Metrics", hr_metrics_data.to_string(index=False))
        else:
            messagebox.showerror("Error", "No HRV Metrics found for this VP.")
    else:
        messagebox.showerror("Error", f"Data for VP {vp_id} not found.")

def on_vp_select(event):
    vp_id = vp_combobox.get()
    excel_data = load_data(vp_id)
    if excel_data is not None:
        clip_ids = [sheet_name.replace('_filtered', '') for sheet_name in excel_data.sheet_names if '_filtered' in sheet_name]
        clip_combobox['values'] = clip_ids
        clip_combobox.set('')
    else:
        messagebox.showerror("Error", f"Data for VP {vp_id} not found.")

root = tk.Tk()
root.title("ECG Data Analysis")

frame = ttk.Frame(root, padding="10")
frame.pack(fill=tk.BOTH, expand=True)

vp_label = ttk.Label(frame, text="Select VP:")
vp_label.pack(side=tk.LEFT)
vp_combobox = ttk.Combobox(frame, values=vp_folders)
vp_combobox.pack(side=tk.LEFT, padx=5)
vp_combobox.bind("<<ComboboxSelected>>", on_vp_select)

clip_label = ttk.Label(frame, text="Select Clip ID:")
clip_label.pack(side=tk.LEFT)
clip_combobox = ttk.Combobox(frame)
clip_combobox.pack(side=tk.LEFT, padx=5)

plot_ecg_button = ttk.Button(frame, text="Plot ECG", command=lambda: plot_ecg(clip_combobox.get(), vp_combobox.get()))
plot_ecg_button.pack(side=tk.LEFT, padx=5)

plot_bpm_button = ttk.Button(frame, text="Plot BPM", command=lambda: plot_bpm(vp_combobox.get()))
plot_bpm_button.pack(side=tk.LEFT, padx=5)

classification_button = ttk.Button(frame, text="Clasificación", command=lambda: show_classification(vp_combobox.get(), clip_combobox.get()))
classification_button.pack(side=tk.LEFT, padx=5)

hrv_metrics_button = ttk.Button(frame, text="HRV Metrics", command=lambda: plot_hrv_metrics(vp_combobox.get()))
hrv_metrics_button.pack(side=tk.LEFT, padx=5)

category_text = tk.Text(root, wrap=tk.WORD, height=10)
category_text.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

canvas = None

root.mainloop()
