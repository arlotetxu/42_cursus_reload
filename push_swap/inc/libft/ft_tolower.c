/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_tolower.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joflorid <joflorid@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/09/17 10:37:16 by joflorid          #+#    #+#             */
/*   Updated: 2025/09/17 10:45:34 by joflorid         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

/*
================================================================================
DESCRIPTION
	The  ft_tolower() function converts a uppercase alpha character into their
	corresponding lowercase.

	Prototype:
	int	ft_tolower(int c);

PARAMETERS
	c --> integer value that represents the character to be converted.


RETURN VALUE
	the converted character or the same character in case it was already
	in lowercase or it is a non alpha character.
================================================================================
*/

int	ft_tolower(int c)
{
	if (c >= 65 && c <= 90)
		return (c + 32);
	return (c);
}
