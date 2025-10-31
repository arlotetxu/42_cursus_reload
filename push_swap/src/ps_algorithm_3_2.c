/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ps_algorithm_3_2.c                                 :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joflorid <joflorid@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/31 10:26:46 by joflorid          #+#    #+#             */
/*   Updated: 2025/10/31 15:38:51 by joflorid         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../inc/libft/libft.h"
#include "push_swap.h"

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

void	ft_sort_2(t_node **stack, char stack_id)
{
	if (!ft_check_sorting(*stack) || ft_get_stack_size(*stack) != 2)
		return ;
	ft_swap(stack, stack_id);
}
