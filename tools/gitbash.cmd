@echo off
setlocal

REM Run a single Git Bash command from Windows cmd.exe.
REM This avoids accidental routing through WSL relays when invoking `bash`.

set "BASH=C:\Program Files\Git\usr\bin\bash.exe"
if not exist "%BASH%" set "BASH=C:\Program Files\Git\bin\bash.exe"

if not exist "%BASH%" (
  echo ERROR: Git Bash not found. Expected at:
  echo   C:\Program Files\Git\usr\bin\bash.exe
  echo   C:\Program Files\Git\bin\bash.exe
  exit /b 1
)

if "%~1"=="" (
  echo Usage: tools/gitbash.cmd "<bash command>"
  exit /b 2
)

if "%GITBASH_DEBUG%"=="1" (
  echo [GITBASH_DEBUG] exe=%BASH%
  echo [GITBASH_DEBUG] cmd=%~1
)

"%BASH%" -lc "%~1"
