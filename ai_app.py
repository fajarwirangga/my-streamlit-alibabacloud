import streamlit as st
import os
import dashscope
from dashscope import Generation

# Set your key here
DASHSCOPE_API_KEY = 'sk-8df1be7f178d46bca355735b2ff11757'
dashscope.base_http_api_url = 'https://dashscope-intl.aliyuncs.com/api/v1'


st.title("🤖 My First AI App")
st.write("Ask me anything and I'll use AI to answer!")

user_input = st.text_input("Your Question:")

if st.button("Get Answer"):
    if not user_input.strip():
        st.warning("Please enter a question first.")
    else:
        with st.spinner("Thinking..."):
            try:
                messages = [
                    {'role':'system','content':'you are a helpful assistant'},
                    {'role': 'user','content': user_input}
                ]
                response = dashscope.Generation.call(
                    # If environment variable is not configured, replace the line below with: api_key="sk-xxx",
                    api_key=DASHSCOPE_API_KEY,
                    model="qwen-turbo", 
                    messages=messages,
                    result_format='message'
                    )
                #response = Generation.call(model='qwen-plus', prompt=user_input)

                answer = response.output.choices[0].message.content
                st.markdown("### 🧠 Response:")
                st.success(answer)
            except Exception as e:
                st.error(f"An error occurred: {str(e)}")