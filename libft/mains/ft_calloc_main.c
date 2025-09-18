//Warning, compile the program with -fsanitize=address -g3
int	main(void)
{
	char	*test_p;
	int		i;
	char	n;

	test_p = ft_calloc(8, sizeof(int));

	n = '$';
	i = 0;
	while (i < 9)
	{
		test_p[i] = n;
		i++;
	}
	printf("Before free: %s\n", test_p);
	free(test_p);
	printf("After free: %s\n", test_p);
	return (0);
}
