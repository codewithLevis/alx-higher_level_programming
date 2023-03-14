#include "lists.h"

int real_palindrome(int *arr, int len);

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

	i = 0;
	while (ptr != NULL)
	{
		i++;
		ptr = ptr->next;
	}
	arr_int = malloc(sizeof(int) * i);

	if (arr_int == NULL)
		return (0);
	j = 0;
	ptr = *head;

	while (ptr != NULL)
	{
		arr_int[j] = ptr->n;

		ptr = ptr->next;
		j++;
	}

	return (real_palindrome(arr_int, j - 1));
}

/**
*real_palindrome - check for palindrome
*@arr: pointer array of ints
*@len: position to the end of array
*Return: 0 or 1
*/
int real_palindrome(int *arr, int len)
{
	int i, j;

	for(i = 0, j = len; i < j; i++, j--)
	{
		if (arr[i] != arr[j])
		{
			free(arr);
			return (0);
		}
	}
	free(arr);
	return (1);
}
