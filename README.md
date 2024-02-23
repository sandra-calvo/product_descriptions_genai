# Product Description Generator with GenAI and Streamlit

APLICATION DESCRIPTION 
This project provides a flexible Streamlit application to generate product descriptions using the power of Vertex AI's GenAI models.

**Key Features**

* **Dual-Mode Generation:**
    * Describe products from images (provide an image URL and a descriptive prompt).
    * Generate descriptions based on structured product data in JSON format, combined with a user-supplied prompt.
* **Powered by Vertex AI GenAI:** Leverages advanced generative text capabilities from Vertex AI.
* **User-Friendly Streamlit Interface:** Provides an intuitive web interface for product description generation.


**Run the Application locally (on Cloud Shell)**
NOTE: Before you move forward, ensure that you have followed the instructions in SETUP.md. Additionally, ensure that you have cloned this repository and you are currently in the gemini-streamlit-cloudrun folder. This should be your active working directory for the rest of the commands.

To run the Streamlit Application locally (on cloud shell), we need to perform the following steps:

Setup the Python virtual environment and install the dependencies:

In Cloud Shell, execute the following commands:

```bash
python3 -m venv gemini-streamlit
source gemini-streamlit/bin/activate
pip install -r requirements.txt
```

Your application requires access to two environment variables:

GCP_PROJECT : This the Google Cloud project ID.
GCP_REGION : This is the region in which you are deploying your Cloud Run app. For e.g. us-central1.
These variables are needed since the Vertex AI initialization needs the Google Cloud project ID and the region. The specific code line from the app.py function is shown here: vertexai.init(project=PROJECT_ID, location=LOCATION)

In Cloud Shell, execute the following commands:

```bash
export GCP_PROJECT='<Your GCP Project Id>'  # Change this
export GCP_REGION='us-central1'             # If you change this, make sure the region is supported.
```
To run the application locally, execute the following command:

In Cloud Shell, execute the following command:

```bash
streamlit run app.py \
  --browser.serverAddress=localhost \
  --server.enableCORS=false \
  --server.enableXsrfProtection=false \
  --server.port 8080
```

The application will startup and you will be provided a URL to the application. Use Cloud Shell's web preview function to launch the preview page. You may also visit that in the browser to view the application. Choose the functionality that you would like to check out and the application will prompt the Vertex AI Gemini API and display the responses.

Build and Deploy the Application to Cloud Run
NOTE: Before you move forward, ensure that you have followed the instructions in SETUP.md. Additionally, ensure that you have cloned this repository and you are currently in the gemini-streamlit-cloudrun folder. This should be your active working directory for the rest of the commands.

To deploy the Streamlit Application in Cloud Run, we need to perform the following steps:

Your Cloud Run app requires access to two environment variables:

GCP_PROJECT : This the Google Cloud project ID.
GCP_REGION : This is the region in which you are deploying your Cloud Run app. For e.g. us-central1.

These variables are needed since the Vertex AI initialization needs the Google Cloud project ID and the region. The specific code line from the app.py function is shown here: vertexai.init(project=PROJECT_ID, location=LOCATION)

In Cloud Shell, execute the following commands:

```bash
export GCP_PROJECT='<Your GCP Project Id>'  # Change this
export GCP_REGION='us-central1'             # If you change this, make sure the region is supported.
```
Now you can build the Docker image for the application and push it to Artifact Registry. To do this, you will need one environment variable set that will point to the Artifact Registry name. Included in the script below is a command that will create this Artifact Registry repository for you.

In Cloud Shell, execute the following commands:

```bash
export AR_REPO='<REPLACE_WITH_YOUR_AR_REPO_NAME>'  # Change this
export SERVICE_NAME='gemini-streamlit-app' # This is the name of our Application and Cloud Run service. Change it if you'd like.

#make sure you are in the active directory for 'gemini-streamlit-cloudrun'
gcloud artifacts repositories create "$AR_REPO" --location="$GCP_REGION" --repository-format=Docker
gcloud auth configure-docker "$GCP_REGION-docker.pkg.dev"
gcloud builds submit --tag "$GCP_REGION-docker.pkg.dev/$GCP_PROJECT/$AR_REPO/$SERVICE_NAME"
```
The final step is to deploy the service in Cloud Run with the image that we had built and had pushed to the Artifact Registry in the previous step:

In Cloud Shell, execute the following command:
```bash
gcloud run deploy "$SERVICE_NAME" \
  --port=8080 \
  --image="$GCP_REGION-docker.pkg.dev/$GCP_PROJECT/$AR_REPO/$SERVICE_NAME" \
  --allow-unauthenticated \
  --region=$GCP_REGION \
  --platform=managed  \
  --project=$GCP_PROJECT \
  --set-env-vars=GCP_PROJECT=$GCP_PROJECT,GCP_REGION=$GCP_REGION
```
On successful deployment, you will be provided a URL to the Cloud Run service. You can visit that in the browser to view the Cloud Run application that you just deployed. Choose the functionality that you would like to check out and the application will prompt the Vertex AI Gemini API and display the responses.

Congratulations!

**Web Interface:** The app will open in your web browser.

**Image-Based Generation:** 
  * Enter an image URL in the designated field.
  * Provide a descriptive prompt.
  * Click "Generate descriptions" button.
    
**JSON-Based Generation:**
  * Craft a descriptive prompt for the product.
  * Upload a JSON file containing your product data.
  * Click "Generate descriptions" button.


**License**
This project is licensed under the MIT License. See LICENSE for details.
