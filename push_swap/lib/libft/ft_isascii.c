/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_isascii.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joflorid <joflorid@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/09/15 13:14:01 by joflorid          #+#    #+#             */
/*   Updated: 2025/09/24 12:00:23 by joflorid         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

/*
================================================================================
DESCRIPTION
	The  ft_isascii() function checks if a value (given as ascii value - int)
	is withing the ascii code.
	Prototype:
	int	ft_isascii(int c)

PARAMETERS
	c --> ascii value (int).

RETURN VALUE
	1 --> the value is an ascii value.

	0 --> the value is not an ascii value.
================================================================================
*/

int	ft_isascii(int c)
{
	return ((c >= 0 && c <= 127));
}
