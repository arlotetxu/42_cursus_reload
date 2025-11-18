/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   so_long.h                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joflorid <joflorid@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/08 19:43:30 by joflorid          #+#    #+#             */
/*   Updated: 2025/11/18 16:55:14 by joflorid         ###   ########.fr       */
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
// # define WIN_L 1600
// # define WIN_H 800
# define IMG_PIX_L 100
# define IMG_PIX_H 100
# define WALL "./assets/wall_100.xpm"
# define FLOOR "./assets/floor_100.xpm"
# define PLAYER "./assets/batmovil_100.xpm"
# define COLLECT "./assets/batsenal_100.xpm"
# define EXIT_ "./assets/exit_100.xpm"
# define TRANS "./assets/batman_100.xpm"

typedef struct	s_text
{
	void	*wall;
	void	*floor;
	void	*collect;
	void	*player;
	void	*exit_;
	void	*trans;
}				t_text;

typedef struct	s_map_data
{
	char	**map;
	int		lines;
	int		column;
	int		start_x;
	int		start_y;
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
	t_text		tex;
	int			mov_count;
}				t_mlx_data;


//====================PROTOTYPES===================
//===========sl_utils_1.c===========
void	ft_print_error(int err_n);
void	ft_freeing(char **str, t_mlx_data *mlx_data);
int		ft_strlen_sl(char *str);
void	ft_free_double(char **str);

//===========sl_utils_2.c===========
int		ft_load_textures(t_mlx_data *mlx_data);
void	ft_destroy_textures(t_mlx_data *mlx_data);
int		ft_close_window(t_mlx_data *mlx_data, int ret);

//===========sl_parse_map.c===========
//static int	ft_get_map_lines(int fd, t_mlx_data *mlx_data);
//static void	ft_get_map_columns(t_mlx_data *mlx_data);
//static int	ft_feed_map_line(int fd, char **map_line);
int				ft_ber2map(int fd, char *map_path, t_mlx_data *mlx_data);

//===========sl_initial_checks1.c===========
int	ft_check_map_ext(char *argv1);
int	ft_map_rectangle(t_mlx_data *mlx_data);
int	ft_map_is_closed(t_mlx_data *mlx_data);
int	ft_check_chars(t_mlx_data *mlx_data);

//===========sl_initial_checks2.c===========
int	ft_count_char(t_mlx_data *mlx_data, char c);
int	ft_total_chars(t_mlx_data *mlx_data);

//===========sl_initial_checks3.c===========
char	**ft_map_dup(t_map_data *map_data);
//static void	ft_start_posit(t_map_data *map_data);
//static void	ft_flood_fill(char **map_copy, t_map_data *data, int start_x,
//	int start_y);
char	**ft_flood_fill_start(t_map_data *map_data);
int		ft_check_map_possible(t_mlx_data *mlx_data);

//===========sl_graphics.c===========
void	*ft_get_textures(char map_char, t_mlx_data *mlx_data);
int		ft_render_map(t_mlx_data *mlx_data);
int		ft_graphics_init(t_mlx_data *mlx_data);

//===========sl_moves.c===========
int		ft_print_key(t_mlx_data *mlx_data);
int		ft_moves(int keycode, t_mlx_data *mlx_data);

//===========so_long.c===========
void	ft_init_mlx(t_mlx_data *mlx_data);
//static int	ft_launcher(int fd, char *map_path, t_mlx_data *mlx_data);
//static int	ft_intial_checks(char *map_path, t_mlx_data *mlx_data);

#endif