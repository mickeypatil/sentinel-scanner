# 🔍 Sentinel Scanner

A lightweight cybersecurity toolkit for basic **port scanning**, **service detection**, and **vulnerability lookup using CVE API**.  
Built with Python and Streamlit for an interactive and easy-to-use dashboard.

---

## ⚙️ Features

- 🚀 Fast TCP Port Scanning (1-1024)
- 🔎 Service Banner Grabbing
- 🛡️ CVE Lookup for Detected Services (via NVD API)
- 📊 Streamlit Dashboard for Interactive UI
- ✅ Clean & Minimal Python Codebase

---

## 📁 Project Structure

```
sentinel-scanner/
│
├── scanner/
│   ├── port_scanner.py
│   ├── cve_lookup.py
│   ├── vuln_lookup.py
│   └── __pycache__/
│
├── dashboard/
│   └── app.py
│
├── config.ini
├── requirements.txt
└── README.md
```

---

## 🧑‍💻 How to Run It

### 1. Clone the project

```bash
git clone https://github.com/mickeypatil/sentinel-scanner.git
cd sentinel-scanner
```

### 2. Create virtual environment

```bash
python -m venv venv
venv\Scripts\activate  # (or use source venv/bin/activate on Linux/Mac)
```

### 3. Install requirements

```bash
pip install -r requirements.txt
```

### 4. Add your NVD API Key

1. Go to [https://nvd.nist.gov/developers](https://nvd.nist.gov/developers)
2. Sign up and get your API key.
3. Create a file named `config.ini` and paste this inside:

```ini
[NVD]
api_key = YOUR_API_KEY_HERE
```

---

### 5. Run the Streamlit dashboard

```bash
streamlit run dashboard/app.py
```

---

## 🖥️ Demo Screenshot

![Sentinel Scanner UI](https://github.com/mickeypatil/sentinel-scanner/blob/8105b69b92aa5c5744449f2a65a3dc21859d25ec/assets/Screenshot1.png)
![Sentinel Scanner UI2](https://github.com/mickeypatil/sentinel-scanner/blob/8105b69b92aa5c5744449f2a65a3dc21859d25ec/assets/screenshot2.png)

---

## 💡 Example Output

- ✅ Port 22 open | Service: SSH-2.0-OpenSSH_6.6.1p1 Ubuntu-2ubuntu2.13  
  🔍 Searching CVEs...  
  🛑 CVE-2021-41617 | Severity: HIGH  
  Improper privilege separation in OpenSSH before 8.8 could allow...

---

## 📌 Future Enhancements

- Full TCP/UDP scanning
- Export reports as PDF/CSV
- Real-time CVSS scoring summary
- Add WHOIS + GeoIP integration

---

## 👨‍💻 Author

**Aryan Patil**  
🔗 [GitHub Profile](https://github.com/mickeypatil)

---

## 📄 License

This project is licensed under the MIT License.
