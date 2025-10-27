/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_atoi.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joflorid <joflorid@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/09/17 16:36:08 by joflorid          #+#    #+#             */
/*   Updated: 2025/09/17 17:11:11 by joflorid         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

/*
================================================================================
DESCRIPTION
	The function ft_atoi() converts the alpha numbers contained in the string
	'nptr' in an integer number. Atoi does not detect errors. The right string
	composition should be:
	1 - spaces or values from 9 to 13 in ascii code.
	2 - only one sign.
	3 - numeric characters
	Other different string composition must return 0.

	Prototype:
	int	ft_atoi(const char *nptr);

PARAMETERS
	nptr --> String that have alpha numbers

RETURN VALUE
	0 --> If the conversion cannot be done.

	Converted value
================================================================================
*/

static int	ft_count_sign(const char *ptr)
{
	int	i;
	int	count;

	count = 0;
	i = 0;
	while (ptr[i] == '+' || ptr[i] == '-')
	{
		count++;
		i++;
	}
	return (count);
}

int	ft_atoi(const char *nptr)
{
	int	i;
	int	result;
	int	sign;

	result = 0;
	sign = 1;
	i = 0;
	while (nptr[i] == 32 || (nptr[i] >= 9 && nptr[i] <= 13))
		i++;
	while (nptr[i] == '+' || nptr[i] == '-')
	{
		if (ft_count_sign(&nptr[i]) > 1)
			return (0);
		if (nptr[i] == '-')
			sign = -1;
		i++;
	}
	while (nptr[i] >= '0' && nptr[i] <= '9')
	{
		result = result * 10 + (nptr[i] - '0');
		i++;
	}
	return (result * sign);
}
