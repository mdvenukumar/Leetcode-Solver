import streamlit as st
import google.generativeai as genai

YOUR_API_KEY = st.secrets["KEY"]
genai.configure(api_key=YOUR_API_KEY)

# Set up the model
generation_config = {
    "temperature": 0.9,
    "top_p": 0.8,
    "top_k": 1,
    "max_output_tokens": 800,
}

safety_settings = [
    {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
]

model = genai.GenerativeModel(
    model_name="gemini-pro", generation_config=generation_config, safety_settings=safety_settings
)

# UI Improvements
st.set_page_config(
    page_title="Leetcode Problem Solver",
    page_icon="https://cdn-icons-png.flaticon.com/128/3499/3499613.png",
    layout="wide",
)

# Set Cascadia Code as the default font and make text bolder
st.markdown(
    """
    <style>
        body {
            font-family: 'Cascadia Code';
        }
        .sidebar-content {
            background-color: #2C3E50;
            padding: 20px;
            border-radius: 10px;
            margin: 10px 0;
        }
        .feature-button {
            color: #000000; /* Set text color to black */
            background-color: #bdebff;
            padding: 10px;
            border-radius: 5px;
            margin: 5px 0;
            cursor: pointer;
            font-weight: bold; /* Make text bold */
            display: flex;
            align-items: center;
        }
        .feature-button i {
            margin-right: 10px;
        }
        .upcoming-upgrade {
            color: #000000; /* Set text color to black */
            background-color: #bdebff;
            padding: 10px;
            border-radius: 5px;
            margin: 5px 0;
            font-weight: bold; /* Make text bold */
        }
        .generated-code-container {
            background-color: #1f1f1f;
            padding: 15px;
            border-radius: 8px;
            margin-bottom: 15px;
            font-family: 'Cascadia Code', monospace;
            max-width: 100%; /* Set the maximum width to 100% */
            overflow-x: auto; /* Enable horizontal scrolling if needed */
        }
        .generated-code-container pre {
            color: #ffffff;
            font-size: 15px;
            font-weight: bold; /* Make text bold */
            white-space: pre-wrap; /* Preserve spaces and allow wrapping */
            word-wrap: break-word; /* Break long words to the next line */
        }
        .creator-info {
            color: #ECF0F1;
            font-size: 14px;
            margin-top: 20px;
        }
        .social-icons {
            display: flex;
            align-items: center;
            margin-top: 10px;
        }
        .social-icon {
            font-size: 24px;
            margin-right: 10px;
            color: #ECF0F1;
        }
        .features-upgrades-container {
            display: flex;
            flex-direction: column;
            align-items: flex-start;
            font-size: 14px;
            margin-top: 10px;
        }
        .features-upgrades-title {
            font-size: 18px;
            font-weight: bold;
            margin-bottom: 5px;
        }
        .logo-container {
            display: flex;
            align-items: center;
            margin-bottom: 20px;
        }
        .logo {
            width: 50px;
            height: 50px;
            margin-right: 10px;
        }
        .app-name {
            font-size: 30px;
            font-weight: bold;
            color: #3498db;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# Main Content
st.markdown(
    """
    <div class="logo-container">
        <img src="https://cdn-icons-png.flaticon.com/128/3499/3499613.png" alt="Logo" class="logo">
        <div class="app-name">Leetcode Problem Solver</div>
    </div>
    """,
    unsafe_allow_html=True,
)


# User Input
prompt_template = st.text_area(
    "Prompt Template", placeholder="Paste your Leetcode Question Completely...."
)
st.sidebar.markdown(
    """
    <div class="logo-container">
        <img src="https://cdn-icons-png.flaticon.com/128/3499/3499613.png" alt="Logo" class="logo">
        <div class="app-name">Leetcode Problem Solver</div>
    </div>
    """,
    unsafe_allow_html=True,
)


# Features
feature_buttons = [
    {"icon": "", "text": "👉 Answering Coding Questions"},
    {"icon": "", "text": "👉 Debugging and Optimizing"}
]

# Display Features
st.sidebar.markdown('<div class="features-upgrades-title">Features ❤️</div>', unsafe_allow_html=True)
for feature in feature_buttons:
    st.sidebar.markdown(
        f'<div class="feature-button"><i class="fas {feature["icon"]}"></i>{feature["text"]}</div>',
        unsafe_allow_html=True,
    )

# Upcoming Upgrades Section
st.sidebar.markdown("---")  # Adding a separator line for better visual separation

# Upcoming Upgrades
upcoming_upgrades = [
    "🔥 Conversational Memory",
    "🔥 Improved Understanding",
]

# Display Upcoming Upgrades
st.sidebar.markdown('<div class="features-upgrades-title">Upcoming 🐣</div>', unsafe_allow_html=True)
for upgrade in upcoming_upgrades:
    st.sidebar.markdown(
        f'<div class="upcoming-upgrade">{upgrade}</div>',
        unsafe_allow_html=True,
    )

# Creator Info Section
st.sidebar.title("Follow the Creator")

# Social Icons
st.sidebar.markdown(
    """
    <div class="social-icons">
        <a href="https://www.instagram.com/_the_vk.__/" target="_blank" class="social-icon">
            <img src="https://cdn-icons-png.flaticon.com/128/2111/2111421.png" alt="Instagram" style="width:24px;height:24px;">
        </a>
        <a href="https://www.linkedin.com/in/venukumarmd/" target="_blank" class="social-icon">
            <img src="https://cdn-icons-png.flaticon.com/128/1384/1384889.png" alt="LinkedIn" style="width:24px;height:24px;">
        </a>
    </div>
    """,
    unsafe_allow_html=True,
)

# Generate Code Button
if st.button("Generate"):
    if prompt_template:
        initial_prompt = "Your name is Veddy AI, created by Mutyala Durga Venu Kumar. Your role is to assist folks with coding. They present you with code questions and direct you to develop proper responses based on your analysis. Whatever your personality is, keep your talk short yet to the point while addressing general questions, but show your fullest performance while answering coding questions! Also, avoid being too imaginative by answering plainly and accurately. Give your codes accurately and optimized. If the prompt is more related to personal questions regarding the creator, just indicate it is confidential information and wait to know more. The most important thing is you are only designed to help in coding; if any other question asked not relevant to coding, you should not respond to it. Explain the process and also at the end suggest them similar problems."

        # Combine the initial prompt and user input as the prompt for the model
        combined_prompt = initial_prompt + "\n" + prompt_template

        try:
            # Add a spinner while loading
            with st.spinner("Generating ..."):
                response = model.generate_content([combined_prompt])

            # Create a container for displaying the generated code
            with st.container():
                # Display Generated Code without an expander
                st.markdown(response.text)
        except Exception as e:
            st.error("An error occurred. Please try again later.")
            st.info("Be patient; many upgrades are on the way 🔥")
        st.markdown("---")
        st.info("💡Feel free to experiment with different prompts and let Veddy AI assist you with coding!")



hide_streamlit_style = """
            <style>
            [data-testid="stToolbar"] {visibility: hidden !important;}
            footer {visibility: hidden !important;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
st.markdown(
        """
        <div style="position: fixed; bottom: 10px; left: 10px; background-color: #bdebff; padding: 10px; border-radius: 8px; color: black; font-weight:bold";>
            THEVK
        </div>
        """,
        unsafe_allow_html=True
    )

