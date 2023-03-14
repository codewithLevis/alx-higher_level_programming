#include "lists.h"

/**
*is_palindrome - C that checks if a singly
*linked list is a palindrome
*@head: pointer to list
*Return: 1 or 0
*/
int is_palindrome(listint_t **head)
{
        int *arr_int, j, k, i;
        listint_t *ptr;

        ptr = *head;

        while ((*head) != NULL)
        {
                i++;
                *head = (*head)->next;
        }
        arr_int = malloc(sizeof(int) * (i + 1));

	if (arr_int == NULL)
		return (NULL);
        j = 0;
        ptr = *head;

        while (ptr != NULL)
        {
                arr_int[j] = ptr->n;

                ptr = ptr->next;
                j++;
        }
        i = 0;
        k = j;

        while (arr_int[i] && i < j / 2)
        {
                if (arr_int[i] != arr_int[k])
                        return (0);
                i++;
                k--;
        }
	free(arr_int);
        return (1);
}
