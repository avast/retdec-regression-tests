@echo off
cls
echo This is a sample batch file. Let me show you the list of files in the current directory:
echo.
echo -[*]- File List ----------------
for %%a in (*) do echo %%a
echo --------------------------------
