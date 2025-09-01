import speech_recognition as sr
import pyttsx3

#Speech Recognition
r = sr.Recognizer()
start_word = "start"
stop_word = "stopp"

with sr.Microphone() as source:
    print("Warte auf Codewort zum Starten...")

    while True:
        
        audio = r.listen(source, phrase_time_limit=15)
        r.adjust_for_ambient_noise(source, duration=1)
        try:
            command = r.recognize_google(audio, language="de-DE").lower()
            print("Erkannt:", command)
            if start_word in command:
                print("Aufnahme gestartet...")
                break
        except sr.UnknownValueError:
            print("Nicht verstanden.")
        except sr.RequestError as e:
            print("Fehler bei der Anfrage:", e)

    recorded_text = ""
    while True:
        audio = r.listen(source, phrase_time_limit=15)
        r.adjust_for_ambient_noise(source, duration=1)
        try:
            command = r.recognize_google(audio, language="de-DE").lower()
            print("Erkannt:", command)
            if stop_word in command:
                command = command.split(stop_word)[0]
                recorded_text += command.strip() + " "
                print("Aufnahme gestoppt.")
                break
            else:
                recorded_text += command + " "
        except sr.UnknownValueError:
            print("Nicht verstanden.")
        except sr.RequestError as e:
            print("Fehler bei der Anfrage:", e)

#Textausgabe
engine = pyttsx3.init()

# Stimme auswählen
for voice in engine.getProperty('voices'):
    if "Hedda" in voice.name:
        engine.setProperty('voice', voice.id)
        break
engine.setProperty('rate', 150)  # Sprechgeschwindigkeit
engine.setProperty('volume', 1.0)  # Lautstärke (0.0 bis 1.0)

print("Gesamter erkannter Text:")
print(recorded_text)

engine.say(recorded_text)
engine.runAndWait()
