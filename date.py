# save this as app.py
import streamlit as st

# Config page
st.set_page_config(page_title="💌 Surprise pour toi", page_icon="💖", layout="centered")

# Custom CSS pour fond romantique et style
st.markdown("""
    <style>
    body {
        background: linear-gradient(to bottom right, #ffe6f0, #ffb3c6);
        color: #d6336c;
        font-family: 'Arial', sans-serif;
        text-align: center;
    }
    .stButton button {
        background-color: #ff4d94;
        color: white;
        border-radius: 8px;
        padding: 10px 20px;
        font-size: 16px;
        margin: 5px;
        cursor: pointer;
    }
    .stButton button:hover {
        transform: scale(1.1);
    }
    .gift {
        font-size: 80px;
        animation: pop 0.5s;
    }
    @keyframes pop {
        0% { transform: scale(0); }
        80% { transform: scale(1.2); }
        100% { transform: scale(1); }
    }
    </style>
""", unsafe_allow_html=True)

st.title("💌 Surprise pour toi 💌")
st.write("Avant la grande question, revivons quelques souvenirs 🥰")

# Questions et réponses
questions = {
    "Date de notre premier rendez-vous ?": ("22 avril", "Après, on a fêté comme il se doit 😆🤣"),
    "Premier cadeau que je t’ai offert ?": ("Strass", "Pour la Saint-Valentin 🥰"),
    "Ma couleur préférée ?": ("Bleu", "Kif mon amour 😍"),
    "Mon plat préféré ?": ("Lasagne", "Même les pâtes à la sauce blanche faites par toi… je les adore 😁 hh"),
    "Mon pays préféré ?": ("Suisse", "N’importe quel endroit tant que c’est avec toi ❤️")
}

# Stocker les réponses
if "step" not in st.session_state:
    st.session_state.step = 0
if "finished" not in st.session_state:
    st.session_state.finished = False

question_keys = list(questions.keys())

if not st.session_state.finished:
    q = question_keys[st.session_state.step]
    options = ["autre", questions[q][0]]  # réponse correcte + "autre"
    st.write(f"**{st.session_state.step+1}️⃣ {q}**")
    choice = st.radio("Choisis ta réponse :", options, key=st.session_state.step)
    
    if st.button("Valider"):
        if choice == questions[q][0]:
            st.success(questions[q][1])
            if st.session_state.step < len(questions)-1:
                st.session_state.step += 1
                st.experimental_rerun()
            else:
                st.session_state.finished = True
                st.experimental_rerun()
        else:
            st.error("Essaie encore 😅")
            st.experimental_rerun()
else:
    st.write("🎀 Veux-tu sortir avec moi pour un rendez-vous le 14 février ? 💖")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("YES 💖"):
            st.balloons()
            st.success("Tu n’imagines pas à quel point je suis heureux… j’attends le 14 février 💙")
            st.markdown('<div class="gift">🎁</div>', unsafe_allow_html=True)
    with col2:
        if st.button("NO 💔"):
            st.warning("Il reste encore une surprise… mais pas comme je l’espérais 😅")
            st.markdown('<div class="gift">🎁</div>', unsafe_allow_html=True)
