int	main(void)
{
	char	*str1;
	char	*str2;
	size_t	n;

	str1 = "This is the s1 string";
	str2 = "This is the s2 string";
	n = 50;
	printf("Return created: %i\n", ft_memcmp(str1, str2, n));
	printf("Return standard: %i\n", memcmp(str1, str2, n));
	return (0);
}
