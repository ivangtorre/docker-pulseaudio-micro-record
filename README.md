# Docker-pulseaudio-micro-record
This is a minimal Docker-Ubuntu configuration that is able to record sounds from a microphone using Pyaudio.

Getting access to microphone from Pyaudio is a requirement in many Speech Recognition Systems and they are usually based on Dockers. It is not uncommon that accessing microphones from those Docker containers to become one of the biggest issues. Known problems include not having access at all or mute signal recorded.

# Requirements
This repo has been tested with Ubuntu 18.04, Python 3.6.9, Pyaudio 0.2.11, Docker version 19.03.11 and Pulseaudio 11.1. However it works with many other configurations.

# Instructions
## First configure pulseaudio.
In terminal:
```bash
sudo apt-get install paprefs
```
In terminal:
```bash
paprefs
```
In the pop up window (pulseaudio preferences) on "Network Server" tab: Check "Enable network access to local sound devices" and check “don’t require authentification”.

Then **restart Ubuntu**

## Exectue test
Clone repository:
```bash
git clone https://github.com/ivangtorre/Docker-pulseaudio-micro-record && cd Docker-pulseaudio-micro-record
```

Build docker:
```bash
sudo docker build -t pyaudio .
```

Execute docker:
```bash
sudo docker run -it --rm --network host -e DISPLAY=$DISPLAY -v /tmp/.X11-unix/:/tmp/.X11-unix -v /home:/home --device /dev/bus/usb --device /dev/snd pyaudio
```

Execute test:
The test first will show available input devices and ask the user to input the number of the device to use. Then, it will record sounds from that file during two seconds and save an audio file.

```bash
python3 test.py
```

To check the audio file copy it to outside Docker (replace $user with any other path):

```bash
cp pyaudiotest.wav /home/$user/
```







