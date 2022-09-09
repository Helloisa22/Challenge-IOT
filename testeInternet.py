from logging import exception
import speech_recognition as sr
r = sr.Recognizer()

def Conversion():
    all_ = []
    audio_file = "audio02.wav"
    with sr.AudioFile(audio_file) as source:
        print("Fetching file")
        audio_text = r.listen(source)
    try:
        print("Conversing audio to text.....")
        text = r.recognize_google(audio_text, language='pt-BR')
        all_.append(text)
    except exception as e:
        print(e)
    
    return all_
Conversion()