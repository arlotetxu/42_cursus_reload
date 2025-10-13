/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_toupper.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joflorid <joflorid@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/09/17 10:24:51 by joflorid          #+#    #+#             */
/*   Updated: 2025/09/17 10:41:07 by joflorid         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

/*
================================================================================
DESCRIPTION
	The ft_toupper() function converts a lowercase alpha character into their
	corresponding uppercase.

	Prototype:
	int	ft_toupper(int c);

PARAMETERS
	c --> integer value that represents the character to be converted.


RETURN VALUE
	The converted character or the same character in case it was already
	in uppercase or it is a non alpha character.
================================================================================
*/

int	ft_toupper(int c)
{
	if (c >= 97 && c <= 122)
		return (c - 32);
	return (c);
}
