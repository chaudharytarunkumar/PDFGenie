from gtts import gTTS

def text_to_speech(text, filename="pdf_audio.mp3"):
    tts = gTTS(text)
    tts.save(filename)
    return filename