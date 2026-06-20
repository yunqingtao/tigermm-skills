"""QR code generator"""
def skill_info():
    return {"name": "qr_code", "desc": "Generate QR code as text/URL", "tags": ["qr", "encode"], "triggers": ["qr", "barcode"]}
def execute(args):
    text = args.get("text", "https://maryask.com")
    url = f"https://api.qrserver.com/v1/create-qr-code/?size=150x150&data={text}"
    return f"QR Code: {url}"