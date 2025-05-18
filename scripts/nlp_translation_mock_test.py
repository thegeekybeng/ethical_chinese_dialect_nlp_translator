import pandas as pd

df = pd.read_csv("sample_dialect_dataset.csv")
dialect = df.loc[0, 'dialect_text']
mandarin = df.loc[0, 'mandarin_text']
english = df.loc[0, 'english_translation']

print("Dialect Input:", dialect)
print("→ Mandarin:", mandarin)
print("→ English:", english)