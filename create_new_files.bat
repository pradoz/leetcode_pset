@echo off
set /p problem_name=Enter Problem Name: 
subl py\%problem_name%.py
subl cpp\%problem_name%.cpp
echo %problem_name%.py
echo %problem_name%.cpp