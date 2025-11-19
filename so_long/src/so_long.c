/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   so_long.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joflorid <joflorid@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/12 11:50:56 by joflorid          #+#    #+#             */
/*   Updated: 2025/11/19 10:41:27 by joflorid         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../inc/so_long.h"

/*==============================================================================
DESCRIPTION:
	ft_init_mlx() initializes all the values of the main structure mlx_data.

PARAMETERS:
	*mlx_data --> A pointer to the general structure that contains all the data
		needed in the program.

RETURN:
	Nothing
==============================================================================*/
void	ft_init_mlx(t_mlx_data *mlx_data)
{
	if (!mlx_data)
		return ;
	mlx_data->mlx_ptr = NULL;
	mlx_data->win_info.win_ptr = NULL;
	mlx_data->map_info.map = NULL;
	mlx_data->tex.wall = NULL;
	mlx_data->tex.floor = NULL;
	mlx_data->tex.player = NULL;
	mlx_data->tex.collect = NULL;
	mlx_data->tex.exit_ = NULL;
	mlx_data->mov_count = 0;
}

/*==============================================================================
DESCRIPTION:
	ft_intial_checks() calls to the different functions used to check if the
	program input is ok

PARAMETERS:
	*map_path --> The path to the map file got from argv[1]

	*mlx_data --> A pointer to the general structure that contains all the data
		needed in the program.

RETURN:
	0 --> OK

	ret --> Error code value
==============================================================================*/
static int	ft_intial_checks(char *map_path, t_mlx_data *mlx_data)
{
	int	ret;

	ret = 0;
	ret = ft_check_map_ext(map_path);
	if (ret)
		return (ret);
	ret = ft_map_rectangle(mlx_data);
	if (ret)
		return (ret);
	ret = ft_map_is_closed(mlx_data);
	if (ret)
		return (ret);
	ret = ft_check_chars(mlx_data);
	if (ret)
		return (ret);
	ret = ft_total_chars(mlx_data);
	if (ret)
		return (ret);
	ret = ft_check_map_possible(mlx_data);
	if (ret)
		return (ret);
	return (ret);
}

/*==============================================================================
DESCRIPTION:
	ft_launcher() starts the program. It calls the function ft_ber2map() to
	parse the map file to a char ** to do all the needed checks. Then, it starts
	the graphics and finally it starts the game in the function
	ft_graphics_init().

PARAMETERS:
	*map_path --> The path to the map file got from argv[1]

	*mlx_data --> A pointer to the general structure that contains all the data
		needed in the program.

RETURN:
	0 --> OK

	ret --> Error code value
==============================================================================*/
static int	ft_launcher(int fd, char *map_path, t_mlx_data *mlx_data)
{
	int	ret;

	ret = 0;
	ret = ft_ber2map(fd, map_path, mlx_data);
	close(fd);
	if (ret)
		return (ft_print_error(ret), ret);
	ret = ft_intial_checks(map_path, mlx_data);
	if (ret)
		return (ft_print_error(ret), ret);
	ret = ft_graphics_init(mlx_data);
	if (ret)
		return (ft_print_error(ret), ret);
	return (ret);
}

/*
RETURN ERROR CODES
1 - Invalid number of arguments
2 - Cannot open the map file.
3 - Cannot load the map. Memory issues.
4 - Cannot load the map in array.
5 - Memory issues checking the map extension. int	ft_check_map_ext()
6 - Map extension not valid.
7 - The map is not a rectangle
8 - Map with different line's length.
9 - Wrong character type in the map.
10 - Wrong characters number.
11 - Map with no solution.
12 - Couldn't get a map copied in ft_check_map_possible()
13 - The X server cannot be initilizated
14 - The Window couldn't be created
15 - The textures couldn't be loaded.
*/
int	main(int argc, char **argv)
{
	int			fd;
	int			ret;
	t_mlx_data	*mlx_data;

	if (argc != 2)
		return (ft_print_error(1), 1);
	fd = open(argv[1], O_RDONLY);
	if (fd == -1)
		return (ft_print_error(2), 2);
	mlx_data = malloc(sizeof(t_mlx_data));
	if (!mlx_data)
		return (3);
	ft_init_mlx(mlx_data);
	ret = 0;
	ret = ft_launcher(fd, argv[1], mlx_data);
	if (ret)
		return (ft_freeing(mlx_data->map_info.map, mlx_data), ret);
	ft_close_window(mlx_data, ret);
	return (ret);
}
