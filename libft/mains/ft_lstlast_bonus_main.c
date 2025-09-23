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
	ft_lstadd_front(&lst, new_node);

	//Checking the size
	printf("Last node content: %s\n", (char *) ft_lstlast(lst)->content);
	
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