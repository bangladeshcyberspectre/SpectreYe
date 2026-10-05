```
╔══════════════════════════════════════════════════════════════════════╗
║                                                                      ║
║  ███████╗██████╗ ███████╗ ██████╗████████╗██████╗ ███████╗██╗   ██╗ ║
║  ██╔════╝██╔══██╗██╔════╝██╔════╝╚══██╔══╝██╔══██╗██╔════╝╚██╗ ██╔╝ ║
║  ███████╗██████╔╝█████╗  ██║        ██║   ██████╔╝█████╗   ╚████╔╝  ║
║  ╚════██║██╔═══╝ ██╔══╝  ██║        ██║   ██╔══██╗██╔══╝    ╚██╔╝   ║
║  ███████║██║     ███████╗╚██████╗   ██║   ██║  ██║███████╗   ██║    ║
║  ╚══════╝╚═╝     ╚══════╝ ╚═════╝   ╚═╝   ╚═╝  ╚═╝╚══════╝   ╚═╝    ║
║                                                                      ║
║           SpectreYe — Admin Panel Hunter  v1.0.0                     ║
║           Team   : Bangladesh Cyber Spectre (BCS)                    ║
║           Coder  : Ochena Gamer                                      ║
║                                                                      ║
╚══════════════════════════════════════════════════════════════════════╝
```

---

## 🐦‍⬛ About

**SpectreYe** is an interactive, fully menu-driven admin panel discovery tool built by **Ochena Gamer** for **Bangladesh Cyber Spectre (BCS)**.

No command-line arguments needed — just run it, answer the prompts, and let SpectreYe hunt.

---

## ⚡ Features

- ✅ **Fully interactive** — no flags, no args, just prompts
- ✅ **500+ built-in admin paths** (WordPress, Joomla, Drupal, phpMyAdmin, etc.)
- ✅ **Multi-threaded** — up to 100+ concurrent threads
- ✅ **Real-time progress bar** with percentage
- ✅ **Color-coded output** by HTTP status
- ✅ **Custom wordlist** support
- ✅ **Auto-named output files** per target
- ✅ **Verbose mode** for full response logging
- ✅ **Multi-scan** — scan again without restarting
- ✅ **SSL bypass** built-in

---

## 🛠 Installation

```bash
git clone https://github.com/bangladeshcyberspectre/SpectreYe.git
cd SpectreYe
pip install -r requirements.txt
python spectreye.py
```

---

## 🚀 Usage

```bash
python spectreye.py
```

SpectreYe will interactively ask:

```
❯ Target URL       : http://target.com
❯ Threads          : 30
❯ Timeout          : 8
❯ Save output?     : y
❯ Output file      : spectreye_target.com_143022.txt
❯ Verbose mode?    : n
❯ Custom wordlist? : (leave blank for built-in)
```

Then it launches, shows live progress, and prints all found panels.

---

## 🎨 Status Code Colors

| Color    | Code      | Meaning                  |
|----------|-----------|--------------------------|
| 🟢 Green  | 200       | Directly accessible      |
| 🟡 Yellow | 301 / 302 | Redirect — follow it     |
| 🟣 Magenta| 403       | Forbidden — panel exists |
| 🔵 Cyan   | 401       | Needs authentication     |
| 🔴 Red    | 404 / 500 | Not found / Error        |

---

## 📁 Project Structure

```
spectreye/
├── spectreye.py       ← Main tool (run this)
├── requirements.txt   ← Dependencies
├── README.md          ← Documentation
└── LICENSE            ← MIT License
```

---

## 📦 Requirements

- Python 3.8+
- `requests`
- `colorama`
- `urllib3`

---

## ⚠️ Legal Notice

For **authorized penetration testing and security research only**. Only use on systems you own or have explicit written permission to test.

---

## 👥 Team

```
Tool    : SpectreYe
Team    : Bangladesh Cyber Spectre (BCS)
Coder   : Ochena Gamer
Version : 1.0.0
```

---

*Bangladesh Cyber Spectre — Strike clean. Deliver sharp.*
