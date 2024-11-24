import streamlit as st
import requests
import io
from PIL import Image

# API configuration
API_URL = "https://api-inference.huggingface.co/models/black-forest-labs/FLUX.1-dev"
headers = {"Authorization": "Bearer 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"}

# Function to generate image
def generate_image(prompt):
    payload = {
        "inputs": prompt,
        "parameters": {
            "guidance_scale": guidance_scale,
            "num_inference_steps": num_steps,
            "width": width,
            "height": height,
        }
    }
    if seed != -1:
        payload["parameters"]["seed"] = seed
    
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.content

# Set page title and configuration
st.set_page_config(
    page_title="AI Image Generator",
    layout="wide",
    initial_sidebar_state="expanded",
    page_icon="🎨"
)

# Custom CSS
st.markdown("""
    <style>
    .main {
        padding: 2rem;
    }
    .stTitle {
        color: #1E88E5;
        font-size: 2.5rem !important;
        padding-bottom: 2rem;
        white-space: nowrap;
    }
    .stButton>button {
        width: 100%;
        padding: 0.5rem;
        font-size: 1.2rem;
    }
    .sidebar .block-container {
        padding-top: 2rem;
    }
    </style>
    """, unsafe_allow_html=True)

# Main content
col1, col2, col3 = st.columns([1, 3, 1])
with col2:
    st.title("🎨 Flux AI Image Generation App")
    

# Sidebar with advanced settings
with st.sidebar:
    st.markdown("### 🛠️ Advanced Settings")
    st.info("Adjust these parameters to fine-tune your image generation")
    
    st.markdown("#### Model Parameters")
    guidance_scale = st.slider("🎯 Guidance Scale", 
                             min_value=1.0, max_value=20.0, value=7.0, step=0.5,
                             help="Higher values make images more closely match the prompt")
    
    num_steps = st.slider("🔄 Number of Steps", 
                         min_value=1, max_value=100, value=30, step=1,
                         help="More steps = higher quality but slower generation")
    
    st.markdown("#### Image Dimensions")
    width = st.select_slider("📏 Width", 
                           options=[128, 256, 384, 512, 640, 768, 896, 1024], 
                           value=384,
                           help="Smaller sizes generate faster")
    height = st.select_slider("📐 Height", 
                            options=[128, 256, 384, 512, 640, 768, 896, 1024], 
                            value=384,
                            help="Smaller sizes generate faster")
    
    st.markdown("#### Advanced Options")
    seed = st.number_input("🎲 Seed (-1 for random)", 
                          min_value=-1, max_value=2147483647, value=-1,
                          help="Use the same seed to reproduce results")

# Main interface
st.markdown("### Enter Your Prompt")
user_prompt = st.text_area("Describe the image you want to generate:", 
                          "Astronaut riding a horse",
                          height=100,
                          help="Be as descriptive as possible for better results")

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    generate_button = st.button("🚀 Generate Image", use_container_width=True)

if generate_button:
    if user_prompt:
        try:
            with st.spinner("🎨 Creating your masterpiece..."):
                image_bytes = generate_image(user_prompt)
                image = Image.open(io.BytesIO(image_bytes))
                
                # Center the image using columns
                col1, col2, col3 = st.columns([1, 2, 1])
                with col2:
                    st.image(image, 
                            caption=f"🖼️ Generated Image: {user_prompt}", 
                            width=400)  # Fixed display width
                    
                    # Resize image to 1024x1024 for download
                    download_image = image.resize((1024, 1024), Image.Resampling.LANCZOS)
                    buf = io.BytesIO()
                    download_image.save(buf, format="PNG")
                    st.download_button(
                        label="📥 Download Image",
                        data=buf.getvalue(),
                        file_name="generated_image.png",
                        mime="image/png",
                        use_container_width=True
                    )
        except Exception as e:
            st.error(f"❌ An error occurred: {str(e)}")
    else:
        st.warning("⚠️ Please enter a prompt first!")

# Footer
st.markdown("---")
col1, col2 = st.columns(2)
with col1:
    st.markdown("Powered by FLUX.1 model from Hugging Face")
with col2:
    st.markdown("<div style='text-align: right'>Created with ❤️ by Junaid using Streamlit</div>", 
                unsafe_allow_html=True)

