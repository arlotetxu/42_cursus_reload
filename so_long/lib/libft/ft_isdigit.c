/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_isdigit.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joflorid <joflorid@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/09/15 12:39:22 by joflorid          #+#    #+#             */
/*   Updated: 2025/09/24 12:01:34 by joflorid         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

/*
================================================================================
DESCRIPTION
	The  ft_isdigit() function checks if a value (given as ascii value - int)
	is numeric.
	Prototype:
	int	ft_isdigit(int n)

PARAMETERS
	n --> ascii value (int).

RETURN VALUE
	1 --> the value is numeric.

	0 --> the value is not numeric.
================================================================================
*/

int	ft_isdigit(int n)
{
	return ((n >= 48 && n <= 57));
}
