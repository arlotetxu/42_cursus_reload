/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_memchr.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joflorid <joflorid@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/09/17 13:14:55 by joflorid          #+#    #+#             */
/*   Updated: 2025/09/17 14:16:41 by joflorid         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

/*
================================================================================
DESCRIPTION
	The fuction ft_memchr() checks for the first occurrence of 'c' in the 'n'
	first bytes of the string pointed by 's'. Both 'c' and the bytes of the
	memory area pointed to by 's' are interpreted as unsigned char.
	Prototype:
	void	*ft_memchr(const void *s, int c, size_t n);

PARAMETERS
	s --> String to search in.

	c --> character to be searched.

	n --> number of bytes or characters to check.

RETURN VALUE
	a pointer to the matching byte or NULL if the character does not occur in
	the given memory area.
================================================================================
*/

void	*ft_memchr(const void *s, int c, size_t n)
{
	size_t			i;
	unsigned char	*str;
	unsigned char	ch;

	str = (unsigned char *)s;
	ch = (unsigned char)c;
	i = 0;
	while (i < n)
	{
		if (str[i] == ch)
			return (&str[i]);
		i++;
	}
	return (NULL);
}
