/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ps_moves_1.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joflorid <joflorid@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/30 12:02:24 by joflorid          #+#    #+#             */
/*   Updated: 2025/10/30 14:14:23 by joflorid         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../inc/libft/libft.h"
#include "push_swap.h"

void	ft_rotate(t_node **stack, char stack_id)
{
	t_node	*first;
	t_node	*last;

	if (!stack || !*stack || !(*stack)->next)
		return ;
	first = *stack;
	last = *stack;
	while (last->next != NULL)
		last = last->next;
	*stack = first->next;
	(*stack)->prev = NULL;
	last->next = first;
	first->prev = last;
	first->next = NULL;
	if (stack_id == 'a' || stack_id == 'b')
		ft_printf("r%c\n", stack_id);
}

void	ft_rotate_2(t_node **stack_a, t_node **stack_b, char stack_id)
{
	if (!stack_a || !*stack_a || !(*stack_a)->next)
		return ;
	if (!stack_b || !*stack_b || !(*stack_b)->next)
		return ;
	if (stack_id != 'r')
		return ;
	ft_rotate(stack_a, stack_id);
	ft_rotate(stack_b, stack_id);
	ft_printf("rr%c\n", stack_id);
}

void	ft_rotate_r(t_node **stack, char stack_id)
{
	t_node	*first;
	t_node	*last;
	t_node	*prev;

	if (!stack || !*stack || !(*stack)->next)
		return ;
	first = *stack;
	last = *stack;
	while (last->next != NULL)
	{
		prev = last;
		last = last->next;
	}
	prev->next = NULL;
	last->prev = NULL;
	last->next = first;
	first->prev = last;
	*stack = last;
	ft_printf("rr%c\n", stack_id);
}

void	ft_rotate_r_2(t_node **stack_a, t_node **stack_b, char stack_id)
{
	if (!stack_a || !*stack_a || !(*stack_a)->next)
		return ;
	if (!stack_b || !*stack_b || !(*stack_b)->next)
		return ;
	if (stack_id != 'r')
		return ;
	ft_rotate_r(stack_a, stack_id);
	ft_rotate_r(stack_b, stack_id);
	ft_printf("rr%c\n", stack_id);
}
