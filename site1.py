import streamlit as st

#Conras Imports
import qrcode
#import os
from PIL import Image, ImageDraw, ImageFont

#Formulario
st.markdown("<h1 style= 'text-align: center;'> Gerador de <br>Cartão de visita</h1>", unsafe_allow_html=True)
with st.form("Form 1"):
  #Campos
  col1,col2=st.columns([0.6, 0.4])
  f_name = col1.text_input("Nome")
  cargo = col1.text_input("Cargo")
  email = col1.text_input("e-mail")
  unidade = col1.text_input("Unidade")
  endereco = col1.text_input("Endereco")
  cidade = col1.text_input("Cidade")
  tel_agenda = col1.text_input("Tel_agenda")
  tel_sec = col1.text_input("Tel_sec")
  tel_pessoa = col1.text_input("Tel_pessoal")

  #Botão
  s_state=col1.form_submit_button("Submit", on_click=None )
  if s_state: # Campos Obrigatorios
    if f_name == "" or unidade == "":
      st.warning("Campos Obrigatorios")
#End Formulario

