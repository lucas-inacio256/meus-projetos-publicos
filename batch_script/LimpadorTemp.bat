@echo off
cls

title Limpador de Arquivos Temporarios
color 2
:menu
time /t
date /t
echo ======================================================
echo =           Limpador de Arquivos Temporarios         =
echo ======================================================
echo =                                                    =
echo =            Escolha uma das opcoes abaixo           =
echo =                                                    =
echo ======================================================
echo =                                                    =
echo =            1: Excluir arquivos Temporaios          =
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
   rmdir C:\Windows\temp /s /q
   rmdir C:\Users\%USERNAME%\AppData\Local\Temp /s /q
   rmdir C:\Windows\Prefetch /s /q
   rmdir C:\Windows\SoftwareDistribution\Download /s /q
   cls

goto menu
:2
   exit
