@echo off
REM Neuronix Setup Script for Windows
REM This script helps you configure API keys and set up Neuronix

setlocal enabledelayedexpansion

echo.
echo ==============================================================================
echo                    NEURONIX SETUP - Windows Edition
echo ==============================================================================
echo.

python setup.py

if errorlevel 1 (
    echo.
    echo ERROR: Python is not installed or setup.py failed
    echo Please make sure Python 3.10+ is installed and available in PATH
    pause
    exit /b 1
)

echo.
echo Setup complete! Press any key to exit...
pause
