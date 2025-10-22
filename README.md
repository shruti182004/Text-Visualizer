# Text-Visualizer
This project is a Streamlit web application that functions as a user-friendly interface for AI-powered image generation. It allows users to turn their text descriptions (prompts) into visual images.


<img width="1920" height="807" alt="Screenshot (244)" src="https://github.com/user-attachments/assets/d841e860-cda3-481a-b8d3-da15769ea665" />
<img width="1920" height="736" alt="Screenshot (245)" src="https://github.com/user-attachments/assets/76c29786-7e12-4e8a-b1f7-ab1a4d9e07aa" />

## ✨ Core Features

- Text-to-Image Generation: Transforms any text description into a high-quality image.

- Negative Prompts: Allows you to specify what you don't want to see in the image, giving you finer control over the output.

- Multi-Image Support: Generate 1 to 4 images at a time to find the best result.

- Downloadable Results: Instantly download any generated image as a .png file.

- Secure API Handling: Uses Streamlit's built-in secrets management to keep your Hugging Face API token safe and secure.

- Smart Error Handling: Automatically retries if the AI model is loading (503 Error) and provides clear messages for other errors.

## 🤝 Collaborators
* [**Jitin Nair**](https://github.com/Jitin10)

## 🛠️ Tech Stack

- Python

- Streamlit (for the web app interface)

- Hugging Face Inference API (for AI model access)

- Requests (for making API calls)

## 🚀 How to Run (Locally)

Follow these steps to run the app on your own computer.

**1. Clone the Repository**

git clone [https://github.com/YourUsername/text-visualizer.git](https://github.com/YourUsername/text-visualizer.git)
cd text-visualizer


(Replace YourUsername with your actual GitHub username)

**2. Create a Virtual Environment (Recommended)** 

# For Windows
```python -m venv venv```
```.\venv\Scripts\activate```

# For macOS/Linux
```python3 -m venv venv```
```source venv/bin/activate```


**3. Install Dependencies**

Install all the required Python libraries.

```pip install -r requirements.txt```


**4. Add Your API Key (Critical Step)**

- This app will not run without your Hugging Face API key.

- In your project folder (text-visualizer), create a new folder named .streamlit.

- Inside the .streamlit folder, create a new file named secrets.toml.

- Open secrets.toml and add your API key like this:

```HF_API_TOKEN = "hf_YOUR_HUGGING_FACE_TOKEN_HERE"```


**5. Run the App**

- Now you're ready to go!

```streamlit run app.py```


## ☁️ How to Deploy on Streamlit Cloud

- The easiest way to share your app is to deploy it for free on Streamlit Community Cloud.

- Push to GitHub: Make sure your repository is fully uploaded to GitHub (including app.py, requirements.txt, and this README.md).

- Sign Up: Create a free account on Streamlit Community Cloud.

**Deploy:**

- Click "New App" and connect your GitHub account.

- Select your text-visualizer repository.

- IMPORTANT: Click the "Advanced settings..." button.

- In the "Secrets" section, paste your API key exactly as you did in your local secrets.toml file:

```HF_API_TOKEN = "hf_YOUR_HUGGING_FACE_TOKEN_HERE"```

- Click "Save".

Click "Deploy!" and your app will be live on the internet.
