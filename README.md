# 🛡️ Sentinel Scanner

A simple and effective **Port & Service Scanner** with built-in **CVE vulnerability lookup** using the [NVD API](https://nvd.nist.gov/developers).  
Built with **Python** and **Streamlit** for easy, interactive use.

---

## 🔍 Features

- 🚀 Fast scan of common ports on any domain or IP
- 📡 Automatic service banner detection
- 🧠 CVE lookup for detected services via NVD
- 💻 Simple web UI powered by Streamlit
- 📦 Clean project structure & easily extensible

---

## 📸 Screenshot

![UI Preview](screenshot.png) <!-- Replace with your screenshot file name -->

---

## 🧰 Technologies Used

- Python 3
- Streamlit
- Socket
- NVD API (National Vulnerability Database)

---

## 📦 Installation

```bash
git clone https://github.com/mickeypatil/sentinel-scanner.git
cd sentinel-scanner
python -m venv venv
venv\Scripts\activate        # On Windows
pip install -r requirements.txt
