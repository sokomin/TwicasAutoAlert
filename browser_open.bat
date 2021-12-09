@echo off
FOR /F "usebackq delims== tokens=1,2" %%a IN ("config.txt") DO SET %%a=%%b
python twicas_alert_batch.py
rem 戻り値が1ならブラウザ起動
if %ERRORLEVEL% equ 1 (
    start chrome.exe "https://twitcasting.tv/%USER_ID%"
)