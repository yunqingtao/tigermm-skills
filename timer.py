"""Countdown timer"""
import time
def skill_info():
    return {"name": "timer", "desc": "Countdown timer with notification", "tags": ["timer", "utility"], "triggers": ["timer", "countdown"]}
def execute(args):
    seconds = int(args.get("seconds", 10))
    for i in range(seconds, 0, -1):
        time.sleep(1)
    return f"Timer done! ({seconds}s)"