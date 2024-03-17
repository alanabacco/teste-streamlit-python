import requests
import streamlit as st

BASE_URL = 'https://passeios-turisticos-bba-server.vercel.app'

def selectInfo(info):
	url = f'{BASE_URL}/{info}'
	response = requests.get(url)
	if response.status_code == 200:
		return response.json()
	else:
		return None

def ui():
    st.title("Passeios Turísticos")
    selected_option = st.selectbox("Selecione uma opção", ["atracoes-turisticas", "hospedagens"])

    if st.button("Buscar"):
        data = selectInfo(selected_option)
        if data is not None:
           st.write(data)

ui()
