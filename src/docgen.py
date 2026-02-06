import os
import ast

# -----------------------------------
# Scan the project directory
# -----------------------------------
def find_python_files(folder_path):
    python_files = []

    for root, _, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".py"):
                python_files.append(os.path.join(root, file))

    return python_files


# -----------------------------------
# Analyze a Python file using AST
# -----------------------------------
def analyze_code(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        source_code = f.read()

    tree = ast.parse(source_code)

    functions = []
    classes = []

    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            functions.append({
                "name": node.name,
                "doc": ast.get_docstring(node) or "No description provided"
            })

        if isinstance(node, ast.ClassDef):
            classes.append({
                "name": node.name,
                "doc": ast.get_docstring(node) or "No description provided"
            })

    return functions, classes


# -----------------------------------
# Generate Markdown documentation
# -----------------------------------
def generate_documentation(project_path):
    documentation = "# Project Documentation\n\n"

    python_files = find_python_files(project_path)

    for file in python_files:
        functions, classes = analyze_code(file)

        documentation += f"## File: {os.path.basename(file)}\n\n"

        documentation += "### Classes\n"
        if classes:
            for cls in classes:
                documentation += f"- {cls['name']}: {cls['doc']}\n"
        else:
            documentation += "- None\n"

        documentation += "\n### Functions\n"
        if functions:
            for func in functions:
                documentation += f"- {func['name']}: {func['doc']}\n"
        else:
            documentation += "- None\n"

        documentation += "\n"

    return documentation


# -----------------------------------
# Save documentation to file
# -----------------------------------
def save_documentation(content):
    os.makedirs("docs", exist_ok=True)

    with open("docs/DOCUMENTATION.md", "w", encoding="utf-8") as f:
        f.write(content)

    print("Documentation generated successfully!")


# -----------------------------------
# Main execution
# -----------------------------------
if __name__ == "__main__":
    project_folder = "sample_project"
    docs = generate_documentation(project_folder)
    save_documentation(docs)
