# Blood-Donation-System
A Web Application to reduce time complexity in search of blood and to become a blood donor across multiple cities.

![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=flat&logo=fastapi)
![Python](https://img.shields.io/badge/Python-3796AB?style=flat&logo=python)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=flat&logo=postgresql)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat&logo=streamlit)
![Gemini](https://img.shields.io/badge/Gemini-8E75B2?style=flat&logo=google)


## ✨ Features

- 🔍 **Smart Donor Search** — Search available donors by blood group and city with indexed queries returning results in under 30ms
- 🗺️ **Live Donor Map** — Real-time map showing nearest available donors using OpenStreetMap and Nominatim geocoding
- ❤️ **Donor Registration** — Register as a donor with a form connected directly to PostgreSQL via FastAPI
- 🤖 **AI Helpdesk** — Floating chat widget powered by Gemini 2.5 Flash answering blood donation queries 24/7
- 🩸 **Blood Compatibility Chart** — Interactive reference chart for all 8 blood groups showing donate-to and receive-from relationships
- 🚨 **Emergency Bloodline** — National helpline number (104) displayed persistently on every page
- 📊 **Statistics Dashboard** — Homepage showing total donors, cities covered, blood groups and average search time
- 🌍 **Multi-city Coverage** — 500+ donor records seeded across 20 major Indian cities


## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Frontend | Streamlit |
| Backend | FastAPI |
| Database | PostgreSQL |
| Maps | OpenstreetMap + Nominatim |
| AI | Gemini |
| ORM | SQLAlchemy |
| Project Management | Jira |


## 🚀 How to Run Locally

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/BloodConnect.git
cd BloodConnect
```

### 2. Create and activate virtual environment
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Set up PostgreSQL database
- Open pgAdmin
- Create a new database called `blood_donation_db`
- Run the SQL schema from `Database/blood_donation.sql`

### 5. Configure environment variables
Create a `.env` file in the root folder:
```
DATABASE_URL=postgresql://postgres:YOUR_PASSWORD@localhost:5432/blood_donation_db
GEMINI_API_KEY=your_gemini_api_key_here
```

### 6. Run FastAPI backend
```bash
cd "Blood Donation System"
uvicorn main:app --reload
```

### 7. Run Streamlit frontend
Open a new terminal:
```bash
cd "Blood Donation System"
streamlit run home.py
```

### 8. Open in browser
- **Streamlit App:** http://localhost:8501
- **FastAPI Docs:** http://localhost:8000/docs


## 📡 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/donors/search` | Search available donors by blood group, city and name |
| POST | `/donors/register` | Register a new donor and save to database |
| POST | `/ai/helpdesk` | Send a question to Gemini AI and get a blood donation related answer |

## 📁 Project Structure

```
Blood Donation System/
├── main.py                    ← FastAPI backend — all API endpoints
├── database.py                ← PostgreSQL connection and session management
├── models.py                  ← SQLAlchemy ORM models mirroring database tables
├── seed_data.py               ← Script to seed 500+ realistic donor records
├── home.py                    ← Streamlit homepage with hero, stats, how it works
├── requirements.txt           ← All Python dependencies
├── .env                       ← API keys and database URL (not pushed to GitHub)
├── pages/
│   ├── Find_Blood.py          ← Donor search page with map integration
│   ├── Become_Donor.py        ← Donor registration form
│   └── Compatibility_Chart.py ← Blood compatibility reference chart
├── components/
│   ├── styles.py              ← Global CSS, logo, AI chat widget
│   ├── donor_card.py          ← Reusable donor profile card component
│   └── emergency_footer.py    ← Emergency helpline footer component
├── Database/
│   └── blood_donation.sql     ← PostgreSQL schema and table definitions
└── .streamlit/
    └── config.toml            ← Streamlit theme configuration
```


## 🔮 Future Plans

- 🔐 **Donor Login System** — Allow donors to update availability, phone number and city
- 📱 **Twilio SMS Alerts** — Send real-time SMS notifications to donors during blood emergencies
- 📧 **SendGrid Email Notifications** — Email alerts for blood requests to registered donors
- 🐳 **Docker Containerization** — Package entire app into containers for easy deployment
- 🔍 **SonarQube Integration** — Automated code quality analysis and reporting
- 📊 **Admin Dashboard** — Hospital admin panel for managing blood requests and inventory
- 🌐 **Deployment** — Deploy on cloud platform (AWS/GCP/Azure)

---

## 👥 Team

Developed as part of an academic project at **National Institute of Technology, Andhra Pradesh**

| Role | Responsibilities |
|------|-----------------|
| Scrum Master | Sprint planning, Jira management, team coordination |
| Product Manager | Stakeholder research, feature prioritization, documentation |
| Developer | Full-stack development, database design, API integration |

---

## 📄 License

This project is for academic purposes at NIT Andhra Pradesh.

---

## 🙏 Acknowledgements

- [FastAPI](https://fastapi.tiangolo.com/) — Backend framework
- [Streamlit](https://streamlit.io/) — Frontend framework  
- [OpenStreetMap](https://www.openstreetmap.org/) — Map data
- [Nominatim](https://nominatim.org/) — Geocoding service
- [Google Gemini](https://ai.google.dev/) — AI helpdesk
- [Faker](https://faker.readthedocs.io/) — Sample data generation