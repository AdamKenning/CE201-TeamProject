## deactivate virtual environment if currently in one
if ($env:VIRTUAL_ENV) {
    deactivate
}
Write-Host "[1/3] Starting Virtual Environment..."
set-Location (Split-Path $MyInvocation.MyCommand.Path) # set location to wherever this file is
. .\venv\Scripts\Activate
Set-Location djangoProject
Write-Host "[2/3] Applying Migrations..."
python manage.py migrate *> $null
Write-Host "[3/3] Starting the Server..."
python manage.py runserver