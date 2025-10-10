/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_prints_1.c                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joflorid <joflorid@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/05 10:17:29 by joflorid          #+#    #+#             */
/*   Updated: 2025/10/10 16:33:31 by joflorid         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf.h"

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

int	ft_print_char(int c)
{
	char	c_c;

	c_c = (char)c;
	write(1, &c_c, 1);
	return (1);
}

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
	ret = len;
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
	ft_print_string(result);
	free(result);
	return (ret);
}

int	ft_print_int(int n)
{
	char	*res;
	int		len;

	res = ft_itoa(n);
	len = ft_print_string(res);
	free(res);
	return (len);
}
