# auto-form-fill-gemini
India’s digital ecosystem still forces users to manually fill the same personal details across banking, education, healthcare, and government forms, despite having verified documents. This leads to inefficiency, errors, and frustration due to the absence of intelligent, context-aware form automation.
# AutoFormFill – Intelligent Document-Based Form Autofill

## Overview
AutoFormFill is a multi-modal application that automatically extracts and validates user details from identity documents such as Aadhaar, PAN, Passport, and Driving License using the Gemini API.

## Problem
Manual form filling is repetitive, error-prone, and time-consuming, especially when users repeatedly enter the same information across platforms.

## Solution
We leverage Gemini’s multi-modal reasoning to:
- Detect document type automatically
- Extract structured user details
- Validate extracted fields
- Assign confidence scores for reliability

## Features
- Supports images (PNG, JPG, JPEG) and PDFs
- Automatic document-type detection
- Field-level validation flags
- Confidence scoring for extracted data
- JSON output ready for form integration

## Tech Stack
- Python
- Google Gemini 2.5 Flash
- PIL, PyMuPDF
- Prompt-based intelligence (no model training)

## Setup
1. Clone the repository
2. Install dependencies:
   pip install -r requirements.txt
3. Add your Gemini API key:
   export GEMINI_API_KEY="your_api_key_here"
5. Run:
   python3 app.py
## API Key Disclaimer
⚠️ Do NOT hardcode API keys. Use environment variables only.

## Future Scope
- Form auto-submission
- Cross-document verification
- Confidence-based human review
