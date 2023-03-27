import streamlit as st
import matplotlib.pyplot as plt
from utils.utils import get_audio_figure_from_path

#function
@st.cache_data
def load_spectrogram_audio(spec_dir, audio_dir, i) -> plt.figure:
    return get_audio_figure_from_path(spec_dir, audio_dir, i) 

#page
st.subheader("Spectrogram labeled")
(save, sr) = load_spectrogram_audio('dataset/spectrograms', 'dataset/audio', 10)
col1, col2, col3 = st.columns(3)
with col1:
    for i in range(0, len(save), 3):
        st.pyplot(save[i][0])
        st.audio(save[i][1], sample_rate= sr)
with col2:
    for i in range(1, len(save), 3):
        st.pyplot(save[i][0])
        st.audio(save[i][1], sample_rate= sr)
with col3:
    for i in range(2, len(save), 3):
        st.pyplot(save[i][0])
        st.audio(save[i][1], sample_rate= sr)