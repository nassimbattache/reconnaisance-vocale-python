# Speech Recognition Python

## Installation and Execution Guide for the "projet_caa" Program

This project aims to create an algorithm that processes speech recognition functionality.

### Step 1: Download the "projet_caa" Python File

* Download the "projet_caa" Python file.

### Step 2: Install Required Libraries

* For Windows users, execute the following three command lines to install the necessary modules for speech recognition: Pyaudio, SpeechRecognition, and Pyttsx3.
  ```shell
  pip install pyaudio
  pip install SpeechRecognition
  pip install pyttsx3

* If you encounter any issues with Pyaudio installation, you can use the Windows terminal and execute the following two command lines:
  ```shell
  pip install pipwin
  pipwin install pyaudio
* For Linux or macOS users, use the following commands:
  ```shell
  sudo apt-get install python-pyaudio python3-pyaudio
  pip install SpeechRecognition
  pip install pyttsx3
  
## Step 3: Verify Internet Connection

Ensure that you are connected to the internet, as the program requires an internet connection to function properly.

## Step 4: Execute the Program

Once you have established an internet connection and installed the required libraries, you are ready to execute the program.

## Program Functionality

After execution, you will see the message "Please start speaking after one second" displayed on your terminal.

* From this point, you have one second to start speaking.
* Note that if you exceed three seconds, the program will automatically stop, and you will need to recompile it.

The program is equipped with a threshold frequency to filter the sound source, distinguishing between speech and noise. It is recommended to be close to your computer for better speech recognition.

When you start speaking, your words will be transcribed on your terminal and then converted from text to speech.

Additionally, the program includes a mini assistant that can respond to certain questions, such as providing the current day or greeting you when you say "hello." If the program doesn't understand what you said, it will ask you to repeat it.

That covers the capabilities of our program.
