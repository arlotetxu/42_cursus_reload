/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_isprint.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joflorid <joflorid@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/09/15 13:33:41 by joflorid          #+#    #+#             */
/*   Updated: 2025/09/24 12:02:48 by joflorid         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

/*
================================================================================
DESCRIPTION
	The  ft_isprint() function checks if a value (given as ascii value - int)
	is within the printable set of ascii values.
	Prototype:
	int	ft_isprint(int c)

PARAMETERS
	c --> ascii value (int).

RETURN VALUE
	1 --> the value is alphabetical.

	0 --> the value is not alphabetical.
================================================================================
*/

int	ft_isprint(int c)
{
	return (c >= 32 && c <= 126);
}
