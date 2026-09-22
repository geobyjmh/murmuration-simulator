@echo off
setlocal

where py >nul 2>nul
if %errorlevel%==0 (
    py -m pip install -r requirements.txt
) else (
    python -m pip install -r requirements.txt
)

if %errorlevel% neq 0 (
    echo Failed to install Pygame.
    exit /b %errorlevel%
)

echo Pygame installed successfully.
pause
