#!/usr/bin/env python3
"""Fetch https://intranet.hbtn.io/status using urllib and print body info."""
import urllib.request

if __name__ == "__main__":
    url = "https://intranet.hbtn.io/status"
    with urllib.request.urlopen(url) as response:
        body = response.read()

    print("Body response:")
    print("    - type: {}".format(type(body)))
    print("    - content: {}".format(body))
    try:
        utf8_content = body.decode("utf-8")
    except Exception:
        # Əgər decode uğursuz olarsa, təhlükəsiz fallback üçün 'replace' istifadə et
        utf8_content = body.decode("utf-8", errors="replace")
    print("    - utf8 content: {}".format(utf8_content))
