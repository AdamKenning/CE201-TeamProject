# python check
Write-Host "[1/9] Checking Python installation"
$pythonCheck = Get-Command python3 -ErrorAction SilentlyContinue
if (-not $pythonCheck) {
    Write-Host "[1/9] Python3 not installed. Please install it from: https://www.python.org/downloads/"
    Exit
}

# virtual environment
Write-Host "[2/9] Setting up virtual environment..."
python3 -m venv venv
. .\venv\Scripts\Activate

# install requirements
Write-Host "[3/9] Installing project requirements..."
pip install -r requirements.txt

# set working directory
Write-Host "[4/9] Setting directory..."
Set-Location djangoProject

# database migrations
Write-Host "[5/9] Running database migrations..."
python manage.py migrate

# load example data
$loadData = Read-Host "[6/9] (Optional) Load the example data? (y/n)"
if ($loadData -eq 'y' -or $loadData -eq 'Y') {

    # 6.1 : flush existing data (if needed)
    $flushData = Read-Host "[6/9] Flush the database to avoid possible duplicate errors? (y/n)"
    if ($flushData -eq 'y' -or $flushData -eq 'Y') {
        Write-Host "[6/9] Flushing database..."
        python manage.py migrate
    }
    Write-Host "[6/9] Loading example Data..."
    python manage.py loaddata fixtures/example_data.json
}

# admin access
$setupAdmin = Read-Host "[7/9] (Optional) Set up admin access? (y/n)"
if ($setupAdmin -eq 'y' -or $setupAdmin -eq 'Y') {
    python manage.py createsuperuser
}

# run the server
Write-Host "[8/9] Starting the server..."
Start-Process python -ArgumentList "manage.py runserver"

# 9 : complete
Write-Host "[9/9] Setup complete!"
