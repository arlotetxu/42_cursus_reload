int	main(void)
{
	char	*s1;
	char	*s2;
	size_t	n;

	s1 = "This is the s1 string";
	s2 = "This is The s2 string";
	n = 15;
	printf("Returned created: %i\n", ft_strncmp(s1, s2, n));
	printf("Returned standard: %i\n", strncmp(s1, s2, n));
	return (0);
}
