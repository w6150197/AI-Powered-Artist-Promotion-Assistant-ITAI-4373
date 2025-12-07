# AI-Powered-Artist-Promotion-Assistant-ITAI-4373
 deliver a working Proof of Concept (POC) of the AI-Powered Artist Promotion Assistant for your client, Joe Fleishman.
Contibutors: Annette, Natalia, Mcmanus and Fleishman
AI-Powered Artist Promotion Assistant - Proof of Concept (POC)
Project Overview
This project is a Proof-of-Concept implementation of the AI-Powered Artist Promotion Assistant. It is designed to help independent artists, such as Joe Fleishman, monitor online engagement, score potential leads, and generate AI-assisted outreach suggestions, all while keeping the artist in control.
Key Features:
•	Monitor engagements on Instagram and TikTok (or CSV uploads as fallback)
•	AI-based opportunity scoring system
•	AI-generated personalized messages with brand voice
•	User-friendly dashboard for artist review and approval
•	Analytics and performance tracking (KPI charts, CTR, conversions)
Tech Stack
•	Python (backend processing, AI integration)
•	Streamlit (dashboard)
•	OpenAI API (GPT-4) or Claude API for AI functions
•	Google Sheets or SQLite for lightweight lead database
•	Optional: Flask/FastAPI for API endpoints
Setup Instructions
1.	Clone the repository
git clone https://github.com/yourusername/ai-artist-poc.git
cd ai-artist-poc
2.	Install dependencies
pip install -r requirements.txt
3.	Set environment variables
export OPENAI_API_KEY='your_api_key_here'
4.	Run the dashboard
streamlit run dashboard/streamlit_app.py
5.	Upload engagement CSV or connect APIs according to instructions in ARCHITECTURE.md
Repository Structure
/ai-artist-poc
├─ /backend
│  ├─ app.py
│  ├─ scoring.py
│  ├─ ai_prompts.py
│  └─ requirements.txt
├─ /dashboard
│  ├─ streamlit_app.py
│  └─ ui_helpers.py
├─ /data
│  └─ sample_uploads/
├─ /docs
│  ├─ ARCHITECTURE.md
│  └─ ETHICAL_AUDIT.md
├─ Dockerfile
└─ tests/
Running Tests
pytest tests/
Ethical Guidelines
See docs/ETHICAL_AUDIT.md for compliance checklist.
License
All artwork and data remain the property of the artist.

