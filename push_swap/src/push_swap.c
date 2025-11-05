/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   push_swap.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joflorid <joflorid@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/27 10:41:59 by joflorid          #+#    #+#             */
/*   Updated: 2025/11/05 13:54:40 by joflorid         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../inc/libft/libft.h"
#include "push_swap.h"

/*
	RETURNS EN MAIN
1 --> Wrong argument number
2 --> Wrong characters in the input (non digits or non digit after a sign)
3 --> There are duplicated numbers
4 --> Cannot get the string with all the arguments with ft_strjoin_2()
5 --> The arr_args couldn't nbe created at ft_load_stack_a()
6 --> The list is already sorted.
7 --> The stack_b couldn't be created
*/

static void	ft_launcher(t_node **stack_a, t_node **stack_b)
{
	if (ft_get_stack_size(*stack_a) == 3)
		return (ft_sort_3(stack_a, 'a'));
	if (ft_get_stack_size(*stack_a) == 2)
		return (ft_sort_2(stack_a, 'a'));
	ft_push_b(stack_a, stack_b);
	ft_push_b(stack_a, stack_b);
	while (ft_get_stack_size(*stack_a) > 3)
	{
		ft_apply_target_a(*stack_a, *stack_b);
		ft_get_moves_a(stack_a, stack_b);
		ft_do_moves(stack_a, stack_b, 'a');
	}
	ft_sort_3(stack_a, 'a');
	while (ft_get_stack_size(*stack_b) != 0)
	{
		ft_apply_target_b(*stack_a, *stack_b);
		ft_get_moves_b(stack_a, stack_b);
		ft_do_moves(stack_a, stack_b, 'b');
	}
	ft_last_sort(stack_a);
}

static int	ft_input_check(char *full_args)
{
	if (!full_args)
		return (4);
	if (ft_check_chars_argv(full_args))
	{
		write(2, "\x1b[41m", 6);
		write(2, "Error\n", 6);
		write(2, "\x1b[0m", 5);
		return (2);
	}
	if (ft_check_dupli(full_args))
	{
		write(2, "\x1b[41m", 6);
		write(2, "Error\n", 6);
		write(2, "\x1b[0m", 5);
		return (3);
	}
	return (0);
}

int	main(int argc, char **argv)
{
	int		ret;
	char	*full_args;
	t_node	*stack_a;
	t_node	*stack_b;

	if (argc < 2)
		return (1);
	full_args = ft_strjoin_2(argc, argv);
	stack_a = NULL;
	stack_b = NULL;
	ret = 0;
	if (argc >= 2)
		ret = ft_input_check(full_args);
	if (ret)
		return (free(full_args), ret);
	ret = ft_load_stack_a(full_args, &stack_a);
	if (ret)
		return (free(full_args), ret);
	ft_launcher(&stack_a, &stack_b);
	free(full_args);
	ft_free_stack(&stack_a);
	ft_free_stack(&stack_b);
	return (ret);
}
