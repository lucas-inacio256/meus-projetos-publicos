@echo off
cls

title BugScan
color 2

:menu
time /t
date /t
echo ======================================================
echo =                     BugScan                        =
echo ======================================================
echo =                                                    =
echo =            Escolha uma das opcoes abaixo           =
echo =                                                    =
echo ======================================================
echo =                                                    =
echo =            1: Veriicar sistema                     =
echo =            2: Sair do Programa                     =
echo =                                                    =
echo ======================================================
echo =               By: Lucas Inacio                     =
echo ======================================================
echo.
echo.
echo.
echo.
set /p op=   Escolha sua opcao =^>

if %op% equ 1 goto 1
if %op% equ 2 goto 2

goto menu
:1
   sfc /scannow
   cls

goto menu
:2
   exit
