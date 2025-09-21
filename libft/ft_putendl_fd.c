/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_putendl_fd.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joflorid <joflorid@student.42urduliz.co    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/09/21 09:48:40 by joflorid          #+#    #+#             */
/*   Updated: 2025/09/21 09:53:27 by joflorid         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

/*
================================================================================
DESCRIPTION
	The fuction ft_putendl_fd() sends the string 's' to the file descriptor
	(fd), adding a \n at the end. A file descriptor is an integer value that
	represents a file in the system.
	Prototype:
	void	ft_putendl_fd(char *s, int fd);

PARAMETERS
	s --> String to be sent to the file descriptor (fd).

	fd --> File descriptor that receives the character.

RETURN VALUE
	Nothing.
================================================================================
*/

void	ft_putendl_fd(char *s, int fd)
{
	if (fd < 0 || !s)
		return ;
	while (*s)
	{
		write(fd, s, 1);
		s++;
	}
	write(fd, "\n", 1);
}
