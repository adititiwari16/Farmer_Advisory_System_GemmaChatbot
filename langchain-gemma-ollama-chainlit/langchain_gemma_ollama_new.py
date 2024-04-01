from langchain_community.llms import Ollama
from langchain.prompts import ChatPromptTemplate
from langchain.schema import StrOutputParser
from langchain.schema.runnable import Runnable
from langchain.schema.runnable.config import RunnableConfig

import chainlit as cl

# Assuming you have a function to determine the user profile based on your logic
def determine_user_profile():
    # Implement your logic here to determine the user profile
    # For demonstration, let's return a placeholder profile
    return "profile1" # Placeholder return

# Define default messages for each profile
default_messages = {
    "profile1": "Hello there, I am Gemma. How can I help you?",
    "profile2": "Greetings! I'm here to assist you. What can I do for you today?",
    "profile3": "Welcome! I'm here to provide you with the information you need. How may I assist you?"
}

@cl.on_chat_start
async def on_chat_start():
    # Determine the user profile
    user_profile = determine_user_profile()

    # Select the Ollama model based on the user profile
    if user_profile == "profile1":
        model_name = "Pushkar"
    elif user_profile == "profile2":
        model_name = "gyaneshwar"
    else:
        model_name = "lalith"

    # Instantiate the Ollama model
    model = Ollama(model=model_name)

    # Store the model in the user session
    cl.user_session.set("model", model)

    # Send the initial message based on the user profile
    elements = [
        cl.Image(name="image1", display="inline", path="gemma.jpeg")
    ]
    default_message = default_messages.get(user_profile, "Hello! How can I assist you today?")
    await cl.Message(content=default_message, elements=elements).send()

@cl.on_message
async def on_message(message: cl.Message):
    model = cl.user_session.get("model") # Retrieve the model from the session

    if model is None:
        # Handle the case where model is not set
        await cl.Message(content="Sorry, I couldn't find the model. Please start a new chat.").send()
        return

    msg = cl.Message(content="")

    # Assuming the model has a method to process the message and return the response
    response = model.process(message.content)

    await msg.send(response)

# Adding user profiles to the interact with
@cl.set_chat_profiles
async def chat_profile():
    return [
        cl.ChatProfile(
            name="Pushkar",
            markdown_description="Pushkar is a **English Based Guide**.",
            icon="https://picsum.photos/250",
        ),
        cl.ChatProfile(
            name="Gyaneshwar",
            markdown_description="Gyaneshwar is a **Hindi Based Guide**.",
            icon="https://picsum.photos/200",
        ),
        cl.ChatProfile(
            name="Lalit",
            markdown_description="Lalit is a **Govenrment-official**.",
            icon="https://picsum.photos/250"
        ),
    ]
