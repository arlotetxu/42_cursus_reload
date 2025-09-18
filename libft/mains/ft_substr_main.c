int	main(void)
{
	char	*src;
	unsigned int	start;
	unsigned int	len;

	src = "This is a test string";
	start = 2;
	len = 25;
	printf("Return created: %s\n", ft_substr(src, start, len));
	return (0);
}
