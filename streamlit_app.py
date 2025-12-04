import streamlit as st
from src.chat_manager import ChatManager
from src.personalities import PERSONALITIES
from src.ui_components import (
    render_sidebar, 
    render_message, 
    render_typing_indicator,
    apply_custom_css
)
from datetime import datetime
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Page configuration
st.set_page_config(
    page_title="AI Chatbot with Personality",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Apply custom CSS
apply_custom_css()

# Initialize session state
if 'messages' not in st.session_state:
    st.session_state.messages = []

if 'current_personality' not in st.session_state:
    st.session_state.current_personality = 'professional_assistant'

if 'chat_manager' not in st.session_state:
    st.session_state.chat_manager = None

if 'groq_api_key' not in st.session_state:
    # Get API key from environment variables or Streamlit secrets
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        try:
            api_key = st.secrets.get("GROQ_API_KEY", "")
        except Exception:
            api_key = ""
    
    st.session_state.groq_api_key = api_key
    
    if not st.session_state.groq_api_key:
        st.error("❌ Groq API key not found. Please set GROQ_API_KEY in environment variables or Streamlit secrets.")
        st.stop()

if 'message_count' not in st.session_state:
    st.session_state.message_count = 0

# Main title
st.markdown("""
<div style='text-align: center; margin-bottom: 40px; padding-top: 20px;'>
    <h1 style='margin: 0; color: #f8fafc; font-size: 3rem; font-weight: 300; letter-spacing: -1px;'>AI Chatbot</h1>
    <p style='color: #cbd5e1; font-size: 18px; margin: 12px 0 0 0; font-weight: 300;'>
        Conversational Intelligence with Sophisticated Personality Modes
    </p>
</div>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.markdown("""
    <div style='text-align: center; margin-bottom: 24px;'>
        <h2 style='color: #f8fafc; margin: 0; font-size: 24px; font-weight: 300;'>Settings</h2>
        <div style='height: 2px; width: 40px; background: linear-gradient(90deg, #4f46e5 0%, #06b6d4 100%); margin: 10px auto; border-radius: 1px;'></div>
    </div>
    """, unsafe_allow_html=True)
    
    st.divider()
    
    st.markdown("""<p style='color: #cbd5e1; font-weight: 300; margin-bottom: 10px; font-size: 13px; text-transform: uppercase; letter-spacing: 0.5px;'>Personality</p>""", unsafe_allow_html=True)
    # Personality selector
    selected_personality = st.selectbox(
        "Select Your AI",
        options=list(PERSONALITIES.keys()),
        format_func=lambda x: f"{PERSONALITIES[x]['emoji']} {PERSONALITIES[x]['name']}",
        index=list(PERSONALITIES.keys()).index(st.session_state.current_personality),
        help="Choose the personality that will guide the conversation",
        label_visibility="collapsed"
    )
    
    # Show personality description
    st.markdown(f"""
    <div style='background: rgba(30, 41, 59, 0.4); backdrop-filter: blur(12px); border-left: 3px solid #4f46e5; padding: 12px; border-radius: 6px; margin-top: 12px;'>
        <p style='color: #f8fafc; font-weight: 300; margin: 0 0 8px 0; font-size: 14px;'>{PERSONALITIES[selected_personality]['emoji']} {PERSONALITIES[selected_personality]['name']}</p>
        <p style='color: #cbd5e1; margin: 0; font-size: 13px; line-height: 1.5; font-weight: 300;'>{PERSONALITIES[selected_personality]['description']}</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Model and Parameters Section
    st.divider()
    st.markdown("""<p style='color: #cbd5e1; font-weight: 300; margin-bottom: 10px; font-size: 13px; text-transform: uppercase; letter-spacing: 0.5px;'>Model Settings</p>""", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        model_name = st.selectbox(
            "AI Model",
            options=[
                "llama-3.3-70b-versatile",
                "llama-3.1-8b-instant",
                "mixtral-8x7b-32768",
                "gemma2-9b-it"
            ],
            index=0,
            help="Select the language model to use",
            label_visibility="collapsed"
        )
    
    with col2:
        temperature = st.slider(
            "Creativity",
            min_value=0.0,
            max_value=1.0,
            value=PERSONALITIES[selected_personality]['temperature'],
            step=0.1,
            help="0 = Focused, 1 = Creative",
            label_visibility="collapsed"
        )
    
    # Statistics Section
    st.divider()
    st.markdown("""<p style='color: #cbd5e1; font-weight: 300; margin-bottom: 12px; font-size: 13px; text-transform: uppercase; letter-spacing: 0.5px;'>Session Stats</p>""", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div style='background: rgba(30, 41, 59, 0.4); backdrop-filter: blur(12px); border: 1px solid rgba(71, 85, 105, 0.3); border-radius: 8px; padding: 12px; text-align: center;'>
            <p style='color: #94a3b8; font-size: 11px; margin: 0 0 6px 0; text-transform: uppercase; letter-spacing: 0.5px;'>Messages</p>
            <p style='color: #f8fafc; font-size: 20px; font-weight: 300; margin: 0;'>{}</p>
        </div>
        """.format(st.session_state.message_count), unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div style='background: rgba(30, 41, 59, 0.4); backdrop-filter: blur(12px); border: 1px solid rgba(71, 85, 105, 0.3); border-radius: 8px; padding: 12px; text-align: center;'>
            <p style='color: #94a3b8; font-size: 11px; margin: 0 0 6px 0; text-transform: uppercase; letter-spacing: 0.5px;'>Active</p>
            <p style='color: #f8fafc; font-size: 20px; font-weight: 300; margin: 0;'>{}</p>
        </div>
        """.format(PERSONALITIES[selected_personality]['emoji']), unsafe_allow_html=True)
    
    # Example Prompts Section
    st.divider()
    st.markdown("""<p style='color: #cbd5e1; font-weight: 300; margin-bottom: 12px; font-size: 13px; text-transform: uppercase; letter-spacing: 0.5px;'>Quick Starters</p>""", unsafe_allow_html=True)
    
    for i, prompt in enumerate(PERSONALITIES[selected_personality]['example_prompts']):
        if st.button(prompt, use_container_width=True, key=f"prompt_{i}"):
            st.session_state.user_input = prompt
    
    # Action Buttons Section
    st.divider()
    st.markdown("""<p style='color: #cbd5e1; font-weight: 300; margin-bottom: 12px; font-size: 13px; text-transform: uppercase; letter-spacing: 0.5px;'>Tools</p>""", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Clear Chat", use_container_width=True, type="secondary"):
            st.session_state.messages = []
            st.session_state.message_count = 0
            st.session_state.chat_manager = None
            st.rerun()
    
    with col2:
        if st.button("📥 Export", use_container_width=True, type="secondary"):
            if st.session_state.messages:
                chat_text = "\n\n".join([
                    f"{'User' if msg['is_user'] else 'Assistant'} ({msg['timestamp']}): {msg['content']}"
                    for msg in st.session_state.messages
                ])
                st.download_button(
                    "Download Chat",
                    chat_text,
                    file_name=f"chat_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt",
                    mime="text/plain",
                    key="export_btn"
                )
    
    # Footer Section
    st.divider()
    st.markdown("""
    <div style='text-align: center; padding: 16px 0; border-top: 1px solid rgba(71, 85, 105, 0.3);'>
        <p style='font-size: 12px; color: #94a3b8; margin: 0 0 8px 0; font-weight: 300;'>
            <strong style='color: #f8fafc;'>AI Chatbot</strong><br/>
            Powered by Groq & LangChain
        </p>
        <a href='https://console.groq.com' target='_blank' style='color: #4f46e5; text-decoration: none; font-size: 11px; font-weight: 300;'>Get API Key →</a>
    </div>
    """, unsafe_allow_html=True)

# Update personality if changed
if selected_personality != st.session_state.current_personality:
    st.session_state.current_personality = selected_personality
    # Update temperature
    PERSONALITIES[selected_personality]['temperature'] = temperature
    # Reinitialize chat manager
    st.session_state.chat_manager = ChatManager(
        api_key=st.session_state.groq_api_key,
        personality=PERSONALITIES[selected_personality],
        model_name=model_name
    )

# Initialize chat manager if needed
if st.session_state.chat_manager is None:
    PERSONALITIES[selected_personality]['temperature'] = temperature
    st.session_state.chat_manager = ChatManager(
        api_key=st.session_state.groq_api_key,
        personality=PERSONALITIES[selected_personality],
        model_name=model_name
    )

# Display chat messages
chat_container = st.container()
with chat_container:
    if not st.session_state.messages:
        # Welcome message
        st.markdown(f"""
        <div style='background: linear-gradient(135deg, rgba(79, 70, 229, 0.1) 0%, rgba(2, 132, 199, 0.05) 100%); backdrop-filter: blur(12px); border: 1px solid rgba(71, 85, 105, 0.3); border-radius: 12px; padding: 40px; text-align: center; margin: 40px auto;'>
            <div style='font-size: 56px; margin-bottom: 20px;'>{PERSONALITIES[selected_personality]['emoji']}</div>
            <h2 style='color: #f8fafc; margin: 0 0 10px 0; font-size: 28px; font-weight: 300;'>Welcome to {PERSONALITIES[selected_personality]['name']}</h2>
            <p style='color: #cbd5e1; margin: 12px 0; font-size: 15px; line-height: 1.6; font-weight: 300;'>{PERSONALITIES[selected_personality]['description']}</p>
            <p style='color: #94a3b8; margin-top: 20px; font-size: 14px; font-weight: 300;'>💡 Try one of the quick starters in the left sidebar to get started!</p>
        </div>
        """, unsafe_allow_html=True)
    else:
        for message in st.session_state.messages:
            render_message(
                message['content'],
                message['is_user'],
                PERSONALITIES[message.get('personality', selected_personality)],
                message['timestamp']
            )

# Chat input
user_input = st.chat_input("Type your message here...", key="chat_input")

# Handle user input from button or chat input
if 'user_input' in st.session_state and st.session_state.user_input:
    user_input = st.session_state.user_input
    del st.session_state.user_input

if user_input:
    # Add user message
    timestamp = datetime.now().strftime("%H:%M:%S")
    st.session_state.messages.append({
        "content": user_input,
        "is_user": True,
        "timestamp": timestamp,
        "personality": selected_personality
    })
    st.session_state.message_count += 1
    
    # Get and stream response
    with st.spinner("🤖 Thinking..."):
        try:
            response_text = ""
            with st.chat_message("assistant", avatar=PERSONALITIES[selected_personality]['emoji']):
                response_placeholder = st.empty()
                
                # Stream response
                for chunk in st.session_state.chat_manager.stream_response(user_input):
                    response_text += chunk
                    response_placeholder.markdown(response_text)
                
                # Store complete response
                timestamp = datetime.now().strftime("%H:%M:%S")
                st.session_state.messages.append({
                    "content": response_text,
                    "is_user": False,
                    "timestamp": timestamp,
                    "personality": selected_personality
                })
                st.session_state.message_count += 1
        except Exception as e:
            st.error(f"❌ Error: {str(e)}")
    
    st.rerun()
