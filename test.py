import pyaudio
import wave

# Show available devices 
p = pyaudio.PyAudio()
info = p.get_host_api_info_by_index(0)
numdevices = info.get('deviceCount')
for i in range(0, numdevices):
        dev_info = p.get_device_info_by_host_api_device_index(0, i)
        if (p.get_device_info_by_host_api_device_index(0, i).get('maxInputChannels')) > 0:
            print("Input Device ID {:d} - {:s} (inputs={:.0f}) (sample_rate={:.0f})".format(i,
              dev_info.get('name'), dev_info.get('maxInputChannels'), dev_info.get('defaultSampleRate')))

print("")
value = input("Please input device number and press enter: ")
value = int(value)

dev_info = p.get_device_info_by_host_api_device_index(0, value)

FORMAT = pyaudio.paInt16
CHANNELS = int(dev_info.get('maxInputChannels')) # Otherwise 1 or 2
RATE = int(dev_info.get('defaultSampleRate')) # otherwise 44100, 16000, etc
CHUNK = 256
WAVE_OUTPUT_FILENAME = "pyaudiotest.wav"
MIC_INDEX = value
 
audio = pyaudio.PyAudio()
 
# start Recording
#stream = audio.open(format=FORMAT, channels=CHANNELS, input=True, rate=RATE, frames_per_buffer=CHUNK)
stream = audio.open(format=FORMAT, channels=CHANNELS, input=True, rate=RATE, frames_per_buffer=CHUNK, input_device_index=MIC_INDEX)
print ("recording...")
frames = []
 
for i in range(0, int(RATE / CHUNK * 3)):
    data = stream.read(CHUNK, exception_on_overflow = False)
    frames.append(data)
print ("finished recording")

# stop Recording
stream.stop_stream()
stream.close()
audio.terminate()

waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
waveFile.setnchannels(CHANNELS)
waveFile.setsampwidth(audio.get_sample_size(FORMAT))
waveFile.setframerate(RATE)
waveFile.writeframes(b''.join(frames))
waveFile.close()
