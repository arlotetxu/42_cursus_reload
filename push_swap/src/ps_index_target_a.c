/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ps_index_target_a.c                                :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joflorid <joflorid@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/31 10:40:18 by joflorid          #+#    #+#             */
/*   Updated: 2025/11/06 12:58:20 by joflorid         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../inc/libft/libft.h"
#include "push_swap.h"

/*==============================================================================
DESCRIPTION:
	ft_apply_index() adds to the node data (n_data) the index of the node
	within the list. This information is needed to calculate the cheapest
	movements later on (i.e ra or rra).

PARAMETERS:
	*stack --> a pointer to the stack

RETURN:

==============================================================================*/
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

/*==============================================================================
DESCRIPTION:
	ft_find_target_a() gets the target number whithin the stack_b after pushing
	the numbers to it. In this case (stack_a), the target of each number in
	stack_a is the closest number in stack_b being it less.
	If there is not a less number, then the target is the maximum value of
	stack_b.

PARAMETERS:
	*node_a --> a pointer to the node to get the target.

	*stack_b --> a pointer to the list in which look for the target.

RETURN:
	Nothing.
==============================================================================*/
static void	ft_find_target_a(t_node *node_a, t_node *stack_b)
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

/*==============================================================================
DESCRIPTION:
	ft_apply_target_a() adds the target found to the node information (n_data)
	through the function ft_find_target(). ft_apply_target_a() passes each node
	of the stack_a to the ft_find_target() to find and save the right target.

PARAMETERS:
	*stack_a --> a pointer to the list stack_a.

	*stack_b --> a pointer to the list stack_b.

RETURN:
	Nothing.
==============================================================================*/
void	ft_apply_target_a(t_node *stack_a, t_node *stack_b)
{
	t_node	*cur_a;

	if (!stack_a || !stack_b)
		return ;
	cur_a = stack_a;
	while (cur_a)
	{
		ft_find_target_a(cur_a, stack_b);
		cur_a = cur_a->next;
	}
}
