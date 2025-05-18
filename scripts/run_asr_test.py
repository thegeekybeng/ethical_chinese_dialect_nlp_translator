import pandas as pd

# Simulate torchaudio (not supported on Alpine)
df = pd.read_csv("../sample_dialect_dataset.csv")

sample = df.iloc[0]
print("Simulated audio load for:", sample['audio_file_path'])
print("Sample Rate: 16000")
print("Waveform shape: (1, 32000)")