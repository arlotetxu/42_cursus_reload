// A function to apply to each node's content (the 'f' parameter)
// This function duplicates the string and adds " mapped!" to it.
void	*map_function(void *content)
{
    char	*str = (char *)content;
    char	*result;
    char	*suffix = " mapped!";

    result = (char *)malloc(strlen(str) + strlen(suffix) + 1);
    if (!result)
        return (NULL);
    strcpy(result, str);
    strcat(result, suffix);
    return (result);
}

// A function to delete a node's content (the 'del' parameter)
void	del_function(void *content)
{
    // In this case, content is allocated with malloc (by strdup and map_function)
    free(content);
}

// A helper function to print the list contents
void	print_list(t_list *lst)
{
    int i = 0;
    while (lst)
    {
        printf("  Node %d: \"%s\"\n", i, (char *)lst->content);
        lst = lst->next;
        i++;
    }
}

int	main(void)
{
    t_list	*original_list = NULL;
    t_list	*mapped_list;

    // 1. Create the original list
    // Note: strdup allocates memory, which del_function will free.
    ft_lstadd_back(&original_list, ft_lstnew(strdup("Hello")));
    ft_lstadd_back(&original_list, ft_lstnew(strdup("World")));
    ft_lstadd_back(&original_list, ft_lstnew(strdup("Test")));

    printf("--- Original List ---\n");
    print_list(original_list);

    // 2. Apply ft_lstmap to create a new list
    printf("\n--- Calling ft_lstmap ---\n");
    mapped_list = ft_lstmap(original_list, &map_function, &del_function);

    // 3. Print the new mapped list
    if (mapped_list)
    {
        printf("\n--- Mapped List (Success!) ---\n");
        print_list(mapped_list);
    }
    else
    {
        printf("\n--- Mapped List (ft_lstmap returned NULL) ---\n");
    }

    // 4. Clean up memory for both lists
    printf("\n--- Cleaning up memory ---\n");
    ft_lstclear(&original_list, &del_function);
    ft_lstclear(&mapped_list, &del_function);
    printf("Memory cleared.\n");

    return (0);
}
