int	main(void)
{
	//char	*src = "Hello";
	//char	dest[10] = " Mundo";
	char	*src_1 = "Hello";
	char	dest_1[15] = "World";

	//printf("Original: %i\n", strlcat(dest, src, 10));
	printf("Propia: %zu\n", ft_strlcat(dest_1, src_1, 6));
	return (0);
}
