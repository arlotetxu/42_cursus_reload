/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ps_last_sort.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joflorid <joflorid@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/04 16:46:51 by joflorid          #+#    #+#             */
/*   Updated: 2025/11/06 11:34:21 by joflorid         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../inc/libft/libft.h"
#include "push_swap.h"

/*==============================================================================
DESCRIPTION:
	ft_min_index() gets and returns the index of the minimum value in the stack
	passed as argument. This is helpful to calculate later on the cheapest
	movements at the end of the algorithim process, when all the numbers are
	again in the stack_a sorted but rotated.

PARAMETERS:
	**stack --> A pointer to the stack in which look for the minimum value.

RETURN:
	min_ind --> The index of the minimum value in the stack.
==============================================================================*/
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

/*==============================================================================
DESCRIPTION:
	ft_last_sort() calculates and makes the cheapest movements to get the
	stack_a sorted.

PARAMETERS:
	**stack_a --> A pointer to the stack to be sorted.

RETURN:
	Nothing.
==============================================================================*/
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
