import librosa
import numpy as np
import os
import matplotlib.pyplot as plt

def get_spectrogram(audio : np.array, sr:int, args : dict) -> list[np.array]:
    """Create mel-spectrogram from audio

    Args:
        audio (np.array): audio to create mel-spectrogram from
        sr (int): sample rate
        args (dict): arguments

    Returns:
        list[np.array]: list of mel-spectrograms
    """
    # Split signal into five second chunks
    sig_splits = []
    for i in range(0, len(audio), int(args["signal_length"] * sr)):
        split = audio[i:i + int(args["signal_length"] * sr)]

        # End of signal?
        if len(split) < int(args["signal_length"] * sr):
            break
        
        sig_splits.append(split)
        
    # Extract mel spectrograms for each audio chunk
    specs = []
    for chunk in sig_splits:
        
        mel_spec = librosa.feature.melspectrogram(y=chunk, 
                                                  sr=sr, 
                                                  n_fft=1024, 
                                                  hop_length=args["hop_length"], 
                                                  n_mels=args["num_mels"], 
                                                  fmin=args["fmin"], 
                                                  fmax=args["fmax"])
    
        mel_spec = librosa.power_to_db(mel_spec, ref=np.max) 
        
        # Normalize
        
        mel_spec -= mel_spec.mean()
        mel_spec /= mel_spec.std()
        
        specs.append(mel_spec)
        
    return specs

def get_audio_figure_from_path(dataset_dir : str, audio_dir : str, num_species : int = 10 ) -> tuple[list[list[plt.figure,np.ndarray]], int]:
    """Get audio and figure from path

    Args:
        dataset_dir (str): spectrogram directory
        audio_dir (str): audio directory
        num_species (int, optional): number of species to show. Defaults to 10.

    Returns:
        list[list[plt.figure,np.ndarray]]: list of audio and spectrogram
        int : sample rate
    """
    labels = os.listdir(dataset_dir)
    files = [[file for file in os.listdir(os.path.join(dataset_dir, label))] for label in labels]
    audios = [[file for file in os.listdir(os.path.join(audio_dir, label))] for label in labels]
    saves = []
    for i in range(num_species):
        for j in range(3):
            label = labels[i]
            audio, sr = librosa.load(os.path.join(audio_dir, label, audios[i][j]))
            fig, ax = plt.subplots(1,1, figsize = (10, 5))
            ax.imshow(plt.imread(os.path.join(dataset_dir, label, files[i][j])))
            ax.set_title(label)
            ax.xaxis.set_visible(False)
            ax.yaxis.set_visible(False)
            saves.append([fig, audio])
    return saves, sr
