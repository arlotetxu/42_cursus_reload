/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strlcat.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joflorid <joflorid@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/09/16 15:56:41 by joflorid          #+#    #+#             */
/*   Updated: 2025/09/16 17:07:09 by joflorid         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

/*
================================================================================
DESCRIPTION
	The  ft_strlcpy() function appends 'size' - 1 characters from the string
	'src' to the string 'dst', Null terminating the result. It copies 'size' -1
	characters or untill '\0' is found in src string.
	The strlcat() function appends the NUL-terminated string src to the end of
	dst. It will append at most size - strlen(dst) - 1 bytes, NUL-terminating
	the result.

	Prototype:
	size_t	strlcat(char *dst, const char *src, size_t size);

PARAMETERS

	dst --> final string

	src --> source string to be copied into dst.

	size -->

RETURN VALUE
	the number of characters the function would copied independing of the
	result of the real copy.
================================================================================
*/

size_t	ft_strlcat(char *dst, const char *src, size_t size)
{
	size_t	i;
	size_t	j;

	if (size == 0)
		return (ft_strlen(src));
	i = 0;
	while (dst[i] != '\0' && i < size)
		i++;
	if (i >= size)
		return (size + ft_strlen(src));
	j = 0;
	while (src[j] != '\0' && (i + j + 1) < size)
	{
		dst[i + j] = src[j];
		j++;
	}
	if ((i + j) < size)
		dst[i + j] = '\0';
	return (i + ft_strlen(src));
}
