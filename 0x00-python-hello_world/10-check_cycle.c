#include "lists.h"
/**
*check_cycle - checks for a loop/cycle in
*singly-linked list
*@list: list pointer
*Return: 0 if there is no cycle, 1 if there is a cycle
*/
int check_cycle(listint_t *list)
{
	listint_t *first, *second;

	if (!list)
		return (0);

	first = list->next, second = list;

	 while (first != NULL && first->next != NULL)
	{
		first = first->next->next, second = second->next;

		if (first == second)
			return (1);

	} 

	return (0);
}
