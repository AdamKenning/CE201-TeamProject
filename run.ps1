## deactivate virtual environment if currently in one
if ($env:VIRTUAL_ENV) {
    if (Get-Command deactivate -ErrorAction SilentlyContinue) {
        Write-Host "[0/4] Deactivating current virtual environment..."
        deactivate
    }
}
Write-Host "[1/4] Checking Python installation..."
$pythonCommand = $null
if     (Get-Command python3 -ErrorAction SilentlyContinue)  {$pythonCommand = "python3"}
elseif (Get-Command python  -ErrorAction SilentlyContinue)  {$pythonCommand = "python"}
elseif (Get-Command py      -ErrorAction SilentlyContinue)  {$pythonCommand = "py"}
else {
    Write-Host "[1/4] Python is not installed. Please install it from: https://www.python.org/downloads/"
    Exit
}

Write-Host "[2/3] Activating virtual environment..."
set-Location (Split-Path $MyInvocation.MyCommand.Path) # set location to wherever this file is
& $pythonCommand -m venv venv
& .\venv\Scripts\Activate
$venvPython = "..\.\venv\Scripts\python.exe"

Set-Location djangoProject
Write-Host "[3/4] Applying Migrations..."
& $venvPython manage.py migrate

Write-Host "[4/4] Starting the Server..."
Start-Process -NoNewWindow -FilePath $venvPython -ArgumentList "manage.py", "runserver"
