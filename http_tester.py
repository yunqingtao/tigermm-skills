"""HTTP API tester"""
import urllib.request, json
def skill_info():
    return {"name": "http_tester", "desc": "Test HTTP endpoints", "tags": ["http", "api", "test"], "triggers": ["http", "api test", "rest"]}
def execute(args):
    url = args.get("url", "https://httpbin.org/get")
    try:
        with urllib.request.urlopen(url, timeout=5) as r:
            return f"Status: {r.status}\n{json.dumps(json.loads(r.read()), indent=2)[:500]}"
    except Exception as e:
        return f"Error: {e}"