/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   so_long.h                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joflorid <joflorid@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/08 19:43:30 by joflorid          #+#    #+#             */
/*   Updated: 2025/11/12 13:59:34 by joflorid         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef SO_LONG_H
# define SO_LONG_H

//====================LIBRARIES====================
# include "../lib/minilibx-linux/mlx.h"
# include "../lib/libft/libft.h"
# include "../lib/gnl/get_next_line.h"
# include <stdlib.h>
# include <X11/keysym.h>
# include <fcntl.h>
# include <math.h>

//===================DEFINITIONS===================
# define WIN_L 1600
# define WIN_H 800

typedef struct	s_map_data
{
	char	**map;
	int		lines;
	int		column;
}				t_map_data;

typedef struct	s_win_data
{
	void	*win_ptr;
	int		win_height;
	int		win_length;
}				t_win_data;

typedef struct	s_mlx_data
{
	void		*mlx_ptr;
	t_win_data	win_info;
	t_map_data	map_info;
}				t_mlx_data;


//====================PROTOTYPES===================
//===========sl_utils.c===========
void	ft_print_error(int err_n);
void	ft_double_free(char **str);

//===========sl_input_check.c===========
int	ft_ber2map(int fd, char *map_path, t_mlx_data *mlx_data);

#endif