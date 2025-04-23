def create_shortcut(app_name, vbs_name):
    shortcut_vbs = f"""Set WshShell = CreateObject("WScript.Shell")
Set FSO = CreateObject("Scripting.FileSystemObject")

desktop = WshShell.SpecialFolders("Desktop")
currentDir = FSO.GetParentFolderName(WScript.ScriptFullName)

Set shortcut = WshShell.CreateShortcut(desktop & "\\{app_name}.lnk")
shortcut.TargetPath = currentDir & "\\{vbs_name}"
shortcut.WorkingDirectory = currentDir
shortcut.WindowStyle = 1
shortcut.Save
    """

    with open("create_shortcut.vbs", "w", encoding="utf-8") as f:
        f.write(shortcut_vbs)

if __name__ == '__main__':
    app_name=input('Nome do app')
    vbs_name = input('nome do vbs')
    create_shortcut(app_name, vbs_name)