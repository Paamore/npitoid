import streamlit as st
from datetime import datetime

st.set_page_config(page_title="Générateur d'ID", page_icon="🧩", layout="centered")

st.markdown("""
    <style>
        #MainMenu {visibility: hidden;}    
        header {visibility: hidden;} 
        footer {visibility: hidden;}

        .stApp {
            background: linear-gradient(135deg, #f0f4f8, #d9e2ec);
            font-family: 'Roboto', sans-serif;
            padding: 2rem;
            display: flex;
            justify-content: center;
            align-items: center;
        }

        div[data-testid="stTextInput"] > div > input {
            background-color: #ffffff;
            color: #333333;
            border: 1px solid #d1d5db;
            border-radius: 10px;
            padding: 10px;
            width: 250px; /* Contrôle de la largeur */
            text-align: center; /* Centre le texte à l'intérieur */
        }

        div[data-testid="stButton"] button {
            background-color: #3B82F6;
            color: white;
            border: none;
            border-radius: 8px;
            font-weight: bold;
            padding: 0.75rem 1.25rem;
            font-size: 1rem;
            transition: all 0.3s ease;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }

        div[data-testid="stButton"] button:hover {
            background-color: #2563EB;
            box-shadow: 0 0 15px #3B82F6;
            transform: scale(1.05);
        }

        div[data-testid="stButton"] button:active {
            background-color: #1D4ED8;
            box-shadow: 0 0 20px #1D4ED8;
            transform: scale(0.98);
        }
    </style>
""", unsafe_allow_html=True)


st.title("🔹 Easy_id 🔹")

a = st.text_input("Le NPI")
b= st.text_input("Les deux derniers chiffres de l'année d'émission")

if st.button("Générer ID"):
    if not (a.isdigit() and b.isdigit()):
        st.error("❌ Ce champs ne peut contenir que des chiffres")
    else:
        if int(b) <= int(str(datetime.now().year)[2:4]) and (len(a) == 10):
            result = "20" + a[::-1] + b
            st.success("✅ ID généré avec succès !")
            st.code(result, language="text", line_numbers=False)
        else:
            st.warning("Veuillez vérifier les informations renseignées")
