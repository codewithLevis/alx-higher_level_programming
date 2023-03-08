#include "lists.h"

/**
 * insert_node - inserts a number into a sorted list
 * @head: head of list
 * @number: integer
 * Return: address of the added node else NULL
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *prev, *new, *current;

	if (head == NULL)
		return (NULL);

	new = malloc(sizeof(listint_t));

	if (new == NULL)
		return (NULL);

	new->n = number;
	prev = NULL;
	current = *head;

	for (; current != NULL && current->n < number;)
	{
		prev = current;
		current = current->next;
	}

	new->next = current;

	if (prev != NULL)
		prev->next = new;
	else
		*head = new;

	return (new);
}
