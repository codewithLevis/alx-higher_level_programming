#include "lists.h"
#define ARR_LEN(n) n

int real_palindrome(int *arr, int len);

/**
*len_list - finds len of list
*@head: start of list
*Return: len
*/
int len_list(listint_t **head)
{
	listint_t *ptr = *head;
	int i = 0;

	while (ptr != NULL)
	{
		i++;
		ptr = ptr->next;
	}

	return (i);
}
/**
*is_palindrome - C that checks if a singly
*linked list is a palindrome
*@head: pointer to list
*Return: 1 or 0
*/
int is_palindrome(listint_t **head)
{
	int j, i = len_list(head);
	int arr_int[ARR_LEN(i)];
	listint_t *ptr;

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

	for (i = 0, j = len; i < j; i++, j--)
	{
		if (arr[i] != arr[j])
			return (0);
	}
	return (1);
}
