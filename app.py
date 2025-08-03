import gradio as gr
import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")  # Store key as HF Secret

def clarify(text):
    prompt = f"""
You're Clarity AI, an assistant helping users gain mental clarity.

The user just wrote: "{text}"

1. Analyze and summarize their message in terms of logic, emotion, and blind spots.
2. Suggest 3 clear actions they can take today.
3. Offer one short mindset shift, quote, or reframe to help them move forward.

Respond in clean sections:
- Analysis:
- 3 Suggested Actions:
- Mindset Shift:
"""
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response["choices"][0]["message"]["content"]

demo = gr.Interface(fn=clarify, inputs="text", outputs="text", title="Clarity AI")
demo.launch()
