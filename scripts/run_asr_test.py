import pandas as pd
import torchaudio

# Load dataset
df = pd.read_csv("sample_dialect_dataset.csv")

# Pick a sample record with audio path
sample = df.iloc[0]
audio_path = sample['audio_file_path']
print(f"Loading audio from: {audio_path}")

# Load audio (this assumes you have the .wav file at the specified path)
try:
    waveform, sample_rate = torchaudio.load(audio_path)
    print(f"Sample rate: {sample_rate}")
    print(f"Waveform shape: {waveform.shape}")
except FileNotFoundError:
    print("Audio file not found. Please check if the file exists at the specified path.")