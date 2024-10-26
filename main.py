import speech_recognition as sr

rec = sr.Recognizer()

with sr.Microphone(2) as mic:       
    rec.adjust_for_ambient_noise(mic)
    print("Fale algo")
            
    audio = rec.listen(mic)
            
    text = rec.recognize_google(audio, language="pt-BR")  
        
    print(text)        