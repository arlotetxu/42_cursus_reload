/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   get_next_line.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joflorid <joflorid@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/13 16:32:46 by joflorid          #+#    #+#             */
/*   Updated: 2025/10/13 17:07:11 by joflorid         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "get_next_line.h"

char	*get_next_line(int fd)
{
	///static char	*stack;
	char		*buffer;
	//char		*line;
	int			bytes_r;

	if (fd < 0)
		return (NULL);
	buffer = malloc(BUFFER_SIZE + 1);
	if (!buffer)
		return (NULL);
	bytes_r = 1;
	while (bytes_r > 0)
	{
		bytes_r = read(fd, buffer, BUFFER_SIZE);//funcion read
		buffer[bytes_r] = '\0';
		printf("Valor de buffer: %s\n", buffer); //!!PRINTF
		printf("bytes leidos: %i\n", bytes_r); //!!PRINTF
	}
	free(buffer);
	return (NULL);
}

int	main(void)
{
	int	fd = open("joflorid.txt", O_RDONLY);

	if (fd < 0)
		return (0);
	get_next_line(fd);
	//close(fd);
	return (0);
}
