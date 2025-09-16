int	main(void)
{
	char	s[15] = "Hola Hola";
	char	dst[4];
	int		i = -1;
	int		n = 3;

	printf("-------- IMPLEMENTACION ---------\n");
	printf("Cadena Original: %s\n", dst);
	fflush(stdout);
	ft_memcpy(dst, s, n);
	while (++i < n)
		write(1, &dst[i], 1);
	return (0);
}
/* int	main(void)
{
	char	src1[] = "Hola Mundo";
	char	dest1[20] = "XXXXXXXXXX";

	printf("Caso 1: Copia normal\n");
	printf("Antes: %s\n", dest1);
	ft_memcpy(dest1, src1, strlen(src1) + 1); // incluye el '\0'
	printf("Despues: %s\n\n", dest1);

	char	src2[] = "ABCDE";
	char	dest2[10] = "ZZZZZZ";

	printf("Caso 2: Copia parcial (3 bytes)\n");
	printf("Antes: %s\n", dest2);
	ft_memcpy(dest2, src2, 3);
	printf("Despues: %s\n\n", dest2);

	int	arr_src[5] = {1, 2, 3, 4, 5};
	int	arr_dest[5] = {0};

	printf("Caso 3: Copia de enteros (memoria binaria)\n");
	ft_memcpy(arr_dest, arr_src, sizeof(arr_src));
	for (int i = 0; i < 5; i++)
		printf("%d ", arr_dest[i]);
	printf("\n");

	return 0;
} */
