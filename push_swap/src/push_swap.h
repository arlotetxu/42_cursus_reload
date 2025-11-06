/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   push_swap.h                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joflorid <joflorid@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/27 10:29:30 by joflorid          #+#    #+#             */
/*   Updated: 2025/11/06 16:01:16 by joflorid         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef PUSH_SWAP_H
# define PUSH_SWAP_H

//===========STD LIBRARIES===========
# include <unistd.h>
# include <stdlib.h>
//# include <stdarg.h>
# include <limits.h>

//===========OTHER LIBRARIES===========
# include "../inc/libft/libft.h"

//=============DEFINITIONS=============
typedef struct s_n_data
{
	int	nb;
	int	index;
	int	target;
	int	ra;
	int	rb;
	int	rr;
	int	rra;
	int	rrb;
	int	rrr;
	int	total;
}	t_n_data;

typedef struct s_node
{
	t_n_data		n_data;
	struct s_node	*prev;
	struct s_node	*next;
}	t_node;

//==================PROTOTYPES==================
//==============================================
//=============ps_initial_checks.c=============
int		ft_check_chars_argv(char *str);
char	*ft_strjoin_2(int argc, char **argv);
int		*ft_load_nbr_arr(char *full_args, int *len);
int		ft_check_dupli(char *full_args);

//=============ps_utils_1.c=============
void	ft_free_double(char **d_pointer);
void	ft_free_stack(t_node **stack);
void	ft_print_stack(t_node *stack);
int		ft_check_sorting(t_node *stack);
int		ft_check_sorting_r(t_node *stack);

//=============ps_utils_2.c=============
int		ft_get_max_index(t_node *stack);
int		ft_get_min_in_stack(t_node *stack);
int		ft_get_max_in_stack(t_node *stack);
int		ft_get_stack_size(t_node *stack);

//=============ps_index_target_a.c=============
void	ft_apply_index(t_node *stack);
//static void	ft_find_target_a(t_node *node_a, t_node *stack_b);
void	ft_apply_target_a(t_node *stack_a, t_node *stack_b);

//=============ps_moves_a.c=============
void	ft_init_moves(t_node *node);
void	ft_get_moves_a(t_node **stack_a, t_node **stack_b);
void	ft_get_moves_a_t(t_node **stack_a, t_node **stack_b);
void	ft_opti_moves(t_node **stack);

//=============ps_target_b.c=============

//static void	ft_find_target_b(t_node *node_b, t_node *stack_a);
void	ft_apply_target_b(t_node *stack_a, t_node *stack_b);

//=============ps_moves_b.c=============
void	ft_get_moves_b(t_node **stack_a, t_node **stack_b);
void	ft_get_moves_b_t(t_node **stack_a, t_node **stack_b);

//=============ps_last_sort_6.c=============
int		ft_min_index(t_node **stack);
void	ft_last_sort(t_node **stack_a);

//=============ps_load_stack_a.c=============
void	ft_insert_end(t_node **stack_a, int nbr);
int		ft_load_stack_a(char *full_args, t_node **stack_a);

//=============ps_moves_1.c=============
void	ft_rotate(t_node **stack, char stack_id);
void	ft_rotate_2(t_node **stack_a, t_node **stack_b, char stack_id);
void	ft_rotate_r(t_node **stack, char stack_id);
void	ft_rotate_r_2(t_node **stack_a, t_node **stack_b, char stack_id);

//=============ps_moves_2.c=============
void	ft_push_b(t_node **stack_a, t_node **stack_b);
void	ft_push_a(t_node **stack_a, t_node **stack_b);
void	ft_swap(t_node **stack, char stack_id);

//=============ps_algorithim_3_2.c=============
void	ft_sort_3(t_node **stack, char stack_id);
void	ft_sort_2(t_node **stack, char stack_id);

//=============ps_move_a2b.c=============
t_node	*ft_node2pass(t_node **stack);
void	ft_do_moves(t_node **stack_a, t_node **stack_b, char stack_id);
void	ft_do_moves_2(t_node *select, t_node **stack_a, t_node **stack_b, \
	char stack_id);

#endif