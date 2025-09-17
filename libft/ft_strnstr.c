/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strnstr.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joflorid <joflorid@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/09/17 15:26:10 by joflorid          #+#    #+#             */
/*   Updated: 2025/09/17 16:26:24 by joflorid         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

/*
================================================================================
DESCRIPTION
	The fuction ft_strnstr() locates the first occurrence of the 'little' string
	into the 'big' string. The search is not longer than 'len' what means that
	'little' is search in the first 'len' bytes.
	Prototype:
	char	*strnstr(const char *big, const char *little, size_t len);

PARAMETERS
	big --> String where to search in.

	little --> String to find.

	len --> number of bytes or values to check.

RETURN VALUE
	big --> if 'little' is empty.

	NULL --> if 'little' is not contained in 'big'.

	Pointer to the first character --> if 'little' is found.
================================================================================
*/

char	*ft_strnstr(const char *big, const char *little, size_t len)
{
	size_t	i;
	size_t	j;

	i = 0;
	j = 0;
	if (!little[j])
		return ((char *)big);
	while (i < len && big[i])
	{
		j = 0;
		while ((i + j) < len && little[j] && big[i + j])
		{
			if (big[i + j] == little[j])
				j++;
			else
				break ;
			if (little[j] == '\0')
				return (&((char *)big)[i]);
		}
		i++;
	}
	return (NULL);
}
