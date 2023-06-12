#include "lists.h"

/**
 * list_reverse - function to reverse the second half of list
 *
 * @headr: head of list
 * Return: no return
 */
void list_reverse(listint_t **headr)
{
	listint_t *previous;
	listint_t *current;
	listint_t *next;

	previous = NULL;
	current = *headr;

	while (current != NULL)
	{
		next = current->next;
		current->next = previous;
		previous = current;
		current = next;
	}

	*headr = previous;
}

/**
 * list_compare - function to compare between int of list
 *
 * @head1: first head of list
 * @head2: second head of list
 * Return: 1 if are equals, 0 if not
 */
int list_compare(listint_t *head1, listint_t *head2)
{
	listint_t *tp1;
	listint_t *tp2;

	tp1 = head1;
	tp2 = head2;

	while (tp1 != NULL && tp2 != NULL)
	{
		if (tp1->n == tp2->n)
		{
			tp1 = tp1->next;
			tp2 = tp2->next;
		}
		else
		{
			return (0);
		}
	}

	if (tp1 == NULL && tp2 == NULL)
	{
		return (1);
	}

	return (0);
}

/**
 * is_palindrome - checks if a singly linked list
 * is a palindrome
 * @head: pointer to head of list
 * Return: 0 if it is not a palindrome,
 * 1 if it is a palndrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *slw, *fast, *previous_slw;
	listint_t *scan_hlf, *mdl;
	int is_plin;

	slw = fast = previous_slw = *head;
	mdl = NULL;
	is_plin = 1;

	if (*head != NULL && (*head)->next != NULL)
	{
		while (fast != NULL && fast->next != NULL)
		{
			fast = fast->next->next;
			previous_slw = slw;
			slw = slw->next;
		}

		if (fast != NULL)
		{
			mdl = slw;
			slw = slw->next;
		}

		scan_hlf = slw;
		previous_slw->next = NULL;
		list_reverse(&scan_hlf);
		is_plin = list_compare(*head, scan_hlf);

		if (mdl != NULL)
		{
			previous_slw->next = mdl;
			mdl->next = scan_hlf;
		}
		else
		{
			previous_slw->next = scan_hlf;
		}
	}

	return (is_plin);
}
