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
    st.header("⚙️ settings")
    analysis_type = st.selectbox(
        "Select analysis type:",
        ["Summary", "Bullet Points", "Critical Analysis", "Simplified Language"]
    )
    st.info("This application uses the Gemini 2.0 Flash model.")

st.title("🇬🇪 Georgian text AI agent")
st.write("Copy the text below and get an instant analysis.")

col1, col2 = st.columns([1, 1])

with col1:
    input_text = st.text_area("Text:", height=400, placeholder="Enter text here to parse...")
    submit_button = st.button("Analyze text")

with col2:
    st.subheader("Result")
    if submit_button:
        if not API_KEY:
            st.error("API გასაღები ვერ მოიძებნა.")
        elif not input_text:
            st.warning("Please enter text.")
        else:
            try:
                client = genai.Client(api_key=API_KEY)
                
                prompts = {
                    "მოკლე შინაარსი (Summary)": "შენ ხარ რედაქტორი. შეაჯამე ტექსტი მოკლედ:",
                    "ძირითადი პუნქტები (Bullet Points)": "გამოყავი ტექსტიდან მნიშვნელოვანი ფაქტები პუნქტებად:",
                    "კრიტიკული ანალიზი": "მოახდინე ტექსტის კრიტიკული ანალიზი:",
                    "გამარტივებული ენა": "გადაწერე ეს ტექსტი მარტივი ქართულით:"
                }
                
                with st.spinner('The agent is processing the data...'):
                    response = client.models.generate_content(
                        model="gemini-2.5-flash",
                        contents=f"{prompts[analysis_type]}\n\n{input_text}"
                    )
                    st.success("it is Ready!")
                    st.markdown(response.text)
            except Exception as e:
                st.error(f"შეცდომა: {str(e)}")
    else:
        st.write("The result will appear here.")
