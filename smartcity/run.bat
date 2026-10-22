@echo off
set PROJECT_NAME=SmartCity
title %PROJECT_NAME% Runner

:: Colors for better visibility (9=Light Blue, A=Light Green, C=Light Red)
color 0F

echo.
echo ============================================================
echo   %PROJECT_NAME% AUTOMATED RUNNER
echo ============================================================
echo.

:: [1/5] Check Python
echo [1/5] Checking Python installation...
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo.
    echo [ERROR] Python is not installed or not in PATH.
    echo Please install Python and try again.
    pause
    exit /b
)

:: [2/5] Virtual Environment Setup
echo [2/5] Setting up Virtual Environment...
if not exist venv (
    echo [INFO] Creating new virtual environment...
    python -m venv venv
    if %errorlevel% neq 0 (
        echo [ERROR] Failed to create virtual environment.
        pause
        exit /b
    )
) else (
    echo [INFO] Virtual environment found.
)

:: Activate venv
echo [INFO] Activating virtual environment...
call venv\Scripts\activate
if %errorlevel% neq 0 (
    echo [ERROR] Failed to activate virtual environment.
    pause
    exit /b
)

:: [3/5] Dependencies
echo [3/5] Installing/Updating dependencies (Speed Mode)...
python -m pip install --upgrade pip --quiet
pip install -r requirements.txt --quiet
if %errorlevel% neq 0 (
    echo [WARNING] Some dependencies failed to install. Please check requirements.txt.
)

:: [4/5] Database Migrations
echo [4/5] Syncing Database...
python manage.py makemigrations --noinput
python manage.py migrate --noinput

:: [5/5] Launch Server
echo [5/5] Launching SmartCity Platform...
echo.
echo ------------------------------------------------------------
echo   SERVER IS STARTING!
echo   Local Access: http://127.0.0.1:8000
echo   Admin Panel:  http://127.0.0.1:8000/admin
echo.
echo   [To stop the server, press Ctrl + C]
echo ------------------------------------------------------------
echo.

python manage.py runserver

if %errorlevel% neq 0 (
    echo.
    echo [CRITICAL] The server has stopped unexpectedly.
)

echo.
echo Execution finished. Press any key to exit this window.
pause >nul
