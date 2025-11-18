/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   sl_utils_2.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joflorid <joflorid@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/17 16:35:53 by joflorid          #+#    #+#             */
/*   Updated: 2025/11/18 16:01:14 by joflorid         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../inc/so_long.h"

/*==============================================================================
DESCRIPTION:
	ft_load_textures() loads textures in memory.

PARAMETERS:
	*mlx_data --> A pointer to the general structure that contains all the data
		needed in the program.

RETURN:
	0 --> OK

	15 --> In case of error loading the textures.
==============================================================================*/
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
	mlx_data->tex.trans = mlx_xpm_file_to_image(mlx_data->mlx_ptr, TRANS,
		&w, &h);
	if (!mlx_data->tex.wall || !mlx_data->tex.floor || !mlx_data->tex.player
		|| !mlx_data->tex.collect || !mlx_data->tex.exit_
		|| !mlx_data->tex.trans)
		return (15);
	return (0);
}

/*==============================================================================
DESCRIPTION:
	ft_destroy_textures() destroys all the textures (images) saved in memory.

PARAMETERS:
	*mlx_data --> A pointer to the general structure that contains all the data
		needed in the program.

RETURN:
	Nothing.
==============================================================================*/
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
	if (mlx_data->tex.trans)
		mlx_destroy_image(mlx_data->mlx_ptr, mlx_data->tex.trans);
}

/*==============================================================================
DESCRIPTION:
	ft_close_window() destroys all the graphic stuff, frees the memory and exit.

PARAMETERS:
	*mlx_data --> A pointer to the general structure that contains all the data
		needed in the program.

	ret --> error code.

RETURN:
	Nothing.
==============================================================================*/
int	ft_close_window(t_mlx_data *mlx_data, int ret)
{
	if (mlx_data->mlx_ptr)
		ft_destroy_textures(mlx_data);
	if (mlx_data->win_info.win_ptr && mlx_data->mlx_ptr)
		mlx_destroy_window(mlx_data->mlx_ptr, mlx_data->win_info.win_ptr);
	if (mlx_data->mlx_ptr)
	{
		mlx_destroy_display(mlx_data->mlx_ptr);
		ft_freeing(mlx_data->map_info.map, mlx_data);
	}
	ft_print_error(ret);
	exit(55);
}