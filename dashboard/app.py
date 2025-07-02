# dashboard/app.py
# Sentinel Scanner - A simple port and service scanner with CVE lookup
import streamlit as st
import socket
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from scanner.cve_lookup import search_cve
from scanner.port_scanner import scan_port  # Port scanner function
from scanner.cve_lookup import search_cve  # CVE lookup function

st.set_page_config(page_title="Sentinel Scanner", layout="centered")

st.title("🔍 Sentinel Port & Service Scanner")

target = st.text_input("Enter a domain or IP address", "scanme.nmap.org")
start_scan = st.button("Start Scan")

def scan(ip):
    results = []
    for port in [22, 80, 443, 3306, 8080]:
        try:
            sock = socket.socket()
            sock.settimeout(0.5)
            sock.connect((ip, port))
            try:
                sock.sendall(b"Hello\r\n")
                banner = sock.recv(1024).decode(errors="ignore").strip()
                if not banner:
                    banner = "Unknown"
            except:
                banner = "Unknown"
            results.append((port, banner))
            sock.close()
        except:
            pass
    return results

if start_scan:
    try:
        ip = socket.gethostbyname(target)
        st.write(f"🛰️ Scanning `{ip}`...")
        scan_results = scan(ip)

        if scan_results:
            for port, service in scan_results:
                st.success(f"✅ Port {port} open | Service: {service}")

                # 🔍 CVE Lookup
                if service != "Unknown":
                    st.write(f"🔍 Searching CVEs for `{service}`...")
                    cves = search_cve(service)

                    if cves:
                        for cve in cves:
                            with st.expander(f"🛑 {cve['id']} | Severity: {cve['severity']}"):
                                st.write(cve['description'])
                    else:
                        st.info("No known CVEs found.")
        else:
            st.warning("No open ports found in the scanned range.")
    except socket.gaierror:
        st.error("❌ Invalid domain or IP address.")
    except Exception as e:
        st.error(f"Unexpected error: {e}")