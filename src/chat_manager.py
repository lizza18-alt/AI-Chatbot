from langchain_groq import ChatGroq
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from typing import Generator
import streamlit as st

class ChatManager:
    """Manages chat interactions with Groq API using LangChain"""
    
    def __init__(self, api_key: str, personality: dict, model_name: str = "llama-3.3-70b-versatile"):
        """
        Initialize chat manager with Groq configuration
        
        Args:
            api_key: Groq API key
            personality: Personality configuration dict
            model_name: Groq model to use
        """
        self.api_key = api_key
        self.personality = personality
        self.model_name = model_name
        
        # Initialize Groq LLM with streaming
        self.llm = ChatGroq(
            groq_api_key=api_key,
            model_name=model_name,
            temperature=personality.get("temperature", 0.7),
            max_tokens=2000,
            streaming=True
        )
        
        # Chat history storage (last 10 exchanges)
        self.chat_history = []
        self.max_history = 10
        
        # System message with personality
        self.system_message = SystemMessage(
            content=personality["system_prompt"]
        )
    
    def get_response(self, user_input: str) -> str:
        """
        Get complete response from Groq
        
        Args:
            user_input: User's message
            
        Returns:
            AI's response as string
        """
        try:
            # Build messages list
            messages = [self.system_message]
            messages.extend(self.chat_history)
            
            # Add current user message
            messages.append(HumanMessage(content=user_input))
            
            # Get response
            response = self.llm.invoke(messages)
            
            # Save to history
            self.chat_history.append(HumanMessage(content=user_input))
            self.chat_history.append(AIMessage(content=response.content))
            
            # Keep only last max_history exchanges
            if len(self.chat_history) > self.max_history * 2:
                self.chat_history = self.chat_history[-(self.max_history * 2):]
            
            return response.content
            
        except Exception as e:
            return f"Error communicating with Groq API: {str(e)}"
    
    def stream_response(self, user_input: str) -> Generator[str, None, None]:
        """
        Stream response token by token from Groq
        
        Args:
            user_input: User's message
            
        Yields:
            Response tokens as they arrive
        """
        try:
            # Build messages list
            messages = [self.system_message]
            messages.extend(self.chat_history)
            
            # Add current user message
            messages.append(HumanMessage(content=user_input))
            
            # Stream response
            full_response = ""
            for chunk in self.llm.stream(messages):
                if hasattr(chunk, 'content'):
                    full_response += chunk.content
                    yield chunk.content
            
            # Save to history
            self.chat_history.append(HumanMessage(content=user_input))
            self.chat_history.append(AIMessage(content=full_response))
            
            # Keep only last max_history exchanges
            if len(self.chat_history) > self.max_history * 2:
                self.chat_history = self.chat_history[-(self.max_history * 2):]
            
        except Exception as e:
            yield f"⚠️ Error: {str(e)}"
    
    def clear_memory(self):
        """Clear conversation memory"""
        self.chat_history = []
