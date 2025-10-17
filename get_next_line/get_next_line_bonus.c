/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   get_next_line_bonus.c                              :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joflorid <joflorid@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/17 12:03:39 by joflorid          #+#    #+#             */
/*   Updated: 2025/10/17 12:24:52 by joflorid         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "get_next_line_bonus.h"

/*==============================================================================
DESCRIPTION
	The function ft_read_file() reads the file descriptor 'fd' and save each
	read in 'stack' while '\n' character is not found and a read is successful
	(bytes_r > 0. Otherwise bytes_r < 0).

PARAMETERS
	fd --> File descriptor (id of the file to read)

	stack --> The string in which the line has to be removed.

RETURN
	stack --> The string where all the characters received from read function
		are stored.
==============================================================================*/
static char	*ft_read_file(int fd, char *stack)
{
	char		*buffer;
	int			bytes_r;

	buffer = malloc(sizeof(char) * (BUFFER_SIZE + 1));
	if (!buffer)
		return (NULL);
	bytes_r = 1;
	while (!ft_check_char(stack) && bytes_r > 0)
	{
		bytes_r = read(fd, buffer, BUFFER_SIZE);
		if (bytes_r < 0)
			return (free(buffer), NULL);
		buffer[bytes_r] = '\0';
		stack = ft_strjoin(stack, buffer);
		if (!stack)
			return (free(buffer), NULL);
	}
	free(buffer);
	return (stack);
}

/*==============================================================================
DESCRIPTION
	The function get_next_line() does initial checks before call the
	ft_read_file(). It checks if the file descriptor and BUFFER_SIZE (in header
	file) are OK. It load in the 'stack' static variable the reads. Then,
	depeding on the value of 'stack' return the line through it load with
	function ft_fill_line() or NULL

PARAMETERS
	fd --> File descriptor (id of the file to read)

RETURN
	line --> The line got from 'stack'.

	NULL in case of errors
==============================================================================*/
char	*get_next_line(int fd)
{
	static char	*stack[1024];
	char		*line;

	if (fd < 0 || BUFFER_SIZE <= 0)
		return (NULL);
	stack[fd] = ft_read_file(fd, stack[fd]);
	if (!stack[fd] || !stack[fd][0])
		return (free(stack[fd]), stack[fd] = NULL, NULL);
	if (!ft_check_char(stack[fd]))
		return (line = stack[fd], stack[fd] = NULL, line);
	line = ft_fill_line(stack[fd]);
	stack[fd] = ft_clean_stack(stack[fd]);
	return (line);
}

/* int	main(void)
{
	int	fd1 = open("joflorid_bonus1.txt", O_RDONLY);
	int	fd2 = open("joflorid_bonus2.txt", O_RDONLY);
	int	fd3 = open("joflorid_bonus3.txt", O_RDONLY);
	int	fd4 = open("joflorid_bonus4.txt", O_RDONLY);
	int	fd5 = open("joflorid_bonus5.txt", O_RDONLY);
	char	*line;

	if (fd1 < 0 || fd2 < 0 || fd3 < 0 || fd4 < 0 || fd5 < 0)
		return (0);
	int i = 0;
	while (i < 5)
	{
		line = get_next_line(fd1);
		printf("Valor de line en fd(%i): %s\n", fd1, line); //!!PRINTF
		free(line);
		line = get_next_line(fd2);
		printf("Valor de line en fd(%i): %s\n", fd2, line); //!!PRINTF
		free(line);
		line = get_next_line(fd1);
		printf("Valor de line en fd(%i): %s\n", fd1, line); //!!PRINTF
		free(line);
		line = get_next_line(fd3);
		printf("Valor de line en fd(%i): %s\n", fd3, line); //!!PRINTF
		free(line);
		line = get_next_line(fd3);
		printf("Valor de line en fd(%i): %s\n", fd3, line); //!!PRINTF
		free(line);
		line = get_next_line(fd4);
		printf("Valor de line en fd(%i): %s\n", fd4, line); //!!PRINTF
		free(line);
		line = get_next_line(fd5);
		printf("Valor de line en fd(%i): %s\n", fd5, line); //!!PRINTF
		printf("==========================================================\n");
		free(line);
		i++;
	}
	close(fd1);
	close(fd2);
	close(fd3);
	close(fd4);
	close(fd5);
	return (0);
} */
