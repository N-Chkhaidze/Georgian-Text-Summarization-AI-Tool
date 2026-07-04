🇬🇪 Georgian Text Summarization AI Tool
A secure and efficient web application built with Streamlit and Google Gemini AI to provide high-quality summaries of Georgian language texts.

🚀 Overview
This application serves as a centralized AI service. Users can input Georgian text and receive a concise, accurate summary without needing to provide their own API keys. The app handles authentication and processing entirely on the backend.

1) 🛠 Technical Overview
The application is architected as a server-side authenticated service:

1.1) Authentication: The app uses a single master API_KEY. This key is stored securely in st.secrets (on the cloud) or a local .env file (for development) and is injected into the runtime environment. The key is never exposed to the user or committed to version control.

1.2) API Integration: It utilizes the google-genai SDK to communicate with the Gemini 2.5 Flash model.


2) Request Lifecycle:

2.1) Trigger: To protect against API abuse, all requests are gated by an st.button element, ensuring the AI only processes data when a user explicitly initiates a request.

2.2) Processing: The app captures input, transmits it via HTTPS to Google’s infrastructure, and renders the AI-generated summary back to the UI.

2.3) Error Handling: Built-in try-except blocks ensure the app remains stable, catching API errors before they can crash the user experience.
