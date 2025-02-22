# Script written for windows
if ($IsWindows) {
    Write-Host "[0/9] Starting Setup..."
}else{
    Exit
}

# python check
Write-Host "[1/9] Checking Python installation..."
$pythonCommand = $null
if     (Get-Command python3 -ErrorAction SilentlyContinue)  {$pythonCommand = "python3"}
elseif (Get-Command python  -ErrorAction SilentlyContinue)  {$pythonCommand = "python"}
elseif (Get-Command py      -ErrorAction SilentlyContinue)  {$pythonCommand = "py"}
else {
    Write-Host "[1/9] Python is not installed. Please install it from: https://www.python.org/downloads/"
    Exit
}
Write-Host "[1/9] Using $pythonCommand" (& $pythonCommand --version)

# virtual environment
Write-Host "[2/9] Setting up virtual environment..."
# deactivate virtual environment if currently in one
if ($env:VIRTUAL_ENV) {
    if (Get-Command deactivate -ErrorAction SilentlyContinue) {
        Write-Host "[2/9] Deactivating current virtual environment..."
        deactivate
    }
}
Set-Location (Split-Path $MyInvocation.MyCommand.Path) # set location to wherever this file is
& $pythonCommand -m venv venv
Write-Host "[2/9] Activating virtual environment..."
& .\venv\Scripts\Activate
$venvPythonCmd = ".\venv\Scripts\python.exe"
$venvPython = "..\.\venv\Scripts\python.exe"

# install requirements
Write-Host "[3/9] Installing project requirements..."
& $venvPythonCmd "-m" pip install "-r" ".\\requirements.txt"

# set working directory
Write-Host "[4/9] Setting directory..."
Set-Location djangoProject

# database migrations
Write-Host "[5/9] Running database migrations..."
& $venvPython manage.py migrate

# load example data
$loadData = Read-Host "[6/9] (Optional) Load the example data? (y/n)"
if ($loadData -match "^[yY]$") {

    # 6.1 : flush existing data (if needed)
    $flushData = Read-Host "[6/9] Flush the database to avoid possible duplicate errors? (y/n)"
    if ($flushData -match "^[yY]$") {
        Write-Host "[6/9] Flushing database..."
        & $venvPython manage.py flush --no-input
    }
    Write-Host "[6/9] Loading example Data..."
    & $venvPython manage.py loaddata fixtures/example_data.json
}

# admin access
$setupAdmin = Read-Host "[7/9] (Optional) Set up admin access? (y/n)"
if ($setupAdmin -match "^[yY]$") {
    & $venvPython manage.py createsuperuser
}

# complete
Write-Host "[8/9] Setup complete!"

# run the server
Write-Host "[9/9] Starting the server..."
Start-Process -NoNewWindow -FilePath $venvPython -ArgumentList "manage.py", "runserver"
