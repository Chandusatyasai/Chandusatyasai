@echo off
echo ========================================
echo   Portfolio Deployment Helper
echo ========================================
echo.

echo Checking if Git is installed...
git --version >nul 2>&1
if %errorlevel% neq 0 (
    echo.
    echo [ERROR] Git is not installed!
    echo.
    echo Please install Git first:
    echo 1. Download from: https://git-scm.com/download/win
    echo 2. Install with default settings
    echo 3. Restart this script
    echo.
    echo OR use GitHub Desktop instead:
    echo Download: https://desktop.github.com/
    echo.
    pause
    exit /b 1
)

echo [OK] Git is installed!
echo.

echo ========================================
echo   Deployment Steps
echo ========================================
echo.
echo 1. First, create a repository on GitHub:
echo    - Go to: https://github.com/new
echo    - Name it: portfolio
echo    - Make it PUBLIC
echo    - Click "Create repository"
echo.
echo 2. Then come back here and press any key...
pause
echo.

set /p GITHUB_USERNAME="Enter your GitHub username: "
set /p REPO_NAME="Enter repository name (default: portfolio): "
if "%REPO_NAME%"=="" set REPO_NAME=portfolio

echo.
echo Initializing Git...
git init

echo.
echo Adding files...
git add index.html styles.css script.js README.md DEPLOY.md GITHUB_DEPLOY_GUIDE.md

echo.
echo Creating commit...
git commit -m "Initial commit: Professional portfolio website"

echo.
echo Adding remote repository...
git remote add origin https://github.com/%GITHUB_USERNAME%/%REPO_NAME%.git

echo.
echo Setting main branch...
git branch -M main

echo.
echo ========================================
echo   Ready to Push!
echo ========================================
echo.
echo Next steps:
echo 1. You'll be asked for GitHub credentials
echo 2. Use a Personal Access Token (not password)
echo    Get one at: https://github.com/settings/tokens
echo 3. After pushing, enable GitHub Pages:
echo    - Go to: https://github.com/%GITHUB_USERNAME%/%REPO_NAME%/settings/pages
echo    - Source: main branch, / (root) folder
echo    - Click Save
echo.
pause

echo.
echo Pushing to GitHub...
git push -u origin main

if %errorlevel% equ 0 (
    echo.
    echo ========================================
    echo   SUCCESS! 
    echo ========================================
    echo.
    echo Your portfolio is being deployed!
    echo.
    echo Next: Enable GitHub Pages:
    echo https://github.com/%GITHUB_USERNAME%/%REPO_NAME%/settings/pages
    echo.
    echo Your site will be live at:
    echo https://%GITHUB_USERNAME%.github.io/%REPO_NAME%/
    echo.
) else (
    echo.
    echo [ERROR] Push failed!
    echo.
    echo Common issues:
    echo - Wrong username or repository name
    echo - Need to use Personal Access Token
    echo - Repository doesn't exist yet
    echo.
    echo Try manual upload via GitHub website instead.
    echo.
)

pause

