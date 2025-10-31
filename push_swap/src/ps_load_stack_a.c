/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ps_load_stack_a.c                                  :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joflorid <joflorid@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/29 11:35:54 by joflorid          #+#    #+#             */
/*   Updated: 2025/10/31 15:32:08 by joflorid         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../inc/libft/libft.h"
#include "push_swap.h"

static t_node	*ft_create_node(int nbr)
{
	t_node	*new_node;

	new_node = malloc (sizeof(t_node)); //!MALLOC
	if (!new_node)
		return (NULL);
	new_node->n_data.nb = nbr;
	new_node->n_data.index = 0;
	new_node->n_data.target = 0;
	new_node->n_data.ra = 0;
	new_node->n_data.rb = 0;
	new_node->n_data.rra = 0;
	new_node->n_data.rrb = 0;
	new_node->n_data.total = new_node->n_data.ra + new_node->n_data.rb
		+ new_node->n_data.rra + new_node->n_data.rrb;
	new_node->next = NULL;
	new_node->prev = NULL;
	return (new_node);
}

void	ft_insert_end(t_node **stack_a, int nbr)
{
	t_node	*new_node;
	t_node	*current;

	new_node = ft_create_node(nbr);
	if (!new_node)
		return ;
	if (!*stack_a)
	{
		*stack_a = new_node;
		return ;
	}
	current = *stack_a;
	while (current->next)
		current = current->next;
	current->next = new_node;
	new_node->prev = current;
}

int	ft_load_stack_a(char *full_args, t_node **stack_a)
{
	int	*args_arr;
	int	len;
	int	i;

	len = 0;
	args_arr = ft_load_nbr_arr(full_args, &len);
	if (!args_arr)
		return (5);
	i = -1;
	while (++i < len)
		ft_insert_end(stack_a, args_arr[i]);
	ft_apply_index(*stack_a);
	if (!ft_check_sorting(*stack_a))
		return (free(args_arr), 6);
	return (free(args_arr), 0);
}
