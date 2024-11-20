# this file manually runs the script that starts the file
# i found an easier way to run it. this file is not necessary any more

# Navigate to the scripts directory and activate the virtual environment
& "C:\Users\calis\24-25_CE201-col_team02\24-25_CE201-col_team02\backendTest\venv\Scripts\Activate.ps1"

# Navigate back to the root directory of your project
Set-Location -Path "C:\Users\calis\24-25_CE201-col_team02\24-25_CE201-col_team02\backendTest"

# Run Flask app
flask run

# website available at : 127.0.0.1:5000