"""JSON pretty printer and validator"""
import json
def skill_info():
    return {"name": "json_formatter", "desc": "Format and validate JSON", "tags": ["json", "format"], "triggers": ["json", "format json"]}
def execute(args):
    text = args.get("json", "{}")
    try:
        return json.dumps(json.loads(text), indent=2, ensure_ascii=False)
    except:
        return "Invalid JSON"