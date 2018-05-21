from gtts import gTTS

def tts(text_file, lang, name_file):
	with open(text_file, "r") as file:
		text = file.read()
	file = gTTS(text=text,lang=lang)
	filename = name_file
	file.save(filename)

tts("sistema_nervioso.txt", "ES", "sistema_nervioso.mp3")