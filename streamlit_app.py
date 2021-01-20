import streamlit as st
import datetime as dt
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
apikey='9k_lDFLbTNzQD_upMVCWze72a0yZy5eFi5eOqKrT-Ghw'
url='https://api.eu-gb.language-translator.watson.cloud.ibm.com/instances/29a391c4-ec76-4dc9-bd5e-58ebd984d31d'

st.title('Simple Api Translator  Using IBM watson ')
now=dt.datetime.now()

st.write(f"Datetime {now}")

input_text=st.text_input('Enter English  Word')


authenticator = IAMAuthenticator(apikey)
lt = LanguageTranslatorV3(version='2018-05-01', authenticator=authenticator)
lt.set_service_url(url)

dict={'hindi': 'en-hi','arabic': 'en-ar','bengali': 'en-bn','english': 'en-en','french': 'en-fr','gujarati': 'en-gu','indonesian': 'en-id','japanese': 'en-ja',
    'malayalam': 'en-ml',

    'myanmar': 'en-my',
    'nepali': 'en-ne',
    'sindhi': 'en-sd',
    'punjabi': 'en-pa',
    'tamil': 'en-ta',
    'telugu': 'en-te',
    'marathi': 'en-mr',
    }
option = st.selectbox( 'Choose Language in this menu',('arabic','bengali','french','gujarati','hindi','indonesian','japanese','malayalam','marathi','myanmar','nepali','punjabi','sindhi','tamil','telugu'))


#if st.button('Listen output'):
#    tts = gtts.gTTS(result, lang=dict[option])
#    tts.save("hola.mp3")
#    playsound("hola.mp3")
#    os.remove("hola.mp3")'''

if st.button('Translate'):
    translation = lt.translate(text=input_text, model_id=dict[option]).get_result()
    st.success(translation['translations'][0]['translation'])
    #st.write(type(dict[option]))
    #st.write('You selected:',dict[option])
if st.button('Fork This Repo'):
    st.success('https://github.com/ameerazam0/translator')
