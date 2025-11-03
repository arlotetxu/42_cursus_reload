/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ps_utils_1.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joflorid <joflorid@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/27 10:56:12 by joflorid          #+#    #+#             */
/*   Updated: 2025/11/03 10:36:53 by joflorid         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../inc/libft/libft.h"
#include "push_swap.h"

void	ft_free_double(char **d_pointer)
{
	int	i;

	if (!d_pointer)
		return ;
	i = 0;
	while (d_pointer[i])
	{
		free(d_pointer[i]);
		i++;
	}
	free(d_pointer);
}

void	ft_free_stack(t_node **stack)
{
	t_node	*temp;
	t_node	*current;

	if (!stack || !*stack)
		return ;
	current = *stack;
	while (current != NULL)
	{
		temp = current;
		current = current->next;
		free(temp);
	}
	*stack = NULL;
}

void	ft_print_stack(t_node *stack)
{
	t_node	*current;
	int		i;

	if (!stack)
		return ;
	current = stack;
	i = -1;
	while (current != NULL && ++i >= 0)
	{
		ft_printf("=============Node[%i]=============\n", i);
		ft_printf("\tnbr: %i\n", current->n_data.nb);
		ft_printf("\ttarget: %i\n", current->n_data.target);
		ft_printf("\tindex: %i\n", current->n_data.index);
		ft_printf("\tprev node: %p\n", current->prev);
		ft_printf("\tcurr node: %p\n", current);
		ft_printf("\tnext node: %p\n", current->next);
		ft_printf("\tra: %i\n", current->n_data.ra);
		ft_printf("\trb: %i\n", current->n_data.rb);
		ft_printf("\trr: %i\n", current->n_data.rr);
		ft_printf("\trra: %i\n", current->n_data.rra);
		ft_printf("\trrb: %i\n", current->n_data.rrb);
		ft_printf("\trrr: %i\n", current->n_data.rrr);
		ft_printf("\tTotal movements: %i\n", current->n_data.total);
		current = current->next;
	}
}

int	ft_check_sorting(t_node *stack)
{
	while (stack->next != NULL)
	{
		if (stack->n_data.nb > stack->next->n_data.nb)
			return (1);
		stack = stack->next;
	}
	return (0);
}

int	ft_check_sorting_r(t_node *stack)
{
	while (stack->next != NULL)
	{
		if (stack->n_data.nb < stack->next->n_data.nb)
			return (1);
		stack = stack->next;
	}
	return (0);
}
