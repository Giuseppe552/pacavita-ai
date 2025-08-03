import os
import gradio as gr
from openai import OpenAI

# Get OpenAI API key from Hugging Face secret
openai_api_key = os.getenv("OPENAI_API_KEY")

if not openai_api_key:
    raise ValueError("OPENAI_API_KEY environment variable not set in Hugging Face secrets.")

# Initialize OpenAI client
client = OpenAI(api_key=openai_api_key)

# System prompt for GPT
system_prompt = """
You are ClarityGPT, an expert mental clarity and decision-making assistant.

When a user pastes their thoughts, dilemmas, or goals, your job is to:

1. Understand their thought process or challenge deeply.
2. Break it down into components: logic, emotion, blind spots.
3. Offer a clear 3-step action plan.
4. Provide one short mindset reframe or motivational quote.

Your tone is calm, honest, structured, and empowering. Avoid fluff.
Always structure your response with the following headers:
- 🔍 Analysis
- 💡 Insights
- ✅ Action Plan (3 steps)
- 🧠 Mindset Shift
"""

def clarify(input_text):
    if not input_text or input_text.strip() == "":
        return "Please enter some thoughts, dilemmas, or goals."

    try:
        # Chat completion using new SDK
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": input_text}
            ],
            temperature=0.7
        )

        reply = response.choices[0].message.content
        return reply

    except Exception as e:
        return f"❌ Error: {str(e)}"

# Set up Gradio UI
description = """
### 🧠 Pacavita - Mental Clarity Assistant

Paste your current thoughts, dilemma, or goal. Get a structured AI-powered breakdown:
- 🔍 Logic, emotion, and blind spots
- ✅ 3 recommended next steps
- 🧠 A mindset shift to help you move forward

Powered by OpenAI. Built with 💡 by Giuseppe552.
"""

iface = gr.Interface(
    fn=clarify,
    inputs=gr.Textbox(lines=10, placeholder="Paste your current thoughts, dilemma, or goal..."),
    outputs=gr.Textbox(lines=20, label="Clarity Response"),
    title="Pacavita - Clarity AI",
    description=description,
    allow_flagging="never"
)

# Launch the app
if __name__ == "__main__":
    iface.launch()
