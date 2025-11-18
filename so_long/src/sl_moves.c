/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   sl_moves.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joflorid <joflorid@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/18 13:36:34 by joflorid          #+#    #+#             */
/*   Updated: 2025/11/18 16:55:03 by joflorid         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../inc/so_long.h"


int	ft_print_key(t_mlx_data *mlx_data)
{
	ft_printf("Move nbr: %i\n", mlx_data->mov_count);
	// if (keycode == XK_Escape)
	// 	ft_printf("Closing the window...\n");
	return (0);
}

void	ft_moving(t_mlx_data *mlx_data, int ret, int l, int c)
{
	int	start_l;
	int	start_c;

	start_l = mlx_data->map_info.start_y;
	start_c = mlx_data->map_info.start_x;
	if (ret == 1)
	{
		if (mlx_data->map_info.map[start_l][start_c] == 'X')
			mlx_data->map_info.map[start_l][start_c] = 'E';
		else
		mlx_data->map_info.map[start_l][start_c] = '0';
		mlx_data->map_info.start_y = l;
		mlx_data->map_info.start_x = c;
		mlx_data->map_info.map[l][c] = 'p';
	}
	else if (ret == 2)
	{
		mlx_data->map_info.map[start_l][start_c] = '0';
		mlx_data->map_info.start_y = l;
		mlx_data->map_info.start_x = c;
		mlx_data->map_info.map[l][c] = 'X';
	}
	ft_render_map(mlx_data);
}

int	ft_next_map_value(t_mlx_data *mlx_data, int l, int c)
{
	if (mlx_data->map_info.map[l][c] == '0'
		|| mlx_data->map_info.map[l][c] == 'c'
		|| mlx_data->map_info.map[l][c] == 'C'
		|| mlx_data->map_info.map[l][c] == 'X')
		return (1);
	if ((mlx_data->map_info.map[l][c] == 'E'
		|| mlx_data->map_info.map[l][c] == 'e')
		&& ft_count_char(mlx_data, 'c') + ft_count_char(mlx_data, 'C') > 0)
		return (2);
	if ((mlx_data->map_info.map[l][c] == 'E'
		|| mlx_data->map_info.map[l][c] == 'e')
		&& ft_count_char(mlx_data, 'c') + ft_count_char(mlx_data, 'C') == 0)
		ft_close_window(mlx_data, 0);
	return (0);
}
/*
UP --> 65362
W --> 119

DOWN --> 65364
S --> 115

LEFT --> 65361
A --> 97

RIGHT --> 65363
D --> 100
*/
int	ft_moves(int keycode, t_mlx_data *mlx_data)
{
	int	next_l;
	int	next_c;
	int	ret;

	ret = 0;
	next_l = mlx_data->map_info.start_y;
	next_c = mlx_data->map_info.start_x;
	if (keycode == XK_Escape)
		ft_close_window(mlx_data, 0);
	if ((keycode == 65362 || keycode == 119))
		next_l = mlx_data->map_info.start_y - 1;
	else if ((keycode == 65364 || keycode == 115))
		next_l = mlx_data->map_info.start_y + 1;
	else if ((keycode == 65361 || keycode == 97))
		next_c = mlx_data->map_info.start_x - 1;
	else if ((keycode == 65363 || keycode == 100))
		next_c = mlx_data->map_info.start_x + 1;
	ret = ft_next_map_value(mlx_data, next_l, next_c);
	if (ret)
	{
		ft_moving(mlx_data, ret, next_l, next_c);
		mlx_data->mov_count++;
		ft_print_key(mlx_data);
	}
	return(0);
}
