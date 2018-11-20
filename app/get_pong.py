import re
import subprocess, platform

def get_pong(server):
    ip_regexp = "(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)(\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)){3}"
    if server:
        if re.match(ip_regexp, server) is not None:
            ping_str = "-n 1" if platform.system().lower() == "windows" else "-c 1"
            args = "ping " + " " + ping_str + " " + server
            need_sh = False if platform.system().lower() == "windows" else True
            return subprocess.call(args, shell=need_sh) == 0

