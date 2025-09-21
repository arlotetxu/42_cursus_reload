int	main(void)
{
	int		fd;
	char	*s;

	s = "This is a new string that has been sent to the file descriptor";
	// El tercer argumento 0644 da permisos de lectura/escritura al propietario.
	fd = open("../../../../Temp/ft_putendl_fd.txt", O_CREAT | O_WRONLY, 0644);
	if (fd < 0)
		return (1);
	ft_putendl_fd(s, fd);
	close(fd);
	return (0);
}