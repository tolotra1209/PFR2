import tkinter as tk
import speech_recognition as sr
from record_audio import record_audio

recognizer = sr.Recognizer()
app = tk.Tk()
result_label = tk.Label(app, text="",font="ExtraCondensed 20" )

class recognize_speech :
    def recognize_speech():
        audio_data = record_audio()
        try:
            # Utilisez l'API Google Speech Recognition pour reconnaître la parole
            text = recognizer.recognize_google(audio_data, language="en-EN")
            result_label.config(text="You said: \n" + text)
        except sr.UnknownValueError:
            result_label.config(text="Google Speech Recognition was unable to understand the audio.")
        except sr.RequestError as e:
            result_label.config(text="Unable to access Google Speech Recognition API : " + str(e))