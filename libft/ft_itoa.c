/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_itoa.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joflorid <joflorid@student.42urduliz.co    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/09/19 15:16:34 by joflorid          #+#    #+#             */
/*   Updated: 2025/09/25 12:16:34 by joflorid         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

/*
================================================================================
DESCRIPTION
	The fuction ft_itoa() creates an string from an integer value.
	Prototype:
	char	*ft_itoa(int n);

PARAMETERS
	n --> Integer value to be converted.

RETURN VALUE
	A pointer to the string created.
================================================================================
*/

static int	ft_count_digits(int n)
{
	int	count;

	count = 0;
	if (n < 0)
	{
		count++;
		n = n * (-1);
	}
	if (n < 10)
		return (++count);
	while (n > 0)
	{
		count++;
		n = n / 10;
	}
	return (count);
}

static char	*ft_nbr_str(int n)
{
	char	*nbr;
	int		len;
	int		till;

	till = 0;
	len = ft_count_digits(n);
	nbr = malloc(sizeof(char) * (len + 1));
	if (!nbr)
		return (NULL);
	if (n < 0)
	{
		nbr[0] = '-';
		n *= -1;
		till = 1;
	}
	nbr[len] = '\0';
	while (len > till)
	{
		len--;
		nbr[len] = (n % 10) + '0';
		n = n / 10;
	}
	return (nbr);
}

char	*ft_itoa(int n)
{
	char	*nbr;

	if (n == -2147483648)
	{
		nbr = malloc(sizeof(char) * 12);
		if (!nbr)
			return (NULL);
		ft_strlcpy(nbr, "-2147483648", 12);
		return (nbr);
	}
	else
		nbr = ft_nbr_str(n);
	return (nbr);
}
