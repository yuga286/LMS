@echo off
if "%1"=="venv" (
    python -m venv %2
) else (
    echo The command '%1' is not recognized.
)
