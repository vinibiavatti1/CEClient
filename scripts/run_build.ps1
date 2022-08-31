# Back
Set-Location ".."

# Build
Invoke-Expression ".\.venv\Scripts\python.exe build.py"

# Done
Set-Location ".\scripts"
Read-Host -Prompt "Press Enter to exit"
