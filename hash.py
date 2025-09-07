#!/usr/bin/env python3

import mmh3
import requests
import base64
import pyfiglet

def hash_favicon(url):
    try:
        if not url.startswith("http"):
            url = "http://" + url
            
        # Try to fetch favicon.ico
        favicon_url = url.rstrip("/") + "/favicon.ico"
        print(f"[+] Fetching favicon from {favicon_url}")
        
        response = requests.get(favicon_url, timeout=5, verify=False)
        
        if response.status_code == 200:
            # Encode favicon in base64
            favicon_base64 = base64.encodebytes(response.content)
            
            # Generate murmurhash3 (Used by shodan.io/fofa)
            favicon_hash = mmh3.hash(favicon_base64)
            
            print(f"[+] Result Favicon Hash: {favicon_hash}")
            return favicon_hash
        else:
            print("[-] Could not fetching favicon")    
            return none 
    except Exception as e:
        print(f"[-] Error: {e}")
            
if __name__ == "__main__":
    banner = pyfiglet.figlet_format("Hashing-Recon")
    print(banner)
    print("🧑‍💻 Author: https://github.com/JulioPryd")
    
    target = input("Enter website URL: ")
    hash_favicon(target)
