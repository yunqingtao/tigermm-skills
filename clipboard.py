"""Clipboard read/write"""
def skill_info():
    return {"name": "clipboard", "desc": "Read and write system clipboard", "tags": ["clipboard", "system"], "triggers": ["clipboard", "copy"]}
def execute(args):
    try:
        import subprocess, sys
        if args.get("text"):
            subprocess.run(["clip"], input=args["text"].encode(), capture_output=True)
            return f"Written to clipboard"
        return subprocess.run(["powershell", "Get-Clipboard"], capture_output=True, text=True).stdout.strip()
    except:
        return "Clipboard access failed (Windows only)"