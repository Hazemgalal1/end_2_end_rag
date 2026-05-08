# %%
from dotenv import load_dotenv
import os

load_dotenv("D:/ai_rag/.env", override=True)

model = os.getenv("QWEN_MODEL")
print(f"QWEN_MODEL: {model}")
# %%