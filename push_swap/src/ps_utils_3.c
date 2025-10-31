/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ps_utils_3.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joflorid <joflorid@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/31 15:58:50 by joflorid          #+#    #+#             */
/*   Updated: 2025/10/31 16:01:46 by joflorid         ###   ########.fr       */
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