/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ps_mov_a2b2a.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joflorid <joflorid@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/03 11:50:57 by joflorid          #+#    #+#             */
/*   Updated: 2025/11/06 12:19:38 by joflorid         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../inc/libft/libft.h"
#include "push_swap.h"

/*==============================================================================
DESCRIPTION:
	ft_do_moves_2() does the same actions than ft_do_moves() with the rest of
	the movements.

PARAMETERS:
	select --> A pointer to the node with the information about to the movements
		to be done. This node should be the one with the less total movements.

	**stack_a --> A pointer to the stack_a list.

	**stack_b --> A pointer to the stack_b list.

	stack_id --> Stack identification

RETURN:
	new_node --> The new node created.
==============================================================================*/
void	ft_do_moves_2(t_node *select, t_node **stack_a, t_node **stack_b, \
	char stack_id)
{
	int		rb_rem;
	int		rra_rem;
	int		rrb_rem;

	rb_rem = select->n_data.rb - select->n_data.rr;
	rra_rem = select->n_data.rra - select->n_data.rrr;
	rrb_rem = select->n_data.rrb - select->n_data.rrr;
	while (rb_rem-- > 0)
		ft_rotate(stack_b, 'b');
	while (rra_rem-- > 0)
		ft_rotate_r(stack_a, 'a');
	while (rrb_rem-- > 0)
		ft_rotate_r(stack_b, 'b');
	if (stack_id == 'a')
		ft_push_b(stack_a, stack_b);
	else if (stack_id == 'b')
		ft_push_a(stack_a, stack_b);
}

/*==============================================================================
DESCRIPTION:
	ft_do_moves() makes the corresponding movements according to the information
	contained in each node of the stack. The functions selects the right stack
	considering the value of the parameter stack_id. This function calls the
	function ft_do_moves_2() to continue with the movements passing to it the
	selected node in each case.

PARAMETERS:
	**stack_a --> A pointer to the stack_a list.

	**stack_b --> A pointer to the stack_b list.

	stack_id --> Stack identification

RETURN:
	Nothing.
==============================================================================*/
void	ft_do_moves(t_node **stack_a, t_node **stack_b, char stack_id)
{
	t_node	*select;
	int		ra_rem;
	int		rr;
	int		rrr;

	select = ft_node2pass(stack_b);
	if (stack_id == 'a')
		select = ft_node2pass(stack_a);
	ra_rem = select->n_data.ra - select->n_data.rr;
	rr = select->n_data.rr;
	rrr = select->n_data.rrr;
	while (rr-- > 0)
		ft_rotate_2(stack_a, stack_b, 'r');
	while (rrr-- > 0)
		ft_rotate_r_2(stack_a, stack_b, 'r');
	while (ra_rem-- > 0)
		ft_rotate(stack_a, 'a');
	ft_do_moves_2(select, stack_a, stack_b, stack_id);
}

/*==============================================================================
DESCRIPTION:
	ft_node2pass() selects and returns the node with the cheapest total
	movements from the stack passed as argument.

PARAMETERS:
	**stack --> A pointer to the stack to be evaluated.

RETURN:
	select --> The node with the lowest total movements (the cheapest).
==============================================================================*/
t_node	*ft_node2pass(t_node **stack)
{
	t_node	*select;
	t_node	*cur_a;
	int		total_m;

	total_m = INT_MAX;
	select = NULL;
	cur_a = *stack;
	while (cur_a != NULL)
	{
		if (cur_a->n_data.total < total_m)
		{
			total_m = cur_a->n_data.total;
			select = cur_a;
		}
		cur_a = cur_a->next;
	}
	return (select);
}
