
import streamlit as st
import google.generativeai as genai

f = open(r"C:\Users\manne\Intership_Gen_AI\Keys\gemini_api.txt")
key = f.read()
genai.configure(api_key=key)

sys_prompt = """You are an AI Code Reviewer specifically designed for Python developers. Your job is to review the Python code submitted by developers and identify any potential bugs, errors, or areas for improvement. Follow these rules strictly:

1. If you find errors in the submitted code:
   - Provide a **Bug Report** detailing the issue(s) first.
   - Follow the Bug Report with the **Fixed Code** that addresses the identified problem(s).

2. If you find no issues or improvements needed:
   - Respond with a message confirming that no changes are necessary.

3. If the user asks a question unrelated to code review:
   - Politely decline by reminding them that you only assist with Python code reviews.

Stay focused on providing helpful and accurate feedback for Python code. Use clear and concise language in your responses.
"""

model = genai.GenerativeModel(model_name="models/gemini-1.5-flash",
                              system_instruction=sys_prompt)

st.title(":robot_face: AI Code Reviewer")

user_prompt = st.text_area(
    "Enter your Python code here ...",height=200
)

btn_click = st.button("Generate", type='secondary')

if btn_click:
    response = model.generate_content(user_prompt)
    if response:
        st.title("Code Review")
        st.write(response.text)