/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strlcpy.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joflorid <joflorid@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/09/16 13:05:54 by joflorid          #+#    #+#             */
/*   Updated: 2025/09/16 15:51:09 by joflorid         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

/*
================================================================================
DESCRIPTION
	The  ft_strlcpy() function copies 'size' - 1 characters from the string
	'src' to the string 'dst', Null terminating the result. It copies 'size' -1
	characters or untill '\0' is found in src string.

	Prototype:
	size_t	strlcpy(char *dst, const char *src, size_t size);

PARAMETERS

	dst --> final string

	src --> source string to be copied into dst.

	size --> quantity of characters from 'src' to be copied in 'dst'.

RETURN VALUE
	The length of 'src' or 0 in case 'size' is equal to 0 or the strings are
	null.
	!!If the value returned is greater than or equal than 'size', there is a
	TRUNCATION.
================================================================================
*/

size_t	ft_strlcpy(char *dst, const char *src, size_t size)
{
	size_t	i;

	if (!src || !dst || size == 0)
		return (0);
	if (size > 0)
	{
		i = -1;
		while (++i < size - 1 && src[i] != '\0')
			dst[i] = src[i];
		dst[i] = '\0';
	}
	return (ft_strlen(src));
}
