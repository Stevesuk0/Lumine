@echo off

echo Packing portable version...
pyinstaller --icon=App.ico src/lumine.py --uac-admin -w