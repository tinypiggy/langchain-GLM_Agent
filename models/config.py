import os

LOCAL_CONTENT = os.path.join(os.path.dirname(__file__), "../docs")
VS_PATH = os.path.join(os.path.dirname(__file__), "../vector_store/FAISS")
CHUNK_SIZE = 800
CHUNK_OVERLAP = 70
VECTOR_SEARCH_TOP_K = 2
os.environ["SERPAPI_API_KEY"] = "662e7afcfe3733eb1b2e372756e1e753e2857975aed2c9b7b7ae9644ee3c0d4e"

PROMPT_TEMPLATE = """已知信息：
{context}

根据上述已知信息，简洁和专业的来回答用户的问题。如果无法从中得到答案，请给出你认为最合理的回答。答案请使用中文。 问题是：{question}"""
