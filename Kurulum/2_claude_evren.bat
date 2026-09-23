@echo off
chcp 65001 >nul
title CLAUDE CODE - EVREN
rem Bu ayarlar sadece bu pencere icin gecerli. Pencereyi kapatinca normal Pro kullanimina donersin.
set ANTHROPIC_API_KEY=
set ANTHROPIC_BASE_URL=http://localhost:4000
set ANTHROPIC_AUTH_TOKEN=evren-yerel
set ANTHROPIC_MODEL=glm-5.3
set ANTHROPIC_DEFAULT_OPUS_MODEL=glm-5.3
set ANTHROPIC_DEFAULT_SONNET_MODEL=glm-5.3
set ANTHROPIC_DEFAULT_HAIKU_MODEL=glm-5.3
set CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC=1
claude --model glm-5.3
