import pytest
import sys
sys.path.append('../')
import api.main as main
import os
import numpy as np
import requests

def test_last_number():
    assert main.last_number('dataset_test/test_last_number/') == 1
    
def test_save_spectrogram():
    audio = np.random.rand(16000*5)
    sr = 16000
    args = {"signal_length" : 5, "hop_length" : 512, "num_mels" : 128, "fmin" : 20, "fmax" : 16000}
    number = main.last_number('dataset_test/test_last_number/') + 1
    main.save_spectrogram(audio, sr, number, 'dataset_test/test_save_spectrogram/', args)
    assert os.path.exists(f'dataset_test/test_save_spectrogram/{number}.png')
    
def test_get_audio():
    headers = {
        'accept': 'application/json',
    }

    files = {
        'file': open('XC6671.ogg', 'rb'),
    }

    response = requests.post('http://0.0.0.0:9600/module/1', headers=headers, files=files)
    assert response.status_code == 200

    
    
    
