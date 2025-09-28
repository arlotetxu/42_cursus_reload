int	main(void)
{
	const char	*str;
	//char		c;

	str = "tripouille";
	//c = 'i';
	printf("Returned created: %s\n", ft_strchr(str, 't' + 256));
	printf("Returned standard: %s\n", strchr(str, 't' + 256));
	return (0);
}
