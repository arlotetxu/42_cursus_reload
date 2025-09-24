/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strncmp.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joflorid <joflorid@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/09/17 12:14:01 by joflorid          #+#    #+#             */
/*   Updated: 2025/09/24 14:22:53 by joflorid         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

/*
================================================================================
DESCRIPTION
	The function ft_strncmp() compares the string 's1' and 's2' and returns the
	difference. The comparison will never be greater than 'n' bytes of
	characters.
	Prototype:
	int	ft_strncmp(const char *s1, const char *s2, size_t n);

PARAMETERS
	s1 --> String1.

	s2 --> String2.

	n --> number of bytes or characters to compare.

RETURN VALUE
	0 --> if 's1' and 's2' are identical.

	(int)Difference between both strings (s1 - s2) --> the strings are not
		similar
================================================================================
*/

int	ft_strncmp(const char *s1, const char *s2, size_t n)
{
	size_t	i;

	i = 0;
	while (i < n && s1[i] && s2[i])
	{
		if ((unsigned char)s1[i] != (unsigned char)s2[i])
			return ((unsigned char)s1[i] - (unsigned char)s2[i]);
		i++;
	}
	if (i < n)
		return ((unsigned char)s1[i] - (unsigned char)s2[i]);
	return (0);
}
