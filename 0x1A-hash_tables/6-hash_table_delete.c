#include "hash_tables.h"

/**
 * hash_table_delete - hashtabledelete
 * @ht: ht
 */

void hash_table_delete(hash_table_t *ht)
{
	unsigned long int counter = 0;
	hash_node_t *node;

	while (counter < ht->size)
	{
		while (ht->array[counter] != NULL)
		{
			node = ht->array[counter]->next;
			free(ht->array[counter]->key);
			free(ht->array[counter]->value);
			free(ht->array[counter]);
			ht->array[counter] = node;
		}
		counter++;
	}
	free(ht->array);
	free(ht);
}
