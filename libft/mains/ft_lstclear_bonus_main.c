void print_list(t_list *head)
{
	t_list *current = head;
	int i = 0;
	printf("---- List content ----\n");
	if (head == NULL)
	{
		printf("The list is empty.\n");
	}
	else
	{
		while (current != NULL)
		{
			printf("Node %d: Content = \"%s\"\n", i, (char *)current->content);
			current = current->next;
			i++;
		}
	}
	printf("-----------------------------\n\n");
}

void	del_content(void *content)
{
	(void)content;
}

int main(void)
{
	t_list	*head = NULL;

	printf("--- Testing ft_lstclear ---\n\n");

	// 1. creating the list with 3 nodes.
	printf("Creating a list with 3 nodes...\n");
	ft_lstadd_front(&head, ft_lstnew("Node 1"));
	ft_lstadd_front(&head, ft_lstnew("Node 2"));
	ft_lstadd_front(&head, ft_lstnew("Node 3"));

	// 2. Printing the list.
	printf("List initial state:\n");
	print_list(head);
	// Expected: [Node 3] -> [Node 2] -> [Node 1]

	// 3. Calling ft_lstclear to delete the full list.
	printf("Calling to ft_lstclear to delete the full list...\n");
	ft_lstclear(&head, &del_content);

	// 4. Printing again the list.
	printf("List final state:\n");
	print_list(head);
	// Expected: The list is empty.

	return (0);
}