import os
import json
from PIL import Image
from dotenv import load_dotenv
import google.generativeai as genai
from pdf2image import convert_from_path

# ---------------------------
# Load environment variables
# ---------------------------
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError("GEMINI_API_KEY not found. Set it as an environment variable.")

# ---------------------------
# Configure Gemini
# ---------------------------
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("models/gemini-2.5-flash")

# ---------------------------
# Load extraction prompt
# ---------------------------
with open("prompts/extraction_prompt.txt", "r") as f:
    PROMPT = f.read()

# ---------------------------
# File path (image or PDF)
# ---------------------------
FILE_PATH = "sample_docs/Rishi_ID.jpeg"  # change as needed
file_ext = os.path.splitext(FILE_PATH)[1].lower()

inputs = []

# ---------------------------
# Handle Images
# ---------------------------
if file_ext in [".jpg", ".jpeg", ".png"]:
    try:
        image = Image.open(FILE_PATH)
        image.verify()
        image = Image.open(FILE_PATH)  # reload after verify
        inputs = [PROMPT, image]
    except Exception as e:
        raise ValueError(f"Invalid image file: {e}")

# ---------------------------
# Handle PDFs (convert to images)
# ---------------------------
elif file_ext == ".pdf":
    try:
        pages = convert_from_path(FILE_PATH, dpi=200)
        inputs = [PROMPT]
        for page in pages:
            inputs.append(page)
    except Exception as e:
        raise ValueError(f"Failed to process PDF: {e}")

else:
    raise ValueError("Unsupported file format. Use JPG, PNG, or PDF.")

# ---------------------------
# Gemini API call
# ---------------------------
response = model.generate_content(
    inputs,
    generation_config={
        "temperature": 0,
        "response_mime_type": "application/json"
    }
)

# ---------------------------
# Parse & display output
# ---------------------------
try:
    extracted_data = json.loads(response.text)
    print("\n✅ Extracted Structured Data:\n")
    print(json.dumps(extracted_data, indent=2))
except json.JSONDecodeError:
    print("❌ Gemini returned invalid JSON:")
    print(response.text)
