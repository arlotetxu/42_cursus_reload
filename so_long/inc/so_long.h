/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   so_long.h                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: arlo <arlo@student.42.fr>                  +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/08 19:43:30 by joflorid          #+#    #+#             */
/*   Updated: 2025/11/15 09:35:20 by arlo             ###   ########.fr       */
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
	int		start_x; //!Posicion inicial del player coordenada x (column)
	int		start_y; //!Posicion inicial del player coordenada y (line)
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
void	ft_freeing(char **str, t_mlx_data *mlx_data);
int		ft_strlen_sl(char *str);
void	ft_free_double(char **str);

//===========sl_parse_map.c===========
int	ft_ber2map(int fd, char *map_path, t_mlx_data *mlx_data);

//===========sl_initial_checks1.c===========
int	ft_check_map_ext(char *argv1);
int	ft_map_rectangle(t_mlx_data *mlx_data);
int	ft_map_is_closed(t_mlx_data *mlx_data);
int	ft_check_chars(t_mlx_data *mlx_data);

//===========sl_initial_checks2.c===========
int	ft_total_chars(t_mlx_data *mlx_data);

//===========sl_initial_checks3.c===========
char	**ft_map_dup(t_map_data *map_data);
char	**ft_flood_fill_start(t_map_data *map_data);
int		ft_check_map_possible(t_mlx_data *mlx_data);

#endif