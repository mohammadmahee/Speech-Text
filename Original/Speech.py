import speech_recognition as sr


def speech():
    
    r = sr.Recognizer()

    while True:

            try:
                with sr.Microphone() as mic:

                    r.adjust_for_ambient_noise(mic, duration=0.2)
                    audio= r.listen(mic)

                    text = r.recognize_google(audio)
                    text = text.lower()

                    print("Recognized:",text)

                    if text == 'exit':
                        print("Speech Recognition Stopped.")
                        break

            except sr.UnknownValueError:

                r = sr.Recognizer()
                continue
            




            