# 1 : python check
$pythonCheck = Get-Command python3 -ErrorAction SilentlyContinue
if (-not $pythonCheck) {
    Write-Host "Python3 not installed. Please install it from: https://www.python.org/downloads/"
    Exit
}

# 2 : virtual environment
Write-Host "Setting up virtual environment..."
python3 -m venv venv
. .\venv\Scripts\Activate

# 3 : install requirements
Write-Host "Installing project requirements..."
pip install -r requirements.txt

# 4 : set working directory
Write-Host "Setting directory..."
Set-Location djangoProject

# 5 : database migrations
Write-Host "Running migrations..."
python manage.py migrate

# 6 : load example data
$loadData = Read-Host "(Optional) Load the example data? (y/n)"
if ($loadData -eq 'y' -or $loadData -eq 'Y') {

    # 6.1 : flush existing data (avoid duplication)
    $flushData = Read-Host "Flush database (y/n) (if this is a clean install, you can skip this)"
    if ($flushData -eq 'y' -or $flushData -eq 'Y') {
        Write-Host "Flushing database..."
        Start-Process python -ArgumentList "manage.py flush --no-input"
    }else{
        Write-Host "Warning, Load may fail due to existing database"
    }
    Write-Host "Loading example Data..."
    python manage.py loaddata fixtures/example_data.json
}

# 7 : admin access
$setupAdmin = Read-Host "(Optional) Set up admin access? (y/n)"
if ($setupAdmin -eq 'y' -or $setupAdmin -eq 'Y') {
    python manage.py createsuperuser
}

# 8 : run the server
Write-Host "Running the server..."
Start-Process python -ArgumentList "manage.py runserver"

# 9 : complete
Write-Host "Setup complete!"
