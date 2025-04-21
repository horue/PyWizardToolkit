from tkinter import Tk
from tkinter.filedialog import askdirectory
import subprocess
import os

def generate_requirements():
    Tk().withdraw()
    
    projeto_dir = askdirectory(title="Escolha o diretório do projeto (contendo o venv)")
    if not projeto_dir:
        print("[✘] Diretório do projeto não selecionado.")
        return
    
    venv_dir = os.path.join(projeto_dir, ".venv", "Scripts", "pip.exe")

    if not os.path.exists(venv_dir):
        print("[✘] Ambiente virtual não encontrado no diretório selecionado ou venv não está configurado corretamente.")
        return
    
    diretorio_destino = askdirectory(title="Escolha o diretório para salvar o requirements.txt")
    if not diretorio_destino:
        print("[✘] Diretório de destino não selecionado.")
        return

    requirements_path = os.path.join(diretorio_destino, "requirements.txt")

    with open(requirements_path, "w") as req:
        subprocess.run([venv_dir, "freeze"], stdout=req)

    print(f"[✓] Arquivo 'requirements.txt' gerado em {requirements_path}.")


generate_requirements()
