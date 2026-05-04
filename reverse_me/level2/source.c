#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

static void no(void) {
	printf("Nope.\n");
	exit(0);
}

static void yes(void) {
	printf("Good job.\n");
	exit(0);
}

int main(int ac, char **av)
{
	char input[10000];

	unsigned int uVar1;
	size_t sVar2;
	int iVar3;
	bool bVar4;
	char local_3d;
	char local_39[24];
	char local_21[9];
	unsigned int local_18;
	int local_14;
	int local_10;
	
	printf("Please enter key: ");
	local_10 = scanf("%23s", &local_39);
	// printf("LOCAL_10: [%d]\n", local_10);
	// printf("LOCAL_39: [%s]\n", local_39);
	// if (local_10 != 1)
	// 	no();
	// if (local_39[1] != '0')
	// 	printf("dkowajdowa");
	// 	no();
	// if (local_39[0] != '0')
	// 	printf("ddddd");
	// 	no();

	memset(local_21, 0, 9);
	local_21[0] = 'd';
	local_18 = 2;
	local_14 = 1;

	while (true) {
		sVar2 = strlen(local_21);
		uVar1 = local_18;
		bVar4 = false;
	
		if (sVar2 < 8) {
			sVar2 = strlen(local_39);
			bVar4 = uVar1 < sVar2;
		}
	
		if (!bVar4) {
			printf("EXITING BECAUSE: [%d] < [%d]\n", uVar1, sVar2);
			break;
		}
	
		local_3d = local_39[local_18];
		iVar3 = atoi(&local_3d);
		printf("iVar3: [%d]\n", iVar3);
		local_21[local_14] = (char)iVar3;
		local_18 = local_18 + 3;
		local_14 = local_14 + 1;
	}
	local_21[local_14] = '\0';

	printf("INPUT IS NOW: [%s]\n", local_21);
	iVar3 = strcmp(local_21, "delabere");


	if (iVar3 == 0) {
		yes();
	} else {
		printf("Quitting here.\n");
		no();
	}

	return (0);
}
