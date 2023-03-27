from fastapi import FastAPI, File
import librosa
import io
import soundfile as sf
import os
import numpy as np
from PIL import Image
import api.utils as utils
import datetime
import uvicorn

def last_number(path : str) -> int:
    """Function to find the last number of the file in the directory

    Args:
        path (str): directory path

    Returns:
        int: last number of the file
    """
    file_name = os.listdir(path)
    if len(file_name) == 0:
        return 0
    file_name = sorted(file_name, key=lambda x: int(x.split('.')[0]))
    return int(file_name[-1].split('.')[0])

def save_spectrogram(audio : np.ndarray, sr : int, number : int, path : str, args : dict) -> None:
    """save spectrogram

    Args:
        audio (np.ndarray): audio to process
        sr (int): sample rate
        number (int): number to save the file
        path (str): path to save the file
        args (dict): arguments to process the audio
    """    
    specs = utils.get_spectrogram(audio, sr, args)
    for mel_spec in specs:
        im = Image.fromarray(mel_spec * 255.0).convert("L")
        im.save(path + f'{number}.png')

app = FastAPI()
args = {"signal_length" : 5, "hop_length" : 512, "num_mels" : 128, "fmin" : 20, "fmax" : 16000}

@app.post("/module/{module_id}")
async def get_audio(module_id: int, file : bytes = File(...)) -> int:
    """Function to get audio from the modules

    Args:
        module_id (int): Id of the module to identify it
        file (bytes, optional): audio file(wav/ogg/mp3). Defaults to File(...).

    Returns:
        int: http code
    """
    audio, sr = librosa.load(io.BytesIO(file))
    sf.write(f'api/last_audio/{module_id}.wav', audio, sr, subtype='PCM_24')
    number = last_number(f'dataset/audio_module/module{module_id}/') + 1 # find last audio/spec name
    sf.write(f'dataset/audio_module/module{module_id}/{number}.wav', audio, sr, subtype='PCM_24')
    save_spectrogram(audio, sr, number, f'dataset/spectrogram_module/module{module_id}/', args)
    #save the last post time
    with open(f'api/{module_id}.txt', 'w') as f:
        f.write(datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
    return 200

if __name__ == "__main__":
    uvicorn.run(app, host = "0.0.0.0", port=9600)