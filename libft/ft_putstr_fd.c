/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_putstr_fd.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joflorid <joflorid@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/09/21 09:19:55 by joflorid          #+#    #+#             */
/*   Updated: 2025/09/24 13:21:41 by joflorid         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

/*
================================================================================
DESCRIPTION
	The function ft_putstr_fd() sends the string 's' to the file descriptor
	(fd). A file descriptor is an integer value that represents a file in the
	system.
	Prototype:
	void	ft_putstr_fd(char *s, int fd);

PARAMETERS
	s --> String to be sent to the file descriptor (fd).

	fd --> File descriptor that receives the character.

RETURN VALUE
	Nothing.
================================================================================
*/

void	ft_putstr_fd(char *s, int fd)
{
	if (fd < 0 || !s)
		return ;
	while (*s)
	{
		write(fd, s, 1);
		s++;
	}
}
