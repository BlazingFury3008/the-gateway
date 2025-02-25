@echo off
cd /d "%~dp0src"
uvicorn main:app --host 0.0.0.0 --port 8000 --reload --log-level debug
