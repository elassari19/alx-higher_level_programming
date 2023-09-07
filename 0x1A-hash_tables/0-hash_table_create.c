#include "hash_tables.h"

/**
 * hash_table_create - hash table create
 * @size: size
 * Return: hash_table_t
 */

hash_table_t *hash_table_create(unsigned long int size)
{
	hash_table_t *hashT = malloc(sizeof(hash_table_t));

	if (hashT == NULL)
	{
		fprintf(stderr, "Error: malloc failed\n");
		return (NULL);
	}

	hashT->size = size;
	hashT->array = malloc(sizeof(hash_node_t *) * size);
	if (hashT->array == NULL)
	{
		fprintf(stderr, "Error: malloc failed\n");
		return (NULL);
	}

	for (unsigned int i = 0; i < size; i++)
		hashT->array[i] = NULL;

	return (hashT);
}
