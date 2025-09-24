/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_isalnum.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joflorid <joflorid@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/09/15 12:49:45 by joflorid          #+#    #+#             */
/*   Updated: 2025/09/24 11:59:14 by joflorid         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

/*
================================================================================
DESCRIPTION
	The  ft_isalnum() function checks if a value (given as ascii value - int)
	is alphabetical or numeric.
	Prototype:
	int	ft_isalnum(int c)

PARAMETERS
	c --> ascii value (int).

RETURN VALUE
	1 --> the value is alphanumeric.

	0 --> the value is not alphanumeric.
================================================================================
*/

int	ft_isalnum(int c)
{
	return ((ft_isalpha(c) || ft_isdigit(c)));
}
