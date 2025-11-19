/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   sl_graphics.c                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joflorid <joflorid@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/17 11:03:53 by joflorid          #+#    #+#             */
/*   Updated: 2025/11/19 10:45:46 by joflorid         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../inc/so_long.h"

/*==============================================================================
DESCRIPTION:
	ft_get_textures() determines what is the right texture to apply according
	to the map coordenates value.

PARAMETERS:
	map_char --> map value coordenate.

	*mlx_data --> A pointer to the general structure that contains all the data
		needed in the program.

RETURN:
	A pointer to the right texture (image).

	NULL --> In case of error.
==============================================================================*/
void	*ft_get_textures(char map_char, t_mlx_data *mlx_data)
{
	if (map_char == '1')
		return (mlx_data->tex.wall);
	else if (map_char == '0')
		return (mlx_data->tex.floor);
	else if (map_char == 'c' || map_char == 'C')
		return (mlx_data->tex.collect);
	else if (map_char == 'P' || map_char == 'p')
		return (mlx_data->tex.player);
	else if (map_char == 'e' || map_char == 'E')
		return (mlx_data->tex.exit_);
	else if (map_char == 'x' || map_char == 'X')
		return (mlx_data->tex.trans);
	return (NULL);
}

/*==============================================================================
DESCRIPTION:
	ft_render_map() renders the map according to the value. It gets the right
	texture and places it in the game window.

PARAMETERS:
	*mlx_data --> A pointer to the general structure that contains all the data
		needed in the program.

RETURN:
	0 --> OK

	15 --> Couldn't load the texture.
==============================================================================*/
int	ft_render_map(t_mlx_data *mlx_data)
{
	int		line;
	int		col;
	void	*img_ptr;

	line = -1;
	while (mlx_data->map_info.map[++line])
	{
		col = -1;
		while (mlx_data->map_info.map[line][++col]
			&& mlx_data->map_info.map[line][col] != '\n')
		{
			img_ptr = ft_get_textures(mlx_data->map_info.map[line][col],
					mlx_data);
			if (img_ptr)
				mlx_put_image_to_window(mlx_data->mlx_ptr,
					mlx_data->win_info.win_ptr, img_ptr, col * IMG_PIX_L,
					line * IMG_PIX_H);
			else
				return (15);
		}
	}
	return (0);
}

/*==============================================================================
DESCRIPTION:
	ft_graphics_init() starts all the graphic stuff (display, window, images).
	It creates the hooks to get the key pushes.

PARAMETERS:
	*mlx_data --> A pointer to the general structure that contains all the data
		needed in the program.

RETURN:
	0 --> OK

	ret --> Error code value
==============================================================================*/
int	ft_graphics_init(t_mlx_data *mlx_data)
{
	int	ret;

	ret = 0;
	mlx_data->mlx_ptr = mlx_init();
	if (!mlx_data->mlx_ptr)
		return (13);
	mlx_data->win_info.win_height = IMG_PIX_H * mlx_data->map_info.lines;
	mlx_data->win_info.win_length = IMG_PIX_L * mlx_data->map_info.column;
	mlx_data->win_info.win_ptr = mlx_new_window(mlx_data->mlx_ptr,
			mlx_data->win_info.win_length, mlx_data->win_info.win_height,
			"42_BATMAN");
	if (!mlx_data->win_info.win_ptr)
		ft_close_window(mlx_data, 14);
	ret = ft_load_textures(mlx_data);
	if (ret)
		ft_close_window(mlx_data, ret);
	mlx_hook(mlx_data->win_info.win_ptr, 17, 0, ft_close_window, mlx_data);
	mlx_hook(mlx_data->win_info.win_ptr, 02, (1L << 0), ft_moves, mlx_data);
	ft_render_map(mlx_data);
	mlx_loop(mlx_data->mlx_ptr);
	return (0);
}
