// Aux function to print the list and check the order.
void print_list(t_list *head)
{
	t_list *current = head;
	int i = 0;
	printf("---- List content ----\n");
	while (current != NULL)
	{
		printf("Node %d: Content = \"%s\"\n", i, (char *)current->content);
		current = current->next;
		i++;
	}
	if (head == NULL)
	{
		printf("The list is empty.\n");
	}
	printf("-----------------------------\n\n");
}

int main(void)
{
	t_list *head = NULL;
	t_list *new_node;

	// 1. The list is empty at the beginning
	printf("Initial State:\n");
	print_list(head);

	// 2. Adding first node: "Node 1"
	printf("Añadiendo 'Node 1'...\n");
	new_node = ft_lstnew("Node 1");
	ft_lstadd_front(&head, new_node);
	print_list(head);
	// Expected: head -> ["Node 1"]

	// 3. Adding a second node: "Node 2"
	printf("Adding 'Node 2' at the beginning...\n");
	new_node = ft_lstnew("Node 2");
	ft_lstadd_front(&head, new_node);
	print_list(head);
	// Expected: head -> ["Node 2"] -> ["Node 1"]

	// 4. Adding third node: "Node 3"
	printf("Adding 'Node 3' at the beginning...\n");
	new_node = ft_lstnew("Node 3");
	ft_lstadd_front(&head, new_node);
	print_list(head);
	// Expected: head -> ["Nodo 3"] -> ["Nodo 2"] -> ["Nodo 1"]

	// Freeing memory (to avoid leaks)
	t_list *tmp;
	while (head != NULL)
	{
		tmp = head;
		head = head->next;
		free(tmp);
	}

	return (0);
}