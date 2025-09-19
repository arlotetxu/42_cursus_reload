int	main(void)
{
	char	*str;
	char	**ret;
	int		delim;
	int		i;

	str = "This is a test";
	delim = 32;
	ret = ft_split(str, delim);
	i = 0;
	while (ret[i])
	{
		printf("String [%i]: %s\n", i, ret[i]);
		i++;
	}
	return (0);
}
