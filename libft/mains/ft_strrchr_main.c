int	main(void)
{
	const char	*str;
	//char		c;

	str = "tripouille";
	//c = 'i';
	printf("Returned created: %s\n", ft_strrchr(str, 'z' + 258));
	printf("Returned standard: %s\n", strrchr(str, 'z' + 258));
	return (0);
}
