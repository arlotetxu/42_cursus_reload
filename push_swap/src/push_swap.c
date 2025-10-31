/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   push_swap.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joflorid <joflorid@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/27 10:41:59 by joflorid          #+#    #+#             */
/*   Updated: 2025/10/31 16:06:25 by joflorid         ###   ########.fr       */
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
	#Si solo hay un numero, no hacer movimientos //?OK, se considera que la lista esta ordenada

	#Cargar numeros en nodos en stack a //?OK
	#Comprobar si la lista esta ordenada //?OK
	#Funcion para liberar stack (lista) //?OK
	#Funciones con los movimientos permitidos
		#ra/b //?OK
		#rr //?OK
		#rra/b //?OK
		#rrr //?OK
		#pb //?OK
		#pa //?OK
		#sa //?OK
		#sb //?OK
	#Pasar 2 a stack_b
	#Calcular target de cada numero en stack_a y cargarlo en sus datos //?OK
	#Calcular cuantos movimientos de cada tipo se necesitan para poner el nodo
		en su lugar correcto en stack_b.
	#Funcion para ordenar 3 nodos (numeros) //?OK
	#Funcion para ordenar 2 nodos (numeros) //?OK

*/

/*
	RETURNS EN MAIN
1 --> Wrong argument number
2 --> Wrong characters in the input (non digits or non digit after a sign)
3 --> There are duplicated numbers
4 --> Cannot get the string with all the arguments with ft_strjoin_2()
5 --> The arr_args couldn't nbe created at ft_load_stack_a()
6 --> The list is already sorted.
7 --> The stack_b couldn't be created
*/

static void	ft_launcher(t_node **stack_a, t_node **stack_b)
{
	ft_push_b(stack_a, stack_b);
	ft_push_b(stack_a, stack_b);
	ft_apply_target(*stack_a, *stack_b);
	//while (ft_check_sorting())
	//# Obtener el target en 'b' de cada elemento de 'a'
	//# Calcular el numero de movimientos en base al valor del indice respecto
	// de la mediana del tamaño del stack_a y stack_b
}

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
	t_node	*stack_b;

	if (argc < 2)
		return (1); //!Error
	full_args = ft_strjoin_2(argc, argv);
	stack_a = NULL;
	stack_b = NULL;
	ret = 0;
	if (argc >= 2)
		ret = ft_input_check(full_args);
	if (ret)
		return (free(full_args), ret);
	ret = ft_load_stack_a(full_args, &stack_a);
	if (ret)
		return (free(full_args), ret);
	if (ft_get_stack_size(stack_a) == 3)
		return (ft_sort_3(&stack_a, 'a'), 0);
	if (ft_get_stack_size(stack_a) == 2)
		return (ft_sort_2(&stack_a, 'a'), 0);
	ft_launcher(&stack_a, &stack_b);
	//ft_rotate(&stack_a, 'a');
	//ft_rotate_r(&stack_a, 'a');
	//ft_printf("Tamaño stack_a: %i\n", ft_get_stack_size(stack_a));
	// ft_push_b(&stack_a, &stack_b);
	// ft_push_b(&stack_a, &stack_b);
	// ft_swap(&stack_a, 'a');
	// ft_swap(&stack_b, 'b');
	// ft_push_a(&stack_a, &stack_b);
	// ft_push_a(&stack_a, &stack_b);
	ft_printf("============STACK_A=================\n");
	ft_print_stack(stack_a);
	fflush(stdout);
	ft_printf("============STACK_B=================\n");
	ft_print_stack(stack_b);
	fflush(stdout);
	free(full_args);
	ft_free_stack(&stack_a);
	ft_free_stack(&stack_b);
	return (ret);
}
