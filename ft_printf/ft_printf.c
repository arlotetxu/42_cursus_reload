/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_printf.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joflorid <joflorid@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/01 15:00:17 by joflorid          #+#    #+#             */
/*   Updated: 2025/10/13 14:15:58 by joflorid         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf.h"

/*==============================================================================
DESCRIPTION:
	ft_distributor() calls different functions to perform the writting depending
	on the placeholder received (the character after the '%' character).

PARAMETERS:
	c --> the placeholder (s, c, %, x, X, p, i, d, u)

	args --> a pointer to the variadic arguments list. Be carefull... each time
	we call the list (with va_arg), it updates its position to the next varible
	in the variadic list.

RETURN:
	The number of characters printed.
==============================================================================*/
int	ft_distributor(int c, va_list *args)
{
	unsigned long	n;

	if (c == 's')
		return (ft_print_string(va_arg(*args, char *)));
	else if (c == 'c')
		return (ft_print_char(va_arg(*args, int)));
	else if (c == '%')
		return (ft_print_char('%'));
	else if (c == 'x' || c == 'X')
		return (ft_print_hexa(va_arg(*args, unsigned int), c));
	else if (c == 'p')
	{
		n = va_arg(*args, unsigned long);
		if (n == 0)
			return (ft_print_string("(nil)"));
		return (ft_print_string("0x") + ft_print_hexa(n, 'x'));
	}
	else if (c == 'i' || c == 'd')
		return (ft_print_int(va_arg(*args, int)));
	else if (c == 'u')
		return (ft_print_uint(va_arg(*args, unsigned int)));
	return (0);
}

/*==============================================================================
DESRIPTION:
	ft_printf() checks if there is any '%' character in the string
	passed as argument and stores the next character in the variable p_h to
	be passed to the function ft_distributor(9.)
	If not any '%' is found, the functions prints the character and add +1 to
	the varible count.

PARAMETERS:
	str --> String to be evaluated

	... --> variadic arguments. They could be a range of different variables
		identified depending on the character read after the '%' character.

RETURN:
	The number of characters printed. Same behaviour than standar C function
	printf().
==============================================================================*/
int	ft_printf(char const *str, ...)
{
	char	p_h;
	va_list	args;
	int		count;

	va_start(args, str);
	count = 0;
	while (*str)
	{
		if (*str == '%')
		{
			p_h = *(++str);
			count += ft_distributor(p_h, &args);
			str++;
		}
		else
		{
			write(1, str, 1);
			count++;
			str++;
		}
	}
	va_end(args);
	return (count);
}

int	main(void)
{
	unsigned long	p = NULL;
	unsigned int	i = 1591817179;

	printf("Retorno: %i\n", ft_printf("%s -- %s %c %% %x %X end.", "Hello",
		"World!!", 'X', p, p));

	printf("\n===========impresion de memoria===========\n");
	printf("p en estandar: %p\n", &p);
	fflush(stdout);
	ft_printf("p en creada: %p\n", &p);
	printf("p en estandar: %p\n", (void *)0);
	fflush(stdout);
	ft_printf("p en creada: %p\n", 0);

	printf("\n===========impresion hexadecimal min===========\n");
	printf("\np en hexa estandar: %lx\n", p);
	fflush(stdout);
	ft_printf("p en hexa creada: %x\n", p);

	printf("\n===========impresion hexadecimal may===========\n");
	printf("\np en hexa estandar: %lx\n", p);
	fflush(stdout);
	ft_printf("p en hexa creada: %X\n", p);

	printf("\n===========impresion cadena===========\n");
	printf("%s\n", "Esto es una cadena");
	fflush(stdout);
	ft_printf("%s\n", "Esto es una cadena");

	printf("\n===========impresion caracter===========\n");
	printf("Caracter: %c\n", 'E');
	fflush(stdout);
	ft_printf("Caracter: %c\n", 'E');

	printf("\n===========impresion int===========\n");
	printf("int: %i\n", i);
	fflush(stdout);
	ft_printf("int: %i\n", i);

	printf("\n===========impresion de porcentage===========\n");
	fflush(stdout);
	printf("%% probando\n");
	fflush(stdout);
	ft_printf("%% probando\n");

	printf("\n===========impresion unsigned int (%%u)===========\n");
	printf("u_int: %u\n", (unsigned int)-1);
	fflush(stdout);
	ft_printf("u_int: %u\n", (unsigned int)-1);

	printf("\n===========impresion unsigned int (%%u)===========\n");
	printf("u_int: %u\n", i);
	fflush(stdout);
	ft_printf("u_int: %u\n", i);

	return (0);
}
