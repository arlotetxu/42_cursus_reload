int	main(void)
{
	const char	*s;

	s = "Esto es una prueba: 22";
	printf("Bytes propia: %lu\n", ft_strlen(s));
	printf("Bytes estandar: %lu\n", strlen(s));
	return (0);
}
