from tkinter import Tk
from tkinter.filedialog import askopenfilename, askdirectory
import os


def criar_arquivos_exec():
    Tk().withdraw() 

    nome_script = askopenfilename()
    nome_script = os.path.basename(nome_script)
    print(f"Script selecionado: {nome_script}")

    diretorio_destino = askdirectory(title="Escolha o diretório para salvar os arquivos")

    # Se o usuário cancelar a escolha do diretório, retorna
    if not diretorio_destino:
        print("[✘] Diretório não selecionado.")
        return

    #.bat
    bat_content = f"""@echo off
cd /d "%~dp0"
call ".venv\\Scripts\\activate"
pythonw {nome_script}
    """
    
    #.vbs
    vbs_content = f"""Set WshShell = CreateObject("WScript.Shell")
Set objFSO = CreateObject("Scripting.FileSystemObject")
currentDir = objFSO.GetParentFolderName(WScript.ScriptFullName)
batFilePath = currentDir & "\\{os.path.splitext(nome_script)[0]}.bat"
WshShell.Run Chr(34) & batFilePath & Chr(34), 0, False
    """


    bat_file_path = os.path.join(diretorio_destino, f"{os.path.splitext(nome_script)[0]}.bat")
    vbs_file_path = os.path.join(diretorio_destino, f"{os.path.splitext(nome_script)[0]}.vbs")

    with open(bat_file_path, "w", encoding="utf-8") as bat_file:
        bat_file.write(bat_content)

    with open(vbs_file_path, "w", encoding="utf-8") as vbs_file:
        vbs_file.write(vbs_content)

    print(f"[✓] Arquivos '{bat_file_path}' e '{vbs_file_path}' criados.")

if __name__ == '__main__':
    criar_arquivos_exec()
