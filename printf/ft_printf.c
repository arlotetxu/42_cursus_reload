/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_printf.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joflorid <joflorid@student.42urduliz.co    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/01 15:00:17 by joflorid          #+#    #+#             */
/*   Updated: 2025/10/05 13:49:18 by joflorid         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "printf.h"

/*
%c --> OK
%s --> OK
%p
%d
%i
%u
%x
%X
%% --> OK
*/


int	ft_distributor(int c, va_list *args)
{
	if (c == 's')
		return(ft_print_string(va_arg(*args, char *)));
		//printf("Valor de va_arg: %d\n", va_arg(args, int));
	else if (c == 'c')
		return(ft_print_char(va_arg(*args, int)));
	else if (c == '%')
	{
		write(1, "%", 1);
		return (1);
	}
	return (0);
}

int	ft_printf(char const *str, ...)
{
	char	p_h;
	va_list	args;
	int		count;
	//va_list copy_args;

	//printf("str: %s\n", str);
	va_start(args, str);
	//va_copy(copy_args, args);
	count = 0;
	while(*str)
	{
		    //printf("Procesando carácter: '%c' (ASCII: %d)\n", *str, *str);  // DEBUG
		if (*str == '%')
		{
			p_h = *(++str);
			//printf("Especificador encontrado: '%c'\n", p_h);  // DEBUG
			//printf("valor de p_h en ft_print: %c\n", p_h);
			count += ft_distributor(p_h, &args);
			//str++;
		}
		else
		{
			write(1, str, 1);
			count++;
		}
		str++;
	}
	va_end(args);
	return (count);
}

int	main(void)
{
	int	p = -5345;
	//printf("Retorno: %i\n", ft_printf("%s -- %s %c %% end.", "Hello", "World!!", 'X'));
	printf("p en pointer: %p\n", &p);
	printf("p en hexa estandar: %x\n", p);
	printf("p en hexa creada: %s\n", ft_int_hexa(p));
	return (0);
}