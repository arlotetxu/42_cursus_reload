int	main(void)
{
	char	src[] = "Hola656565656";
	char	dst[20];
	//char	dst_2[20];
	char	dst_3[2];
	//char	dst_4[2];
	size_t	n;

	n = 4;
	printf("Prueba escenario 1 - suficiente memoria en dst -\n");
	printf("Valor devuelto: %zu\n", ft_strlcpy(dst, src, n));
	//printf("Funcion estandar: %d\n", strlcpy(dst_2, src, n));
	printf("Cadena destino 1: %s\n\n", dst);

	printf("Prueba escenario 2 - NO suficiente memoria en dst -\n");
	printf("Valor devuelto: %zu\n", ft_strlcpy(dst_3, src, n));
	//printf("Funcion estandar: %d\n", strlcpy(dst_4, src, n));
	printf("Cadena destino 3: %s\n", dst_3);

	return (0);
}
