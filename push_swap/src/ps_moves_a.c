/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ps_moves_a.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joflorid <joflorid@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/31 15:58:50 by joflorid          #+#    #+#             */
/*   Updated: 2025/11/06 16:14:56 by joflorid         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../lib/libft/libft.h"
#include "../inc/push_swap.h"

/*==============================================================================
DESCRIPTION:
	ft_init_moves() initializes all the movements in a node to 0

PARAMETERS:
	*node --> A pointer to the node to be initialized.

RETURN:
	Nothing.
==============================================================================*/
void	ft_init_moves(t_node *node)
{
	node->n_data.ra = 0;
	node->n_data.rb = 0;
	node->n_data.rra = 0;
	node->n_data.rrb = 0;
	node->n_data.rr = 0;
	node->n_data.rrr = 0;
	node->n_data.total = 0;
}

/*==============================================================================
DESCRIPTION:
	ft_opti_moves() optimizes the number of movements grouping ra & rb in rr and
	rra & rrb in rrr in order to reduce the total number of movements.

PARAMETERS:
	**stack --> A pointer to the stack to be optimized.

RETURN:
	Nothing.
==============================================================================*/
void	ft_opti_moves(t_node **stack)
{
	t_node	*cur;

	cur = *stack;
	while (cur != NULL)
	{
		if (cur->n_data.ra > 0 && cur->n_data.rb > 0
			&& cur->n_data.ra >= cur->n_data.rb)
			cur->n_data.rr = cur->n_data.rb;
		else if (cur->n_data.ra > 0 && cur->n_data.rb > 0
			&& cur->n_data.ra < cur->n_data.rb)
			cur->n_data.rr = cur->n_data.ra;
		if (cur->n_data.rra > 0 && cur->n_data.rrb > 0
			&& cur->n_data.rra >= cur->n_data.rrb)
			cur->n_data.rrr = cur->n_data.rrb;
		else if (cur->n_data.rra > 0 && cur->n_data.rrb > 0
			&& cur->n_data.rra < cur->n_data.rrb)
			cur->n_data.rrr = cur->n_data.rra;
		cur->n_data.total = (cur->n_data.ra - cur->n_data.rr)
			+ (cur->n_data.rb - cur->n_data.rr)
			+ (cur->n_data.rra - cur->n_data.rrr)
			+ (cur->n_data.rrb - cur->n_data.rrr)
			+ cur->n_data.rr + cur->n_data.rrr;
		cur = cur->next;
	}
}
/*==============================================================================
DESCRIPTION:
	ft_get_moves_a_t() calculates cheapest number of movements needed to bring
	the target node to the top of the stack_b and saves it in the node
	information (n_data).

PARAMETERS:
	**stack_a --> A pointer to the stack_a with the nodes to be evaluated.

	**stack_b --> A pointer to the stack_b with the target nodes.

RETURN:
	Nothing.
==============================================================================*/

void	ft_get_moves_a_t(t_node **stack_a, t_node **stack_b)
{
	t_node	*cur_a;
	t_node	*cur_b;
	int		s_size_b;

	s_size_b = ft_get_stack_size(*stack_b);
	cur_a = *stack_a;
	while (cur_a != NULL)
	{
		cur_b = *stack_b;
		while (cur_b != NULL)
		{
			if (cur_a->n_data.target == cur_b->n_data.nb
				&& cur_b->n_data.index != 0)
			{
				if (s_size_b - cur_b->n_data.index < cur_b->n_data.index)
					cur_a->n_data.rrb = s_size_b - cur_b->n_data.index;
				else
					cur_a->n_data.rb = cur_b->n_data.index;
			}
			cur_b = cur_b->next;
		}
		cur_a = cur_a->next;
	}
}

/*==============================================================================
DESCRIPTION:
	ft_get_moves_a() calculates cheapest number of movements needed to bring the
	evaluated node to the top of the stack_a and saves it in the node
	information (n_data). Then, calls the function ft_get_moves_a_t() to
	calculate and save the cheapest number of movements to bring the target node
	to the top of the stack_b. Finally, the functions calls the function
	ft_opti_moves() to try to optimize the total number of movements grouping
	ra & ra in rr and rra & rrb in rrr.

PARAMETERS:
	**stack_a --> A pointer to the stack_a with the nodes to be evaluated.

	**stack_b --> A pointer to the stack_b with the target nodes.

RETURN:
	Nothing.
==============================================================================*/
void	ft_get_moves_a(t_node **stack_a, t_node **stack_b)
{
	t_node	*current;
	int		s_size_a;

	if (!stack_a)
		return ;
	s_size_a = ft_get_stack_size(*stack_a);
	current = *stack_a;
	while (current != NULL)
	{
		ft_init_moves(current);
		if (current->n_data.index != 0)
		{
			if (s_size_a - current->n_data.index < current->n_data.index)
				current->n_data.rra = s_size_a - current->n_data.index;
			else
				current->n_data.ra = current->n_data.index;
		}
		current = current->next;
	}
	ft_get_moves_a_t(stack_a, stack_b);
	ft_opti_moves(stack_a);
}
