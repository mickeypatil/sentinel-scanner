# scanner/cve_lookup.py

import requests
import configparser

# Load API Key
config = configparser.ConfigParser()
config.read('config.ini')
API_KEY = config.get('NVD', 'api_key')

headers = {
    "apiKey": API_KEY
}

def search_cve(keyword):
    url = f"https://services.nvd.nist.gov/rest/json/cves/2.0?keywordSearch={keyword}&resultsPerPage=5"
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            if "vulnerabilities" in data:
                return [
                    {
                        "id": item['cve']['id'],
                        "description": item['cve']['descriptions'][0]['value'],
                        "severity": item['cve']['metrics'].get('cvssMetricV31', [{}])[0].get('cvssData', {}).get('baseSeverity', 'N/A')
                    }
                    for item in data["vulnerabilities"]
                ]
            else:
                return []
        else:
            return []
    except Exception as e:
        print(f"Error: {e}")
        return []
