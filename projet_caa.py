import speech_recognition as sr
import pyttsx3
import re
import pdb
import urllib
from urllib.request import  urlopen    
import datetime
pret = True  

def ConnectToInternet (): 
    try : 
        urlopen('https://www.google.com',timeout=1)
        return True 
    except urllib.error.URLError : 
            
        return False     

def SpeechToTeext ( ):  
 global pret     
 engine = pyttsx3.init()
 rec = sr.Recognizer()
 mic = sr.Microphone()
 

 with mic as source:
            
            rec.adjust_for_ambient_noise(source)
            print ("SVP commancer a parler apres une seconde ")
        
         
            while True :
                   
                    audio=rec.listen(source)
                    if ConnectToInternet () :
                        
                     try : 
                         
                        if rec.recognize_google(audio, language="fr-FR")=="bonjour":
                          print("bonjour ! " )
                          engine.say("bonjour!,comment allez vous ?" )
                          engine.runAndWait()
                        elif rec.recognize_google(audio, language="fr-FR")=="qui es-tu":
                          Bot = "je suis votre assistant vertueil cree par monsieur DJAOUAD et monsieur BATTACHE "
                          print(Bot )
                          engine.say(Bot)
                          engine.runAndWait()
                        elif rec.recognize_google(audio, language="fr-FR")=="au revoir":
                          Bot = "a bien tot merci ! " 
                          print(Bot )
                          engine.say(Bot)
                          engine.runAndWait()
                          engine.stop()
                        elif  rec.recognize_google(audio, language="fr-FR") == "on est quel jour"or "quelle jour on est " : 
                            
                         jour = datetime.datetime.today().weekday() + 1
      
                         Day_dict = {1: 'Lundi', 2: 'Mardi', 3: 'Mercredi', 
                                     4: 'Jeudi', 5: 'Vendredi', 6: 'Samedi', 
                                     7: 'Dimanche'} 
      
                         if jour in Day_dict.keys(): 
                             jour_de_la_semaine = Day_dict[jour] 
                             print( "on est le " +jour_de_la_semaine)
                             
                         engine.say(jour_de_la_semaine)
                         engine.runAndWait()
                        else :
                            you = rec.recognize_google(audio, language="fr-FR")
                            print(you )
                            engine.say(you)
                            engine.runAndWait()
                          
                     except : 
                             rec.recognize_google(audio, language="fr-FR")=="" or sr.UnknownValueError 
                             print ("je n'ai pas bien comprie ! veuillez repeter s'il vous plait ")
                             engine.say("je n'ai pas bien comprie ! veuillez repeter s'il vous plait ")
                             engine.runAndWait()
                    else: 
                     pass 



        
if __name__ == '__main__':
 SpeechToTeext ( )      
