/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ps_algorithm_3_2.c                                 :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joflorid <joflorid@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/31 10:26:46 by joflorid          #+#    #+#             */
/*   Updated: 2025/11/06 16:12:46 by joflorid         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../lib/libft/libft.h"
#include "../inc/push_swap.h"

/*==============================================================================
DESCRIPTION:
	ft_sort_3() sort a list of 3 nodes applying the right movements. This
	function is launch at the begining if the input is a stack of only 3 numbers
	and also during the sorting process with a larger stack.

PARAMETERS:
	**stack --> a pointer to the stack to be sorted

	stack_id --> identificacion of the stack. Needed to print the right
		movement when calling them

RETURN:
	Nothing. The function makes directly the movements not returning anything.
==============================================================================*/
void	ft_sort_3(t_node **stack, char stack_id)
{
	t_node	*a;
	t_node	*b;
	t_node	*c;

	if (!ft_check_sorting(*stack) || ft_get_stack_size(*stack) != 3)
		return ;
	a = (*stack);
	b = (*stack)->next;
	c = (*stack)->next->next;
	if (a->n_data.nb < b->n_data.nb && b->n_data.nb > c->n_data.nb \
		&& a->n_data.nb < c->n_data.nb)
		return (ft_rotate_r(stack, stack_id), ft_swap(stack, stack_id));
	else if (a->n_data.nb < b->n_data.nb && b->n_data.nb > c->n_data.nb \
		&& a->n_data.nb > c->n_data.nb)
		return (ft_rotate_r(stack, stack_id));
	else if (a->n_data.nb > b->n_data.nb && a->n_data.nb < c->n_data.nb)
		return (ft_swap(stack, stack_id));
	else if (a->n_data.nb > b->n_data.nb && a->n_data.nb > c->n_data.nb \
		&& b->n_data.nb < c->n_data.nb)
		return (ft_rotate(stack, stack_id));
	else if (a->n_data.nb > b->n_data.nb && a->n_data.nb > c->n_data.nb \
		&& b->n_data.nb > c->n_data.nb)
		return (ft_swap(stack, stack_id), ft_rotate_r(stack, stack_id));
}

/*==============================================================================
DESCRIPTION:
	ft_sort_2() sort a list of 2 nodes applying the right movements, in this

PARAMETERS:
	**stack --> a pointer to the stack to be sorted

	stack_id --> identificacion of the stack. Needed to print the right
		movement when calling them

RETURN:
	Nothing. The function makes directly the movement not returning anything.
==============================================================================*/
void	ft_sort_2(t_node **stack, char stack_id)
{
	if (!ft_check_sorting(*stack) || ft_get_stack_size(*stack) != 2)
		return ;
	ft_swap(stack, stack_id);
}
