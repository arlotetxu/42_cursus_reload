/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ps_utils_4.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joflorid <joflorid@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/04 10:23:02 by joflorid          #+#    #+#             */
/*   Updated: 2025/11/05 13:56:07 by joflorid         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../inc/libft/libft.h"
#include "push_swap.h"

static void	ft_find_target_b(t_node *node_b, t_node *stack_a)
{
	t_node	*curr_a;
	long	best_diff;
	int		target_found;

	best_diff = LONG_MAX;
	target_found = 0;
	curr_a = stack_a;
	while (curr_a)
	{
		if (curr_a->n_data.nb > node_b->n_data.nb
			&& (long)curr_a->n_data.nb - node_b->n_data.nb < best_diff)
		{
			best_diff = (long)curr_a->n_data.nb - node_b->n_data.nb;
			node_b->n_data.target = curr_a->n_data.nb;
			target_found = 1;
		}
		curr_a = curr_a->next;
	}
	if (!target_found)
		node_b->n_data.target = ft_get_min_in_stack(stack_a);
}

void	ft_apply_target_b(t_node *stack_a, t_node *stack_b)
{
	t_node	*cur_b;

	if (!stack_a || !stack_b)
		return ;
	cur_b = stack_b;
	while (cur_b)
	{
		ft_find_target_b(cur_b, stack_a);
		cur_b = cur_b->next;
	}
}

int	ft_get_min_in_stack(t_node *stack)
{
	int	min;

	min = stack->n_data.nb;
	while (stack)
	{
		if (stack->n_data.nb < min)
			min = stack->n_data.nb;
		stack = stack->next;
	}
	return (min);
}
