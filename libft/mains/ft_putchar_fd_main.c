int	main(void)
{
	int		fd;
	char	c;

	c = '@';
	fd = open("../../../../Temp/ft_putchar_fd.txt", O_CREAT | O_WRONLY);
	if (fd < 0)
		return (1);
	ft_putchar_fd(c, fd);
	close(fd);
	return (0);
}