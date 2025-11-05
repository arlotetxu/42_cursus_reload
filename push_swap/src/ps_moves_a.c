/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ps_moves_a.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joflorid <joflorid@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/31 15:58:50 by joflorid          #+#    #+#             */
/*   Updated: 2025/11/05 15:26:16 by joflorid         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../inc/libft/libft.h"
#include "push_swap.h"

void	ft_init_moves(t_node *node)
{
	node->n_data.ra = 0;
	node->n_data.rb = 0;
	node->n_data.rra = 0;
	node->n_data.rrb = 0;
	node->n_data.rr = 0;
	node->n_data.rrr = 0;
	node->n_data.total = 0;
}

void	ft_opti_moves(t_node **stack)
{
	t_node	*cur;

	cur = *stack;
	while (cur != NULL)
	{
		if (cur->n_data.ra > 0 && cur->n_data.rb > 0
			&& cur->n_data.ra >= cur->n_data.rb)
			cur->n_data.rr = cur->n_data.rb;
		else if (cur->n_data.ra > 0 && cur->n_data.rb > 0
			&& cur->n_data.ra < cur->n_data.rb)
			cur->n_data.rr = cur->n_data.ra;
		if (cur->n_data.rra > 0 && cur->n_data.rrb > 0
			&& cur->n_data.rra >= cur->n_data.rrb)
			cur->n_data.rrr = cur->n_data.rrb;
		else if (cur->n_data.rra > 0 && cur->n_data.rrb > 0
			&& cur->n_data.rra < cur->n_data.rrb)
			cur->n_data.rrr = cur->n_data.rra;
		cur->n_data.total = (cur->n_data.ra - cur->n_data.rr)
			+ (cur->n_data.rb - cur->n_data.rr)
			+ (cur->n_data.rra - cur->n_data.rrr)
			+ (cur->n_data.rrb - cur->n_data.rrr)
			+ cur->n_data.rr + cur->n_data.rrr;
		cur = cur->next;
	}
}

void	ft_get_moves_a_t(t_node **stack_a, t_node **stack_b)
{
	t_node	*cur_a;
	t_node	*cur_b;
	int		s_size_b;

	s_size_b = ft_get_stack_size(*stack_b);
	cur_a = *stack_a;
	while (cur_a != NULL)
	{
		cur_b = *stack_b;
		while (cur_b != NULL)
		{
			if (cur_a->n_data.target == cur_b->n_data.nb
				&& cur_b->n_data.index != 0)
			{
				if (s_size_b - cur_b->n_data.index < cur_b->n_data.index)
					cur_a->n_data.rrb = s_size_b - cur_b->n_data.index;
				else
					cur_a->n_data.rb = cur_b->n_data.index;
			}
			cur_b = cur_b->next;
		}
		cur_a = cur_a->next;
	}
}

void	ft_get_moves_a(t_node **stack_a, t_node **stack_b)
{
	t_node	*current;
	int		s_size_a;

	if (!stack_a)
		return ;
	s_size_a = ft_get_stack_size(*stack_a);
	current = *stack_a;
	while (current != NULL)
	{
		ft_init_moves(current);
		if (current->n_data.index != 0)
		{
			if (s_size_a - current->n_data.index < current->n_data.index)
				current->n_data.rra = s_size_a - current->n_data.index;
			else
				current->n_data.ra = current->n_data.index;
		}
		current = current->next;
	}
	ft_get_moves_a_t(stack_a, stack_b);
	ft_opti_moves(stack_a);
}
