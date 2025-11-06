/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_memmove.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joflorid <joflorid@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/09/16 11:13:57 by joflorid          #+#    #+#             */
/*   Updated: 2025/09/16 13:18:29 by joflorid         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

/*
================================================================================
DESCRIPTION
	The  ft_memmove() function copies 'n' bytes from 'src' to 'dest'. To avoid
	the overlapping, if 'dest' is less than 'src' (memory address), the copy
	process is done from the left to the right. Otherwise, the copy process is
	done from the right to the left.
	Prototype:
	void *memmove(void *dest, const void *src, size_t n)

PARAMETERS

	dest --> final string

	src --> source string to be copied into dest.

	n --> quantity of bytes from 'src' to be copied in 'dst'.

RETURN VALUE
	a pointer to 'dest'
================================================================================
*/

void	*ft_memmove(void *dest, const void *src, size_t n)
{
	size_t	i;

	if (dest == NULL || src == NULL)
		return (NULL);
	if (n == 0)
		return (dest);
	if (dest < src)
	{
		i = -1;
		while (++i < n)
			((unsigned char *)dest)[i] = ((const unsigned char *)src)[i];
	}
	else
	{
		while (n > 0)
		{
			n--;
			((unsigned char *)dest)[n] = ((const unsigned char *)src)[n];
		}
	}
	return (dest);
}
