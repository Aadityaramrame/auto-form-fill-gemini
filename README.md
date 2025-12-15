# 🚀 AutoFormFill – Gemini-Powered Intelligent Form Autofill 🇮🇳

India’s digital ecosystem still forces users to repeatedly fill the same personal details across banking, education, healthcare, and government forms — even when verified documents already exist.  
This results in inefficiency, human errors, form rejections, and user frustration due to the lack of **intelligent, context-aware automation**.

---

## 🧠 Overview
**AutoFormFill** is a multi-modal AI application that uses **Google Gemini** to automatically **detect document type**, **extract structured user details**, **validate fields**, and **assign confidence scores** from identity documents such as **Aadhaar, PAN, Passport, and Driving License**.

---

## ❗ Problem
- Manual form filling is repetitive and time-consuming  
- Existing OCR systems lack contextual understanding  
- Small errors often lead to form rejection and rework  
- No universal system exists to intelligently auto-fill forms from documents  

---

## 💡 Solution
We leverage **Gemini’s multi-modal reasoning** to:
- 📄 Automatically detect the type of identity document  
- 🔍 Extract structured personal details in clean JSON  
- ✅ Validate individual fields (name, DOB, ID number, address)  
- 📊 Generate confidence scores to indicate reliability  

---

## ✨ Key Features
- 🖼️ Supports **PNG, JPG, JPEG** and **PDF** documents  
- 🧾 Intelligent **document-type detection**  
- ✔️ Field-level validation flags  
- 📈 Confidence scoring for extracted data  
- 🔗 JSON output ready for direct form integration  

---

## 🛠️ Tech Stack
- 🐍 Python  
- 🤖 Google Gemini **2.5 Flash**  
- 🖼️ PIL, 📄 PyMuPDF  
- 🧠 Prompt-driven intelligence (no model training required)  

---

## ⚙️ Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/auto-form-fill-gemini.git
   cd auto-form-fill-gemini

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt

3. **Set your Gemini API key**
   ```bash
   export GEMINI_API_KEY="your_api_key_here"

4. **Run the application**
   ```bash
   python3 app.py

## 🔐 API Key Disclaimer
- ⚠️ Do NOT hardcode API keys.
   Always use environment variables to keep your credentials secure.
## 🔮 Future Scope
- 📝 Auto-submission of forms
- 🔄 Cross-document verification
- 🧑‍⚖️ Confidence-based human review
- 🌐 Integration with government & enterprise platforms

## ✨ *AutoFormFill focuses on reliability, explainability, and real-world usability — not just extraction.*
