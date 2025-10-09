/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   utils.c                                            :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joflorid <joflorid@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/05 13:08:02 by joflorid          #+#    #+#             */
/*   Updated: 2025/10/09 13:23:34 by joflorid         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "printf.h"

static int	ft_hex_len(unsigned long n)
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

char	*ft_int_hexa(unsigned long n)
{
	char	*hex_chars;
	char	*result;
	int		len;

	hex_chars = "0123456789abcdef";
	len = ft_hex_len(n);
	result = (char *)malloc(sizeof(char) * (len + 1)); //!!MALLOC
	if (!result)
		return (NULL);
	result[len] = '\0';
	if (n == 0)
	{
		result[0] = '0';
		return (result);
	}
	while (len > 0)
	{
		len--;
		result[len] = hex_chars[n % 16];
		n /= 16;
	}
	return (result); //!!Ojo que hay que retornar los caracteres imprimidos en pantalla
}

