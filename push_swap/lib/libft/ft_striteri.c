/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_striteri.c                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joflorid <joflorid@student.42urduliz.co    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/09/20 11:37:01 by joflorid          #+#    #+#             */
/*   Updated: 2025/09/20 11:50:50 by joflorid         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

/*
================================================================================
DESCRIPTION
	The fuction ft_striteri() applies a function received as parameter to all the
	characters of the string pointed by 's'. The arguments the function 'f'
	receives are the index of the string and the address memory of each value
	of the string.
	Prototype:
	void	ft_striteri(char *s, void (*f)(unsigned int,char*));

PARAMETERS
	s --> String to apply the function 'f'.

	f --> Function to pass to 's'
		--> Unsigned int - index from 's
		--> char * - address of each character from 's'

RETURN VALUE
	Nothing.
================================================================================
*/

void	ft_striteri(char *s, void (*f)(unsigned int, char*))
{
	unsigned int	i;

	if (!s || !f)
		return ;
	i = 0;
	while (s[i])
	{
		f(i, &s[i]);
		i++;
	}
}
