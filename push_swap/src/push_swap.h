/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   push_swap.h                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joflorid <joflorid@student.42urduliz.co    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/27 10:29:30 by joflorid          #+#    #+#             */
/*   Updated: 2025/10/29 16:21:18 by joflorid         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef PUSH_SWAP_H
# define PUSH_SWAP_H

//===========STD LIBRARIES===========
# include <unistd.h>
# include <stdlib.h>
# include <stdarg.h>
# include <limits.h>
# include <stdio.h>


//===========OTHER LIBRARIES===========
# include "../inc/libft/libft.h"

//=============DEFINITIONS=============
typedef	struct	s_n_data
{
	int	nb;
	int	index;
	int	target;
	int	ra;
	int	rb;
	int	rra;
	int	rrb;
	int	total;
}	t_n_data;


typedef	struct	s_node
{
	t_n_data		node_data;
	struct s_node	*prev;
	struct s_node	*next;
}	t_node;


//=============PROTOTYPES=============
//====================================
//=============ps_initial_checks.c=============
int		ft_check_chars_argv(char *str);
char	*ft_strjoin_2(int argc, char **argv);
int		*ft_load_nbr_arr(char *full_args, int *len);
int		ft_check_dupli(char *full_args);



//=============ps_utils_1.c=============
void	ft_free_double(char **d_pointer);
void	ft_print_stack(t_node *stack);
int		ft_check_sorting(t_node *stack);

//=============ps_load_stack_a.c=============
void	ft_insert_end(t_node **stack_a, int nbr);
int	ft_load_stack_a(char *full_args, t_node **stack_a);


#endif