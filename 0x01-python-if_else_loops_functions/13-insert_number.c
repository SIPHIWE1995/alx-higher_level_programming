#include "lists.h"

/**
 * insert_node - function that adds number into sorted linked list
 * @head: header pointer
 * @number: inputted number
 * Return: funtion faills return null 
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *head, *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->num = number;

	if (node == NULL || node->num >= number)
	{
		new->next_node = node;
		*head = new;
		return (new);
	}

	while (node && node->next_node && node->next_node->num < number)
		node = node->next_node;

	new->next_node = node->next_node;
	node->next_node = new;

	return (new);
}
