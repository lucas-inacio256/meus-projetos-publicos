#include <stdio.h>
#include <stdlib.h>
#include <string.h>



void sleep(int secs)
{
    /*
    Pausa o programa por tempo determinado.
    */

    char secsf[] = "";
    itoa(secs+1, secsf, 10);

    char command[1000] = "";
    strcat(command, "ping 127.0.0.1 -n ");
    strcat(command, secsf);
    strcat(command, " >nul");

    system(command);
}



void jumpL(int num)
{
    /*
    Pula um determinado numero de linhas no console se (num > 0).
    */

    for (int n = 0; n != num; n++) printf("\n");
}



void menu(char msg[], int num)
{
    /*
    Cria um menu no console.
    Tamanho: <num>

    ===========
       <msg>
    ===========
    */

    for (int n = 0; n != num; n++) printf("=");
    printf("\n");
    for (int n = 0; n != (num-strlen(msg))/2; n++) printf(" ");
    printf("%s", msg);
    for (int n = 0; n != (num-strlen(msg))/2; n++) printf(" ");
    printf("\n");
    for (int n = 0; n != num; n++) printf("=");
}



void option(char msg[], char opt)
{
    /*
    Cria opções no console.
    */

    printf("[ %c ] - %s", opt, msg);
}



void input(char msg[], char type[], int varPoint)
{
    /*
    Solicita que o usuario insira algo e
    retorna o que foi digitado para o endereço <varPoint>
    */

    printf(type, msg);
    scanf(type, varPoint);
    getchar();
}



int startswith(char string[], char stringCmp[])
{
    /*
    Verifica se <string> começa com <stringCmp>
    <0 = não, 1 = sim>.
    */

    int boolean=1;
    for (int n=0; stringCmp[n]; n++)
    {
        if (string[n] != stringCmp[n])
        {
            boolean=0;
        }
    }
    return boolean;
}



int strINstr(char string[], char stringCmp[])
{
    /*
    Verifica se existe <string> em <stringCmp>
    e retorna quantas vezes apareceu <ins>.
    */

    int count=0, a=0, ins=0;
    for (int n=0; stringCmp[n]; n++)
    {
        if (string[a] == stringCmp[n])
        {
            count++;
            a++;
            if (count == strlen(string)) ins++;
        }
        else count=0, a=0;
    }
    return ins;
}



unsigned long int factorial(int num)
{
    if (num != 0 && num != 1)
    {
        unsigned long int result = num;
        for (int n = num-1; n >= 2; n--) result *= n;
        return result;
    }
    else return 1;
}
