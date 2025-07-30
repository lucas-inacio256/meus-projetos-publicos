@echo off
cls

title VirusScan
color 2

:menu
time /t
date /t
echo ======================================================
echo =                      VirusScan                     =
echo ======================================================
echo =                                                    =
echo =            Escolha uma das opcoes abaixo           =
echo =                                                    =
echo ======================================================
echo =                                                    =
echo =            1: Iniciar                              =
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
   C:\Windows\System32\MRT.exe
   cls

goto menu
:2
   exit
