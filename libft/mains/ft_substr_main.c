int	main(void)
{
	char	*src;
	unsigned int	start;
	unsigned int	len;

	src = "lorem ipsum dolor sit amet";
	start = 400;
	len = 20;
	printf("Return created: %s\n", ft_substr(src, start, len));
	return (0);
}
