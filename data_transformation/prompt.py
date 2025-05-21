




class PromptManager:
    @staticmethod
    def create_zephyr_prompt(query: str, context: str = "") -> str:
        return f"""
<|system|>
You are an AI Assistant that follows instructions extremely well.
Please be truthful and give direct answers. Please tell 'I don't know' if user query is not in context
</s>
<|user|>
Context: {context}

Question: {query}
</s>
<|assistant|>
"""