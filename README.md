# <cui cui interface>

## **Description**

This interface consists of a website and an API to receive audio from different microphones in the wild.

## Installation

TO run the program you need to install different libraries before. 

Run the command : ``` pip install -r requiements.txt``` to install the dependencies

## Website

The website run using [Streamlit library](https://docs.streamlit.io/). It is composed of 2 pages.
* The home page to show the latest audios received by the API
* The library page to see and listen spectrogram and audio of different bird's species 

Run the command ``` streamlit run Home.py``` to run the website

## API

The API receive the different audio of the different microphones, process them into spectrogram  and save the both files in the file system. This one is made using [FastAPI library](https://fastapi.tiangolo.com/) ans use [librosa](https://librosa.org/doc/latest/index.html) to process audio into spectrogram.

Run the command ``` python3 -m api.main``` to run the API.