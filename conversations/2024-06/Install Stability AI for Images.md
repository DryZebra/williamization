---
type: Conversation
title: "Install Stability AI for Images"
description: "I want to use stability AI to generate images, can you walk me through step by step on how to get it installed on my desktop?"
resource: "1c121756-7137-4946-8382-e451f3c22121"
timestamp: "2024-06-02T11:25:12.395Z"
tags: ["gpt-4o"]
---

# Install Stability AI for Images

## User

I want to use stability AI to generate images, can you walk me through step by step on how to get it installed on my desktop?

## Assistant



## Assistant

Sure! I can guide you through the process of installing and using Stability AI's image generation tools on your desktop. Here are the steps:

### Step 1: Prepare Your Environment
1. **Install Python:**
   - Download and install Python from the [official website](https://www.python.org/downloads/). Make sure to check the option to add Python to your PATH during installation.

2. **Install Git:**
   - Download and install Git from the [official website](https://git-scm.com/).

### Step 2: Install Dependencies
1. **Create a Virtual Environment (optional but recommended):**
   - Open a terminal or command prompt and run the following commands:
     ```sh
     python -m venv stability_env
     source stability_env/bin/activate  # On Windows, use `stability_env\Scripts\activate`
     ```

2. **Install Required Libraries:**
   - With your virtual environment activated, install the required libraries:
     ```sh
     pip install torch torchvision torchaudio
     pip install transformers
     pip install diffusers
     ```

### Step 3: Clone Stability AI's Repository
1. **Clone the Repository:**
   - In the terminal, navigate to the directory where you want to store the repository and run:
     ```sh
     git clone https://github.com/Stability-AI/Stable-Diffusion.git
     cd Stable-Diffusion
     ```

### Step 4: Configure Your API Key
1. **Get an API Key:**
   - Sign up for an API key from Stability AI's website if required.

2. **Set Up API Key:**
   - Create a `.env` file in the root directory of the cloned repository and add your API key:
     ```sh
     echo "API_KEY=your_api_key_here" > .env
     ```

### Step 5: Run the Script to Generate Images
1. **Run the Image Generation Script:**
   - In the terminal, run the following command to generate an image:
     ```sh
     python scripts/txt2img.py --prompt "A fantasy landscape with a castle and dragons" --n_samples 1 --n_iter 1 --scale 7.5 --ddim_steps 50
     ```

   - Replace the prompt with your desired image description.

### Step 6: View Your Generated Images
1. **Locate the Generated Images:**
   - The generated images will be saved in the `outputs` directory by default.

This should set you up to generate images using Stability AI on your desktop. Let me know if you encounter any issues or need further assistance!

