int	main(void)
{
	char	*str;
	char	c;
	int		n;

	str = "This is a string";
	c = 't';
	n = 25;
	printf("Return created: %s\n", (char *)ft_memchr(str, c, n));
	printf("Return standard: %s\n", (char *)memchr(str, c, n));
	return (0);
}
