from TTS.api import TTS

# Example text to synthesize
text = "你好，我是一个原型语音助手。"

# Load a pretrained Mandarin TTS model
tts = TTS(model_name="tts_models/zh-CN/baker/tacotron2-DDC-GST", progress_bar=False)

# Generate speech and save to file
tts.tts_to_file(text=text, file_path="mandarin_sample_output.wav")
print("Speech synthesis complete. Output saved to 'mandarin_sample_output.wav'")