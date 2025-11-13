/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   get_next_line.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joflorid <joflorid@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/13 16:32:46 by joflorid          #+#    #+#             */
/*   Updated: 2025/11/13 10:11:26 by joflorid         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "get_next_line.h"

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
		stack = ft_strjoin_gnl(stack, buffer);
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
	static char	*stack;
	char		*line;

	if (fd < 0 || BUFFER_SIZE <= 0)
		return (NULL);
	stack = ft_read_file(fd, stack);
	if (!stack || !stack[0])
		return (free(stack), stack = NULL, NULL);
	if (!ft_check_char(stack))
		return (line = stack, stack = NULL, line);
	line = ft_fill_line(stack);
	stack = ft_clean_stack(stack);
	return (line);
}

/* int	main(void)
{
	int	fd = open("joflorid.txt", O_RDONLY);
	char	*line;

	if (fd < 0)
		return (0);
	int i = 0;
	while (i < 6)
	{
		line = get_next_line(fd);
		printf("Valor de line en main: %s\n", line); //!!PRINTF
		free(line);
		i++;
	}
	close(fd);
	return (0);
} */
