/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_putchar_fd.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joflorid <joflorid@student.42urduliz.co    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/09/21 08:42:14 by joflorid          #+#    #+#             */
/*   Updated: 2025/09/21 09:03:21 by joflorid         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

/*
================================================================================
DESCRIPTION
	The fuction ft_putchar_fd() sends the character 'c' to the file descriptor
	(fd). A file descriptor is an integer value that represents a file in the 
	system.
	Prototype:
	void	ft_putchar_fd(char c, int fd);

PARAMETERS
	c --> Character to be sent to the file descriptor (fd).

	fd --> File descriptor that receives the character.

RETURN VALUE
	Nothing.
================================================================================
*/

void	ft_putchar_fd(char c, int fd)
{
	if (fd < 0)
		return ;
	write(fd, &c, 1);
}
