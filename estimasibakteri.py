import pickle
import streamlit as st

model = pickle.load(open('estimasibakteri.sav', 'rb'))
#'aluminium','arsenic','barium','cadmium','chloramine','chromium','copper','flouride','viruses'
# ,'lead','nitrates','nitrites','mercury','perchlorate','radium','selenium','silver','uranium'
st.title('Estimasi pada kandungan air per liternya')
aluminium = st.number_input('Input aluminium Contoh : 1.65')
arsenic = st.number_input('Input arsenic Contohnya : 0.04')
barium = st.number_input('Input barium Contohnya : 2.85')
cadmium = st.number_input('Input cadmium Contohnya : 0.007')
chloramine = st.number_input('Input chloramine Contohnya :0.35 ')
chromium = st.number_input('Input chromium Contohnya : 0.83')
copper = st.number_input('Input copper Contohnya : 0.17')
flouride = st.number_input('Input flouride Contohnya : 0.05')
viruses = st.number_input('Input viruses Contohnya : 0')
lead = st.number_input('Input lead Contohnya : 0.054')
nitrates = st.number_input('Input nitrates Contohnya : 16.08')
nitrites = st.number_input('Input nitrites Contohnya : 1.13')
mercury = st.number_input('Input mercury Contohnya : 0.007')
perchlorate = st.number_input('Input perchlorate Contohnya : 37.75')
radium = st.number_input('Input radium Contohnya : 6.78')
selenium = st.number_input('Input selenium Contohnya : 0.08')
silver = st.number_input('Input silver Contohnya : 0.34')
uranium = st.number_input('Input uranium Contohnya : 0.02')

predict = ''

if st.button('Estimasi Bakteri'):
    predict = model.predict(
        [[aluminium,arsenic,barium,cadmium,chloramine,chromium,copper,flouride,viruses,lead,nitrates,nitrites,mercury,perchlorate,radium,selenium,silver,uranium]]
    )
    st.write ('Estimasi Bakteri: ', predict)