#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <unistd.h>
#include <ctype.h>
#include <string.h>

#ifndef _BUF_SIZE_
#define BUF_SIZE 1024
#define FLAG_SIZE 3
#define LEN_ALPH 26
#endif



/**
 *decrypt_char - decrypts a char with a given shift key
 *lett: the character to be decrypted
 *key: the encryption key:
 *Return: the decrypted char
 */

char decrypt_char(char lett, int key)
{
	char *alph = "abcdefghijklmnopqrstuvwxyz";
	int i;

	if ('A' <= lett || lett <= 'Z')
		lett = tolower(lett);
	if ('a' > lett || 'z' < lett)
		return (lett);

	for (i = 0; *alph; i++)
	{
		if (lett == *(alph + i))
		{
			i = (i - key) % LEN_ALPH;
			return (alph[i]);
		}
	}
	return (lett);
}


/**
 *encrypt_char - encrypets a char with a given shift key
 *lett: the character to be encrypted
 *key: the encryption key:
 *Return: the encrypted char
 */

char encrypt_char(char lett, int key)
{
	char *alph = "abcdefghijklmnopqrstuvwxyz";
	int i;

	if ('A' <= lett || lett <= 'Z')
		lett = tolower(lett);
	if ('a' > lett || 'z' < lett)
		return (lett);

	for (i = 0; *alph; i++)
	{
		if (lett == *(alph + i))
		{
			i = ((i + key) % LEN_ALPH);
			return (alph[i]);
		}
	}
	return (lett);
}

/**
 * main - a program to receive a file
 * from the user and stores the caeser cipher of the text
 * in the filename of ceaser text
 * @argc: number of command line arguments
 * @argv: array of command line arguments
 * Return: Always (0)
 */


int main(int argc, char **argv)
{
	int inputFd, outputFd;
	char buffer[BUF_SIZE + 1];
	char *cipher_buf;
	ssize_t numRead;
	int len = 0, key = 3;
	char flag[FLAG_SIZE] = "-e";
	mode_t filePerms;

	if (argc < 3)
	{
		printf("Usage: %s\n", argv[0]);
		return (0);
	}

	if (argv[3] != NULL)
	{
		flag[0] = argv[3][0], flag[1] = argv[3][1];
		flag[2] = argv[3][2];
	}

	inputFd = open(argv[1], O_RDONLY);

	if (inputFd == -1)
	{
		printf("Unable to open the file %s\n", argv[1]);
		exit(97);
	}

	filePerms = (S_IRUSR | S_IWUSR | S_IWGRP | S_IRGRP | S_WOTH | S_ROTH);
	outputFd = open(argv[2], O_WRONLY | O_CREAT | O_TRUNC, filePerms);
	umask(0);

	if (outputFd == -1)
	{
		printf("Unable to open the file %s\n", argv[2]);
		exit(98);
	}

	while ((numRead = read(inputFd, buffer, BUF_SIZE)) > 0)
	{
		buffer[numRead] =  '\0';

		cipher_buf = malloc(sizeof(buffer));

		if (cipher_buf == NULL)
		{
			printf("Unable to allocate memory\n");
			exit(99);
		}

		len = 0;

		while (*(buffer + len) != '\0')
		{
			if (strcmp(flag, "-d") == 0)
				cipher_buf[len] = decrypt_char(buffer[len], key);
			else
				cipher_buf[len] = encrypt_char(buffer[len], key);
			len++;
		}

		write(outputFd, cipher_buf, numRead);
	}

	if (numRead == -1)
	{
		printf("Error:\n");
		exit(100);
	}

	if (close(inputFd) == -1)
		printf("Unable to close\n");
	if (close(outputFd) == -1)
		printf("Unable to close file\n");

	return (0);
}
