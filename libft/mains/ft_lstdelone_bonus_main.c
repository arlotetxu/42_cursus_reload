// For strings created with malloc/strdup, use free(content).
// For strings literals, do nothing.
void	del_content(void *content)
{
	(void)content;
}

int	main(void)
{
	t_list	*node_to_delete;

	printf("--- Testing ft_lstdelone ---\n\n");

	// 1. Creating a new node to test.
	printf("Creating a new node with content 'Hello world'...\n");
	node_to_delete = ft_lstnew("Hello world");
	if (!node_to_delete)
	{
		printf("Error: The node couldn't be created.\n");
		return (1);
	}

	printf("Node created. Content: \"%s\"\n", (char *)node_to_delete->content);

	// 2. Deleting the node using ft_lstdelone
	printf("\nCalling ft_lstdelone to delete the node...\n");
	ft_lstdelone(node_to_delete, &del_content);

	printf("Node deleted.\n");
	printf("\nIf not Segmentation Fault --> SUCCESS.\n");

	return (0);
}