/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_bzero.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joflorid <joflorid@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/09/15 15:39:00 by joflorid          #+#    #+#             */
/*   Updated: 2025/09/16 11:45:45 by joflorid         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

/*
================================================================================
DESCRIPTION
	The  bzero() function fills the first 'n' bytes of the memory area
	pointed to by 's' with zeros or bytes containing '\0'.
	Prototype:
	void bzero(void *s, size_t n);

PARAMETERS
	s --> string to add the '\0' value to.

	n --> quantity of '\0' to be added to the string 's'. They are added at the
		begining of the string.

RETURN VALUE
	None
================================================================================
*/
void	ft_bzero(void *s, size_t n)
{
	if (n > 0)
		ft_memset(s, 0, n);
}
