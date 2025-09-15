int	main(void)
{
	char	s[15] = "Hello Hello";
	int		i = -1;

	printf("-------- IMPLEMENTACION ---------\n");
	printf("Cadena Original: %s\n", s);
	ft_bzero(s, 5);
	    printf("Modificado: ");
    while (++i < 11)
        //printf("%02X ", (unsigned char)s[i]);
		printf("%c ", (unsigned char)s[i]);
    printf("\n");
	return (0);
}
