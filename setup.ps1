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

# 4 : database migrations
Write-Host "Running migrations..."
python manage.py migrate

# 5 : admin access
$setupAdmin = Read-Host "(Optional) Set up admin access? (y/n)"
if ($setupAdmin -eq 'y' -or $setupAdmin -eq 'Y') {
    python manage.py createsuperuser
}

# 6 : run the server
Write-Host "Running the server..."
Start-Process python -ArgumentList "manage.py runserver"

# 7 : load example data
$loadData = Read-Host "(Optional) Load the example data? (y/n)"
if ($loadData -eq 'y' -or $loadData -eq 'Y') {
    python manage.py loaddata fixtures/example_data.json
}

Write-Host "Setup complete!"
