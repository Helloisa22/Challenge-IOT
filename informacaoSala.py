import os
import speech_recognition as sr

#Função para ouvir e reconhecer a fala
def informacao_sala():
    microfone = sr.Recognizer()

    with sr.Microphone() as source:
        #Redução de ruidos
        microfone.adjust_for_ambient_noise(source)

        print("Deseja abrir o ultimo arquivo de Feedbacks da sala?\nsim\nNao")
        audio = microfone.listen(source)
        resposta = microfone.recognize_google(audio, language='pt-BR')
#  os.system('feedback.txt')
    try:
        if resposta == "sim":
            with open("feedback.txt","w") as arquivo:
                feedback = arquivo.write("Aluna(o) Ana: Aulas com a intencao de manter o aluno imerso em conhecimento\nAluna(o) Pedro: Professor Criativo execelente didatica\nAluna(o) Jose: Professor que sabe interagir com os alunos")
            print("Seu aquivo com os ultimos feddbacks foram criados: Nome do arquivo Feedback.txt")
        elif resposta == "nao":
            print("Ok, não vou abrir..")

    except sr.UnknownValueError:
        print("Não entendi")
    
    return resposta

informacao_sala()