"""Expression calculator"""
def skill_info():
    return {"name": "calculator", "desc": "Evaluate math expressions", "tags": ["math", "calculate"], "triggers": ["calculate", "compute", "math"]}
def execute(args):
    expr = args.get("expr", "1+1")
    try:
        return str(eval(expr, {"__builtins__": {}}, {"abs": abs, "round": round, "pow": pow, "max": max, "min": min}))
    except Exception as e:
        return f"Error: {e}"