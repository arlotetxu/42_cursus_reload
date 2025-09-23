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

int	main(void)
{
	t_list	*lst = NULL;
	t_list	*new_node;

	//Adding 1st node
	new_node = ft_lstnew((char *)"Node 1");
	ft_lstadd_front(&lst, new_node);
	
	//Adding 2nd node
	new_node = ft_lstnew((char *) "Node 2");
	ft_lstadd_front(&lst, new_node);

	//Adding 3rd node
	new_node = ft_lstnew((char *) "Node 3");
	ft_lstadd_back(&lst, new_node);

	//Printing the list
	print_list(lst);
	
	// Freeing memory
	t_list *tmp;
	while (lst != NULL)
	{
		tmp = lst;
		lst = lst->next;
		free(tmp);
	}
	return (0);
}