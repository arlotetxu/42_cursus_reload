/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ps_utils_6.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joflorid <joflorid@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/04 16:46:51 by joflorid          #+#    #+#             */
/*   Updated: 2025/11/05 13:57:40 by joflorid         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../inc/libft/libft.h"
#include "push_swap.h"

int	ft_min_index(t_node **stack)
{
	t_node	*curr;
	int		min;
	int		min_ind;

	curr = *stack;
	min = curr->n_data.nb;
	min_ind = curr->n_data.index;
	while (curr != NULL)
	{
		if (curr->n_data.nb < min)
		{
			min = curr->n_data.nb;
			min_ind = curr->n_data.index;
		}
		curr = curr->next;
	}
	return (min_ind);
}

void	ft_last_sort(t_node **stack_a)
{
	int		stack_size;
	int		min_index;
	int		moves;

	min_index = ft_min_index(stack_a);
	stack_size = ft_get_stack_size(*stack_a);
	if (stack_size - min_index < min_index)
	{
		moves = stack_size - min_index;
		while (moves > 0)
		{
			ft_rotate_r(stack_a, 'a');
			moves--;
		}
	}
	else
	{
		while (min_index > 0)
		{
			ft_rotate(stack_a, 'a');
			min_index--;
		}
	}
}
