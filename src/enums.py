from enum import Enum

class AnalogAgentMode(str, Enum):
    # Using ChatCompletion
    original: str = "original"
    # Using GroupChat Based
    groupchat: str = "groupchat"
    # Using Captain Agent
    captain: str = "captain"
    # Using Swarm Agent
    swarm: str = "swarm"
    # TestBench Mode
    groupchat_tba: str = "groupchat+tba"
    # RAG Mode
    groupchat_rag: str = "groupchat+rag"
    captain_rag: str = "captain+rag"
    # RAG Mode with CoS
    groupchat_rag_cos: str = "groupchat+rag+cos"
    captain_rag_cos: str = "captain+rag+cos"
