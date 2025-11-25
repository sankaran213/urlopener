# 🚀 Send To Laptop  
Send any article or URL from your **phone → laptop** instantly with a single tap.  
Works **offline**, over **WiFi** or **Laptop Hotspot**, with **zero internet required**.

This project creates a lightweight background server on your laptop and a simple sender page on your phone to instantly push URLs to your laptop's browser.

---

## ⭐ Features

- 📲 **Send URLs from phone → laptop instantly**
- 🌐 Works on **same WiFi** or **laptop hotspot**  
- 📴 **No internet required**
- ⚡ Instant browser open on laptop
- 🔎 **Automatic IP discovery using mDNS (sendtolaptop.local)**
- 🖥️ Runs in background on laptop (as Windows Service or Startup)
- 💡 Extremely lightweight (10–20MB RAM)
- 🧰 Simple HTML sender page (or Android shortcut support)

---

## 🎯 How It Works

1. Your laptop runs a lightweight Flask server (`receiver.py`)
2. Your phone opens a small HTML page (`send.html`)
3. When you enter/share a URL → the phone sends it to your laptop  
4. Laptop immediately opens it in your default browser

Communication happens over LAN or hotspot using:

