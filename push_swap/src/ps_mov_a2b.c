/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ps_mov_a2b.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joflorid <joflorid@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/03 11:50:57 by joflorid          #+#    #+#             */
/*   Updated: 2025/11/03 13:26:23 by joflorid         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../inc/libft/libft.h"
#include "push_swap.h"

void	ft_do_moves(t_node **stack_a, t_node **stack_b)
{
	t_node	*select;

	select = ft_node2pass(stack_a);
	while (select->n_data.rr--)
		ft_rotate_2(stack_a, stack_b, 'r');
	while (select->n_data.rrr--)
		ft_rotate_r_2(stack_a, stack_b, 'r');
	while (select->n_data.ra--)
		ft_rotate(stack_a, 'a');
	while (select->n_data.rb--)
		ft_rotate(stack_b, 'b');
	while (select->n_data.rra--)
		ft_rotate_r(stack_a, 'a');
	while (select->n_data.rrb--)
		ft_rotate_r(stack_b, 'b');
	ft_push_b(stack_a, stack_b);
}

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
