from pathlib import Path
import zipfile
import shutil

project_name = "ticket_agent_github"

files = {
    "app.py": '''from fastapi import FastAPI

app = FastAPI(title="Ticket Agent")

@app.get("/")
def root():
    return {"message": "Ticket Agent is running"}
''',

    "requirements.txt": '''fastapi==0.115.0
uvicorn==0.30.6
''',

    "README.md": '''# Ticket Agent

A simple FastAPI project for GitHub.
''',

    ".gitignore": '''__pycache__/
*.pyc
*.db
venv/
.venv/
''',
}

def create_project(root: Path):
    if root.exists():
        shutil.rmtree(root)
    root.mkdir(parents=True, exist_ok=True)

    for file_name, content in files.items():
        file_path = root / file_name
        file_path.parent.mkdir(parents=True, exist_ok=True)
        file_path.write_text(content, encoding="utf-8")

def zip_project(folder: Path, zip_name: str):
    zip_path = Path(zip_name)
    if zip_path.exists():
        zip_path.unlink()

    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zf:
        for path in folder.rglob("*"):
            zf.write(path, arcname=path.relative_to(folder.parent))

if __name__ == "__main__":
    root = Path(project_name)
    zip_name = f"{project_name}.zip"

    create_project(root)
    zip_project(root, zip_name)

    print(f"项目目录已生成: {root.resolve()}")
    print(f"压缩包已生成: {Path(zip_name).resolve()}")
