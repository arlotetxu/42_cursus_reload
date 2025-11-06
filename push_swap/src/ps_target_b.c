/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ps_target_b.c                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joflorid <joflorid@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/04 10:23:02 by joflorid          #+#    #+#             */
/*   Updated: 2025/11/06 12:56:29 by joflorid         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../inc/libft/libft.h"
#include "push_swap.h"

/*==============================================================================
DESCRIPTION:
	ft_find_target_b() gets the target number whithin the stack_a.
	In this case (stack_b), the target of each number in stack_b is the closest
	number in stack_a being it greater than the evaluated.
	If there is not a greater number, then the target is the minimum value of
	stack_a.

PARAMETERS:
	*node_b --> a pointer to the node to get the target.

	*stack_a --> a pointer to the list in which look for the target.

RETURN:
	Nothing.
==============================================================================*/
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

/*==============================================================================
DESCRIPTION:
	ft_apply_target_b() adds the target found to the node information (n_data)
	through the function ft_find_target_b(). ft_apply_target_b() passes each
	node of the stack_b to the ft_find_target_b() to find and save the right
	target.

PARAMETERS:
	*stack_a --> a pointer to the list stack_a.

	*stack_b --> a pointer to the list stack_b.

RETURN:
	Nothing.
==============================================================================*/
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
