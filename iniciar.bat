@echo off
chcp 65001 >nul
title JT.IA - Assistente Pessoal Inteligente
cd /d "%~dp0"

echo ========================================================
echo        Iniciando JT.IA - Assistente Inteligente
echo ========================================================
echo.

if exist ".venv\Scripts\python.exe" (
    set "PYTHON_CMD=.venv\Scripts\python.exe"
) else (
    where py >nul 2>&1
    if %ERRORLEVEL% EQU 0 (
        set "PYTHON_CMD=py -3.12"
    ) else (
        set "PYTHON_CMD=python"
    )
)

echo Usando interpretador: %PYTHON_CMD%
echo.
"%PYTHON_CMD%" main.py %*

if %ERRORLEVEL% NEQ 0 (
    echo.
    echo ========================================================
    echo [AVISO] O aplicativo encerrou com o codigo %ERRORLEVEL%.
    echo Se faltar alguma dependencia, execute: python setup.py
    echo ========================================================
    pause
)
