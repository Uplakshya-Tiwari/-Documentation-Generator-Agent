import os, ast

def find_python_files(folder):
    return [os.path.join(r,f) for r,_,fs in os.walk(folder) for f in fs if f.endswith('.py')]

def analyze_code(file):
    tree = ast.parse(open(file).read())
    funcs, clss = [], []
    for n in ast.walk(tree):
        if isinstance(n, ast.FunctionDef):
            funcs.append((n.name, ast.get_docstring(n) or "No description"))
        if isinstance(n, ast.ClassDef):
            clss.append((n.name, ast.get_docstring(n) or "No description"))
    return funcs, clss

def generate(project):
    doc = "# Project Documentation
"
    for f in find_python_files(project):
        funcs, clss = analyze_code(f)
        doc += f"\n## File: {os.path.basename(f)}\n"
        doc += "\n### Classes\n"
        doc += "\n".join([f"- {c}: {d}" for c,d in clss]) or "- None"
        doc += "\n\n### Functions\n"
        doc += "\n".join([f"- {fn}: {d}" for fn,d in funcs]) or "- None"
    return doc

def save(doc):
    os.makedirs("docs", exist_ok=True)
    open("docs/DOCUMENTATION.md","w").write(doc)

if __name__=='__main__':
    save(generate("sample_project"))
