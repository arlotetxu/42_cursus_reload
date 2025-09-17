int	main(void)
{
	char	*str;
	char	*sub;
	size_t	n;

	str = "This is a string";
	sub = "is";
	n = 25;
	printf("Return created: %s\n", ft_strnstr(str, sub, n));
	//printf("Return standard: %s\n", strnstr(str, sub, n));
	return (0);
}
