/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   toy_program.c                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joflorid <joflorid@student.42urduliz.co    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/08 19:47:14 by joflorid          #+#    #+#             */
/*   Updated: 2025/11/08 21:10:03 by joflorid         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../inc/so_long.h"
#include "../lib/minilibx-linux/mlx.h"
#include <stdlib.h>

int	main(void)
{
    t_mlx_data	*mlx_ptr;

    mlx_ptr = malloc(sizeof(t_mlx_data));
    if (!mlx_ptr)
        return (1);
    mlx_ptr->mlx = mlx_init();
    if (!mlx_ptr->mlx)
    {
        free(mlx_ptr);
        return (1);
    }
    mlx_ptr->win = mlx_new_window(mlx_ptr->mlx, 600, 600, "Mi ventana");
    
    mlx_loop(mlx_ptr->mlx);

    mlx_destroy_window(mlx_ptr->mlx, mlx_ptr->win);
    mlx_destroy_display(mlx_ptr->mlx);
    free(mlx_ptr->mlx);
    free(mlx_ptr);
    return (0);
}