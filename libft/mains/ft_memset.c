int	main(void)
{
	char	s[15] = "Hola Hola";
	char	s2[15] = "Hola Hola";

	// printf("-------- ESTANDAR ---------\n");
	// printf("Cadena Original: %s\n", s2);
	// memset(s2, '*', 15);
	// printf("Cadena modificada: %s\n", s2);
	printf("-------- IMPLEMENTACION ---------\n");
	printf("Cadena Original: %s\n", s);
	ft_memset(s, '*', 5);
	printf("Cadena modificada: %s\n", s);
	return (0);
}
