from logging import exception
import speech_recognition as sr
r = sr.Recognizer()

#Função para ouvir e reconhecer a fala
def receber_feedback():
    #microfone = sr.Recognizer()
    all_ = []
    audio_file = "audio02.wav"
    with sr.AudioFile(audio_file) as source:
        print("Fetching file")
        audio_text = r.listen(source)

    try:
        all_.append(audio_text)
        print(all_)

    except exception as e:
        print(e)
    
    return all_

receber_feedback()