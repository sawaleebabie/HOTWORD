import matplotlib.pyplot as plt
from scipy.io import wavfile
import os
from pydub import AudioSegment

def graph_spectrogram(wav_file):
    rate, data = get_wav_info(wav_file)
    nfft = 200 
    fs = 8000 
    noverlap = 120 
    nchannels = data.ndim
    if nchannels == 1:
        pxx, freqs, bins, im = plt.specgram(data, nfft, fs, noverlap = noverlap)
    elif nchannels == 2:
        pxx, freqs, bins, im = plt.specgram(data[:,0], nfft, fs, noverlap = noverlap)
    return pxx

def get_wav_info(wav_file):
    rate, data = wavfile.read(wav_file)
    return rate, data

def match_target_amplitude(sound, target_dBFS):
    change_in_dBFS = target_dBFS - sound.dBFS
    return sound.apply_gain(change_in_dBFS)

def load_raw_audio():
    activates = []
    backgrounds = []
    negatives = []
    for filename in os.listdir("D:/Babie/DetectHelp/Data/No"):
        if filename.endswith("wav"):
            activate = AudioSegment.from_wav("D:/Babie/DetectHelp/Data/No/"+filename)
            activates.append(activate)
    for filename in os.listdir("D:/Babie/DetectHelp/Data/BG"):
        if filename.endswith("wav"):
            background = AudioSegment.from_wav("D:/Babie/DetectHelp/Data/BG/"+filename)
            backgrounds.append(background)
    for filename in os.listdir("D:/Babie/DetectHelp/Data/Help"):
        if filename.endswith("wav"):
            negative = AudioSegment.from_wav("D:/Babie/DetectHelp/Data/Help/"+filename)
            negatives.append(negative)
    return activates, negatives, backgrounds

# def load_raw_audio():
#     activates = []
#     backgrounds = []
#     negatives = []
#     for filename in os.listdir("C:/Users/sawalee/Desktop/DetectHelp/Data/No"):
#         if filename.endswith("wav"):
#             activate = AudioSegment.from_wav("C:/Users/sawalee/Desktop/DetectHelp/Data/No/"+filename)
#             activates.append(activate)
#     for filename in os.listdir("C:/Users/sawalee/Desktop/DetectHelp/Data/BG"):
#         if filename.endswith("wav"):
#             background = AudioSegment.from_wav("C:/Users/sawalee/Desktop/DetectHelp/Data/BG/"+filename)
#             backgrounds.append(background)
#     for filename in os.listdir("C:/Users/sawalee/Desktop/DetectHelp/Data/Yes"):
#         if filename.endswith("wav"):
#             negative = AudioSegment.from_wav("C:/Users/sawalee/Desktop/DetectHelp/Data/Yes/"+filename)
#             negatives.append(negative)
#     return activates, negatives, backgrounds