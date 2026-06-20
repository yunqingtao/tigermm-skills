"""Markdown to HTML converter"""
def skill_info():
    return {"name": "markdown_preview", "desc": "Convert Markdown to HTML", "tags": ["markdown", "html"], "triggers": ["markdown", "md to html"]}
def execute(args):
    md = args.get("text", "# Hello")
    try:
        import markdown
        return markdown.markdown(md)
    except:
        return f"<h1>{md.replace('#','').strip()}</h1>"