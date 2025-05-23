import streamlit as st
from PIL import Image
import base64
import time

# Chargement de l'image de fond
background_image = Image.open("image4.jpg")

# Conversion image fond en base64
def get_base64(image):
    from io import BytesIO
    buffer = BytesIO()
    image.save(buffer, format="JPEG")
    return base64.b64encode(buffer.getvalue()).decode()

bg_base64 = get_base64(background_image)

# Configuration de la page
st.set_page_config(page_title="Promotion 11 Bravo", layout="wide")

# 🎈 Animation des ballons pendant 3 secondes
with st.empty():
    st.balloons()
    #time.sleep(3)
    
# HTML + CSS complet
st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url("data:image/jpeg;base64,{bg_base64}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
        margin: 0;
        padding: 0;
        font-family: 'Georgia', serif;
        color: white;
        min-height: 100vh;
    }}

    .footer {{
        position: fixed;
        bottom: 0;
        left: 0;
        width: 100%;
        background-color: rgba(0, 0, 0, 0.7);
        padding: 8px 0 40px 0; /* padding-bottom pour libérer la place du bouton */
        text-align: center;
        z-index: 999;
    }}

    .footer p {{
        margin: 5px auto;
        font-style: italic;
        font-size: 13px;
        line-height: 1.4;
        max-width: 90%;
    }}

    .whatsapp-button {{
        position: fixed;
        bottom: 5px;
        left: 50%;
        transform: translateX(-50%);
        z-index: 1000;
    }}

    .whatsapp-button a {{
        background-color: #25D366;
        color: white;
        padding: 8px 16px;
        border-radius: 25px;
        text-decoration: none;
        font-size: 14px;
        font-weight: bold;
        box-shadow: 0px 4px 8px rgba(0,0,0,0.3);
    }}

    .whatsapp-button a:hover {{
        background-color: #1ebe5d;
    }}
    </style>

    <!-- Texte en bas -->
    <div class="footer">
        <p>
        Nous sommes heureux de vous accueillir dans la salle des messes de l’armée de l’air.<br>
        Merci de faire partie de ce moment de fraternité, de mémoire et de célébration.<br>
        <strong>Ensemble, plus forts. 11 Bravo, une famille unie !</strong><br>
        <em>SCH MBOUMBA MABICKA Christ Arnold – Président de la Promotion 11 Bravo</em>
        </p>
    </div>

    <!-- Bouton WhatsApp centré en dessous -->
    <div class="whatsapp-button">
        <a href="https://wa.me/24107779633" target="_blank">Cliquez sur WhatsApp</a>
    </div>
    """,
    unsafe_allow_html=True
)
