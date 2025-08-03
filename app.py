import os
import gradio as gr
import openai

# Load API key from Hugging Face secret
openai.api_key = os.environ["OPENAI_API_KEY"]

def clarity_ai(input_text):
    prompt = f"""
    The user has written the following about their current situation, goals, or dilemma:

    "{input_text}"

    Give a structured response that includes:
    1. Logic-based analysis
    2. Emotional insight
    3. Potential blind spots
    4. Three suggested next actions
    5. A mindset shift or motivational quote
    """

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
            max_tokens=500,
        )
        return response['choices'][0]['message']['content'].strip()
    except Exception as e:
        return f"Error: {e}"

demo = gr.Interface(fn=clarity_ai, inputs="text", outputs="text", title="Pacavita AI")

demo.launch()
