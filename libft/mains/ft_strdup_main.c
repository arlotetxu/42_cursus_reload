int	main(void)
{
	const char	*str;

	str = "This is a test";
	printf("Return created: %s\n", ft_strdup(str));
	printf("Return standard: %s\n", strdup(str));
	return (0);
}
