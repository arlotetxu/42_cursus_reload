int	main(void)
{
	char	*str;
	char	*set;

	str = "###DEF#GHI###";
	set = "#";
	// printf("Return left: %i\n", ft_cut_left(str, set));
	// printf("Return right: %i\n", ft_cut_right(str, set));
	printf("Final result: %s\n", ft_strtrim(str, set));
	return (0);
}
