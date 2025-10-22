import streamlit as st
from io import BytesIO
import requests
import time

# --- Constants ---
# Using Kandinsky 2.1, which is available on the free inference API
MODEL_ID = "stabilityai/stable-diffusion-xl-base-1.0"
API_URL = f"https://api-inference.huggingface.co/models/{MODEL_ID}"

# --- Load API Key from Streamlit Secrets ---
# This is the secure way to handle API keys.
# DO NOT hardcode your key here.
# This is correct
HF_API_TOKEN = st.secrets.get("HF_API_TOKEN")


# --- Function to Generate Images using Hugging Face ---
def generate_images_with_hf(api_token, prompt, negative_prompt):
    """
    Generates an image using the Hugging Face Inference API and returns the image bytes.
    """
    headers = {"Authorization": f"Bearer {api_token}"}
    
    payload = {
        "inputs": prompt,
        "parameters": {
            "negative_prompt": negative_prompt,
        }
    }
    
    try:
        response = requests.post(API_URL, headers=headers, json=payload, timeout=300)
        
        # --- Handle Response Status Codes ---
        if response.status_code == 200:
            return response.content
        elif response.status_code == 503:
            # Model is loading, wait and retry
            estimated_time = response.json().get("estimated_time", 20.0)
            st.info(f"Model is currently loading. Please wait... (Est. time: {int(estimated_time)} seconds)")
            time.sleep(estimated_time)
            # Retry the request once after waiting
            retry_response = requests.post(API_URL, headers=headers, json=payload, timeout=300)
            if retry_response.status_code == 200:
                return retry_response.content
            else:
                st.error(f"Error after retry: {retry_response.status_code} - {retry_response.text}")
                return None
        elif response.status_code == 401:
            st.error("Authentication Error: The Hugging Face API token is invalid or has expired. Please check your Streamlit secrets.")
            return None
        else:
            st.error(f"Error: {response.status_code} - {response.text}")
            return None
            
    except requests.exceptions.RequestException as e:
        st.error(f"An unexpected network error occurred: {e}")
        return None


# --- Main Streamlit App ---

st.set_page_config(page_title="Text Visualizer Pro", page_icon="🎨", layout="wide")

# --- Main Page ---
st.title("🎨 Text Visualizer Pro (Free Model)")
# Updated to Kandinsky 2.1 to match the model
st.markdown("Transform your ideas into stunning visuals with the power of **Kandinsky 2.1**.")

# --- Input Fields ---
col1, col2 = st.columns([2, 1])

with col1:
    prompt = st.text_area(
        "**Enter your prompt:**",
        height=150,
        placeholder="A birthday cake with the words 'Happy Birthday' written in frosting, cinematic lighting",
        help="Be as descriptive as possible for the best results. This model is good at rendering text."
    )
    negative_prompt = st.text_area(
        "**Negative prompt (features to avoid):**",
        height=100,
        placeholder="cartoon, drawing, text, watermark, blurry, deformed",
        help="List things you don't want to see in the image."
    )

with col2:
    st.subheader("Image Configuration")
    num_images = st.slider("**Number of images to generate:**", min_value=1, max_value=4, value=1)
    

# --- Generate Button and Image Display ---
if st.button("Generate Images", type="primary", use_container_width=True):
    # This is the new, cleaner check.
    if not HF_API_TOKEN:
        st.error("Authentication Error: Hugging Face API Token not found.")
        st.info("Please add your HF_API_TOKEN to your Streamlit secrets (Settings > Secrets).")
    elif not prompt:
        st.warning("Please enter a prompt to generate an image.")
    else:
        generated_images = []
        
        st.write(f"Generating {num_images} image(s)...")
        progress_bar = st.progress(0)
        
        for i in range(num_images):
            with st.spinner(f"Creating image {i + 1} of {num_images}..."):
                image_bytes = generate_images_with_hf(HF_API_TOKEN, prompt, negative_prompt)
                if image_bytes:
                    generated_images.append(image_bytes)
            progress_bar.progress((i + 1) / num_images)
            
        if generated_images:
            st.success("Your images have been generated successfully!")
            
            # Display images in columns
            cols = st.columns(num_images)
            for i, img_bytes in enumerate(generated_images):
                with cols[i]:
                    st.image(img_bytes, caption=f"Image {i+1}", use_column_width=True)
                    st.download_button(
                        label="Download Image",
                        data=img_bytes,
                        file_name=f"generated_image_{i+1}.png",
                        mime="image/png"
                    )