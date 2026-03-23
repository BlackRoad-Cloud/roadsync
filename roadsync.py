#!/usr/bin/env python3
"""RoadSync — Sync files between fleet nodes via rsync over SSH"""
import subprocess, sys, yaml, os

CONFIG = {
  "nodes": {
    "alice": {"host": "192.168.4.49", "user": "blackroad", "paths": ["/home/blackroad/data"]},
    "cecilia": {"host": "192.168.4.96", "user": "blackroad", "paths": ["/home/blackroad/models", "/home/blackroad/data"]},
    "octavia": {"host": "192.168.4.101", "user": "blackroad", "paths": ["/home/blackroad/repos", "/home/blackroad/workers"]},
    "lucidia": {"host": "192.168.4.38", "user": "blackroad", "paths": ["/home/blackroad/dns", "/home/blackroad/apps"]},
  }
}

def sync(source, target, path=None, dry_run=False):
    src = CONFIG["nodes"].get(source)
    tgt = CONFIG["nodes"].get(target)
    if not src or not tgt:
        print(f"Unknown node: {source if not src else target}")
        return
    paths = [path] if path else src["paths"]
    for p in paths:
        cmd = ["rsync", "-avz", "--progress"]
        if dry_run: cmd.append("--dry-run")
        cmd += [f"{src['user']}@{src['host']}:{p}/", f"{tgt['user']}@{tgt['host']}:{p}/"]
        print(f"  {source}:{p} → {target}:{p}")
        print(f"  Command: {' '.join(cmd)}")
        if not dry_run:
            subprocess.run(cmd)

def status():
    for name, node in CONFIG["nodes"].items():
        r = subprocess.run(["ssh", "-o", "ConnectTimeout=3", f"{node['user']}@{node['host']}", "uptime"],
            capture_output=True, text=True, timeout=5)
        status = "online" if r.returncode == 0 else "offline"
        print(f"  {name:12s} {node['host']:16s} {status}")

if __name__ == "__main__":
    if len(sys.argv) < 2: print("Usage: roadsync.py [sync|status] [--source X --target Y] [--dry-run]"); sys.exit()
    if sys.argv[1] == "sync": sync(sys.argv[3] if "--source" in sys.argv else "alice", sys.argv[5] if "--target" in sys.argv else "cecilia", dry_run="--dry-run" in sys.argv)
    elif sys.argv[1] == "status": status()
