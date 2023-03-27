import sys
sys.path.append('../')
import utils.utils as utils
import numpy as np
    
def test_get_spectrogram():
    args = {"signal_length" : 5, "hop_length" : 512, "num_mels" : 128, "fmin" : 20, "fmax" : 16000}
    audio = np.random.rand(16000*10)
    specs = utils.get_spectrogram(audio, 16000, args)
    assert len(specs) == 2
    assert specs[0].shape == (128, 157)
    assert specs[0].mean() < 0.1 and specs[0].mean() > -0.1
    assert specs[0].std() < 1.1 and specs[0].std() > 0.9
    
def test_get_audio_figure_from_path():
    (save, sr) = utils.get_audio_figure_from_path('../dataset/spectrograms', '../dataset/audio', 10)
    assert len(save) == 30
    assert type(save[0][1]) == np.ndarray
    assert type(sr) == int