'VBScript to not show python application when running script so user doesn't know they're logging out

Set objShell = WScript.CreateObject("WScript.Shell")
objShell.Run("C:\asus-sign-out.bat"), 0, True
