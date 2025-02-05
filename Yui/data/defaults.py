# Copyright (c) 2021 Itz-fork
import os

class Defaults():
    """
    All the default data of Yui Chat bot

    Variables:
        Chat_Log - Default chat log
        Engine - Default OpenAI Ai Engine
        Max_Tokens - Default Maximum token count
        CHAT_LOG_DB - Dict to save users chat logs (temp)
        Engines_list - List of engines names available in OpenAI 
    """
    Chat_Log = """
You: Hey, Wassup?
Yui: Hey there!
You: I'm {uname}!
Yui:
"""
    Engine = "text-davinci-002"
    Max_Tokens = int(os.environ.get("MAX_TOKENS", 100))
    CHAT_LOG_DB = {}
    Engines_list = ["davinci", "curie", "babbage", "ada", "text-davinci-002", "text-curie-001", "text-babbage-001", "text-ada-001",]
