import streamlit as st
import json
import vertexai
from vertexai.preview.generative_models import GenerativeModel

# Initialize Vertex AI with your project ID
vertexai.init(project='YOUR PROJECT ID', location='YOUR LOCATION') ##change to your own project

# Define function to generate text from image
def generate_text_from_image(image_url, prompt):
    try:
        model = GenerativeModel("gemini-pro-vision")
        responses = model.generate_content(
            f"{prompt} Image URL: {image_url}",
            generation_config={
                "max_output_tokens": 2048,
                "temperature": 0.4,
                "top_p": 1,
                "top_k": 32
            },
            safety_settings=[],
            stream=True,
        )

        st.write("**Model Response:**")
        for response in responses:
            st.write(response.text)
    except Exception as e:
        st.error(f"An error occurred: {e}")

# Define function to generate descriptions from JSON
def generate_descriptions_from_json(uploaded_json):
    try:
        model = GenerativeModel("gemini-pro-vision")
        product_data = json.load(uploaded_json)

        # Get the prompt from the UI
        prompt = st.session_state.get("json_prompt", "")
        #Combine prompt and product data 
        combined_input = prompt + "\n" + json.dumps(product_data) 

        # Generate descriptions

        responses = model.generate_content(
            combined_input,
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
            "product_data": product_data,
            "prompt": prompt,
            "description": []
        }

        for response in responses:
            output["description"].append(response.text)

        for description in output['description']:
            st.write(description)
    except Exception as e:
        st.error(f"An error occurred: {e}")

# Company Logo URL
company_logo_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/5/51/Google_Cloud_logo.svg/1280px-Google_Cloud_logo.svg.png" ##Upload company logo

# App Title and Logo
st.title("Product description generator powered by GenAI")
st.image(company_logo_url, width=200)

# App UI
option = st.selectbox(
    "Choose an option:",
    ("Generate Text from Image", "Generate Descriptions from JSON file")
)

if option == "Generate Text from Image":
    image_url = st.text_input("Enter an image URL")
    prompt = st.text_area("Write your prompt for the image", height=150)
    if st.button("Generate descriptions"):
        if image_url and prompt:
            with st.spinner("Generating product description based on an image..."):
                generate_text_from_image(image_url, prompt)
        else:
            st.warning("Please enter an image URL and a prompt.")
elif option == "Generate Descriptions from JSON file":
    # Display prompt area first
    prompt = st.text_area("Write your prompt for the product:", height=150, key ="json_prompt")

    uploaded_json = st.file_uploader("Upload product data as a JSON file", type=["json"])
    if st.button("Generate descriptions"):
        if uploaded_json:
            with st.spinner("Generating descriptions based on product data..."):
                generate_descriptions_from_json(uploaded_json)
        else:
            st.warning("Please upload a product data JSON file.")


# Add CSS for word-wrapping
st.markdown("""
    <style>
    .stText { 
        word-break: break-word; /* Force word-wrapping within the container */
        white-space: pre-wrap;  /* Preserve line breaks from the original text */
    }
    </style>
""", unsafe_allow_html=True)

