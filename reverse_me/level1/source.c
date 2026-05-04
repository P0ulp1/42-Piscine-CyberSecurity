#include <string.h>
#include <stdio.h>
#include <stdlib.h>

int main(int ac, char **av)
{
    char input[10000];
    char *key = malloc(sizeof(char) * 14);

    strncpy(key, "__stack_check", 13);
    printf("Please enter key: ");
    scanf("%s", &input);

    if (strcmp(key, input)) {
        printf("Nope.\n");
    } else {
        printf("Good job.\n");
    }

    return (0);
}