/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   push_swap.h                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joflorid <joflorid@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/27 10:29:30 by joflorid          #+#    #+#             */
/*   Updated: 2025/10/27 16:48:11 by joflorid         ###   ########.fr       */
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
	struct s_node	*prev;
	struct s_node	*next;
}	t_node;


//=============PROTOTYPES=============
//====================================
//=============ps_initial_checks.c=============
int	ft_check_chars_argv(int argc, char **argv);
int	*ft_load_nbr_arr(char **argv, int *len);
int	ft_check_duplicates(char **argv);


//=============ps_utils_1.c=============
void	ft_free_double(char **d_pointer);

#endif