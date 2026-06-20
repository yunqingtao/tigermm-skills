"""Strong password generator"""
import secrets, string
def skill_info():
    return {"name": "password_gen", "desc": "Generate secure passwords", "tags": ["security", "password"], "triggers": ["password", "generate password"]}
def execute(args):
    length = int(args.get("length", 16))
    chars = string.ascii_letters + string.digits + "!@#$%^&*"
    return secrets.SystemRandom().choice(string.ascii_uppercase) + ''.join(secrets.choice(chars) for _ in range(length-1))