import streamlit as st
from google import genai
import os
from dotenv import load_dotenv

load_dotenv(override=True)

st.set_page_config(page_title="Georgian AI Analyzer", page_icon="🇬🇪", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #f5f7f9; }
    .stButton>button { width: 100%; border-radius: 5px; height: 3em; background-color: #4CAF50; color: white; }
    .stTextArea { border-radius: 10px; }
    </style>
    """, unsafe_allow_html=True)

API_KEY = os.getenv("GEMINI_API_KEY")

with st.sidebar:
    st.header("⚙️ პარამეტრები")
    analysis_type = st.selectbox(
        "აირჩიეთ ანალიზის ტიპი:",
        ["მოკლე შინაარსი (Summary)", "ძირითადი პუნქტები (Bullet Points)", "კრიტიკული ანალიზი", "გამარტივებული ენა"]
    )
    st.info("ეს აპლიკაცია იყენებს Gemini 2.0 Flash მოდელს.")

st.title("🇬🇪 ქართული ტექსტის AI აგენტი")
st.write("ჩააკოპირეთ ტექსტი ქვემოთ და მიიღეთ მყისიერი ანალიზი.")

col1, col2 = st.columns([1, 1])

with col1:
    input_text = st.text_area("ტექსტი:", height=400, placeholder="აქ ჩაწერეთ ტექსტი გასაანალიზებლად...")
    submit_button = st.button("🚀 გაანალიზე ტექსტი")

with col2:
    st.subheader("📝 შედეგი")
    if submit_button:
        if not API_KEY:
            st.error("API გასაღები ვერ მოიძებნა.")
        elif not input_text:
            st.warning("⚠️ გთხოვთ, ჩაწეროთ ტექსტი.")
        else:
            try:
                client = genai.Client(api_key=API_KEY)
                
                prompts = {
                    "მოკლე შინაარსი (Summary)": "შენ ხარ რედაქტორი. შეაჯამე ტექსტი მოკლედ:",
                    "ძირითადი პუნქტები (Bullet Points)": "გამოყავი ტექსტიდან მნიშვნელოვანი ფაქტები პუნქტებად:",
                    "კრიტიკული ანალიზი": "მოახდინე ტექსტის კრიტიკული ანალიზი:",
                    "გამარტივებული ენა": "გადაწერე ეს ტექსტი მარტივი ქართულით:"
                }
                
                with st.spinner('⏳ აგენტი ამუშავებს მონაცემებს...'):
                    response = client.models.generate_content(
                        model="gemini-2-flash",
                        contents=f"{prompts[analysis_type]}\n\n{input_text}"
                    )
                    st.success("მზადაა!")
                    st.markdown(response.text)
            except Exception as e:
                st.error(f"შეცდომა: {str(e)}")
    else:
        st.write("შედეგი აქ გამოჩნდება.")
