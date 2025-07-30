#include<stdio.h>

int main(){

    FILE *archive;

    char a=97, b=2, c=3, d=4, e=5, f=6;
    int n, p, i;
    int counter = 0;

    archive = fopen("generator.c", "w");

    printf("This program write a program for calculate all combination of n elements in p groups.\n");
    printf("Value for n: ");
    scanf("%d", &n);

    printf("Value for p (p<=25): ");
    scanf("%d", &p);

    fprintf(archive, "#include<stdio.h>\n");
    fprintf(archive, "int main () {\n");
    fprintf(archive, "FILE *archive;\n");
    fprintf(archive, "int ");

    for(i = 1; i <= p; i++) {
        fprintf(archive, "%c=%d", 96+i, i);

        if(i!=p) {
            fprintf(archive, ",");
        } else {
            fprintf(archive, ";\n");
        }
    }

    fprintf(archive, "int ");

    for(i = 1; i <= p; i++) {
        fprintf(archive,"%c%c=%d",96+i,96+i,0);

        if(i!=p){
            fprintf(archive, ",");
        } else {
            fprintf(archive, ";\n");
        }
    }

    fprintf(archive, "int counter=0;\n");

    fprintf(archive, "archive=fopen(\"list.txt\",\"w\" ); \n");

    for(i = 1; i <= p; i++) {
        if(i == 1) {
            fprintf(archive, "for(a=1;a<=%d;a++){ \n", n-p+1);
        }

        if(i != 1 && i != p) {
            fprintf(archive, "for(%c=%c%c+1+%c;%c<=%d;%c++){ \n", 96+i, 96+i, 96+i, 96+i-1, 96+i, n-p+1+i, 96+i);
        }

        if(i == p) {
            fprintf(archive, "for(%c=%c+1;%c<=%d;%c++){\n", 96+i, 96+i-1, 96+i, n, 96+i );
            fprintf(archive, "fprintf(archive,\"");

            for(i = 1; i <= p; i++) {
                if (i+1 > p) {
                    fprintf(archive, "\%%d");
                } else {
                    fprintf(archive, "\%%d ");
                }
            }

            fprintf(archive, "\\n\" ");

            for(i = 1; i <= p; i++) {
                fprintf(archive, ",%c",96+i);
            }

            fprintf(archive, ");} \n");
            }
    }

    for(i = p; i > 1; i--) {
        fprintf(archive, " if(%c==%d){%c%c++;} \n }", 96+i, 55+i, 96+i-1, 96+i-1);
    }

    fprintf(archive, "\n }");
    printf("\nCompleted!");

    fclose(archive);
    return(0);
}
