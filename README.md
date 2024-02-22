# Product Description Generator with GenAI and Streamlit

This project provides a flexible Streamlit application to generate product descriptions using the power of Vertex AI's GenAI models.

**Key Features**

* **Dual-Mode Generation:**
    * Describe products from images (provide an image URL and a descriptive prompt).
    * Generate descriptions based on structured product data in JSON format, combined with a user-supplied prompt.
* **Powered by Vertex AI GenAI:** Leverages advanced generative text capabilities from Vertex AI.
* **User-Friendly Streamlit Interface:** Provides an intuitive web interface for product description generation.

**Installation**

**Dependencies:**
* Check `requirements.txt` 

**Install:**
```bash
pip install -r requirements.txt
```

**Usage:**
```bash
streamlit run app.py
```

**Web Interface:** The app will open in your web browser.

**Image-Based Generation:** 
  * Enter an image URL in the designated field.
  * Provide a descriptive prompt.
  * Click "Generate descriptions" button.
    
**JSON-Based Generation:**
  * Craft a descriptive prompt for the product.
  * Upload a JSON file containing your product data.
  * Click "Generate descriptions" button.

**Deployment to Google Cloud**

Prerequisites:
* Google Cloud account
* Google Cloud Project
* Google Cloud SDK installed and configured

**Instructions:**
* Environment: Choose an appropriate Google Cloud service (App Engine, Cloud Run, etc.) and create an environment.
* Containerization (if needed): If your chosen deployment method requires containerization, package your app using Docker.
* Deployment: Use gcloud commands to deploy to your chosen Google Cloud service.
* Access: Retrieve the URL to access your deployed application.

**License**
This project is licensed under the MIT License. See LICENSE for details.
