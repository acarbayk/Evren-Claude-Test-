@echo off
chcp 65001 >nul
title EVREN PROXY - bu pencereyi kapatma
cd /d "%~dp0"
set PYTHONUTF8=1
set LITELLM_USE_CHAT_COMPLETIONS_URL_FOR_ANTHROPIC_MESSAGES=true
if "%EVREN_API_KEY%"=="" (
  echo EVREN_API_KEY bulunamadi. Anahtarini yapistir ve Enter a bas:
  set /p EVREN_API_KEY=
)
echo.
echo EVREN proxy baslatiliyor: http://localhost:4000
echo "Uvicorn running" yazisini gorunce 2_claude_evren.bat dosyasini ac.
echo.
python -m litellm.proxy.proxy_cli --config evren_config.yaml --port 4000
pause
