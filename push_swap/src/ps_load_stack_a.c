/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ps_load_stack_a.c                                  :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joflorid <joflorid@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/29 11:35:54 by joflorid          #+#    #+#             */
/*   Updated: 2025/11/06 11:52:44 by joflorid         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../inc/libft/libft.h"
#include "push_swap.h"

/*==============================================================================
DESCRIPTION:
	ft_create_node() creates a new node and initilizes its values. Add the nb
	value from the argument nbr received.

PARAMETERS:
	nbr --> The number to be added to the node.

RETURN:
	new_node --> The new node created.
==============================================================================*/
static t_node	*ft_create_node(int nbr)
{
	t_node	*new_node;

	new_node = malloc (sizeof(t_node));
	if (!new_node)
		return (NULL);
	new_node->n_data.nb = nbr;
	new_node->n_data.index = 0;
	new_node->n_data.target = 0;
	new_node->n_data.ra = 0;
	new_node->n_data.rb = 0;
	new_node->n_data.rr = 0;
	new_node->n_data.rra = 0;
	new_node->n_data.rrb = 0;
	new_node->n_data.rrr = 0;
	new_node->n_data.total = 0;
	new_node->next = NULL;
	new_node->prev = NULL;
	return (new_node);
}

/*==============================================================================
DESCRIPTION:
	ft_insert_end() calls the function ft_create_node() to create a new node and
	puts it at the end of the stack_a.

PARAMETERS:
	**stack_a --> The stack in which the new node has to be added.

	nbr --> The number to be added to the node.

RETURN:
	Nothing.
==============================================================================*/
void	ft_insert_end(t_node **stack_a, int nbr)
{
	t_node	*new_node;
	t_node	*current;

	new_node = ft_create_node(nbr);
	if (!new_node)
		return ;
	if (!*stack_a)
	{
		*stack_a = new_node;
		return ;
	}
	current = *stack_a;
	while (current->next)
		current = current->next;
	current->next = new_node;
	new_node->prev = current;
}

/*==============================================================================
DESCRIPTION:
	ft_load_stack_a() calls the function ft_load_nbr_arr() to create a new
	integer array with all the input previously converted to int and then calls
	the function ft_insert_end() to start the loading of the stack_a. This
	function also call the function ft_apply_index() to add the index to each
	node created. Once the stack_a has been loaded, the string args_arr is
	freed.

PARAMETERS:
	*full_args --> A string that contains all the input arguments

	**stack_a --> The stack to be loaded.

RETURN:
	5 --> If the int array coudn't be created.

	6 --> if the stack_a is already sorted.

	0 --> OK
==============================================================================*/
int	ft_load_stack_a(char *full_args, t_node **stack_a)
{
	int	*args_arr;
	int	len;
	int	i;

	len = 0;
	args_arr = ft_load_nbr_arr(full_args, &len);
	if (!args_arr)
		return (5);
	i = -1;
	while (++i < len)
		ft_insert_end(stack_a, args_arr[i]);
	ft_apply_index(*stack_a);
	if (!ft_check_sorting(*stack_a))
		return (free(args_arr), 6);
	return (free(args_arr), 0);
}
