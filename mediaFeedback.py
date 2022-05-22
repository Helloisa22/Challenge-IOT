import webbrowser as wb
import speech_recognition as sr

#Função para ouvir e reconhecer a fala
def media_feedback():
    microfone = sr.Recognizer()

    with sr.Microphone() as source:
        #Redução de ruidos
        microfone.adjust_for_ambient_noise(source)

        print("Retornar os dados com as medias dos alunos: \nSim\nNao")
        audio = microfone.listen(source)
        resposta = microfone.recognize_google(audio, language='pt-BR')

    try:
        if resposta == "sim":
            wb.open(r'https://docs.google.com/spreadsheets/d/1lxExv5sOKdoHJcaRn2tk4GEQKsxe4vHKzsQ403udqk0/edit?usp=sharing')
            print("Sua respota foi: " + resposta)

    except sr.UnknownValueError:
        print("Não entendi")
    
    return resposta

media_feedback()