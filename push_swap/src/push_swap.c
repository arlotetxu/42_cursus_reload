/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   push_swap.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joflorid <joflorid@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/27 10:41:59 by joflorid          #+#    #+#             */
/*   Updated: 2025/11/04 16:42:27 by joflorid         ###   ########.fr       */
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
	#Pasar 2 a stack_b //?OK
	#Calcular target de cada numero en stack_a y cargarlo en sus datos //?OK
	#Calcular cuantos movimientos de cada tipo se necesitan para poner el nodo
		en su lugar correcto en stack_b. //?OK
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


/*
He revisado la estructura general de tu código en la carpeta src y, en general, la lógica que has implementado sigue correctamente las fases principales del algoritmo Turco. ¡Buen trabajo!

Has dividido el problema en las partes correctas y la secuencia de llamadas en tu main y ft_launcher es la adecuada.

Aquí tienes un análisis de lo que está bien y algunos puntos de mejora o posibles errores a tener en cuenta:

Lo que está bien (La lógica general es correcta)
Fase de Inicialización (ft_launcher en push_swap.c):

Empiezas moviendo dos nodos de A a B con ft_push_b. Esto es correcto, ya que crea un stack_b con el que trabajar para calcular los targets.
El bucle principal while (ft_get_stack_size(*stack_a) > 3) es la condición de parada correcta para esta fase.
Cálculo de Costes (El corazón del algoritmo):

Dentro del bucle, llamas a ft_get_moves. Esta función orquesta correctamente los pasos:
Calcula los costes de ra/rra para cada nodo en A.
Llama a ft_get_moves_t, que a su vez depende de ft_apply_target (en ps_utils_2.c) para encontrar el target en B y luego calcular los costes de rb/rrb.
Llama a ft_opti_moves para encontrar movimientos rr y rrr y calcular el total.
Esta secuencia es la implementación correcta de la fase de cálculo de costes del algoritmo.
Selección y Ejecución (ps_mov_a2b.c):

Después de calcular los costes, llamas a ft_do_moves.
Esta función primero llama a ft_node2pass para encontrar el nodo con el total más bajo, lo cual es correcto.
Luego, ejecuta la secuencia de movimientos (rr, rrr, ra, rb, etc.) y finaliza con ft_push_b. Esto también es correcto.
Fases Finales (ft_launcher):

Una vez que en A solo quedan 3 nodos, llamas a ft_sort_3 (asumo que está en ps_algorithm_3_2.c). Correcto. //?AQUI
Luego llamas a ft_mov_b2a para devolver los nodos de B a A. Correcto.
Finalmente, llamas a ft_final_sort para rotar A hasta que el número más pequeño quede arriba. Correcto.
Puntos a revisar y posibles errores
Aunque la estructura general es buena, hay algunos detalles en la implementación que podrían estar incorrectos o ser ineficientes.

Función ft_mov_b2a (No la he visto, pero es crucial):

Esta es la segunda parte más compleja del algoritmo. Para cada nodo en B, debes encontrar su posición correcta en A (el número más pequeño en A que sea más grande que el nodo de B).
Luego, debes calcular el coste para llevar ambos a la cima de sus respectivas pilas y hacer el pa. La lógica es similar a la de A->B, pero a la inversa. Asegúrate de que esta parte esté bien implementada.
Función ft_final_sort:

Esta función debe encontrar el nodo con el índice más bajo (o el número más pequeño) y calcular si es más barato usar ra o rra para llevarlo a la cima. La lógica es la misma que ya usas para calcular costes de un solo stack.
Conclusión
Tu programa tiene el esqueleto correcto del algoritmo Turco. Los problemas que has estado solucionando eran errores de implementación dentro de las funciones, pero la forma en que las llamas y la secuencia de operaciones es la adecuada.

Si el programa aún no ordena correctamente, los errores probablemente se encuentren en:

Las fórmulas exactas de cálculo de costes (rra/rrb).
La implementación de la fase de retorno de B a A (ft_mov_b2a).
La ordenación final de la pila A (ft_final_sort).
¡Estás muy cerca! Ahora es cuestión de depurar estas fases finales.
*/

static void	ft_launcher(t_node **stack_a, t_node **stack_b)
{
	ft_push_b(stack_a, stack_b);
	ft_push_b(stack_a, stack_b);

	while (ft_get_stack_size(*stack_a) > 3)
	{
		ft_apply_target_a(*stack_a, *stack_b);
		ft_get_moves_a(stack_a, stack_b);
		ft_do_moves(stack_a, stack_b, 'a');
	}
	ft_sort_3(stack_a, 'a');

	while (ft_get_stack_size(*stack_b) != 0)
	{
		ft_apply_target_b(*stack_a, *stack_b);
		ft_get_moves_b(stack_a, stack_b);
		ft_do_moves(stack_a, stack_b, 'b');
	}
	//COMPROBAR DONDE ESTA EL VALOR MINIMO Y LLEVARLO ARRIBA DE LA MANERA MAS BARATA
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
