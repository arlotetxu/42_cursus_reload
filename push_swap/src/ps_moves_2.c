/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ps_moves_2.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joflorid <joflorid@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/30 14:14:37 by joflorid          #+#    #+#             */
/*   Updated: 2025/10/30 16:49:26 by joflorid         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../inc/libft/libft.h"
#include "push_swap.h"

void	ft_push_b(t_node **stack_a, t_node **stack_b)
{
	t_node	*aux;

	if (!stack_a || !stack_b || !*stack_a)
		return;
	aux = *stack_a;
	*stack_a = (*stack_a)->next;
	if (*stack_a)
		(*stack_a)->prev = NULL;
	aux->prev = NULL;
	aux->next = *stack_b;
	if (*stack_b)
		(*stack_b)->prev = aux;
	*stack_b = aux;
	ft_printf("pb\n");
}

void	ft_push_a(t_node **stack_a, t_node **stack_b)
{
	t_node	*aux;

	if (!stack_b || !stack_a || !*stack_b)
		return;
	aux = *stack_b;
	*stack_b = (*stack_b)->next;
	if (*stack_b)
		(*stack_b)->prev = NULL;
	aux->prev = NULL;
	aux->next = *stack_a;
	if (*stack_a)
		(*stack_a)->prev = aux;
	*stack_a = aux;
	ft_printf("pa\n");
}

void	ft_swap(t_node **stack, char stack_id)
{
	t_node	*first;
	t_node	*second;

	if (!stack || !*stack || !(*stack)->next)
		return ;
	first = *stack;
	second = (*stack)->next;

	first->next = second->next;
	if (second->next != NULL)
		second->next->prev = first;
	second->prev = NULL;
	second->next = first;
	first->prev = second;
	*stack = second;
	if (stack_id == 'a' || stack_id == 'b')
		ft_printf("s%c\n", stack_id);
}