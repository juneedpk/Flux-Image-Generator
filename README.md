
# Flux AI Image Generator

🎨 A Streamlit application that generates images based on user prompts using the FLUX.1 model from Hugging Face.

## Features

- Generate images from text prompts.
- Adjustable parameters for fine-tuning image generation:
  - Guidance Scale
  - Number of Steps
  - Image Dimensions (Width and Height)
  - Seed for reproducibility

## Requirements

To run this application, you need to install the following Python packages:

- `streamlit`
- `requests`
- `Pillow`

You can install the required packages using the following command:

## Usage

1. Clone the repository or download the files.
2. Navigate to the directory containing the `ima.py` file.
3. Run the application using Streamlit:

   ```bash
   streamlit run ima.py
   ```

4. Open your web browser and go to `http://localhost:8501` to access the application.

## How to Use

- Enter a descriptive prompt in the text area.
- Adjust the parameters in the sidebar to customize the image generation.
- Click the "Generate Image" button to create your image.
- Download the generated image using the provided button.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Powered by the FLUX.1 model from Hugging Face.
- Created with ❤️ by Junaid using Streamlit.
