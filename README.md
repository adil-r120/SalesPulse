# 📊 SalesPulse — Interactive Sales Analytics & AI Intelligence Dashboard

<p align="center">
  <img src="https://img.shields.io/badge/React-18.3-61DAFB?style=for-the-badge&logo=react&logoColor=black" alt="React 18" />
  <img src="https://img.shields.io/badge/TypeScript-5.8-3178C6?style=for-the-badge&logo=typescript&logoColor=white" alt="TypeScript" />
  <img src="https://img.shields.io/badge/Vite-5.4-646CFF?style=for-the-badge&logo=vite&logoColor=white" alt="Vite" />
  <img src="https://img.shields.io/badge/TailwindCSS-3.4-06B6D4?style=for-the-badge&logo=tailwindcss&logoColor=white" alt="Tailwind CSS" />
  <img src="https://img.shields.io/badge/FastAPI-0.104-009688?style=for-the-badge&logo=fastapi&logoColor=white" alt="FastAPI" />
  <img src="https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/Google_Gemini-AI-8E75C2?style=for-the-badge&logo=google&logoColor=white" alt="Gemini AI" />
  <img src="https://img.shields.io/badge/Vercel-Deployed-000000?style=for-the-badge&logo=vercel&logoColor=white" alt="Vercel" />
  <img src="https://img.shields.io/badge/Render-Hosted-46E3B7?style=for-the-badge&logo=render&logoColor=black" alt="Render" />
</p>

> **SalesPulse** is a modern, enterprise-grade business intelligence and sales analytics platform. It combines real-time transaction tracking, predictive AI analytics with Google Gemini, live stock market data via Yahoo Finance, goal monitoring, and multi-format reporting into a unified, responsive dashboard.

---

## 🌐 Live Deployments

| Component | Provider | Live URL |
| :--- | :--- | :--- |
| **Frontend Web App** | Vercel | [https://salespulse-three.vercel.app](https://salespulse-three.vercel.app) |
| **Backend REST API** | Render | [https://salespulse-interactive-data-analytics.onrender.com](https://salespulse-interactive-data-analytics.onrender.com) |
| **API Documentation** | Swagger UI | [https://salespulse-interactive-data-analytics.onrender.com/docs](https://salespulse-interactive-data-analytics.onrender.com/docs) |
| **Stock Proxy Microservice** | Render | [https://salespulse-stock.onrender.com](https://salespulse-stock.onrender.com) |

---

## 🚀 Key Features

### 📈 1. Interactive Sales & KPI Analytics
- **Dynamic KPI Dashboards**: Real-time metrics for total revenue, active orders, sales growth, and average order value.
- **Visual Analytics**: Interactive area charts, bar graphs, and pie distributions powered by Recharts.
- **Granular Filtering**: Filter transactions by timeframe (7D, 30D, 90D, YTD, Custom), category, sales rep, and geographical region.
- **Full CRUD Management**: Role-authorized ability to add, edit, and delete sales records with auto-calculated metrics.

### 🤖 2. AI Business Intelligence & Conversational Assistant
- **Gemini-Powered Chatbot**: Ask natural-language questions about your business (e.g., *"What were our best-selling categories last quarter?"* or *"Summarize our sales trends"*).
- **Context-Aware Memory**: Retrieval-augmented conversational pipeline retaining dialogue context and transaction history.
- **Automated Daily Insights**: Real-time automated summaries highlighting daily revenue highlights, anomalies, and recommendations.

### 💹 3. Real-Time Stock Market Intelligence
- **Live Market Feed**: Real-time price tracking, daily highs/lows, changes, and volume for major global equities and indices.
- **Yahoo Finance Proxy**: High-throughput dedicated Node.js microservice proxying real-time market data with cached fallback layers.
- **Interactive Ticker Search**: Search any global ticker symbol (e.g., AAPL, TSLA, MSFT, RELIANCE.NS) directly within the dashboard.

### 🎯 4. Goal Setting & Milestone Tracking
- **Revenue & Unit Targets**: Set customizable sales goals for individuals, teams, or fiscal periods.
- **Progress Tracking**: Visual progress bars and milestone forecasts predicting completion probability based on current velocity.

### 📄 5. Export & Comprehensive Reporting
- **Multi-Format Exports**: One-click exports of filtered datasets to Excel (`.xlsx`), CSV, and presentation-ready PDF reports (`ReportLab` + `html2canvas`).
- **Audit-Ready Summaries**: Formatted executive summaries including charts, top-performing products, and KPIs.

### 🔐 6. Role-Based Access Control (RBAC) & Security
- **JWT Authentication**: Secure JSON Web Token authentication with bcrypt password hashing and token expiration.
- **Role Tiering**: Granular permission boundaries supporting **Viewer**, **Manager**, and **Admin** tiers.
- **Administrative Panel**: User administration, role modification, account management, and centralized feedback monitoring.
- **API Rate Limiting**: SlowAPI protection against denial-of-service and brute-force authentication attempts.

---

## 🏗️ System Architecture

```mermaid
flowchart TD
    subgraph Client ["Frontend (React 18 + Vite + Tailwind)"]
        UI[Interactive Dashboard UI]
        ChatUI[Gemini AI Chatbox]
        StockUI[Stock Market Widget]
        AdminUI[Admin Management Panel]
    end

    subgraph Backend ["Backend API (FastAPI)"]
        Router[FastAPI Router & Rate Limiter]
        AuthModule[JWT Auth & RBAC Guard]
        AnalyticsEngine[Analytics & Reporting Engine]
        AIChatService[AI Assistant Service]
        DB[(SQLite / PostgreSQL Engine)]
    end

    subgraph Microservices ["Stock Proxy (Node.js + Express)"]
        ProxyServer[Yahoo Finance Proxy Server]
    end

    subgraph External ["External Cloud Services"]
        GeminiAPI[Google Gemini / OpenRouter API]
        YahooFin[Yahoo Finance API]
    end

    UI -->|REST API / JSON| Router
    ChatUI -->|Chat Inquiries| Router
    StockUI -->|Ticker Quotes| ProxyServer
    AdminUI -->|Admin Actions| Router

    Router --> AuthModule
    Router --> AnalyticsEngine
    Router --> AIChatService

    AnalyticsEngine --> DB
    AuthModule --> DB
    AIChatService --> DB
    AIChatService -->|Contextual Prompts| GeminiAPI
    ProxyServer -->|Market Data| YahooFin
```

---

## 🛠️ Tech Stack Matrix

| Domain | Technologies |
| :--- | :--- |
| **Frontend Core** | React 18, TypeScript, Vite, React Router v6 |
| **UI Components & Styling** | Tailwind CSS, Radix UI (shadcn/ui), Lucide Icons, Sonner Toasts |
| **Data Visualization** | Recharts, HTML2Canvas, XLSX |
| **Backend API** | Python 3.10+, FastAPI, Uvicorn, Pydantic v2 |
| **Database & ORM** | SQLAlchemy 2.0, SQLite (Local Dev), PostgreSQL (Cloud Production) |
| **AI / LLM Integration** | Google Generative AI (`google-generativeai`), LangChain, OpenRouter |
| **Stock Market Service** | Node.js, Express, `yahoo-finance2`, CORS |
| **Security & Utilities** | Python-JOSE (JWT), PassLib (Bcrypt), SlowAPI (Rate Limiting), ReportLab (PDFs) |

---

## 📁 Repository Structure

```
SalesPulse/
├── backend/                        # FastAPI Backend Application
│   ├── routes/                     # API Route Handlers
│   │   ├── admin.py                # Admin management & feedback inspection
│   │   ├── analytics.py            # Sales analytics & metric calculations
│   │   ├── auth.py                 # User authentication, registration & JWT
│   │   ├── chat.py                 # Gemini conversational AI endpoints
│   │   ├── insights.py             # Automated daily insight generation
│   │   ├── notifications.py        # System alerts & notification center
│   │   ├── reports.py              # PDF/CSV export generation
│   │   └── stock_feedback.py       # Stock feedback ingestion
│   ├── utils/                      # Helper utilities (auth, limiter)
│   ├── conversation_context.py     # RAG context manager for AI chat
│   ├── database.py                 # SQLAlchemy configuration & seed routine
│   ├── main.py                     # FastAPI application entry point
│   ├── models.py                   # SQLAlchemy schema definitions
│   ├── requirements.txt            # Python package dependencies
│   └── run.py                      # Backend launcher script
├── src/                            # React + TypeScript Frontend
│   ├── components/                 # UI Components (Charts, Modals, Forms, Widgets)
│   ├── config/                     # Application configurations
│   ├── hooks/                      # Custom React hooks (use-auth, use-toast)
│   ├── lib/                        # Utility functions
│   ├── pages/                      # Page components (Index, NotFound)
│   └── services/                   # Frontend API communication clients
├── stock-proxy/                    # Node.js Express Stock Proxy Service
│   ├── server.js                   # Yahoo Finance proxy server
│   └── package.json                # Proxy dependencies
├── public/                         # Public static web assets
├── START-SALESPULSE.bat            # Windows 1-click startup script
├── STOP-SALESPULSE.bat             # Windows 1-click shutdown script
├── vite.config.ts                  # Vite build & reverse-proxy configuration
└── package.json                    # Frontend dependencies & scripts
```

---

## ⚡ Quick Start

### Option 1: One-Click Startup (Windows)

Simply double-click or run:
```bash
START-SALESPULSE.bat
```
This automatically boots:
1. **Stock Proxy** on `http://localhost:5000`
2. **FastAPI Backend** on `http://localhost:8000`
3. **Vite Frontend** on `http://localhost:5173`

To gracefully shut down all services at any time:
```bash
STOP-SALESPULSE.bat
```

---

### Option 2: Manual Step-by-Step Setup

#### 1. Prerequisites
- **Node.js** v18+ and **npm**
- **Python** 3.10+ and **pip**
- **Git**

#### 2. Clone Repository
```bash
git clone https://github.com/adil-r120/SalesPulse-Interactive-Data-Analytics-Dashboard.git
cd SalesPulse-Interactive-Data-Analytics-Dashboard
```

#### 3. Setup Frontend
```bash
# Install dependencies
npm install

# Start development server
npm run dev
```
> Frontend will be available at: **`http://localhost:5173`**

#### 4. Setup Backend API
```bash
# Navigate to backend directory
cd backend

# Create and activate virtual environment
python -m venv venv

# Windows:
venv\Scripts\activate
# macOS/Linux:
# source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the backend server
python run.py
```
> Backend API will be available at: **`http://localhost:8000`**  
> Interactive OpenAPI documentation: **`http://localhost:8000/docs`**

#### 5. Setup Stock Proxy Microservice
```bash
# In a new terminal, navigate to stock-proxy directory
cd stock-proxy

# Install dependencies
npm install

# Start stock proxy server
node server.js
```
> Stock proxy service will be available at: **`http://localhost:5000`**

---

## 🔑 Environment Configuration

Create a `.env` file inside the `backend/` directory:

```env
# Application Settings
ENVIRONMENT=development
HOST=0.0.0.0
PORT=8000

# Security (Generate a secure secret key for production)
SECRET_KEY=your_super_secret_jwt_key_here

# Database (Optional - defaults to SQLite salespulse.db)
# DATABASE_URL=postgresql://user:password@localhost:5432/salespulse

# AI Integration (At least one key is recommended for AI Chat & Insights)
GEMINI_API_KEY=your_google_gemini_api_key
# OPENROUTER_API_KEY=your_openrouter_api_key

# Optional Integrations
GOOGLE_API_KEY=your_google_api_key
GOOGLE_CSE_ID=your_custom_search_engine_id
REDIS_URL=redis://localhost:6379/0
```

---

## 👥 Default Test Credentials

When initialized on an empty database, SalesPulse seeds an administrator account along with 50+ realistic sales transactions:

| Role | Username / Email | Password | Permissions |
| :--- | :--- | :--- | :--- |
| **Admin** | `adil_r146` / `adil_r146@salespulse.com` | `Adil@146` | Full system access, User administration, Role management |
| **New Users** | *(Self-registered via `/signup`)* | *(Custom)* | Assigned **Viewer** role by default |

> 💡 **Tip**: Admins can promote any user to **Manager** or **Admin** via the **Admin Dashboard** in the navigation bar.

---

## 🛡️ Role-Based Access Control (RBAC)

| Feature / Capability | Viewer | Manager | Admin |
| :--- | :---: | :---: | :---: |
| View Real-time Sales Dashboards & Charts | ✅ | ✅ | ✅ |
| Query AI Chatbot Assistant | ✅ | ✅ | ✅ |
| Track Stock Market Prices & Quotes | ✅ | ✅ | ✅ |
| Submit User Feedback & Ratings | ✅ | ✅ | ✅ |
| Add New Sales Transactions | ❌ | ✅ | ✅ |
| Edit / Delete Sales Transactions | ❌ | ✅ | ✅ |
| Create & Update Business Goals | ❌ | ✅ | ✅ |
| Export Reports (PDF, CSV, Excel) | ❌ | ✅ | ✅ |
| Access Admin Panel | ❌ | ❌ | ✅ |
| Manage User Roles & Permissions | ❌ | ❌ | ✅ |
| Delete User Accounts & Bulk Actions | ❌ | ❌ | ✅ |
| View Feedback Submissions & Analytics | ❌ | ❌ | ✅ |

---

## 📡 Core API Endpoints

| Category | Method | Endpoint | Description |
| :--- | :--- | :--- | :--- |
| **Auth** | `POST` | `/auth/signup` | Register a new user |
| **Auth** | `POST` | `/auth/login` | Authenticate and receive JWT tokens |
| **Auth** | `GET` | `/auth/me` | Fetch currently authenticated user profile |
| **Analytics** | `GET` | `/api/overview` | KPI summaries (revenue, orders, growth) |
| **Analytics** | `GET` | `/api/revenue-trend` | Time-series data for revenue charts |
| **Analytics** | `GET` | `/api/sales-by-category` | Sales grouped by product categories |
| **Analytics** | `POST` | `/api/sales` | Create a new sales transaction record |
| **AI Chat** | `POST` | `/api/chat` | Send prompt to conversational AI assistant |
| **AI Chat** | `GET` | `/api/chat/history` | Retrieve user chat session history |
| **Insights** | `GET` | `/api/insights/daily` | Generate automated daily sales insights |
| **Reports** | `POST` | `/api/reports/sales` | Export sales report |
| **Stocks** | `GET` | `/stock-api/api/stock?symbol=TICKER` | Fetch quote & statistics for symbol |
| **Admin** | `GET` | `/api/admin/users` | List all system users *(Admin only)* |
| **Admin** | `PUT` | `/api/admin/users/{id}/role` | Update user access role *(Admin only)* |

*Full endpoint documentation and request/response schemas can be explored interactively at `/docs`.*

---

## 🧪 Testing & Code Quality

```bash
# Run Backend Unit & Integration Tests
cd backend
pytest

# Type Check Frontend (TypeScript)
npx tsc --noEmit

# Lint Frontend Codebase
npm run lint

# Build Frontend for Production
npm run build
```

---

## 🤝 Contributing

Contributions are welcomed! Follow these steps to contribute:
1. **Fork** the repository.
2. Create your feature branch (`git checkout -b feature/AmazingFeature`).
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`).
4. Push to the branch (`git push origin feature/AmazingFeature`).
5. Open a **Pull Request**.

---

## 📄 License

This project is licensed under the MIT License — see the repository files for details.

---

<p align="center">
  <b>Built with ❤️ by Adil and the SalesPulse Team</b>
</p>