import streamlit as st
from youtube_analyzer import build_youtube_agent


# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="AI YouTube Analyzer",
    page_icon="🎬",
    layout="centered"
)


# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown(
    """
    <style>

    /* Background */
    .stApp {
        background: linear-gradient(
            135deg,
            #0f172a,
            #111827,
            #0f172a
        );
    }

    /* Main container */
    .block-container {
        max-width: 850px;
        padding-top: 50px;
        padding-bottom: 50px;
    }

    /* Title */
    h1 {
        text-align: center;
        font-size: 44px !important;
        font-weight: 800 !important;
        color: white !important;
        margin-bottom: 10px !important;
    }

    /* Subtitle */
    .subtitle {
        text-align: center;
        color: #cbd5e1;
        font-size: 17px;
        margin-bottom: 40px;
    }

    /* Input label */
    label {
        color: white !important;
        font-weight: 600 !important;
        font-size: 17px !important;
    }

    /* Input box */
    div[data-baseweb="input"] {
        background-color: #1e293b;
        border: 1px solid #475569;
        border-radius: 10px;
    }

    div[data-baseweb="input"] input {
        color: white !important;
        font-size: 16px;
    }

    div[data-baseweb="input"] input::placeholder {
        color: #94a3b8 !important;
    }

    /* Button */
    div.stButton > button {
        width: 100%;
        height: 52px;
        border-radius: 10px;
        border: none;
        background: #ff4b4b;
        color: white;
        font-size: 17px;
        font-weight: 700;
        margin-top: 15px;
    }

    div.stButton > button:hover {
        background: #e63939;
        color: white;
    }

    /* Result heading */
    .result-heading {
        font-size: 25px;
        font-weight: 700;
        color: white;
        margin-top: 35px;
        margin-bottom: 15px;
    }

    /* Footer */
    .footer {
        text-align: center;
        color: #64748b;
        margin-top: 50px;
        font-size: 14px;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# =========================================================
# HEADER
# =========================================================

st.title("🎬 AI YouTube Analyzer")

st.markdown(
    '<div class="subtitle">'
    'Analyze YouTube videos using AI and get meaningful '
    'insights, summaries and key information instantly.'
    '</div>',
    unsafe_allow_html=True
)


# =========================================================
# AGENT
# =========================================================

@st.cache_resource
def get_agent():
    return build_youtube_agent()


agent = get_agent()


# =========================================================
# INPUT
# =========================================================

video_url = st.text_input(
    "🔗 Enter YouTube Video Link",
    placeholder="https://www.youtube.com/watch?v=..."
)


# =========================================================
# BUTTON
# =========================================================

button = st.button("🚀 Analyze Video")


# =========================================================
# ANALYZE
# =========================================================

if button:

    if not video_url.strip():

        st.warning(" Please enter a YouTube video URL.")

    elif (
        "youtube.com" not in video_url
        and "youtu.be" not in video_url
    ):

        st.error(" Please enter a valid YouTube URL.")

    else:

        with st.spinner(" Analyzing your video..."):

            try:

                response = agent.run(
                    f"Analyze this video: {video_url}"
                )

                st.markdown(
                    '<div class="result-heading">'
                    ' Analysis Result'
                    '</div>',
                    unsafe_allow_html=True
                )

                st.markdown(response.content)

            except Exception as e:

                st.error(
                    f" Something went wrong: {e}"
                )


# =========================================================
# FOOTER
# =========================================================

st.markdown(
    '<div class="footer">'
    'Built with BIPIN SINGH  using Streamlit & AI'
    '</div>',
    unsafe_allow_html=True
)