@echo off
cls

color 2
title Desligar PC
:menu
time /t
date /t
echo ======================================================
echo =                     Desligar PC                    =
echo ======================================================
echo =                                                    =
echo =         Escolha uma das opcoes abaixo              =
echo =                                                    = 
echo ======================================================
echo =                                                    =
echo =            1: Desliga em 5s                        =
echo =            2: Enterrompe o Desligamento            =
echo =            3: Sair do Console                      =
echo =                                                    =
echo ======================================================
echo =               By: Lucas Inacio                     =
echo ======================================================
echo.
echo.
echo.
echo.
set /p opcao=   Escolha sua opcao =^>

if %opcao% equ 1 goto 1
if %opcao% equ 2 goto 2
if %opcao% equ 3 goto 3

goto menu
:1
   shutdown -s -t 5
   msg * /time 1 Desligando em 5
   msg * /time 1 Desligando em 4
   msg * /time 1 Desligando em 3
   msg * /time 1 Desligando em 2
   msg * /time 1 Desligando em 1
   msg * /time 1 Desligando...
   cls

goto menu
:2
   shutdown -a
   msg * /time 2 Desligamento enterrompido.
   cls

goto menu
:3
   exit
