@echo off
title Esconde Arquivo
color 2

:menu
cls
time /t
date /t
echo ======================================================
echo =                 Esconde Arquivo                    =
echo ======================================================
echo =                                                    =
echo =            Escolha uma das opcoes abaixo           =
echo =                                                    =
echo ======================================================
echo =                                                    =
echo =            1: Esconde                              =
echo =            2: Desesconde                           =
echo =            3: Sair do Programa                     =
echo =                                                    =
echo ======================================================
echo =               By: Lucas Inacio                     =
echo ======================================================
echo.
echo.
echo.
echo.
set /p op=   Escolha sua opcao =^>

if %op% equ 1 goto Esconde
if %op% equ 2 goto Desesconde
if %op% equ 3 goto Sair

goto menu
:Esconde
   cls
   time /t
   date /t
   echo ======================================================
   echo =                  Esconde Arquivo                   =
   echo ======================================================
   echo =                                                    =
   echo =       Digite o caminho da pasta ou arquivo         =
   echo =           que o programa deve esconder.            =
   echo =                                                    =
   echo ======================================================
   echo =               By: Lucas Inacio                     =
   echo ======================================================
   echo.
   echo.
   echo.
   echo.
   set /p op=   Caminho =^>

   ATTRIB %op% +R +A +S +H
   cls

goto menu
:Desesconde
   cls
   time /t
   date /t
   echo ======================================================
   echo =                Desesconde Arquivo                  =
   echo ======================================================
   echo =                                                    =
   echo =       Digite o caminho da pasta ou arquivo         =
   echo =         que o programa deve desesconder.           =
   echo =                                                    =
   echo ======================================================
   echo =               By: Lucas Inacio                     =
   echo ======================================================
   echo.
   echo.
   echo.
   echo.
   set /p op=   Caminho =^>

   ATTRIB %op% -R -A -S -H
   cls

goto menu
:Sair
   exit
