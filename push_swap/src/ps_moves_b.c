/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ps_moves_b.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joflorid <joflorid@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/04 11:01:49 by joflorid          #+#    #+#             */
/*   Updated: 2025/11/06 12:52:02 by joflorid         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../inc/libft/libft.h"
#include "push_swap.h"

/*==============================================================================
DESCRIPTION:
	ft_get_moves_b_t() calculates cheapest number of movements needed to bring
	the target node to the top of the stack_a and saves it in the node
	information (n_data).

PARAMETERS:
	**stack_a --> A pointer to the stack_a with the target nodes.

	**stack_b --> A pointer to the stack_b with the nodes to be evaluated.

RETURN:
	Nothing.
==============================================================================*/
void	ft_get_moves_b_t(t_node **stack_a, t_node **stack_b)
{
	t_node	*cur_a;
	t_node	*cur_b;
	int		s_size_a;

	s_size_a = ft_get_stack_size(*stack_a);
	cur_b = *stack_b;
	while (cur_b != NULL)
	{
		cur_a = *stack_a;
		while (cur_a != NULL)
		{
			if (cur_b->n_data.target == cur_a->n_data.nb
				&& cur_a->n_data.index != 0)
			{
				if (s_size_a - cur_a->n_data.index < cur_a->n_data.index)
					cur_b->n_data.rra = s_size_a - cur_a->n_data.index;
				else
					cur_b->n_data.ra = cur_a->n_data.index;
			}
			cur_a = cur_a->next;
		}
		cur_b = cur_b->next;
	}
}

/*==============================================================================
DESCRIPTION:
	ft_get_moves_b() calculates the cheapest number of movements needed to bring
	the evaluated node to the top of the stack_b and saves it in the node
	information (n_data). Then, calls the function ft_get_moves_b_t() to
	calculate and save the cheapest number of movements to bring the target node
	to the top of the stack_a. Finally, the functions calls the function
	ft_opti_moves() to try to optimize the total number of movements grouping
	ra & ra in rr and rra & rrb in rrr.

PARAMETERS:
	**stack_a --> A pointer to the stack_b with the target nodes.

	**stack_b --> A pointer to the stack_a with the nodes to be evaluated.

RETURN:
	Nothing.
==============================================================================*/
void	ft_get_moves_b(t_node **stack_a, t_node **stack_b)
{
	t_node	*current;
	int		s_size_b;

	if (!stack_b)
		return ;
	s_size_b = ft_get_stack_size(*stack_b);
	current = *stack_b;
	while (current != NULL)
	{
		ft_init_moves(current);
		if (current->n_data.index != 0)
		{
			if (s_size_b - current->n_data.index < current->n_data.index)
				current->n_data.rrb = s_size_b - current->n_data.index;
			else
				current->n_data.rb = current->n_data.index;
		}
		current = current->next;
	}
	ft_get_moves_b_t(stack_a, stack_b);
	ft_opti_moves(stack_b);
}
