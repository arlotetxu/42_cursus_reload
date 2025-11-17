/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   sl_graphics.c                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joflorid <joflorid@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/17 11:03:53 by joflorid          #+#    #+#             */
/*   Updated: 2025/11/17 16:39:23 by joflorid         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../inc/so_long.h"

int	ft_load_textures(t_mlx_data *mlx_data)
{
	int	w;
	int	h;

	w = IMG_PIX_L;
	h = IMG_PIX_H;

	mlx_data->tex.wall = mlx_xpm_file_to_image(mlx_data->mlx_ptr, WALL, &w, &h);
	mlx_data->tex.floor = mlx_xpm_file_to_image(mlx_data->mlx_ptr, FLOOR,
		&w, &h);
	mlx_data->tex.player = mlx_xpm_file_to_image(mlx_data->mlx_ptr, PLAYER,
		&w, &h);
	mlx_data->tex.collect = mlx_xpm_file_to_image(mlx_data->mlx_ptr, COLLECT,
		&w, &h);
	mlx_data->tex.exit_ = mlx_xpm_file_to_image(mlx_data->mlx_ptr, EXIT_,
		&w, &h);
	if (!mlx_data->tex.wall || !mlx_data->tex.floor || !mlx_data->tex.player
		|| !mlx_data->tex.collect || !mlx_data->tex.exit_)
		return (15);
	return (0);
}

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
	return (NULL);
}

int	ft_render_map(t_mlx_data *mlx_data)
{
	int	line;
	int	col;
	void	*img_ptr;

	line = -1;
	while (mlx_data->map_info.map[++line])
	{
		col = -1;
		while (mlx_data->map_info.map[line][++col])
		{
			img_ptr = ft_get_textures(mlx_data->map_info.map[line][col],
				mlx_data);
			if (img_ptr)
				mlx_put_image_to_window(mlx_data->mlx_ptr,
					mlx_data->win_info.win_ptr, img_ptr, col * IMG_PIX_L,
					line * IMG_PIX_H);
		}
	}
	return (0);
}

void	ft_destroy_textures(t_mlx_data *mlx_data)
{
	if (mlx_data->tex.wall)
		mlx_destroy_image(mlx_data->mlx_ptr, mlx_data->tex.wall);
	if (mlx_data->tex.collect)
		mlx_destroy_image(mlx_data->mlx_ptr, mlx_data->tex.collect);
	if (mlx_data->tex.exit_)
		mlx_destroy_image(mlx_data->mlx_ptr, mlx_data->tex.exit_);
	if (mlx_data->tex.floor)
		mlx_destroy_image(mlx_data->mlx_ptr, mlx_data->tex.floor);
	if (mlx_data->tex.player)
		mlx_destroy_image(mlx_data->mlx_ptr, mlx_data->tex.player);
}

int	ft_graphics_init(t_mlx_data *mlx_data)
{
	int	ret;

	ret = 0;
	mlx_data->mlx_ptr = mlx_init();
	if (!mlx_data->mlx_ptr)
		return (13);
	mlx_data->win_info.win_height = IMG_PIX_H * mlx_data->map_info.lines;
	mlx_data->win_info.win_length = IMG_PIX_L * mlx_data->map_info.column;
	mlx_data->win_info.win_ptr = mlx_new_window(mlx_data->mlx_ptr, mlx_data->win_info.win_length, mlx_data->win_info.win_height, "Mi ventanica");
	if (!mlx_data->win_info.win_ptr)
	{
		//mlx_destroy_display(mlx_data->mlx_ptr);
		ft_freeing(mlx_data->map_info.map, mlx_data);
		return (14);
	}
	mlx_hook(mlx_data->win_info.win_ptr, 17, 0, ft_close_window, mlx_data);
	//!PENDIENTE HOOK PARA CERRAR CON ESC
	ret = ft_load_textures(mlx_data);
	if (ret)
	{
		mlx_destroy_window(mlx_data->mlx_ptr, mlx_data->win_info.win_ptr);
		ft_freeing(mlx_data->map_info.map, mlx_data);
		return (ret);
	}
	ft_render_map(mlx_data);
	mlx_loop(mlx_data->mlx_ptr);

	return (0);
}
