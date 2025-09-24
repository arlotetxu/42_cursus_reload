/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_memcmp.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joflorid <joflorid@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/09/17 14:56:34 by joflorid          #+#    #+#             */
/*   Updated: 2025/09/24 13:12:43 by joflorid         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

/*
================================================================================
DESCRIPTION
	The function ft_memcmp() compares the first 'n' values (interpreted as
	unsigned char) of the strings 's1' and 's2'
	Prototype:
	int	ft_memcmp(const void *s1, const void *s2, size_t n);

PARAMETERS
	s1 --> String1.

	s2 --> String2.

	n --> number of bytes or values to check.

RETURN VALUE
	0 --> if 'n' = 0

	Difference between s1 and s2 (s1 - s2)
================================================================================
*/

int	ft_memcmp(const void *s1, const void *s2, size_t n)
{
	unsigned char	*str1;
	unsigned char	*str2;
	size_t			i;

	str1 = (unsigned char *)s1;
	str2 = (unsigned char *)s2;
	i = 0;
	while (i < n)
	{
		if (str1[i] != str2[i])
			return (str1[i] - str2[i]);
		i++;
	}
	return (0);
}
