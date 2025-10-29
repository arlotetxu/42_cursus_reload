/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   push_swap.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joflorid <joflorid@student.42urduliz.co    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/27 10:41:59 by joflorid          #+#    #+#             */
/*   Updated: 2025/10/29 16:51:02 by joflorid         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../inc/libft/libft.h"
#include "push_swap.h"

/*
TASK LIST
	#Comprobación de que los caracteres en los argumentos son correctos //?OK
		# Comprobación de que tras un signo hay un numero //?OK
	#Comprobación de que no hay duplicados //?OK
		# funcion para liberar un doble puntero. //?OK
	#Comprobar que no se exceden los limites de un int //?OK Controlado en ft_atoi_2()

	#Cargar numeros en nodos en stack a //?OK
	#Comprobar si la lista esta ordenada //?OK
	#Funcion para liberar stack (lista)
	#Funciones con los movimientos permitidos
	#Pasar 2 a stack_b
	#Calcular target de cada numero en stack_a y cargarlo en sus datos
	#Calcular cuantos movimientos de cada tipo se necesitan para poner el nodo
		en su lugar correcto en stack_b.
	Funcion para ordenar 3 nodos (numeros);
*/

/*
	RETURNS EN MAIN
1 --> Wrong argument number
2 --> Wrong characters in the input (non digits or non digit after a sign)
3 --> There are duplicated numbers
4 --> Cannot get the string with all the arguments with ft_strjoin_2()
5 --> The arr_args couldn't nbe created at ft_load_stack_a()
6 --> The list is already sorted.
*/

static int	ft_input_check(char *full_args)
{
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
	return (0);
}

int	main(int argc, char **argv)
{
	int		ret;
	char	*full_args;
	t_node	*stack_a;
	// t_node	*stack_b;

	if (argc < 2)
		return (1); //!Error
	full_args = ft_strjoin_2(argc, argv);
	stack_a = NULL;
	// stack_b = NULL;
	ret = 0;
	if (argc >= 2)
		ret = ft_input_check(full_args);
	if (ret)
		return(free(full_args), ret);
	ret = ft_load_stack_a(full_args, &stack_a);
	ft_print_stack(stack_a);
	free(full_args);
	return (ret);
}
