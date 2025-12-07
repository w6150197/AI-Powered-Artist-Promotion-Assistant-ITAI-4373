System Architecture
Overview
The AI-Powered Artist Promotion Assistant system follows a human-in-the-loop architecture to ensure ethical compliance and artistic control. The system ingests engagement data, applies AI scoring and suggestion generation, and presents actionable outputs through a user-friendly dashboard.
Data Flow
1.	Data Ingestion
o	API pulls from Instagram Graph API and TikTok analytics export.
o	Alternative: CSV upload by artist.
2.	Processing Layer
o	Normalization of engagement data (likes, comments, saves, profile visits).
o	Enrichment with historical activity (repeated engagement, past purchases).
3.	AI Analysis Layer
o	Lead Classification: Determines potential customer persona (Collector, Home Decor Shopper, Gift Buyer).
o	Opportunity Scoring: Numeric score from 0–100 combining engagement metrics and AI intent analysis.
o	Caption/Outreach Generation: AI drafts friendly and professional messages for artist approval.
4.	Human-in-the-Loop Layer
o	Artist reviews all AI-generated suggestions.
o	Approves, edits, or discards outreach messages.
5.	Output Layer
o	Dashboard visualization: KPIs, top leads, opportunity scores.
o	Exportable CSV and analytics plots.
Technical Stack Diagram
[Data Sources] ---> [Processing & AI Layer] ---> [Dashboard & Approval]
    |                       |                      |
 Instagram API          Scoring & LLM          KPI Charts & Exports
 TikTok Analytics       Lead Classification   Manual Approval Buttons
 CSV Upload             Outreach Generation
Backend Services
•	FastAPI / Flask: optional API endpoints for engagement ingestion
•	Python scripts: scoring.py, ai_prompts.py
•	Database: Google Sheets or SQLite
Dashboard Features
•	Upload engagement CSV / connect APIs
•	View top leads and opportunity scores
•	Approve/edit AI-generated messages
•	Track performance metrics and export CSV/graphs
