@echo off
title Semiconductor Final Exam Learning Portal
cd /d "%~dp0"
echo =====================================================================
echo    Launching Semiconductor Specialty Chemicals Final Exam Portal...
echo =====================================================================
python server.py
if %ERRORLEVEL% NEQ 0 (
    echo [ERROR] Python not found or failed to start.
    echo Please ensure Python is installed and added to PATH.
    pause
)
