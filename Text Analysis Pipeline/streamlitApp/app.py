import streamlit as st
import requests
import json

def get_response(user_input):
    url = "http://127.0.0.1:8000/process_text"
    payload = {"text": user_input}
    headers = {"Content-Type": "application/json"}
    
    response = requests.post(url, data=json.dumps(payload), headers=headers)
    
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": f"API Error: {response.status_code}"}

# Streamlit UI
st.title("Conversational Bot")

user_input = st.text_area("Enter your query:")

if st.button("Submit"):
    if user_input.strip():
        with st.spinner("Processing..."):
            response = get_response(user_input)
        
        if "error" in response:
            st.error(response["error"])
        else:
            st.subheader("Response:")
            st.write("**Classification:**", response.get("classification", "N/A"))
            st.write("**Entities:**", ", ".join(response.get("entities", [])))
            st.write("**Summary:**", response.get("summary", "N/A"))
    else:
        st.warning("Please enter a query.")