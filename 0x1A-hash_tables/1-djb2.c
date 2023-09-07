#include "hash_tables.h"

/**
 * hash_djb2 - hash djb2
 * @str: str
 * Return: long int
 */

unsigned long int hash_djb2(const unsigned char *str)
{
	unsigned long int hashdjb2;
	int character;

	hashdjb2 = 5381;
	while ((character = *str++))
	{
		hashdjb2 = ((hashdjb2 << 5) + hashdjb2) + character;
	}
	return (hashdjb2);
}
