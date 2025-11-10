/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   toy_program.c                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joflorid <joflorid@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/08 19:47:14 by joflorid          #+#    #+#             */
/*   Updated: 2025/11/10 13:33:14 by joflorid         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../inc/so_long.h"
#include "../lib/minilibx-linux/mlx.h"
#include <stdlib.h>

int	main(void)
{
	t_mlx_data	*mlx_data;

	mlx_data = malloc(sizeof(t_mlx_data));
	if (!mlx_data)
		return (1);
	mlx_data->mlx_ptr = mlx_init();
	if (!mlx_data->mlx_ptr)
		return (1);
	//mlx_data->win_ptr = mlx_new_window(mlx_data->mlx_ptr, WIN_L, WIN_H, "JFLORID");

	mlx_loop(mlx_data->mlx_ptr);

	//mlx_destroy_window(mlx_data->mlx_ptr, mlx_data->win_ptr);
	mlx_destroy_display(mlx_data->mlx_ptr);
	free(mlx_data->mlx_ptr);
	free(mlx_data);
	return (0);
}
