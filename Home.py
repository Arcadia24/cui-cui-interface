from PIL import Image

import os
import streamlit as st
import librosa
import time
import numpy as np
import time
import datetime


from utils.utils import get_spectrogram

st.set_page_config(
    page_title="Cui cui",
    page_icon="✅",
    layout="wide",
)

@st.cache_data(ttl=5)
def get_audio_module(path : str, number : int) -> tuple[np.ndarray, int, bool]:
    """get last audio from module

    Args:
        path (str): path to audio
        number (int): number of module

    Returns:
        tuple[np.ndarray, int, bool]: audio, sample rate, exist
    """
    if os.path.isfile(path):
        audio, sr = librosa.load(path, duration=5)
        with open(f'api/{number}.txt', 'r') as f:
            time = datetime.datetime.strptime(f.read(), "%d/%m/%Y %H:%M:%S")
            print(time)
            diff = datetime.datetime.now() - time
            print(diff.total_seconds())
            if diff.total_seconds() > 20:
                return audio, sr, False
        return audio, sr, True
    else :
        return None, 0, False

args = {"signal_length" : 5, "hop_length" : 512, "num_mels" : 128, "fmin" : 20, "fmax" : 16000}
oiseau = Image.open('dataset/image/Banner.jpg')
red = Image.open('dataset/image/red.jpg')
green = Image.open('dataset/image/green.png')
no_spec = Image.open('dataset/image/no_spec.jpg')

#page
st.title('Cui cui')
st.image(oiseau)
placeholder = st.empty()
start_time = time.time()

# infinite loop to fake a live stream
while True:
    with placeholder.container():
        col1, col2, col3, col4, col5, col6 = st.columns(6)
        col7, col8, col9 = st.columns(3)
        audio, sr, exist = get_audio_module('api/last_audio/1.wav', 1)
        with col1:
            st.write("module 1")
        with col2:
            if exist:
                st.image(green, width = 50)
            else:
                st.image(red, width = 50)
        with col7:
            if exist:
                st.audio(audio, sample_rate = sr)
                spec = get_spectrogram(audio, sr, args)[0]
                st.image(spec, clamp=True, channels="Mono")
            else:
                st.write("No audio")
                st.image(no_spec, width = 200)
        audio, sr, exist = get_audio_module('api/last_audio/2.wav', 2)
        with col3:
            st.write("module 2")
        with col4:
            if exist:
                st.image(green, width = 50)
            else:
                st.image(red, width = 50)
        with col8:
            if exist:
                st.audio(audio, sample_rate = sr)
                spec = get_spectrogram(audio, sr, args)[0]
                st.image(spec, clamp=True, channels="Mono")
            else:
                st.write("No audio")
                st.image(no_spec, width = 200)
        audio, sr, exist = get_audio_module('api/last_audio/3.wav', 3)
        with col5:
            st.write("module 3")
        with col6:
            if exist:
                st.image(green, width = 50)
            else:
                st.image(red, width = 50)
        with col9:
            if exist:
                st.audio(audio, sample_rate = sr)
                spec = get_spectrogram(audio, sr, args)[0]
                st.image(spec, clamp=True, channels="Mono")
            else:
                st.write("No audio")
                st.image(no_spec, width = 200)
    time.sleep(5)
    
