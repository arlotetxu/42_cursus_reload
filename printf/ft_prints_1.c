/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_prints_1.c                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joflorid <joflorid@student.42urduliz.co    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/05 10:17:29 by joflorid          #+#    #+#             */
/*   Updated: 2025/10/05 10:38:30 by joflorid         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "printf.h"

void	ft_print_string(char *str)
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
}

void	ft_print_char(int c)
{
	char	c_c;

	c_c = (char)c;
	write(1, &c_c, 1);
}