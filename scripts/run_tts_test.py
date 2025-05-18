from TTS.api import TTS

tts = TTS(model_name="tts_models/zh-CN/baker/tacotron2-DDC-GST")
tts.tts_to_file("你好，我是语音合成测试。", "mandarin_sample_output.wav")
print("TTS complete. Output saved.")