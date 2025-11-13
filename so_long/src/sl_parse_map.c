/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   sl_parse_map.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joflorid <joflorid@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/12 12:11:08 by joflorid          #+#    #+#             */
/*   Updated: 2025/11/13 13:35:44 by joflorid         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../inc/so_long.h"

/*==============================================================================
DESCRIPTION:
	ft_get_map_lines() gets the number of lines the map has reading it with
	get_next_line() function and saves it in the corresponding structure.

PARAMETERS:
	fd --> File descriptor of the map file (.ber).

	*mlx_data --> A pointer to the general structure that contains all the data
		needed in the program.

RETURN:
	lines --> number of lines in the map file.
==============================================================================*/
static int	ft_get_map_lines(int fd, t_mlx_data *mlx_data)
{
	int		lines;
	char	*line;

	lines = 0;
	line = get_next_line(fd);
	while (line)
	{
		lines++;
		free(line);
		line = get_next_line(fd);
	}
	close(fd);
	mlx_data->map_info.lines = lines;
	return (lines);
}

/*==============================================================================
DESCRIPTION:
	ft_get_map_columns() gets the number of colums the map has after its
	creation and saves it in the corresponding structure.

PARAMETERS:
	*mlx_data --> A pointer to the general structure that contains all the data
		needed in the program.

RETURN:
	Nothing
==============================================================================*/
static void	ft_get_map_columns(t_mlx_data *mlx_data)
{
	mlx_data->map_info.column = 0;
	if (mlx_data->map_info.lines)
		mlx_data->map_info.column = ft_strlen_sl(mlx_data->map_info.map[0]);
}

/*==============================================================================
DESCRIPTION:
	ft_feed_map_line() gets a line from the map file (fd) thanks to the
	get_next_line() function and saves it in the map array.

PARAMETERS:
	fd --> File descriptor of the map file (.ber)

	**map_line --> Pointer to the line to be filled up.

RETURN:
	4 --> Error getting the line from get_next_line()

	0 --> OK
==============================================================================*/
static int	ft_feed_map_line(int fd, char **map_line)
{
	char	*gnl_line;

	gnl_line = get_next_line(fd);
	if (!gnl_line)
		return (4);
	*map_line = ft_strdup(gnl_line);
	free(gnl_line);
	if (!(*map_line))
		return (4);
	return (0);
}

/*==============================================================================
DESCRIPTION:
	ft_ber2map() parse the info in the .ber file (map) get through the variable
	'*map_path' to a double char array.

PARAMETERS:
	fd --> File descriptor corresponding to the map file.

	*map_path --> contains the path to the map file through the argv[1].

	*mlx_data --> A pointer to the general structure that contains all the data
		needed in the program.

RETURN:
	2 --> Error opening the map file (fd).

	3 --> Error allocating memory for the double char array
		mlx_data->map_info.map.

	4 --> If the parsing is not possible. Issues getting data from
		get_next_line function

	0 --> OK
==============================================================================*/
int	ft_ber2map(int fd, char *map_path, t_mlx_data *mlx_data)
{
	int	lines;
	int	i;
	int	ret;

	ret = 0;
	lines = ft_get_map_lines(fd, mlx_data);
	fd = open(map_path, O_RDONLY);
	if (fd == -1)
		return (2);
	mlx_data->map_info.map = malloc(sizeof(char *) * (lines + 1)); //!MALLOC
	if (!mlx_data->map_info.map)
		return (close(fd), 3);
	i = -1;
	while (++i < lines)
	{
		ret = ft_feed_map_line(fd, &mlx_data->map_info.map[i]);
		if (ret != 0)
			return (mlx_data->map_info.map[i] = NULL, close(fd),
				ft_freeing(mlx_data->map_info.map, mlx_data), ret);
	}
	mlx_data->map_info.map[i] = NULL;
	ft_get_map_columns(mlx_data);
	close(fd);
	return (ret);
}
