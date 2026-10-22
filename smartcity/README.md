# 🛡️ SENTINEL — AI Smart City Surveillance System

**Full-stack Django surveillance platform** powered by AI/ML for real-time crime detection, face recognition, and predictive threat analytics.

---

## 🚀 Quick Start

```bash
# 1. Clone / enter project
cd smartcity

# 2. Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run migrations
python manage.py makemigrations
python manage.py migrate

# 5. Create superuser (admin)
python manage.py createsuperuser

# 6. Run server
python manage.py runserver

# Visit: http://127.0.0.1:8000
```

---

## 📐 Project Structure

```
smartcity/
├── smartcity/          # Core Django project
│   ├── settings.py
│   ├── urls.py
│   └── views.py        # Homepage
├── accounts/           # Auth: Login, Register, Profiles
├── dashboard/          # Police Command Dashboard
├── surveillance/       # Live camera feeds + AI analysis
├── alerts/             # Alert system + emergency dispatch
├── cameras/            # Camera network management
├── analytics/          # Crime analytics + predictions
├── incidents/          # Incident reporting & tracking
├── reports/            # Automated report generation
├── patrol/             # Officer patrol management
├── evidence/           # Secure evidence vault
├── settings_app/       # System configuration
├── map/                # City heatmap & zones
├── notifications/      # Multi-channel notifications
├── audit/              # System audit logs
├── ai_engine/          # ML model configuration
├── templates/          # All HTML templates
│   ├── home.html       # ★ Epic homepage with 20 modules
│   ├── accounts/
│   │   ├── login.html  # ★ Officer login
│   │   └── register.html # ★ Access request form
│   ├── dashboard/
│   └── [all modules]/
├── static/             # CSS, JS, images
├── media/              # Uploaded evidence files
├── manage.py
└── requirements.txt
```

---

## 🤖 20 System Modules

| # | Module | Description |
|---|--------|-------------|
| 1 | **Live Surveillance** | Real-time AI camera feeds with detection overlays |
| 2 | **Police Dashboard** | Command center with KPIs and incident tracking |
| 3 | **Alert System** | Automated threat detection & multi-channel alerts |
| 4 | **Camera Network** | Manage 1,200+ city camera nodes |
| 5 | **Analytics Hub** | Crime patterns & predictive analytics |
| 6 | **Incident Reports** | Document and track all incidents |
| 7 | **Report Generator** | Automated daily/weekly PDF reports |
| 8 | **Patrol Management** | Officer routing & GPS tracking |
| 9 | **Evidence Vault** | Secure encrypted video/image storage |
| 10 | **City Map** | Live threat heatmap & zone management |
| 11 | **Face Recognition** | AI-powered facial identification vs watchlist |
| 12 | **Object Detection** | YOLO weapon & threat detection |
| 13 | **Notifications** | SMS, email, push alert dispatch |
| 14 | **Audit Logs** | Full system access & action audit trail |
| 15 | **AI Engine** | Configure ML models & thresholds |
| 16 | **Suspect Database** | Watchlist & criminal record management |
| 17 | **Traffic Monitor** | Traffic flow & accident detection |
| 18 | **Emergency Response** | SOS dispatch & coordination center |
| 19 | **System Settings** | Configure system parameters & users |
| 20 | **Drone Control** | Aerial surveillance drone management |

---

## 🔧 Tech Stack

### Backend
- **Django 4.2** — Core framework
- **Django Channels** — WebSocket real-time feeds
- **Celery + Redis** — Async task processing
- **SQLite → PostgreSQL** — Database

### AI / Computer Vision
- **YOLOv8** (Ultralytics) — Object & weapon detection
- **OpenCV** — Video frame processing
- **DeepFace / FaceNet** — Face recognition
- **FAISS** — Fast similarity search for faces
- **PyTorch** — Deep learning backbone

### Frontend
- Vanilla HTML/CSS/JS (no framework required)
- **Feather Icons** — UI iconography
- **Orbitron + Share Tech Mono** — Fonts
- Real-time updates via WebSocket

---

## 🔐 Security Features

- Role-based access control (Admin, Commander, Officer, Analyst, Operator, Dispatcher)
- All registrations require admin approval (`is_active=False` by default)
- Full audit logging of all system actions
- Evidence files encrypted at rest
- Session-based authentication with IP logging
- CSRF protection on all forms

---

## 🏗️ Development Roadmap

- [ ] WebSocket integration for live camera feeds
- [ ] YOLOv8 inference pipeline
- [ ] Face recognition database with FAISS
- [ ] Celery tasks for async AI processing
- [ ] Mobile-responsive police app
- [ ] Drone integration API
- [ ] PDF report generation
- [ ] Email/SMS notification dispatch

---

## 📦 Environment Variables

Create `.env` in project root:

```env
SECRET_KEY=your-production-secret-key
DEBUG=False
DATABASE_URL=postgresql://user:pass@localhost/sentinel
REDIS_URL=redis://localhost:6379
ALERT_EMAIL=police@smartcity.gov
EMERGENCY_PHONE=911
YOLO_MODEL_PATH=models/yolov8n.pt
```

---

*SENTINEL — Protecting every corner of your city, 24/7* 🛡️
