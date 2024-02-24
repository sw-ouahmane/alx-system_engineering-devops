#include "stdio.h"
#include "stdlib.h"
#include "unistd.h"

/**
 * infinite_while - runs an infinite loop to make the program sleep
 * Return: 0 in the end
*/
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - entry point of the program
 * Return: 0 on sucess
*/
int main(void)
{
	int count_procs = 0;
	pid_t pid;

	while (count_procs < 5)
	{
		pid = fork();
		if (!pid)
			break;
		printf("Zombie process created, PID: %i\n", (int)pid);
		count_procs++;
	}
	if (pid != 0)
		infinite_while();
	return (0);
}
