/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ps_utils_2.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joflorid <joflorid@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/31 10:40:18 by joflorid          #+#    #+#             */
/*   Updated: 2025/10/31 15:47:50 by joflorid         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../inc/libft/libft.h"
#include "push_swap.h"

void	ft_apply_index(t_node *stack)
{
	int	i;

	if (!stack)
		return ;
	i = 0;
	while (stack != NULL)
	{
		stack->n_data.index = i;
		stack = stack->next;
		i++;
	}
}

static void	ft_find_target(t_node *node_a, t_node *stack_b)
{
	t_node	*curr_b;
	long	best_diff;
	int		target_found;

	best_diff = LONG_MAX;
	target_found = 0;
	curr_b = stack_b;
	while (curr_b)
	{
		if (curr_b->n_data.nb < node_a->n_data.nb
			&& (long)node_a->n_data.nb - curr_b->n_data.nb < best_diff)
		{
			best_diff = (long)node_a->n_data.nb - curr_b->n_data.nb;
			node_a->n_data.target = curr_b->n_data.nb;
			target_found = 1;
		}
		curr_b = curr_b->next;
	}
	if (!target_found)
		node_a->n_data.target = ft_get_max_in_stack(stack_b);
}

void	ft_apply_target(t_node *stack_a, t_node *stack_b)
{
	if (!stack_a || !stack_b)
		return ;
	while (stack_a)
	{
		ft_find_target(stack_a, stack_b);
		stack_a = stack_a->next;
	}
}

int	ft_get_max_in_stack(t_node *stack)
{
	int	max;

	max = stack->n_data.nb;
	while (stack)
	{
		if (stack->n_data.nb > max)
			max = stack->n_data.nb;
		stack = stack->next;
	}
	return (max);
}

int	ft_get_stack_size(t_node *stack)
{
	int	len;

	if (!stack)
		return (0);
	len = 0;
	while (stack != NULL)
	{
		len++;
		stack = stack->next;
	}
	return (len);
}
