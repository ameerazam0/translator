import streamlit as st
import datetime as dt
from googletrans import Translator
import gtts
from playsound import playsound
import os

trans=Translator()
st.title('First streamlit project')
now=dt.datetime.now()

st.write(f"it is now {now}")

input_text=st.text_input('Enter English  Word')
if st.button('Listen input'):
    tts = gtts.gTTS(input_text, lang="en")
    tts.save("hola.mp3")
    playsound("hola.mp3")
    os.remove("hola.mp3")



dict={'arabic': 'ar','bengali': 'bn','english': 'en','french': 'fr','gujarati': 'gu','hindi': 'hi','indonesian': 'id','japanese': 'ja',
    'malayalam': 'ml',
    'marathi': 'mr',
    'myanmar': 'my',
    'nepali': 'ne',
    'punjabi': 'pa',
    'sindhi': 'sd',
    'tamil': 'ta',
    'telugu': 'te',
    }
option = st.selectbox( 'Choose Language in this menu',('arabic','bengali','french','gujarati','hindi','indonesian','japanese','malayalam','marathi','myanmar','nepali','punjabi','sindhi','tamil','telugu'))
result=trans.translate(input_text,dest=dict[option]).text
if st.button('Listen output'):
    tts = gtts.gTTS(result, lang=dict[option])
    tts.save("hola.mp3")
    playsound("hola.mp3")
    os.remove("hola.mp3")
if st.button('Translate'):
    st.success(result)
    st.write(type(dict[option]))
    st.write('You selected:',dict[option])
