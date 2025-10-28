/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   push_swap.h                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joflorid <joflorid@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/27 10:29:30 by joflorid          #+#    #+#             */
/*   Updated: 2025/10/28 14:20:37 by joflorid         ###   ########.fr       */
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
typedef	struct	s_node
{
	int	nb;
	int	index;
}	t_node;


typedef	struct	s_stack
{
	t_node			node;
	struct s_stack	*prev;
	struct s_stack	*next;
}	t_stack;


//=============PROTOTYPES=============
//====================================
//=============ps_initial_checks.c=============
int	ft_check_chars_argv(char *str);
// int	*ft_load_nbr_arr(char **argv, int *len);
// int	ft_check_duplicates(char **argv);
char	*ft_strjoin_2(int argc, char **argv);
int		*ft_load_nbr_arr(char *full_args, int *len);
int		ft_check_dupli(char *full_args);



//=============ps_utils_1.c=============
void	ft_free_double(char **d_pointer);

#endif