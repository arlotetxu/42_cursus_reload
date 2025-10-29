/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ps_utils_1.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joflorid <joflorid@student.42urduliz.co    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/27 10:56:12 by joflorid          #+#    #+#             */
/*   Updated: 2025/10/29 16:12:49 by joflorid         ###   ########.fr       */
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

void	ft_print_stack(t_node *stack)
{
	t_node	*current;
	int		i;

	if (!stack)
	{
		//printf("La lista está vacía.\n"); //!PRINTF
		return ;
	}
	current = stack;
	i = 0;
	while (current != NULL)
	{
		ft_printf("=============Node[%i]=============\n", i);
		ft_printf("\tnbr: %i\n", current->node_data.nb);
		ft_printf("\ttarget: %i\n", current->node_data.target);
		ft_printf("\tprev node: %p\n", current->prev);
		ft_printf("\tcurr node: %p\n", current);
		ft_printf("\tnext node: %p\n", current->next);
		ft_printf("\tTotal movements: %i\n", current->node_data.total);
		current = current->next;
		i++;
	}
}

int	ft_check_sorting(t_node *stack)
{
	while (stack->next != NULL)
	{
		if (stack->node_data.nb > stack->next->node_data.nb)
			return(1);
		stack = stack->next;
	}
	return (0);
}