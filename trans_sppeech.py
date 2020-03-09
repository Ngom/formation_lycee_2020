import IPython.display as ipd
ipd.Audio("/home/elhadji/Desktop/test.wav")

import speech_recognition as sr # importation du module 
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Silence, transcription en cours .... ")
    audio = r.listen(source)


#with sr.AudioWavFile("test.wav") as source:              # use "test.wav" as the audio source
#    audio = r.record(source)                        # extract audio data from the file
   
    try:
        #text = r.recognize_google(audio) anglais par defaut !
        text = r.recognize_google(audio,language="fr-FR")
        print("Transcription : ",text)
        with open("transvidactique", "a") as transcript :
        	transcript = transcript.write("\n"+text)
    except Exception: 
        print("la source sonore est inaudible ! Reprenez.")