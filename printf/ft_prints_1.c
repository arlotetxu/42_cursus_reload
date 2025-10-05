/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_prints_1.c                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joflorid <joflorid@student.42urduliz.co    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/05 10:17:29 by joflorid          #+#    #+#             */
/*   Updated: 2025/10/05 12:35:09 by joflorid         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "printf.h"

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