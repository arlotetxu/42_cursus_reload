/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   get_next_line.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joflorid <joflorid@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/13 16:32:46 by joflorid          #+#    #+#             */
/*   Updated: 2025/10/15 17:45:35 by joflorid         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "get_next_line.h"


// 0 - Leer buffer_size a buffer
// 1 - Append buffer a stack
// 2 - chequear si stack tiene /n
// 3 - si tiene /n, sacar la linea a line y actualizar stack
// 4 - si no tiene, volver a punto 0

char	*ft_fill_line(char *stack)
{
	char	*line;
	int		len;

	if (!stack)
		return (NULL);
	len = 0;
	while (stack[len] != '\n')
		len++;
	//printf("Valor de stack[%i]: %c\n", len, stack[len]); //!!PRINTF
	line = malloc(sizeof(char) * (len + 2));
	if (!line)
		return (NULL);
	len = -1;
	while (stack[++len] != '\n')
		line[len] = stack[len];
	//printf("Valor de line en fill_line: %s\n", line); //!!PRINTF
	//printf("Valor de len: %i\n", len); //!!PRINTF
	if (stack[len] == '\n')
		line[len++] = '\n';
	line[len] = '\0';
	return (line);
}

char	*ft_clean_stack(char *stack)
{
	int		i;
	int		j;
	char	*new_stack;

	if (!stack)
		return (NULL);
	i = 0;
	while (stack[i] != '\n')
		i++;
	if (!stack[i])
		return(free(stack), NULL);
	new_stack = malloc(sizeof(char) * (ft_strlen(stack) - i));
	if (!new_stack)
		return (free(stack), NULL);
	i++;
	j = 0;
	while (stack[i])
		new_stack[j++] = stack[i++];
	new_stack[j] = '\0';
	//printf("Valor de new_stack: %s\n", new_stack); //!!PRINTF
	free(stack);
	stack = NULL;
	return(new_stack);
}

char	*ft_init_gnl(char *buffer, char **stack, int fd)
{
	int			bytes_r;
	char		*line;

	while (!ft_check_char(*stack) && (bytes_r = read(fd, buffer, BUFFER_SIZE)) > 0)
	{
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
	return(line);
}

int	main(void)
{
	int	fd = open("joflorid.txt", O_RDONLY);
	char	*line;

	if (fd < 0)
		return (0);
	int i = 0;
	while (i < 4)
	{
		line = get_next_line(fd);
		printf("Valor de line en main: %s\n", line); //!!PRINTF
		free(line);
		i++;
	}
	close(fd);
	return (0);
}
