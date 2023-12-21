from gtts import gTTS

class textTransform(object):

    def __init__(self, txt_to_transform, name_audio_to_save):
        self.txt_to_transform = txt_to_transform
        self.name_audio_to_save = name_audio_to_save

    def get_audio_from_txt(self):
        self.txt_to_transform = input("Ingrese el texto a convertir: ")
        self.name_audio_to_save = input("Ingrese el nombre con el que se guardara el audio: ")
        tts = gTTS(self.txt_to_transform, lang='es') # To change teh 
        tts.save(self.name_audio_to_save + '.mp3')

def main():
    object_to_transform = textTransform(txt_to_transform='defaultHelloWorld', name_audio_to_save='defaultNameAudio')
    object_to_transform.get_audio_from_txt()

if __name__ == '__main__':
    main()


#It was a simple, quick and easy example, but you can consult the documentation and try other exercises.
#https://gtts.readthedocs.io/en/latest/module.html
