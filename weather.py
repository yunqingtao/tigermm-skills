"""Weather lookup skill"""
def skill_info():
    return {"name": "weather", "desc": "Weather lookup via wttr.in", "tags": ["weather", "forecast"], "triggers": ["weather", "temperature", "forecast"]}
def execute(args):
    import urllib.request
    city = args.get("city", "Jinan")
    url = f"https://wttr.in/{city}?format=3"
    with urllib.request.urlopen(url, timeout=5) as r:
        return r.read().decode()