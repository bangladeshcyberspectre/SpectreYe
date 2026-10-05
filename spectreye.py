#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#   ███████╗██████╗ ███████╗ ██████╗████████╗██████╗ ███████╗██╗   ██╗███████╗
#   ██╔════╝██╔══██╗██╔════╝██╔════╝╚══██╔══╝██╔══██╗██╔════╝╚██╗ ██╔╝██╔════╝
#   ███████╗██████╔╝█████╗  ██║        ██║   ██████╔╝█████╗   ╚████╔╝ █████╗
#   ╚════██║██╔═══╝ ██╔══╝  ██║        ██║   ██╔══██╗██╔══╝    ╚██╔╝  ██╔══╝
#   ███████║██║     ███████╗╚██████╗   ██║   ██║  ██║███████╗   ██║   ███████╗
#   ╚══════╝╚═╝     ╚══════╝ ╚═════╝   ╚═╝   ╚═╝  ╚═╝╚══════╝   ╚═╝   ╚══════╝
#
#   SpectreYe — Admin Panel Hunter
#   Team   : Bangladesh Cyber Spectre (BCS)
#   Coder  : Ochena Gamer
#   Version: 1.0.0
#

import requests
import sys
import os
import time
import threading
from queue import Queue
from datetime import datetime
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

try:
    from colorama import Fore, Back, Style, init
    init(autoreset=True)
except ImportError:
    os.system("pip install colorama -q")
    from colorama import Fore, Back, Style, init
    init(autoreset=True)

# ── Color shortcuts ──────────────────────────────────────────────────────────
R   = Fore.RED
G   = Fore.GREEN
Y   = Fore.YELLOW
C   = Fore.CYAN
W   = Fore.WHITE
M   = Fore.MAGENTA
B   = Fore.BLUE
DM  = Style.DIM
BRT = Style.BRIGHT
RST = Style.RESET_ALL

# ── Admin paths ──────────────────────────────────────────────────────────────
PATHS = [
    "admin","admin/","admin.php","admin.html","admin.asp","admin.aspx",
    "admin/login","admin/login.php","admin/login.html","admin/index.php",
    "admin/index.html","admin/admin.php","admin/dashboard.php",
    "admin/panel.php","admin/cp.php","admin/controlpanel.php",
    "admin/manage.php","admin/admin_login.php","admin/home.php",
    "administrator","administrator/","administrator/index.php",
    "administrator/login.php","administrator/admin.php",
    "panel","panel/","panel.php","panel/login.php",
    "cpanel","cpanel/","cp","cp/","cp.php",
    "control","control/","controlpanel","controlpanel/",
    "control-panel","control_panel",
    "login","login/","login.php","login.html","login.asp","login.aspx",
    "signin","signin.php","signin.html","sign-in","sign_in",
    "user/login","user/signin","member/login",
    "dashboard","dashboard/","dashboard.php","dashboard.html","dash","dash/",
    "wp-admin","wp-admin/","wp-admin/index.php","wp-login.php",
    "wp-admin/login.php","wordpress/wp-admin","blog/wp-admin",
    "blog/wp-login.php",
    "administrator/index.php","joomla/administrator",
    "user","user/login","admin/user/login",
    "index.php/admin","magento/admin","store/admin","shop/admin",
    "adminpanel","admin123","admin1",
    "typo3","typo3/","typo3/index.php",
    "phpmyadmin","phpmyadmin/","phpmyadmin/index.php",
    "pma","pma/","mysql","mysql/","mysqladmin","myadmin","myadmin/",
    "webmail","webmail/","webmail/index.php","mail","mail/",
    "roundcube","roundcube/",
    "forum/admin","forum/admin.php","board/admin",
    "phpbb/admin","vbulletin/admincp","admincp","admincp/",
    "shop/admin","store/admin","ecommerce/admin","cart/admin",
    "manage","manage/","management","management/",
    "moderator","moderator/","webadmin","webadmin/",
    "siteadmin","siteadmin/","sysadmin","sysadmin/",
    "backend","backend/","backoffice","backoffice/",
    "staff","staff/","secure","secure/","secret","secret/",
    "private","private/","hidden","hidden/","manager","manager/",
    "master","master/","superadmin","super-admin","super_admin",
    "account","account/","accounts","accounts/",
    "member","member/","members","members/",
    "user-admin","useradmin","user_admin",
    "filemanager","filemanager/","files","files/",
    "file-manager","file_manager","fm","fm/","elfinder","elfinder/",
    "config","config/","configuration","configuration/",
    "setup","setup/","install","install/","installer","installer/",
    "admin_area","admin_login","admin_panel","admin_cp",
    "admin-login","admin-panel","admin-area","adm","adm/",
    "api/admin","api/v1/admin","api/v2/admin","rest/admin",
    "staging/admin","dev/admin","test/admin","beta/admin","demo/admin",
    "portal","portal/","intranet","intranet/",
    "cms","cms/","cms/admin","cms/login",
    "system","system/","sys","sys/",
    "admin.aspx","admin/default.aspx","admin/login.aspx","login.aspx",
    "default.aspx","manage.aspx","controlpanel.aspx",
    "admin.jsp","admin/login.jsp","login.jsp","dashboard.jsp",
    "django-admin","admin/doc",
    "admin/dashboard","admin/home",
    "console","console/","portal/login","app/admin","app/login",
    "old-admin","old_admin","new-admin","new_admin",
    "temp-admin","tmp/admin","bak/admin","backup/admin",
    "security","security/","waf","waf/",
    "administer","administer/",
]

# ── Globals ───────────────────────────────────────────────────────────────────
found_panels  = []
checked_count = 0
total_paths   = len(PATHS)
lock          = threading.Lock()
scan_done     = False


# ── Helpers ───────────────────────────────────────────────────────────────────
def clear():
    os.system("cls" if os.name == "nt" else "clear")


def slow_print(text, delay=0.012):
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    print()


def normalize(url: str) -> str:
    url = url.strip()
    if not url.startswith(("http://", "https://")):
        url = "http://" + url
    return url.rstrip("/")


def status_color(code: int) -> str:
    if code == 200:           return G
    if code in (301,302,307): return Y
    if code == 403:           return M
    if code == 401:           return C
    return R


# ── Banner ────────────────────────────────────────────────────────────────────
def print_banner():
    clear()
    print(f"""
{C}╔{'═'*68}╗
║{' '*68}║
║{R}  ███████╗██████╗ ███████╗ ██████╗████████╗██████╗ ███████╗██╗   ██╗███████╗  {C}║
║{R}  ██╔════╝██╔══██╗██╔════╝██╔════╝╚══██╔══╝██╔══██╗██╔════╝╚██╗ ██╔╝██╔════╝  {C}║
║{Y}  ███████╗██████╔╝█████╗  ██║        ██║   ██████╔╝█████╗   ╚████╔╝ █████╗    {C}║
║{Y}  ╚════██║██╔═══╝ ██╔══╝  ██║        ██║   ██╔══██╗██╔══╝    ╚██╔╝  ██╔══╝    {C}║
║{G}  ███████║██║     ███████╗╚██████╗   ██║   ██║  ██║███████╗   ██║   ███████╗  {C}║
║{G}  ╚══════╝╚═╝     ╚══════╝ ╚═════╝   ╚═╝   ╚═╝  ╚═╝╚══════╝   ╚═╝   ╚══════╝  {C}║
║{' '*68}║
║{W}          ⚡  Admin Panel Hunter  —  v1.0.0  ⚡                         {C}║
║{' '*68}║
║{DM}  Team   : {W}Bangladesh Cyber Spectre {DM}(BCS){' '*29}{C}║
║{DM}  Coder  : {W}Ochena Gamer{' '*41}{C}║
║{DM}  Engine : {W}{total_paths} paths  |  Multi-threaded  |  Color-coded{' '*13}{C}║
║{' '*68}║
╚{'═'*68}╝{RST}""")


# ── Status legend ─────────────────────────────────────────────────────────────
def print_legend():
    print(f"""
  {C}┌─ Status Legend {'─'*46}┐{RST}
  {C}│{RST}  {G}[200]{RST} Accessible      {Y}[301/302]{RST} Redirect        {M}[403]{RST} Forbidden   {C}│{RST}
  {C}│{RST}  {C}[401]{RST} Needs Auth      {R}[404]{RST}     Not Found                          {C}│{RST}
  {C}└{'─'*62}┘{RST}
""")


# ── Interactive prompts ───────────────────────────────────────────────────────
def prompt(label, default=None, cast=None):
    dflt = f" {DM}[{default}]{RST}" if default is not None else ""
    while True:
        try:
            val = input(f"  {C}❯{RST} {W}{label}{dflt}{RST} : ").strip()
        except (KeyboardInterrupt, EOFError):
            print(f"\n\n  {Y}[!] Interrupted. Goodbye.{RST}\n")
            sys.exit(0)

        if not val and default is not None:
            return default
        if val:
            if cast:
                try:
                    return cast(val)
                except ValueError:
                    print(f"    {R}[!] Invalid value. Try again.{RST}")
                    continue
            return val
        print(f"    {R}[!] Field cannot be empty.{RST}")


def gather_config():
    print_banner()
    print_legend()
    print(f"  {Y}{'─'*62}{RST}")
    print(f"  {BRT}{W}  Configure your scan below. Press Enter to use defaults.{RST}")
    print(f"  {Y}{'─'*62}{RST}\n")

    url     = prompt("Target URL  (e.g. http://target.com)")
    threads = prompt("Threads     (default: 30)", default=30, cast=int)
    timeout = prompt("Timeout     (seconds, default: 8)", default=8, cast=int)

    out_ans = prompt("Save output? (y/n, default: y)", default="y")
    output  = None
    if out_ans.lower() in ("y", "yes"):
        domain  = normalize(url).replace("http://","").replace("https://","").split("/")[0]
        default_out = f"spectreye_{domain}_{datetime.now().strftime('%H%M%S')}.txt"
        output  = prompt(f"Output file", default=default_out)

    verbose_ans = prompt("Verbose mode — show all? (y/n, default: n)", default="n")
    verbose = verbose_ans.lower() in ("y","yes")

    custom_wl = prompt("Custom wordlist path? (leave blank = built-in)", default="")
    wordlist  = PATHS
    if custom_wl and os.path.isfile(custom_wl):
        with open(custom_wl, "r", encoding="utf-8", errors="ignore") as f:
            wordlist = [l.strip() for l in f if l.strip()]
        print(f"  {G}[✓] Loaded {len(wordlist)} paths from {custom_wl}{RST}")
    elif custom_wl:
        print(f"  {Y}[!] File not found — using built-in list.{RST}")

    return {
        "url"      : normalize(url),
        "threads"  : threads,
        "timeout"  : timeout,
        "output"   : output,
        "verbose"  : verbose,
        "wordlist" : wordlist,
    }


# ── Worker ────────────────────────────────────────────────────────────────────
HEADERS = {
    "User-Agent"     : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                       "AppleWebKit/537.36 (KHTML, like Gecko) "
                       "Chrome/120.0.0.0 Safari/537.36",
    "Accept"         : "text/html,application/xhtml+xml,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Connection"     : "keep-alive",
}


def worker(q: Queue, base: str, timeout: int, verbose: bool):
    global checked_count
    while not q.empty():
        path = q.get()
        url  = f"{base}/{path}"
        try:
            r    = requests.get(url, headers=HEADERS, timeout=timeout,
                                allow_redirects=True, verify=False)
            code = r.status_code
            col  = status_color(code)
            with lock:
                checked_count += 1
                if code in (200, 301, 302, 401, 403):
                    found_panels.append({"url": url, "status": code})
                    print(f"\r  {G}[FOUND]{RST} [{col}{code}{RST}] {W}{url}{RST}")
                elif verbose:
                    print(f"\r  {DM}[{code}] {url}{RST}")
        except Exception:
            with lock:
                checked_count += 1
        finally:
            q.task_done()


# ── Progress bar ──────────────────────────────────────────────────────────────
def progress_loop(total: int):
    while not scan_done:
        with lock:
            done = checked_count
        pct  = done / total * 100 if total else 0
        bar  = int(pct / 2)
        line = (f"\r  {C}[{'█'*bar}{'░'*(50-bar)}]{RST} "
                f"{W}{pct:5.1f}%{RST} "
                f"{DM}({done}/{total}){RST}  ")
        sys.stdout.write(line)
        sys.stdout.flush()
        time.sleep(0.15)
    sys.stdout.write("\r" + " " * 80 + "\r")
    sys.stdout.flush()


# ── Save ──────────────────────────────────────────────────────────────────────
def save(target: str, results: list, path: str):
    ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(path, "w", encoding="utf-8") as f:
        f.write("=" * 60 + "\n")
        f.write("  SpectreYe — Admin Panel Hunter\n")
        f.write("  Bangladesh Cyber Spectre | Coded by Ochena Gamer\n")
        f.write("=" * 60 + "\n")
        f.write(f"  Target  : {target}\n")
        f.write(f"  Time    : {ts}\n")
        f.write(f"  Found   : {len(results)} panel(s)\n")
        f.write("=" * 60 + "\n\n")
        if results:
            f.write("[+] FOUND PANELS:\n\n")
            for r in results:
                f.write(f"  [{r['status']}] {r['url']}\n")
        else:
            f.write("[-] No admin panels found.\n")
        f.write("\n" + "=" * 60 + "\n")


# ── Scan ──────────────────────────────────────────────────────────────────────
def run_scan(cfg: dict):
    global scan_done, checked_count, found_panels
    scan_done     = False
    checked_count = 0
    found_panels  = []

    base     = cfg["url"]
    wl       = cfg["wordlist"]
    threads  = cfg["threads"]
    timeout  = cfg["timeout"]
    verbose  = cfg["verbose"]
    output   = cfg["output"]
    total    = len(wl)

    print_banner()

    # scan info box
    print(f"""
  {C}┌─ Scan Configuration {'─'*42}┐{RST}
  {C}│{RST}  {DM}Target  :{RST} {W}{base}{' '*(55-len(base))}{C}│{RST}
  {C}│{RST}  {DM}Paths   :{RST} {W}{total}{' '*(55-len(str(total)))}{C}│{RST}
  {C}│{RST}  {DM}Threads :{RST} {W}{threads}{' '*(55-len(str(threads)))}{C}│{RST}
  {C}│{RST}  {DM}Timeout :{RST} {W}{timeout}s{' '*(54-len(str(timeout)))}{C}│{RST}
  {C}│{RST}  {DM}Output  :{RST} {W}{output if output else 'None'}{' '*(55-len(str(output or 'None')))}{C}│{RST}
  {C}└{'─'*62}┘{RST}

  {Y}[*] Launching scan...{RST}
  {Y}{'─'*62}{RST}
""")
    time.sleep(0.6)

    q = Queue()
    for p in wl:
        q.put(p)

    # start progress thread
    prog = threading.Thread(target=progress_loop, args=(total,), daemon=True)
    prog.start()

    # start workers
    pool = []
    for _ in range(min(threads, total)):
        t = threading.Thread(
            target=worker,
            args=(q, base, timeout, verbose),
            daemon=True
        )
        t.start()
        pool.append(t)

    for t in pool:
        t.join()

    scan_done = True
    prog.join(timeout=1)

    # ── Results ──
    print(f"\n  {Y}{'═'*62}{RST}")
    print(f"\n  {BRT}{G}[✓] Scan Complete{RST}")
    print(f"  {DM}Checked :{RST} {W}{checked_count}{RST} paths")
    print(f"  {DM}Found   :{RST} {G if found_panels else R}{len(found_panels)}{RST} panel(s)\n")

    if found_panels:
        print(f"  {G}{'─'*62}{RST}")
        print(f"  {BRT}{W}  ⚡ Panels Discovered:{RST}\n")
        for p in found_panels:
            col = status_color(p["status"])
            print(f"    {G}►{RST} [{col}{p['status']}{RST}]  {W}{p['url']}{RST}")
        print(f"\n  {G}{'─'*62}{RST}")
    else:
        print(f"  {R}[-] No admin panels found on this target.{RST}")

    if output:
        save(base, found_panels, output)
        print(f"\n  {C}[*] Results saved → {W}{output}{RST}")

    print(f"""
  {C}╔{'═'*62}╗
  ║{'  SpectreYe — Bangladesh Cyber Spectre | Ochena Gamer':^62}║
  ╚{'═'*62}╝{RST}
""")


# ── Replay prompt ─────────────────────────────────────────────────────────────
def ask_again() -> bool:
    try:
        ans = input(f"  {C}❯{RST} {W}Scan another target? (y/n){RST} : ").strip().lower()
        return ans in ("y", "yes")
    except (KeyboardInterrupt, EOFError):
        return False


# ── Entry ─────────────────────────────────────────────────────────────────────
def main():
    while True:
        cfg = gather_config()
        run_scan(cfg)
        if not ask_again():
            print(f"\n  {Y}[*] SpectreYe shutting down. Stay sharp.{RST}\n")
            break


if __name__ == "__main__":
    main()
