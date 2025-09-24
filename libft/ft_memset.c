/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_memset.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joflorid <joflorid@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/09/15 14:30:31 by joflorid          #+#    #+#             */
/*   Updated: 2025/09/24 13:18:34 by joflorid         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

/*
================================================================================
DESCRIPTION
	The  memset() function fills the first n bytes of the memory area
	pointed to by s with the constant byte c.
	Prototype:
	void	*memset(void *s, int c, size_t n);

PARAMETERS
	s --> string to add the 'c' value to. WARNING!! As the string is declared
		as void *, the compiler doesn't know the size of the value pointed in,
		so it is needed to cast the string 's' to a unsigned char *.

	c --> value to add to the first n bytes of the string pointed by 's'.

	n --> quantity of 'c' to be added to the string 's'. They are added at the
		begining of the string. It is casted to unsigned char in order to avoid
		issues with values grater than 127 (ascii)

RETURN VALUE
	The memset() function returns a pointer to the memory area s.
================================================================================
*/

void	*ft_memset(void *s, int c, size_t n)
{
	size_t	i;

	i = -1;
	while (++i < n)
		((unsigned char *)s)[i] = (unsigned char)c;
	return (s);
}
