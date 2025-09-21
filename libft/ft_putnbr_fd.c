/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_putnbr_fd.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joflorid <joflorid@student.42urduliz.co    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/09/21 10:00:02 by joflorid          #+#    #+#             */
/*   Updated: 2025/09/21 10:11:55 by joflorid         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

/*
================================================================================
DESCRIPTION
	The fuction ft_putnbr_fd() sends the number 'n' to the file descriptor
	(fd). A file descriptor is an integer value that represents a file in the
	system.
	Prototype:
	void	ft_putnbr_fd(int n, int fd);

PARAMETERS
	n --> Number to be sent to the file descriptor (fd).

	fd --> File descriptor that receives the character.

RETURN VALUE
	Nothing.
================================================================================
*/

void	ft_putnbr_fd(int n, int fd)
{
	char	*nbr;

	if (fd < 0)
		return ;
	nbr = ft_itoa(n);
	ft_putstr_fd(nbr, fd);
}
