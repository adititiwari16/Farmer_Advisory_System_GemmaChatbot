# from langchain_community.llms import Ollama
# from langchain.prompts import ChatPromptTemplate
# from langchain.schema import StrOutputParser
# from langchain.schema.runnable import Runnable
# from langchain.schema.runnable.config import RunnableConfig

# import chainlit as cl


# @cl.on_chat_start
# async def on_chat_start():
    
#     # Sending an image with the local file path
#     elements = [
#     cl.Image(name="image1", display="inline", path="gemma.jpeg")
#     ]
#     await cl.Message(content="Hello dost, I am Gyaneshwar. How can I help you ?", elements=elements).send()
#     model = Ollama(model="gyaneshwar")
#     prompt = ChatPromptTemplate.from_messages(
#         [
#             (
#                 "system",
#                 "You are bhumika chauhan, a topper and expert programmer, speak only in geek language. interact as an assistant. ",
#             ),
#             ("human", "{question}"),
#         ]
#     )
#     runnable = prompt | model | StrOutputParser()
#     cl.user_session.set("runnable", runnable)


# @cl.on_message
# async def on_message(message: cl.Message):
#     runnable = cl.user_session.get("runnable")  # type: Runnable

#     msg = cl.Message(content="")

#     async for chunk in runnable.astream(
#         {"question": message.content},
#         config=RunnableConfig(callbacks=[cl.LangchainCallbackHandler()]),
#     ):
#         await msg.stream_token(chunk)

#     await msg.send()



from langchain_community.llms import Ollama
from langchain.schema import StrOutputParser
from langchain.schema.runnable import Runnable
from langchain.schema.runnable.config import RunnableConfig

import chainlit as cl

@cl.on_chat_start
async def on_chat_start():
    # Sending an image with the local file path
    elements = [
        cl.Image(name="", display="inline", path="gemma.jpeg")
    ]
    await cl.Message(content="I'm Lalith, your guide to the Uttarakhand government's agricultural schemes and facilities. I'm here to help you navigate through official tasks and understand the support available to you.",  elements=elements).send()
    model = Ollama(model="Pushkar")
    runnable = model | StrOutputParser()
    cl.user_session.set("runnable", runnable)

@cl.on_message
async def on_message(message: cl.Message):
    runnable = cl.user_session.get("runnable") # type: Runnable

    msg = cl.Message(content="")

    # Directly pass the message content as a string to astream
    async for chunk in runnable.astream(
        message.content, # Pass the message content directly
        config=RunnableConfig(callbacks=[cl.LangchainCallbackHandler()]),
    ):
        await msg.stream_token(chunk)

    await msg.send()
