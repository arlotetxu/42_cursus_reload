/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_utils_1.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joflorid <joflorid@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/05 13:08:02 by joflorid          #+#    #+#             */
/*   Updated: 2025/10/13 14:14:12 by joflorid         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf.h"

/*==============================================================================
DESCRIPTION:
	This function calculates the number of characters needed to convert an
	unsigned long in hexadecimal format.

PARAMETER:
	n --> usigned long to be evaluated.

RETURN:
	The number of characters needed to print the nbr in hexadecimal format.
==============================================================================*/
int	ft_hex_len(unsigned long n)
{
	int	len;

	len = 0;
	if (n == 0)
		return (1);
	while (n > 0)
	{
		n /= 16;
		len++;
	}
	return (len);
}

/*==============================================================================
DESCRIPTION:
	This function calculates the number of digits in an unsigned int number.

PARAMETER:
	nbr --> usigned int to be evaluated.

RETURN:
	The number of digits of nbr.
==============================================================================*/
int	ft_nbr_uint_len(unsigned int nbr)
{
	int	len;

	len = 0;
	if (nbr == 0)
		return (1);
	while (nbr != 0)
	{
		len++;
		nbr = nbr / 10;
	}
	return (len);
}
