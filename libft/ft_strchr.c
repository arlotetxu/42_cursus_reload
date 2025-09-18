/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strchr.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joflorid <joflorid@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/09/17 10:50:40 by joflorid          #+#    #+#             */
/*   Updated: 2025/09/18 14:43:11 by joflorid         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

/*
================================================================================
DESCRIPTION
	The fuction ft_strchr() returns a pointer to the first occurrence of the
	character 'c' in the string 's'.
	The terminating null character is also considered as part of the string 's'
	Prototype:
	char	*ft_strchr(const char *s, int c);

PARAMETERS
	s --> The string where to search for the 'c' character.

	c --> Character to look for.

RETURN VALUE
	A pointer to the matched character or NULL if it is not found.
================================================================================
*/

char	*ft_strchr(const char *s, int c)
{
	if (c == 0)
		return (&((char *)s)[ft_strlen(s)]);
	while (*s)
	{
		if (*s == c)
			return ((char *)s);
		s++;
	}
	return (NULL);
}
