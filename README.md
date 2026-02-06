# 📘 DocGen – Automatic Documentation Generator Agent

DocGen is a Python-based documentation generator agent that automatically
analyzes source code and produces structured Markdown documentation.

---

## 🎯 Problem Statement
Maintaining documentation manually is time-consuming and error-prone.
DocGen solves this by acting as an autonomous agent that reads source code
and generates up-to-date documentation without human intervention.

---

## ⚙️ How It Works
1. Scans the project directory
2. Parses Python source files using AST
3. Extracts classes and functions
4. Reads docstrings
5. Generates structured Markdown documentation

---

## ▶️ How to Run
```bash
python src/docgen.py
```

---

## 📂 Project Structure
```
Documentation-Generator-Agent/
├── src/
│   └── docgen.py
├── sample_project/
│   ├── calculator.py
│   └── text_tools.py
├── docs/
│   └── DOCUMENTATION.md
├── screenshots/
├── README.md
├── requirements.txt
└── .gitignore
```

---

## 📸 Screenshots

### Running the Documentation Generator
![Run Output](screenshots/run_output.png)

### Generated Documentation Output
![Generated Documentation](screenshots/generated_documentation.png)

---

## 🧠 Agent Behavior
- **Goal**: Generate documentation automatically
- **Input**: Source code directory
- **Output**: Markdown documentation
- **Autonomy**: Runs without user interaction

---

## 🚀 Use Cases
- Project documentation
- Codebase understanding
- Developer onboarding
- Hackathon demonstrations

---

## 📄 License
Free to use for academic and learning purposes.
