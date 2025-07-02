# 🔍 Sentinel Scanner

Sentinel Scanner is a simple cybersecurity tool built with **Python** and **Streamlit**.  
It scans a target (IP or domain) for **open ports**, detects the **running services**, and searches for related **CVEs** using the official **NVD API**.

---

## 🚀 Features

- ✅ Port scanner (ports 1–1024)
- 📡 Service banner grabbing
- 🛡️ CVE lookup using NVD API
- 📊 Streamlit web dashboard
- 🔑 Uses your API key (secure config.ini file)

---

## 📂 Folder Structure

sentinel-scanner/
├── scanner/
│ ├── port_scanner.py
│ ├── cve_lookup.py
│ └── vuln_lookup.py
├── dashboard/
│ └── app.py
├── config.ini ← (your NVD API key)
├── requirements.txt
└── README.md

---

## 🛠️ How to Run It

### 1. Clone the project
```bash
git clone https://github.com/mickeypatil/sentinel-scanner.git
cd sentinel-scanner

### 2. Create virtual environment
```bash
Copy
Edit
python -m venv venv
venv\Scripts\activate   # (Use source venv/bin/activate if on Linux/Mac)
