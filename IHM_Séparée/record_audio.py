import speech_recognition as sr

recognizer = sr.Recognizer()

class record_audio :
    def record_audio():
            with sr.Microphone() as source:
                print("Speak now...")
                recognizer.adjust_for_ambient_noise(source)  # Réglez le bruit ambiant
                audio_data = recognizer.listen(source)  # Enregistrez l'audio à partir du microphone
            return audio_data