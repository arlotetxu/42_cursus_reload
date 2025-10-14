/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   get_next_line.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joflorid <joflorid@student.42urduliz.co    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/13 16:32:46 by joflorid          #+#    #+#             */
/*   Updated: 2025/10/14 20:12:15 by joflorid         ###   ########.fr       */
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

	len = 0;
	while (stack[len] != '\n')
		len++;
	line = malloc(sizeof(char) * (len + 1));
	if (!line)
		return (NULL);
	len = -1;
	while (stack[++len] != '\n')
		line[len] = stack[len];
	line[len] = '\n';
	return (line);
}

char	*ft_clean_stack(char *stack)
{
	int		start;
	int		stop;
	int		i;
	char	*new_stack;

	start = 0;
	while (stack[start] != '\n')
		start++;
	start++;
	stop = start;
	while (stack[stop])
		stop++;
	new_stack = malloc(sizeof(char) * (stop - start + 1));
	if (!new_stack)
		return (NULL);
	i = 0;
	while (start < stop)
		new_stack[i++] = stack[start++];
	new_stack[i] = '\0';
	//printf("Valor de new_stack: %s\n", new_stack); //!!PRINTF
	free(stack);
	return(new_stack); 
}


char	*get_next_line(int fd)
{
	static char	*stack;
	char		*buffer;
	char		*line;
	int			bytes_r;

	if (fd < 0)
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
		return (free(stack), NULL);
	while ((bytes_r = read(fd, buffer, BUFFER_SIZE)) > 0 || stack[0])
	{
		buffer[bytes_r] = '\0';
		stack = ft_strjoin(stack, buffer); //!!MALLOC
		if (!stack)
			return (free(buffer), NULL);
		//printf("Valor de stack: \n%s\n", stack); //!PRINTF
		if (ft_check_char(stack) == 1)
		{
			line = ft_fill_line(stack);
			stack = ft_clean_stack(stack);//clean stack
			//printf("Valor nuevo de stack: \n%s", stack); //!PRINTF
			//printf("Valor de line: \n%s", line); //!!PRINTF
			return (free(buffer), line);
		}
	}
	return (free(stack), stack = NULL, free(buffer), NULL); //TODO: Liberar stack??
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
		i++;
	}
	close(fd);
	return (0);
}
