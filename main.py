import chainlit as cl
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))  # Don't hardcode the key here

model = genai.GenerativeModel("gemini-1.5-flash")  # Or "gemini-pro"

@cl.on_message
async def on_message(message: cl.Message):
    try:
        # --- Retrieve or initialize conversation memory ---
        history = cl.user_session.get("history", [])

        # Append user's message to history
        history.append({"role": "user", "content": message.content})

        # Create the full prompt from history
        full_prompt = "\n".join([f"{item['role'].capitalize()}: {item['content']}" for item in history])

        # Generate response
        response = model.generate_content(full_prompt)

        # Append assistant's reply to history
        history.append({"role": "assistant", "content": response.text})

        # Save updated history in session memory
        cl.user_session.set("history", history)

        # Send assistant's message
        await cl.Message(content=response.text).send()

    except Exception as e:
        await cl.Message(content=f"❌ Error: {e}").send()
