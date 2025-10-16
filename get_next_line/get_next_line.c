/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   get_next_line.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joflorid <joflorid@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/13 16:32:46 by joflorid          #+#    #+#             */
/*   Updated: 2025/10/16 17:09:11 by joflorid         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "get_next_line.h"

/*==============================================================================
DESCRIPTION
	The function ft_fill_line() fills and return the first line the 'stack'
	string contains.

PARAMETERS
	stack --> The string in which to get the line if there is a line in it.

RETURN
	line --> The line found in the 'stack' string null terminated.
==============================================================================*/
char	*ft_fill_line(char *stack)
{
	char	*line;
	int		len;

	if (!stack)
		return (NULL);
	len = 0;
	while (stack[len] != '\n')
		len++;
	line = malloc(sizeof(char) * (len + 2));
	if (!line)
		return (NULL);
	len = -1;
	while (stack[++len] != '\n' && stack[len])
		line[len] = stack[len];
	if (stack[len] == '\n')
		line[len++] = '\n';
	line[len] = '\0';
	return (line);
}

/*==============================================================================
DESCRIPTION
	The function ft_clean_stack() removes from the 'stack' string the first line
	found on it. //!If the string only contains '\n' or if the string is
	//!empty ('\0), there is nothing to be returned.

PARAMETERS
	stack --> The string in which the line has to be removed.

RETURN
	new_stack --> A string cleaned. This string will be asigned to the 'stack'
		string later on.
==============================================================================*/
char	*ft_clean_stack(char *stack)
{
	int		i;
	int		j;
	char	*new_stack;

	if (!stack)
		return (NULL);
	i = 0;
	while (stack[i] && stack[i] != '\n')
		i++;
	if (!stack[i] || !stack[++i])
		return (free(stack), NULL);
	new_stack = malloc(sizeof(char) * (ft_strlen(stack) - i + 1));
	if (!new_stack)
		return (free(stack), NULL);
	j = 0;
	while (stack[i])
		new_stack[j++] = stack[i++];
	new_stack[j] = '\0';
	free(stack);
	stack = NULL;
	return (new_stack);
}

/*==============================================================================
DESCRIPTION
	The function ft_init_gnl() starts the process. It gets the static variable
		'stack' and buffer, appending 'buffer' to the 'stack'. It calls the
		function ft_fill_line() to get the line from the stack and cleans the
		'stack' string calling to the function ft_clean_stack().

PARAMETERS
	**stack --> The static variable where all the reads are stored. As it is
		static and it is not declared in this function, it must be treated as a
		double pointer

	*buffer --> Contains the reads from the file

	fd --> File descriptor (id of the file to read)

RETURN
	line --> The line got from 'stack'.

	NULL in case of errors
==============================================================================*/
char	*ft_init_gnl(char *buffer, char **stack, int fd)
{
	int			bytes_r;
	char		*line;

	bytes_r = 1;
	while (!ft_check_char(*stack) && bytes_r > 0)
	{
		bytes_r = read(fd, buffer, BUFFER_SIZE); //!! Si recibo bytes_r < 0??
		buffer[bytes_r] = '\0';
		*stack = ft_strjoin(*stack, buffer);
		if (!(*stack))
			return (free(buffer), buffer = NULL, NULL);
	}
	free(buffer);
	if (bytes_r < 0 || !(*stack)[0])
		return (free(*stack), *stack = NULL, NULL);
	if (ft_check_char(*stack))
	{
		line = ft_fill_line(*stack);
		if (!line)
			return (free(*stack), *stack = NULL, NULL);
		*stack = ft_clean_stack(*stack);
		return (line);
	}
	return (line = *stack, *stack = NULL, line);
}

/*==============================================================================
DESCRIPTION
	The function get_next_line() does initial checks before call the
	ft_init_gnl(). It checks if the file descriptor and BUFFER_SIZE (in header
	file) are OK. It initializes the 'stack' static variable and reserves
	memory for 'buffer' where the reads from the 'fd' is stored.

PARAMETERS
	fd --> File descriptor (id of the file to read)

RETURN
	line --> The line got from 'stack'.

	NULL in case of errors
==============================================================================*/
char	*get_next_line(int fd)
{
	static char	*stack;
	char		*buffer;
	char		*line;

	if (fd < 0 || BUFFER_SIZE <= 0)
		return (NULL);
	if (!stack)
	{
		stack = malloc(1);
		if (!stack)
			return (NULL);
		stack[0] = '\0';
	}
	buffer = malloc(BUFFER_SIZE + 1);
	if (!buffer)
		return (free(stack), stack = NULL, NULL);
	line = ft_init_gnl(buffer, &stack, fd);
	return (line);
}

int	main(void)
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
}
