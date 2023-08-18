
# pip install librosa
import librosa

y, sr = librosa.load('Action-Rock.mp3')
Nfft = 256

stft = librosa.stft(y, n_fft=Nfft, window='hann')
freqs = librosa.fft_frequencies(sr=sr, n_fft=Nfft)
print(freqs)
