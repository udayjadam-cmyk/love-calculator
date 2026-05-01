import streamlit as st
import random
import requests
import pandas as pd

# Page setup
st.set_page_config(page_title="Love Calculator 💖", page_icon="💖")

# 🎨 Aesthetic Dark UI
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(to right, #1e1e2f, #2b2b45);
        color: #ffffff;
    }

    /* Title center */
    h1 {
        text-align: center;
    }

    /* Input boxes */
    .stTextInput > div > div > input {
        background-color: #2e2e3e;
        color: white;
        border-radius: 8px;
        border: 1px solid #555;
        padding: 10px;
    }

    /* Buttons */
    .stButton > button {
        background-color: #6c63ff;
        color: white;
        border-radius: 10px;
        height: 3em;
        width: 100%;
        font-size: 16px;
        font-weight: bold;
    }

    .stButton > button:hover {
        background-color: #5753d9;
        color: white;
    }

    /* Dataframe */
    .stDataFrame {
        background-color: #2e2e3e;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Title
st.markdown("<h1>💖 AI Love Calculator</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align:center;'>Find your love compatibility 😄</h4>", unsafe_allow_html=True)

# API
API_URL = "https://sheetdb.io/api/v1/61w7u7pkjil40"

# ❤️ Logic
def love_score(name1, name2):
    random.seed(name1.lower() + name2.lower())
    return random.randint(40, 100)

# 💾 Save silently
def save_data(name1, name2, score):
    data = {
        "data": [
            {
                "Your Name": name1,
                "Crush Name": name2,
                "Score": score
            }
        ]
    }
    try:
        requests.post(API_URL, json=data)
    except:
        pass

# Inputs
name1 = st.text_input("👤 Your Name")
name2 = st.text_input("💘 Crush Name")

# Button
if st.button("❤️ Calculate Love"):
    if name1.strip() == "" or name2.strip() == "":
        st.warning("⚠️ Please enter both names!")
    else:
        score = love_score(name1, name2)

        st.subheader(f"💞 Love Score: {score}%")

        # Messages
        if score > 90:
            st.success("💍 Shaadi pakki 😎")
        elif score > 75:
            st.success("🔥 Strong connection!")
        elif score > 60:
            st.info("🙂 Good chance, try harder!")
        elif score > 50:
            st.warning("😅 Mixed signals bro...")
        else:
            st.error("💔 Friendzone alert!")

        # Save silently
        save_data(name1, name2, score)

# -------------------------------
# Leaderboard
# -------------------------------
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

# Footer
st.markdown("---")
st.caption("😄 This is a fun project, not real love prediction.")