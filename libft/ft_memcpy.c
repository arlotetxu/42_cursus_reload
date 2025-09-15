/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_memcpy.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joflorid <joflorid@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/09/15 17:16:37 by joflorid          #+#    #+#             */
/*   Updated: 2025/09/15 17:37:30 by joflorid         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

/*
DESCRIPTION
	The  memcpy() function copies 'n' bytes from 'src' to 'dst' avoiding the
	overlapping.
	Prototype:
	void *memcpy(void *dest, const void *src, size_t n);

PARAMETERS

	dest --> destination string

	src --> source string.

	n --> quantity of bytes from 'src' to be copied in 'dst'.

RETURN VALUE
       None
*/

void	*ft_memcpy(void *dest, const void *src, size_t n)
{
	size_t	i;

	i = -1;
	while (++i < n)
	{
		((unsigned char *)dest)[i] = ((unsigned char *)src)[i];
	}
	return (dest);
}

int	main(void)
{
	char	s[15] = "Hola Hola";
	char	dst[2];
	int		i = 0;

	// printf("-------- ESTANDAR ---------\n");
	// printf("Cadena Original: %s\n", s2);
	// memset(s2, '*', 15);
	// printf("Cadena modificada: %s\n", s2);
	printf("-------- IMPLEMENTACION ---------\n");
	printf("Cadena Original: %s\n", dst);
	ft_memcpy(dst, s, 4);
	while (++i < 11)
		//printf("%02X ", (unsigned char)s[i]);
		printf("%c ", (unsigned char)dst[i]);
	return (0);
}
