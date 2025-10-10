/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_isalpha.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joflorid <joflorid@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/09/15 12:20:22 by joflorid          #+#    #+#             */
/*   Updated: 2025/09/24 11:59:10 by joflorid         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

/*
================================================================================
DESCRIPTION
	The  ft_isalpha() function checks if a value (given as ascii value - int)
	is alphabetical.
	Prototype:
	int	ft_isalpha(int c)

PARAMETERS
	c --> ascii value (int).

RETURN VALUE
	1 --> the value is alphabetical.

	0 --> the value is not alphabetical.
================================================================================
*/

int	ft_isalpha(int c)
{
	return ((c >= 65 && c <= 90) || (c >= 97 && c <= 122));
}
