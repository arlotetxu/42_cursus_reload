/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   push_swap.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joflorid <joflorid@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/27 10:41:59 by joflorid          #+#    #+#             */
/*   Updated: 2025/10/27 17:06:17 by joflorid         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../inc/libft/libft.h"
#include "push_swap.h"

/*
PENDIENTE
	#Comprobación de que los caracteres en los argumentos son correctos //?OK
	#Comprobación de que no hay duplicados
		# funcion para liberar un doble puntero.
	#Comprobar que no se exceden los limites de un int

*/

int	main(int argc, char **argv)
{
	t_node	*stack_a;
	t_node	*stack_b;

	stack_a = NULL;
	stack_b = NULL;

	if (argc >= 2)
	{
		if (ft_check_chars_argv(argc, argv))
		{
			ft_printf("\x1b[41mError\n\x1b[0m");
			return (1);
		}
		if (argc == 2)
		{
			ft_check_duplicates(argv);
		}
	}
	return (0);
}