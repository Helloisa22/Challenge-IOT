from gtts import gTTS
from pygame import mixer

print("Ultimo feedback")
voz = gTTS("Aulas com a intenção de manter o aluno envolvido com o assunto sempre com novidades e atividades para toda a sala", lang='pt')
voz.save("voz.mp3")
mixer.init()
mixer.music.load("voz.mp3")
mixer.music.play()

fim = input("Digite algo para finalizar")