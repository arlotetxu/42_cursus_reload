/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   sl_utils_2.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joflorid <joflorid@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/17 16:35:53 by joflorid          #+#    #+#             */
/*   Updated: 2025/11/17 16:38:10 by joflorid         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../inc/so_long.h"

int	ft_close_window(t_mlx_data *mlx_data)
{
	ft_destroy_textures(mlx_data);

	if (mlx_data->win_info.win_ptr)
		mlx_destroy_window(mlx_data->mlx_ptr, mlx_data->win_info.win_ptr);

	if (mlx_data->mlx_ptr)
	{
		mlx_destroy_display(mlx_data->mlx_ptr);
		ft_freeing(mlx_data->map_info.map, mlx_data);
	}

	exit(0);
}