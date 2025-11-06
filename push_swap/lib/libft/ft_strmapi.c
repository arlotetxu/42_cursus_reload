/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strmapi.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joflorid <joflorid@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/09/19 17:28:44 by joflorid          #+#    #+#             */
/*   Updated: 2025/09/26 12:56:13 by joflorid         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

/*
================================================================================
DESCRIPTION
	The function ft_strmapi() passes a function received as parameter to all the
	characters of the string pointed by 's'. The arguments the function 'f'
	receives are the index of the string and the value of the index.
	Prototype:
	char *ft_strmapi(char const *s, char (*f)(unsigned int, char));

PARAMETERS
	s --> String to apply the function 'f'.

	f --> Function to pass to 's'
		--> Unsigned int - index from 's
		--> char - character from 's'

RETURN VALUE
	A pointer to the NEW string created after function 'f' application.
================================================================================
*/

char	*ft_strmapi(char const *s, char (*f)(unsigned int, char))
{
	unsigned int	i;
	char			*f_apply;

	if (!s || !f)
		return (NULL);
	f_apply = malloc (sizeof(char) * (ft_strlen(s) + 1));
	if (!f_apply)
		return (NULL);
	i = 0;
	while (s[i])
	{
		f_apply[i] = f(i, s[i]);
		i++;
	}
	f_apply[i] = '\0';
	return (f_apply);
}
