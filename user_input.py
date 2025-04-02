import speech_recognition as sr


def get_user_input():
    recognizer = sr.Recognizer()

    with sr.Microphone(device_index=1) as source:
        print("What is your question for Magik-8?\n Speak now...")
        audio = recognizer.listen(source)
    
    try:
        text = recognizer.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        print("Could not understand audio.")
        return None
    except sr.RequestError as e:
        print(f"Could not request results; {e}")
        return None
