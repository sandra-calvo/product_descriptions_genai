import streamlit as st
import json
import csv
import pandas as pd 
import vertexai
from vertexai.preview.generative_models import GenerativeModel, Part

def generate_descriptions(product_data, prompt):
    model = GenerativeModel("gemini-pro-vision")

    # Incorporate product data into the prompt
    prompt = f"""{json.dumps(product_data)}{prompt}""" 

    responses = model.generate_content(
        prompt,
        generation_config={
            "max_output_tokens": 2048,
            "temperature": 0.4,
            "top_p": 1,
            "top_k": 32
        },
        safety_settings=[],
        stream=True
    )

    output = {
        "product_data": product_data,  # Add product data
        "prompt": prompt,              # Add the prompt
        "description": []
    }

    for response in responses:
         output["description"].append(response.text)

    return output

def main():
    st.title("Product Description Generator")

    # Prompt input
    prompt = st.text_area("Write a prompt to send to the AI model", height=200)  

    # Upload product data file
    uploaded_file = st.file_uploader("Upload product data file (JSON or CSV)")
    
    # Generate descriptions button
    if st.button("Generate descriptions"):

        if uploaded_file is not None:
            if uploaded_file.name.lower().endswith('.json'):  # Check file extension
                product_data = json.load(uploaded_file)
            elif uploaded_file.name.lower().endswith('.csv'):
                product_data = pd.read_csv(uploaded_file).to_dict(orient='records')  # Use pandas to read CSV
            else:
                st.error("Please upload a JSON or CSV file.")
                return

            # Generate descriptions
            output = generate_descriptions(product_data, prompt)
            for description in output['description']:
                st.write(description)

    # Add CSS for word-wrapping
    st.markdown("""
        <style>
        .stText { 
            word-break: break-word; /* Force word-wrapping */
        }
        </style>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
