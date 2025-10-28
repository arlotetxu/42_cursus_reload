/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   push_swap.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joflorid <joflorid@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/27 10:41:59 by joflorid          #+#    #+#             */
/*   Updated: 2025/10/28 17:01:52 by joflorid         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../inc/libft/libft.h"
#include "push_swap.h"

/*
PENDIENTE
	#Comprobación de que los caracteres en los argumentos son correctos //?OK
		# Comprobación de que tras un signo hay un numero //?OK
	#Comprobación de que no hay duplicados //?OK
		# funcion para liberar un doble puntero. //?OK
	#Comprobar que no se exceden los limites de un int //?OK Controlado en ft_atoi_2()

	#Cargar numeros en nodos en stack a
	#Funciones con los movimientos permitidos

*/

/*
	RETURNS EN MAIN
1 --> Wrong argument number
2 --> Wrong characters in the input (non digits or non digit after a sign)
3 --> There are duplicated numbers
4 --> Cannot get the string with all the arguments
*/
int	main(int argc, char **argv)
{
	char	*full_args;
	t_stack	*stack_a;
	t_stack	*stack_b;

	stack_a = NULL;
	stack_b = NULL;
	full_args = NULL;

	if (argc < 2)
		return (1); //!Error
	if (argc >= 2)
	{
		full_args = ft_strjoin_2(argc, argv);
		if (!full_args)
			return (4); //!Error
		if (ft_check_chars_argv(full_args))
		{
			ft_printf("\x1b[41mError\n\x1b[0m");
			return (2); //!Error
		}
		if (ft_check_dupli(full_args))
		{
			ft_printf("\x1b[41mError\n\x1b[0m"); //!Error
			return (3);
		}
	}
	return (0);
}
