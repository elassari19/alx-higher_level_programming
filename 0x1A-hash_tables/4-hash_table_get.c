#include "hash_tables.h"

/**
 * hash_table_get - hash table get
 * @ht: ht
 * @key: key
 * Return: char
 */

char *hash_table_get(const hash_table_t *ht, const char *key)
{
	unsigned long int count;
	hash_node_t *pntr;

	if (ht == NULL)
		return (NULL);
	if (key == NULL)
		return (NULL);
	count = key_index((unsigned char *)key, ht->size);
	if (ht->array[count] == NULL)
		return (NULL);
	if (strcmp(ht->array[count]->key, key) == 0)
		return (ht->array[count]->value);
	pntr = ht->array[count];
	while (pntr != NULL)
	{
		if (strcmp(pntr->key, key) == 0)
			return (pntr->value);
		pntr = pntr->next;
	}
	return (NULL);
}
