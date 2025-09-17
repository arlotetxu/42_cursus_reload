int	main(void)
{
	const char	*str;
	char		c;

	str = "This is a string test";
	c = 'i';
	printf("Returned created: %s\n", ft_strrchr(str, c));
	printf("Returned standard: %s\n", strrchr(str, c));
	return (0);
}
