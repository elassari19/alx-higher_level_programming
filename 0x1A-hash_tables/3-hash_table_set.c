#include "hash_tables.h"

/**
 * free_node - free node
 * @node: node
 * Return: void
 */

void free_node(hash_node_t *node)
{
	free(node->key);
	free(node->value);
	free(node);
}

/**
 * hash_table_set - hash table set
 * @ht: ht
 * @key: key
 * @value: value
 * Return: int
 */

int hash_table_set(hash_table_t *ht, const char *key, const char *value)
{
	unsigned long int pointer;
	hash_node_t *new_node, *stage;

	if (strcmp(key, "") == 0 || key == NULL || ht == NULL)
		return (0);
	pointer = key_index((const unsigned char *)key, ht->size);
	new_node = malloc(sizeof(hash_node_t));
	if (new_node == NULL)
		return (0);
	new_node->key = strdup((char *)key);
	new_node->value = strdup((char *)value);
	new_node->next = NULL;
	if (ht->array[pointer] == NULL)
		ht->array[pointer] = new_node;
	else
	{
		stage = ht->array[pointer];
		if (strcmp(stage->key, key) == 0)
		{
			new_node->next = stage->next;
			ht->array[pointer] = new_node;
			free_node(stage);
			return (1);
		}
		while (stage->next != NULL && strcmp(stage->next->key, key) != 0)
		{ stage = stage->next;
		}
		if (strcmp(stage->key, key) == 0)
		{
			new_node->next = stage->next->next;
			free_node(stage->next);
			stage->next = new_node;
		}
		else
		{
			new_node->next = ht->array[pointer];
			ht->array[pointer] = new_node;
		}
	}
	return (1);
}
