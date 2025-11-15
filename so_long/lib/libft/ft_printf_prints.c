/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_printf_prints.c                                 :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joflorid <joflorid@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/05 10:17:29 by joflorid          #+#    #+#             */
/*   Updated: 2025/10/27 10:28:08 by joflorid         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

/*==============================================================================
DESCRIPTION:
	This function prints a string using the write() function. If there is not a
	string, it prints "(null)". Same behaviour than standar printf() function.

PARAMETER:
	str --> a pointer to the string to be printed.

RETURN:
	The number of characters printed.
==============================================================================*/
int	ft_print_string(char *str)
{
	int	i;

	if (!str)
		str = "(null)";
	i = 0;
	while (str[i])
	{
		write(1, &str[i], 1);
		i++;
	}
	return (i);
}

/*==============================================================================
DESCRIPTION:
	This function prints a character using the write() function.

PARAMETER:
	c --> the character to be printed.

RETURN:
	The number of characters printed. In this case, always 1.
==============================================================================*/
int	ft_print_char(int c)
{
	char	c_c;

	c_c = (char)c;
	write(1, &c_c, 1);
	return (1);
}

/*==============================================================================
DESCRIPTION:
	This function prints an unsigned long variable in its hexadecimal
	equivalence.

PARAMETER:
	n --> the number to be printed in hexadecimal.

	c --> placeholder. 'x' to print in lowercase 6 'X' to print in uppercase.

RETURN:
	The number of characters printed.
==============================================================================*/
int	ft_print_hexa(unsigned long n, char c)
{
	char	*hex_chars;
	char	*hex_chars_u;
	char	*result;
	int		len;
	int		ret;

	hex_chars = "0123456789abcdef";
	hex_chars_u = "0123456789ABCDEF";
	if (c == 'X')
		hex_chars = hex_chars_u;
	len = ft_hex_len(n);
	result = malloc(sizeof(char) * (len + 1));
	if (!result)
		return (0);
	result[len] = '\0';
	while (len > 0)
	{
		len--;
		result[len] = hex_chars[n % 16];
		n /= 16;
	}
	ret = ft_print_string(result);
	free(result);
	return (ret);
}

/*==============================================================================
DESCRIPTION:
	This function prints an integer value. To do this, it uses the ft_itoa()
	function from libft library that converts an integer value in a string.

PARAMETER:
	n --> the number to be printed.

RETURN:
	The number of characters printed.
==============================================================================*/
int	ft_print_int(int n)
{
	char	*res;
	int		len;

	res = ft_itoa(n);
	len = ft_print_string(res);
	free(res);
	return (len);
}

/*==============================================================================
DESCRIPTION:
	This function prints an unsigned int number. It uses recursivity to do it.

PARAMETER:
	nbr --> unsigned int to be printed.

RETURN:
	The number of characters printed.
==============================================================================*/
int	ft_print_uint(unsigned int nbr)
{
	if (nbr >0 && nbr <= 9)
		ft_print_char(nbr + '0');
	if (nbr > 9)
	{
		ft_print_uint(nbr / 10);
		ft_print_uint(nbr % 10);
	}
	return (ft_nbr_uint_len(nbr));
}
