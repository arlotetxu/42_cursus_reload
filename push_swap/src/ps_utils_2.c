/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ps_utils_2.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joflorid <joflorid@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/05 15:23:52 by joflorid          #+#    #+#             */
/*   Updated: 2025/11/05 15:27:19 by joflorid         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../inc/libft/libft.h"
#include "push_swap.h"

int	ft_get_max_index(t_node *stack)
{
	int	max;

	max = stack->n_data.index;
	while (stack)
	{
		if (stack->n_data.index > max)
			max = stack->n_data.index;
		stack = stack->next;
	}
	return (max);
}

int	ft_get_min_in_stack(t_node *stack)
{
	int	min;

	min = stack->n_data.nb;
	while (stack)
	{
		if (stack->n_data.nb < min)
			min = stack->n_data.nb;
		stack = stack->next;
	}
	return (min);
}

int	ft_get_max_in_stack(t_node *stack)
{
	int	max;

	max = stack->n_data.nb;
	while (stack)
	{
		if (stack->n_data.nb > max)
			max = stack->n_data.nb;
		stack = stack->next;
	}
	return (max);
}

int	ft_get_stack_size(t_node *stack)
{
	int	len;

	if (!stack)
		return (0);
	len = 0;
	while (stack != NULL)
	{
		len++;
		stack = stack->next;
	}
	return (len);
}
