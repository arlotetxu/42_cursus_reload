int	main(void)
{
	int		fd;
	int		n;

	n = -2147483648;
	// El tercer argumento 0644 da permisos de lectura/escritura al propietario.
	fd = open("../../temp/ft_putnbr_fd.txt", O_CREAT | O_WRONLY, 0644);
	if (fd < 0)
		return (1);
	ft_putnbr_fd(n, fd);
	close(fd);
	return (0);
}
