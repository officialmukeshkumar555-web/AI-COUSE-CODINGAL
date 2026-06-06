from huggingface_hub import InferenceClient
from datetime import datetime
from PIL import Image

# Replace with your NEW Hugging Face token
HF_API_KEY = "hf_..."

MODELS = [
    "ByteDance/SDXL-Lightning",
    "stabilityai/stable-diffusion-xl-base-1.0",
    "stabilityai/sdxl-turbo",
    "runwayml/stable-diffusion-v1-5",
]

client = InferenceClient(api_key=HF_API_KEY)

print(f"Primary model: {MODELS[0]}")
print("Type 'quit' to exit\n")

while True:
    prompt = input("Enter prompt: ").strip()

    if prompt.lower() in ["quit", "exit", "q"]:
        break

    if not prompt:
        continue

    print("Generating...")
    image = None

    for model in MODELS:
        try:
            image = client.text_to_image(prompt, model=model)
            break
        except Exception:
            print("Trying next model...")
            continue

    if image:
        filename = f"generated_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
        image.save(filename)
        print(f"Saved: {filename}")
        image.show()
    else:
        print("All models failed.")

print("Goodbye!")