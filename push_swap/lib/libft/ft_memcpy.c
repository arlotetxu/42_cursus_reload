/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_memcpy.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joflorid <joflorid@student.42urduliz.co    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/09/15 17:16:37 by joflorid          #+#    #+#             */
/*   Updated: 2025/09/28 07:34:46 by joflorid         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

/*
================================================================================
DESCRIPTION
	The ft_memcpy() function copies 'n' bytes from 'src' to 'dest'. The
	overlapping could happen. It copies values independing of their values (i.e:
	'\0' is copied as a value not considering what it means).
	If the number of copied bytes are greater than the length of 'dest', buffer
	overflow or segmentation fault can happen but this function does not check
	this scenario.
	Prototype:
	void *memcpy(void *dest, const void *src, size_t n);

PARAMETERS

	dest --> destination string

	src --> source string.

	n --> quantity of bytes from 'src' to be copied in 'dest'.

RETURN VALUE
	None
================================================================================
*/

void	*ft_memcpy(void *dest, const void *src, size_t n)
{
	size_t	i;

	if (dest == src)
		return (NULL);
	i = -1;
	while (++i < n)
		((unsigned char *)dest)[i] = ((const unsigned char *)src)[i];
	return (dest);
}
