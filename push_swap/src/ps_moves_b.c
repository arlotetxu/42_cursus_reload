/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ps_utils_5.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joflorid <joflorid@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/04 11:01:49 by joflorid          #+#    #+#             */
/*   Updated: 2025/11/04 16:38:42 by joflorid         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../inc/libft/libft.h"
#include "push_swap.h"

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
