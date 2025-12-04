import streamlit as st
from datetime import datetime

def apply_custom_css():
    """Apply premium dark theme CSS styling to the Streamlit app"""
    st.markdown("""
    <style>
    * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }
    
    /* Root variables - Premium Dark Theme */
    :root {
        --bg-primary: #0f172a;
        --bg-secondary: #1e293b;
        --bg-tertiary: #334155;
        --bg-card: rgba(30, 41, 59, 0.4);
        --border-color: rgba(71, 85, 105, 0.3);
        --border-light: rgba(100, 116, 139, 0.2);
        --text-primary: #f8fafc;
        --text-secondary: #cbd5e1;
        --text-tertiary: #94a3b8;
        --accent-indigo: #4f46e5;
        --accent-amber: #b45309;
        --accent-emerald: #047857;
        --accent-blue: #0284c7;
    }
    
    html, body {
        background: linear-gradient(135deg, #0f172a 0%, #1a1f35 100%) !important;
        color: var(--text-primary) !important;
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', sans-serif !important;
        font-weight: 400 !important;
    }
    
    /* Main container */
    .main {
        background: transparent !important;
        color: var(--text-primary) !important;
    }
    
    .stMainBlockContainer {
        background: transparent !important;
        padding: 2.5rem !important;
        max-width: 100% !important;
    }
    
    /* Sidebar */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #1a2332 0%, #0f172a 100%) !important;
        border-right: 1px solid var(--border-color) !important;
    }
    
    [data-testid="stSidebar"] [data-testid="stVerticalBlockBorderWrapper"] {
        background: transparent !important;
    }
    
    /* All text elements */
    p, span, label, li {
        color: var(--text-secondary) !important;
        font-weight: 400 !important;
    }
    
    [data-testid="stSidebar"] p,
    [data-testid="stSidebar"] label,
    [data-testid="stSidebar"] span,
    [data-testid="stSidebar"] h1,
    [data-testid="stSidebar"] h2,
    [data-testid="stSidebar"] h3,
    [data-testid="stSidebar"] h4,
    [data-testid="stSidebar"] h5,
    [data-testid="stSidebar"] h6 {
        color: var(--text-secondary) !important;
        font-weight: 300 !important;
    }
    
    /* Headers */
    h1, h2, h3, h4, h5, h6 {
        color: var(--text-primary) !important;
        font-weight: 300 !important;
        letter-spacing: -0.5px !important;
    }
    
    h1 {
        font-size: 2.5rem !important;
        margin-bottom: 0.5rem !important;
    }
    
    h2 {
        font-size: 1.875rem !important;
        font-weight: 300 !important;
    }
    
    h3 {
        font-size: 1.125rem !important;
        font-weight: 400 !important;
        letter-spacing: 0.5px !important;
        text-transform: uppercase !important;
    }
    
    /* Markdown text */
    [data-testid="stMarkdown"] {
        color: var(--text-secondary) !important;
    }
    
    [data-testid="stMarkdown"] h1,
    [data-testid="stMarkdown"] h2,
    [data-testid="stMarkdown"] h3,
    [data-testid="stMarkdown"] h4,
    [data-testid="stMarkdown"] h5,
    [data-testid="stMarkdown"] h6 {
        color: var(--text-primary) !important;
        font-weight: 300 !important;
    }
    
    /* Selectbox */
    .stSelectbox label {
        color: var(--text-secondary) !important;
        font-weight: 400 !important;
    }
    
    .stSelectbox [data-baseweb="select"] {
        border: 1px solid var(--border-color) !important;
        border-radius: 10px !important;
        background: var(--bg-card) !important;
        backdrop-filter: blur(8px) !important;
    }
    
    .stSelectbox [role="button"] {
        color: var(--text-primary) !important;
        font-weight: 400 !important;
    }
    
    /* Slider */
    .stSlider label {
        color: var(--text-secondary) !important;
        font-weight: 400 !important;
    }
    
    .stSlider [role="slider"] {
        border-radius: 10px !important;
    }
    
    /* Metric styling */
    .stMetric {
        background: var(--bg-card) !important;
        backdrop-filter: blur(12px) !important;
        padding: 1.25rem !important;
        border-radius: 12px !important;
        border: 1px solid var(--border-color) !important;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3) !important;
    }
    
    .stMetric label {
        color: var(--text-tertiary) !important;
        font-weight: 400 !important;
        font-size: 0.875rem !important;
    }
    
    .stMetric [data-testid="stMetricValue"] {
        color: var(--text-primary) !important;
        font-weight: 300 !important;
        font-size: 2rem !important;
    }
    
    /* Button styling */
    .stButton > button {
        border-radius: 10px !important;
        border: 1px solid var(--border-color) !important;
        background: var(--bg-card) !important;
        color: var(--text-primary) !important;
        font-weight: 500 !important;
        height: 42px !important;
        transition: all 0.3s ease !important;
        backdrop-filter: blur(8px) !important;
    }
    
    .stButton > button:hover {
        background: rgba(79, 70, 229, 0.15) !important;
        border-color: var(--accent-indigo) !important;
        box-shadow: 0 8px 24px rgba(79, 70, 229, 0.2) !important;
        transform: translateY(-2px) !important;
    }
    
    .stButton > button[type="secondary"] {
        background: rgba(100, 116, 139, 0.1) !important;
        border-color: var(--border-color) !important;
    }
    
    .stButton > button[type="secondary"]:hover {
        background: rgba(79, 70, 229, 0.15) !important;
        border-color: var(--accent-indigo) !important;
    }
    
    /* Chat input */
    .stChatInput input {
        border-radius: 12px !important;
        border: 1px solid var(--border-color) !important;
        background: var(--bg-card) !important;
        backdrop-filter: blur(8px) !important;
        color: var(--text-primary) !important;
        font-size: 1rem !important;
        font-weight: 400 !important;
    }
    
    .stChatInput input:focus {
        border-color: var(--accent-indigo) !important;
        box-shadow: 0 0 0 3px rgba(79, 70, 229, 0.1) !important;
    }
    
    .stChatInput input::placeholder {
        color: var(--text-tertiary) !important;
    }
    
    /* Alert/Info boxes */
    .stAlert {
        border-radius: 12px !important;
        border-left: 4px solid var(--accent-indigo) !important;
        background: rgba(79, 70, 229, 0.1) !important;
        padding: 1rem 1.25rem !important;
        backdrop-filter: blur(8px) !important;
    }
    
    .stAlert p {
        color: var(--text-secondary) !important;
    }
    
    /* Divider */
    hr {
        border: none !important;
        height: 1px !important;
        background: var(--border-color) !important;
        margin: 1.5rem 0 !important;
    }
    
    /* Chat messages */
    .stChatMessage {
        padding: 1rem 0 !important;
    }
    
    .stChatMessage > div {
        background: transparent !important;
    }
    
    .stChatMessage p,
    .stChatMessage span {
        color: var(--text-secondary) !important;
        line-height: 1.6 !important;
    }
    
    /* Caption */
    .stCaption {
        color: var(--text-tertiary) !important;
        font-size: 0.875rem !important;
    }
    
    /* Container background */
    [data-testid="stVerticalBlockBorderWrapper"] {
        background: transparent !important;
    }
    
    /* General text */
    p {
        line-height: 1.6 !important;
    }
    
    /* Welcome section styling */
    .welcome-box {
        background: linear-gradient(135deg, rgba(79, 70, 229, 0.1) 0%, rgba(2, 132, 199, 0.05) 100%);
        border: 1px solid var(--border-color);
        border-radius: 16px;
        padding: 3rem;
        text-align: center;
        margin: 2rem auto;
        box-shadow: 0 25px 50px rgba(0, 0, 0, 0.3);
        backdrop-filter: blur(16px);
    }
    
    .welcome-box h2 {
        color: var(--text-primary);
        font-size: 2rem;
        margin: 1rem 0 0.75rem 0;
        font-weight: 300;
    }
    
    .welcome-box p {
        color: var(--text-secondary);
        font-size: 1rem;
        margin: 0.75rem 0;
        line-height: 1.7;
        font-weight: 300;
    }
    
    /* Scrollbar styling */
    ::-webkit-scrollbar {
        width: 8px;
        height: 8px;
    }
    
    ::-webkit-scrollbar-track {
        background: var(--bg-secondary);
    }
    
    ::-webkit-scrollbar-thumb {
        background: var(--accent-indigo);
        border-radius: 4px;
    }
    
    ::-webkit-scrollbar-thumb:hover {
        background: var(--accent-blue);
    }
    
    /* Personality card styling */
    .personality-card {
        background: var(--bg-card);
        backdrop-filter: blur(12px);
        border: 1px solid var(--border-color);
        border-radius: 12px;
        padding: 1rem;
        margin-top: 0.75rem;
    }
    
    .personality-card strong {
        color: var(--text-primary);
        font-weight: 500;
    }
    
    .personality-card p {
        color: var(--text-secondary);
        font-size: 0.9375rem;
        margin-top: 0.5rem;
    }
    </style>
    """, unsafe_allow_html=True)

def render_message(content, is_user, personality, timestamp):
    """
    Render a chat message with appropriate styling
    
    Args:
        content: The message content
        is_user: Whether the message is from the user
        personality: The personality configuration
        timestamp: Message timestamp
    """
    if is_user:
        with st.chat_message("user", avatar="👤"):
            st.markdown(content)
            st.caption(f"🕒 {timestamp}")
    else:
        with st.chat_message("assistant", avatar=personality.get('avatar', '🤖')):
            st.markdown(content)
            st.caption(f"🕒 {timestamp}")

def render_typing_indicator():
    """Render a typing indicator animation"""
    st.markdown("""
    <div class="typing-indicator">
        <span class="typing-dot"></span>
        <span class="typing-dot"></span>
        <span class="typing-dot"></span>
    </div>
    """, unsafe_allow_html=True)

def render_sidebar():
    """Render the sidebar content"""
    st.sidebar.header("⚙️ Settings")
    
    # Add any additional sidebar components here
    st.sidebar.markdown("### About")
    st.sidebar.info(
        "This AI Chatbot demonstrates different personality types using the Groq API. "
        "Select a personality from the dropdown and start chatting!"
    )
    
    st.sidebar.markdown("### Quick Actions")
    if st.sidebar.button("Clear Chat History", use_container_width=True):
        if 'messages' in st.session_state:
            st.session_state.messages = []
        st.rerun()
    
    # Add a footer
    st.sidebar.markdown("---")
    st.sidebar.markdown("""
    <div style="text-align: center;">
        <p>Powered by Groq API & LangChain</p>
        <p>✨ AI Chatbot with Personality ✨</p>
    </div>
    """, unsafe_allow_html=True)
