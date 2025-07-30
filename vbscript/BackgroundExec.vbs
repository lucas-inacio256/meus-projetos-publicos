'Executa programa em segundo plano
'Deve passar o caminho do programa em "PATH"

Set Shell = WScript.CreateObject("WScript.Shell")
Shell.Run "PATH", 0, True
