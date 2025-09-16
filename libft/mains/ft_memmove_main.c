int	main(void)
{
	char	dest[30] = "abcdef";
	int		n;

	n = 1;
	printf("Antes de funcion: %s\n", dest);
	ft_memmove(dest, dest + 2, n);
	printf("Despues de funcion: %s\n", dest);
	return (0);
}
