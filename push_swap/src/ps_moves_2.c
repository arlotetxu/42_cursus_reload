/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ps_moves_2.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joflorid <joflorid@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/30 14:14:37 by joflorid          #+#    #+#             */
/*   Updated: 2025/11/06 12:37:42 by joflorid         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../inc/libft/libft.h"
#include "push_swap.h"

/*==============================================================================
DESCRIPTION:
	ft_push_b() pushes the first node in stack_a to the first position in
	stack_b. Finally, this function prints the corresponding string in the
	terminal.

PARAMETERS:
	**stack_a --> A pointer to the stack_a in which the movement has to be
		applied.

	**stack_b --> A pointer to the stack_b to receive the new node.

RETURN:
	Nothing.
==============================================================================*/
void	ft_push_b(t_node **stack_a, t_node **stack_b)
{
	t_node	*aux;

	if (!stack_a || !stack_b || !*stack_a)
		return ;
	aux = *stack_a;
	*stack_a = (*stack_a)->next;
	if (*stack_a)
		(*stack_a)->prev = NULL;
	aux->prev = NULL;
	aux->next = *stack_b;
	if (*stack_b)
		(*stack_b)->prev = aux;
	*stack_b = aux;
	ft_apply_index(*stack_a);
	ft_apply_index(*stack_b);
	ft_printf("pb\n");
}

/*==============================================================================
DESCRIPTION:
	ft_push_a() pushes the first node in stack_b to the first position in
	stack_a. Finally, this function prints the corresponding string in the
	terminal.

PARAMETERS:
	**stack_a --> A pointer to the stack_a to receive the new node.

	**stack_b --> A pointer to the stack_b in which the movement has to be
		applied..

RETURN:
	Nothing.
==============================================================================*/
void	ft_push_a(t_node **stack_a, t_node **stack_b)
{
	t_node	*aux;

	if (!stack_b || !stack_a || !*stack_b)
		return ;
	aux = *stack_b;
	*stack_b = (*stack_b)->next;
	if (*stack_b)
		(*stack_b)->prev = NULL;
	aux->prev = NULL;
	aux->next = *stack_a;
	if (*stack_a)
		(*stack_a)->prev = aux;
	*stack_a = aux;
	ft_apply_index(*stack_a);
	ft_apply_index(*stack_b);
	ft_printf("pa\n");
}

/*==============================================================================
DESCRIPTION:
	ft_swap() swaps the 2 first nodes in a stack, so the first one becomes the
	second and the second becomes the first. Finally, this function prints the
	corresponding string in the terminal.

PARAMETERS:
	**stack --> A pointer to the stack in which the movement is applied.

	stack_id --> The stack identification to apply the movement.

RETURN:
	Nothing.
==============================================================================*/
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
	ft_apply_index(*stack);
	if (stack_id == 'a' || stack_id == 'b')
		ft_printf("s%c\n", stack_id);
}
