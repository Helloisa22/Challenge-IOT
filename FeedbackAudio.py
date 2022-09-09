import speech_recognition as sr


#Função para ouvir e reconhecer a fala
def receber_feedback():
    microfone = sr.Recognizer()

    with sr.Microphone() as source:
        #Redução de ruidos
        microfone.adjust_for_ambient_noise(source)

        print("De o seu Feedback")
        audio = microfone.listen(source)
        resposta = microfone.recognize_google(audio, language='pt-BR')

    try:
        with open("feedback.txt","w") as arquivo:
                feedback = arquivo.write(resposta)
                print(resposta)

    except sr.UnknownValueError:
        print("Não entendi")
    
    return resposta

receber_feedback()