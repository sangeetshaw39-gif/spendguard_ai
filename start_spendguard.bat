@echo off
TITLE SpendGuard AI Startup

echo =========================================
echo       Starting SpendGuard AI
echo =========================================
echo.

echo Checking and installing dependencies...
python -m pip install -r requirements.txt

echo.
echo Starting the application server...
python main.py

pause
