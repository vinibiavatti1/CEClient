# Variables
$envPath = ".\.venv"
$activateFilePath = "$envPath\Scripts\Activate.ps1"

# Back
Set-Location ".."

# Activate Environment
Invoke-Expression $activateFilePath

# QRC update
Invoke-Expression "pyrcc5 -o src/qrc_resources.py resources/resources.qrc"

# Done
Write-Host "QRC updated successfully!"
Set-Location ".\scripts"
Read-Host -Prompt "Press Enter to exit"
