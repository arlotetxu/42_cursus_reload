/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_printf.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joflorid <joflorid@student.42urduliz.co    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/01 15:00:17 by joflorid          #+#    #+#             */
/*   Updated: 2025/10/05 09:44:51 by joflorid         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdarg.h>
#include <stdio.h>
#include <unistd.h>
/*

*/
static void	ft_print_string(char *str)
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

static void	ft_print_char(int c)
{
	char	c_c;

	c_c = (char)c;
	write(1, &c_c, 1);
}

static void	ft_distributor(int c, va_list *args)
{
	//printf("valor de c en distributor: %d\n", c);
	if (c == 's')
		ft_print_string(va_arg(*args, char *));
		//printf("Valor de va_arg: %d\n", va_arg(args, int));
	else if (c == 'c')
		ft_print_char(va_arg(*args, int));
}

int	ft_printf(char const *str, ...)
{
	char	p_h;
	va_list	args;
	//va_list copy_args;

	//printf("str: %s\n", str);
	va_start(args, str);
	//va_copy(copy_args, args);
	while(*str)
	{
		    //printf("Procesando carácter: '%c' (ASCII: %d)\n", *str, *str);  // DEBUG
		if (*str == '%')
		{
			p_h = *(++str);
			//printf("Especificador encontrado: '%c'\n", p_h);  // DEBUG
			//printf("valor de p_h en ft_print: %c\n", p_h);
			ft_distributor(p_h, &args);
			//str++;
		}
		else
			write(1, str, 1);
		str++;
	}
	va_end(args);
	return (0);
}

int	main(void)
{
	ft_printf("%s -- %s %c", "Hello", " World!!", 'X');
	return (0);
}