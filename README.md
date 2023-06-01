# Reconnaissace-vocale-python :
## Guide d'installation et d'execution du programme projet_caa :
Ce projet a pour objectif de crée un algorithme  qui traite le fonctionnement de la reconnaissance vocale
* premiére étape consiste a telécharger le ficher python projet_caa
* Après avoir finie le téléchargement si vous êtes sur Windows exécuter les trois lignes de commande suivantes afin d’installer ces trois modules Pyaudio, Speechrecognition et Pyttsx3 nécessaire pour la reconnaissance vocale.

pip install pyaudio

pip install Speechrecognition

pip install Pyttsx3

- en cas ou vous rencontrer un problème avec l'installation de Pyaudio qui est parfois compliquer, vous pouvez passer par le terminal de Windows en exécutant les deux lignes de commande suivantes .

pip install pipwin

pipiwin install payaudio

* Dans le cas ou vous travailler sous linux ou MacOs utiliser les commandes suivantes :

sudo apt-get install python-pyaudio python3-pyaudio

pip install Speechrecognition

pip install Pyttsx3

* deuxièmement il faut bien vérifier que vous êtes connectée a internet, sans internet le programme ne marchera pas. 
* Une fois que vous avez établie une connexion internet et que vous avez installé les bibliothèques précédentes , dés a présent vous etes prêt à exécuter le programme.
## Fonctionnement du programme :
Après l’exécution vous allez voir ce message qui s’affichera sur votre terminal « SVP commencer à parler après une seconde »
* A partir de là vous avez une seconde pour commencer à parler ,
Attention si vous dépasser les 3 secondes le programme va s’arrêter automatiquement et il faudra dans ce cas le recompiler une autre fois .
* Le programme est muni d’une fréquence seuil  qui consiste à filtrer le son de la source, autrement dit différencier entre les paroles afin de capter les paroles et non pas le bruite. dans ce cas il est préférable de se rapprocher de votre ordinateur afin d'avoir une meilleure reconnaissance.

* quand vous commencerez a parler, vos paroles vont être transcrite sur votre terminal et puis retranscrite d’un texte a des paroles.  	

* quelques détails aussi, on a rajout d'un mini assistant, qui vous répond a quelques questions par exemple quelle jour il  est ou quand vous lui dite bonjour , il vas par exemple vous donner exactement le jour ou aussi dans le cas ou il ne compred pas ce que vous lui avez dit, dans ce cas il va vous renvoyer un message de répéter et qu’il ne vous a pas compris.

* en fin on a fait le tour sur tout ce que notre programme est capable de faire .

