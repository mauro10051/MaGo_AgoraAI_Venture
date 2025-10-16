import os

# Struttura base del progetto MaGo AgoraAI Venture
structure = {
    "agents": [
        "strategist.py",
        "sociologist.py",
        "engineer.py",
        "financier.py"
    ],
    "core": [
        "orchestrator.py",
        "memory.py",
        "prompts.py",
        "utils.py"
    ],
    "interface": [
        "ui_main.py",
        "cli_main.py",
        "web/app.py"
    ],
    "data": [
        "examples/BP_Orto_per_Ristorazione/.keep",
        "examples/FP_Orto_per_Ristorazione/.keep",
        "templates/feasibility_template.json",
        "templates/businessplan_template.json"
    ],
    "docs": [
        "README_Guida_Minima.pdf",
        "architecture_overview.md",
        "changelog.md"
    ],
    "resources": [
        "icons/.keep",
        "banners/.keep"
    ],
    "tests": [
        "test_agents.py",
        "test_core.py",
        "test_interface.py"
    ]
}

base_files = [
    "requirements.txt",
    "setup.py",
    "main.py"
]

# Funzione per creare cartelle e file
def create_project_structure():
    print("🧠 Creazione struttura progetto MaGo AgoraAI Venture...\n")

    for folder, files in structure.items():
        os.makedirs(folder, exist_ok=True)
        for file in files:
            path = os.path.join(folder, file)
            # Crea sottocartelle se necessario
            os.makedirs(os.path.dirname(path), exist_ok=True)
            # Crea file vuoti (o con commento iniziale)
            if not os.path.exists(path):
                with open(path, "w", encoding="utf-8") as f:
                    if file.endswith(".py"):
                        f.write(f"# {file} – modulo del progetto MaGo AgoraAI Venture\n")
                    elif file.endswith(".md"):
                        f.write(f"# {file}\n\nDocumentazione del progetto MaGo AgoraAI Venture.\n")
                    elif file.endswith(".json"):
                        f.write("{}")
                    elif file == ".keep":
                        pass
                print(f"✅ Creato: {path}")

    for file in base_files:
        if not os.path.exists(file):
            with open(file, "w", encoding="utf-8") as f:
                if file == "main.py":
                    f.write(
                        'if __name__ == "__main__":\n'
                        '    print("🧠 MaGo AgoraAI Venture – Framework multi-agente avviato con successo.")\n'
                    )
                elif file == "requirements.txt":
                    f.write("# Dipendenze Python principali\n")
                    f.write("gradio\nollama\nopenai\n")
                elif file == "setup.py":
                    f.write(
                        'from setuptools import setup, find_packages\n\n'
                        'setup(\n'
                        '    name="MaGo_AgoraAI_Venture",\n'
                        '    version="1.0",\n'
                        '    packages=find_packages(),\n'
                        '    install_requires=["gradio", "openai", "ollama"],\n'
                        '    author="Mauro Maiandi",\n'
                        '    description="Framework multi-agente per piani di fattibilità e business plan",\n'
                        ')\n'
                    )
                print(f"✅ Creato: {file}")

    print("\n🎉 Struttura creata con successo! Puoi ora iniziare a sviluppare i moduli.")

if __name__ == "__main__":
    create_project_structure()
Add setup_structure.py to auto-generate project folders
