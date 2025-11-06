/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ps_utils_2.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joflorid <joflorid@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/05 15:23:52 by joflorid          #+#    #+#             */
/*   Updated: 2025/11/06 16:15:21 by joflorid         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../lib/libft/libft.h"
#include "../inc/push_swap.h"

/*==============================================================================
DESCRIPTION:
	ft_get_max_index() gets the maximum index in a stack.

PARAMETERS:
	*stack --> A pointer to the list to be checked.

RETURN:
	max --> The maximum index found.
==============================================================================*/
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

/*==============================================================================
DESCRIPTION:
	ft_get_min_in_stack() gets the minimum number in a stack.

PARAMETERS:
	*stack --> A pointer to the list to be checked.

RETURN:
	min --> The minimum number found.
==============================================================================*/
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

/*==============================================================================
DESCRIPTION:
	ft_get_max_in_stack() gets the maximum number in a stack.

PARAMETERS:
	*stack --> A pointer to the list to be checked.

RETURN:
	max --> The maximum number found.
==============================================================================*/
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

/*==============================================================================
DESCRIPTION:
	ft_get_stack_size() gets the number of nodes a stack has.

PARAMETERS:
	*stack --> A pointer to the list to be checked.

RETURN:
	len --> The number of nodes in a stack.
==============================================================================*/
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
