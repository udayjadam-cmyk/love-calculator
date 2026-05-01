import streamlit as st
import requests
import pandas as pd
import hashlib

st.set_page_config(page_title="Love Calculator 💖", page_icon="💖")

API_URL = "https://sheetdb.io/api/v1/61w7u7pkjil40"

st.markdown("""
<style>
.stApp {
    background: linear-gradient(-45deg, #1e1e2f, #2b2b45, #3b1d5c, #111827);
    background-size: 400% 400%;
    animation: gradientMove 10s ease infinite;
    color: white;
}

@keyframes gradientMove {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

h1 {
    text-align: center;
    animation: fadeDown 1s ease;
}

@keyframes fadeDown {
    from { opacity: 0; transform: translateY(-25px); }
    to { opacity: 1; transform: translateY(0); }
}

.stTextInput > div > div > input {
    background-color: #2e2e3e;
    color: white;
    border-radius: 10px;
    border: 1px solid #777;
    padding: 12px;
    transition: 0.3s ease;
}

.stTextInput > div > div > input:focus {
    border: 1px solid #a78bfa;
    box-shadow: 0 0 15px #8b5cf6;
}

.stButton > button {
    background: linear-gradient(90deg, #ec4899, #8b5cf6);
    color: white;
    border-radius: 12px;
    height: 3em;
    width: 100%;
    font-size: 16px;
    font-weight: bold;
    border: none;
    transition: 0.3s ease;
    box-shadow: 0 0 18px rgba(139, 92, 246, 0.6);
}

.stButton > button:hover {
    transform: scale(1.04);
    box-shadow: 0 0 30px rgba(236, 72, 153, 0.9);
}

.result-card {
    text-align: center;
    background: rgba(255,255,255,0.10);
    padding: 25px;
    border-radius: 20px;
    margin-top: 25px;
    border: 1px solid rgba(255,255,255,0.18);
    animation: popUp 0.7s ease;
}

@keyframes popUp {
    from { opacity: 0; transform: scale(0.85); }
    to { opacity: 1; transform: scale(1); }
}

.score {
    font-size: 55px;
    font-weight: 900;
    color: #f9a8d4;
}

.watermark {
    position: fixed;
    bottom: 10px;
    right: 15px;
    opacity: 0.55;
    font-size: 13px;
    color: white;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="watermark">Made by Uday 💖</div>', unsafe_allow_html=True)

st.markdown("<h1>💖 AI Love Calculator</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align:center;'>Find your love compatibility 😄</h4>", unsafe_allow_html=True)

def love_score(name1, name2):
    name1 = name1.strip().lower()
    name2 = name2.strip().lower()
    names = sorted([name1, name2])
    combined = names[0] + names[1]
    hash_value = hashlib.md5(combined.encode()).hexdigest()
    return int(hash_value, 16) % 61 + 40

def save_data(name1, name2, score):
    data = {
        "data": [{
            "Your Name": name1,
            "Crush Name": name2,
            "Score": score
        }]
    }
    try:
        requests.post(API_URL, json=data)
    except:
        pass

def get_message(score):
    if score > 90:
        return "💍 Shaadi pakki 😎"
    elif score > 75:
        return "🔥 Strong connection!"
    elif score > 60:
        return "🙂 Good chance, try harder!"
    elif score > 50:
        return "😅 Mixed signals bro..."
    else:
        return "💔 Friendzone alert!"

name1 = st.text_input("👤 Your Name")
name2 = st.text_input("💘 Crush Name")

if st.button("❤️ Calculate Love"):
    if name1.strip() == "" or name2.strip() == "":
        st.warning("⚠️ Please enter both names!")
    else:
        score = love_score(name1, name2)
        save_data(name1, name2, score)

        st.markdown(
            f"""
            <div class="result-card">
                <div class="score">{score}%</div>
                <h3>{get_message(score)}</h3>
            </div>
            """,
            unsafe_allow_html=True
        )

        if score > 90:
            st.balloons()

st.markdown("---")
st.subheader("🔥 Top Love Scores")

try:
    data = pd.read_json(API_URL)
    if not data.empty:
        data["Score"] = data["Score"].astype(int)
        top = data.sort_values(by="Score", ascending=False).head(5)
        st.dataframe(top)
    else:
        st.write("No data yet 😄")
except:
    st.write("Unable to load leaderboard")

st.markdown("---")
st.caption("😄 This is a fun project, not real love prediction.")
