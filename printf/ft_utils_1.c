/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_utils_1.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joflorid <joflorid@student.42urduliz.co    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/05 13:08:02 by joflorid          #+#    #+#             */
/*   Updated: 2025/10/12 10:35:49 by joflorid         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf.h"

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
// !A PARTIR DE AQUI ES ITOA Y HABRIA QUE BORRAR
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

size_t	ft_strlcpy(char *dst, const char *src, size_t size)
{
	size_t	i;

	if (!src || !dst)
		return (0);
	if (size == 0)
		return (ft_strlen(src));
	i = 0;
	while (i < (size - 1) && src[i] != '\0')
	{
		dst[i] = src[i];
		i++;
	}
	dst[i] = '\0';
	return (ft_strlen(src));
}

size_t	ft_strlen(const char *s)
{
	size_t	len;

	len = 0;
	while (s[len] != '\0')
		len++;
	return (len);
}