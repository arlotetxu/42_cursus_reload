/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   sl_initial_checks3.c                               :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joflorid <joflorid@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/13 16:28:05 by joflorid          #+#    #+#             */
/*   Updated: 2025/11/14 14:00:58 by joflorid         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../inc/so_long.h"

/*==============================================================================
DESCRIPTION:
	ft_map_dup() creates a copy of the original map.

PARAMETERS:
	*map_data --> A pointer with information about the original map.

RETURN:
	NULL --> Memory issues when allocating memory.

	map_dup --> The map copy.
==============================================================================*/
char	**ft_map_dup(t_map_data *map_data)
{
	char	**map_dup;
	int		i;

	map_dup = malloc (sizeof(char *) * (map_data->lines + 1));
	if (!map_dup)
		return (NULL);
	i = -1;
	while (map_data->map[++i])
	{
		map_dup[i] = ft_strdup(map_data->map[i]);
		if (!map_dup[i])
		{
			while (--i >= 0)
				free(map_dup[i]);
			free(map_dup);
			return (NULL);
		}
	}
	map_dup[i] = NULL;
	return (map_dup);
}

/*==============================================================================
DESCRIPTION:
	ft_start_posit() determines the coordenates of the starting position
	(position of the character p/P).

PARAMETERS:
	*map_data --> A pointer with information about the original map.

RETURN:
	Nothing
==============================================================================*/
static void	ft_start_posit(t_map_data *map_data)
{
	int	lines;
	int	cols;

	lines = -1;
	while (map_data->map[++lines])
	{
		cols = -1;
		while (map_data->map[lines][++cols])
		{
			if (map_data->map[lines][cols] == 'p'
			|| map_data->map[lines][cols] == 'P')
			{
				map_data->start_y = lines;
				map_data->start_x = cols;
			}
		}
	}
}

/*==============================================================================
DESCRIPTION:
	ft_flood_fill() performs the characters change in the original map copy.

PARAMETERS:
	**map_copy --> The map copy.

	*data --> A pointer with information about the original map.

	start_x --> Position x (column) of the starting point.

	start_y --> Position Y (line) of the starting point.

RETURN:
	Nothing
==============================================================================*/
static void	ft_flood_fill(char **map_copy, t_map_data *data, int start_x,
	int start_y)
{
	if (start_y < 0 || start_y >= data->lines || start_x < 0
		|| start_x >= data->column || map_copy[start_y][start_x] == 'X'
		|| map_copy[start_y][start_x] == '1')
		return ;
	map_copy[start_y][start_x] = 'X';
	ft_flood_fill(map_copy, data, start_x - 1, start_y);
	ft_flood_fill(map_copy, data, start_x + 1, start_y);
	ft_flood_fill(map_copy, data, start_x, start_y - 1);
	ft_flood_fill(map_copy, data, start_x, start_y + 1);
}

/*==============================================================================
DESCRIPTION:
	ft_flood_fill_start() creates a map duplication to be modified later on and
	calls the fucntion ft_start_posit to get the starting position x and y
	(position of the character p/P) being saved in the correspnding structure.
	Finally, the function calls the function ft_flood_fill() to convert the c/C
	and e/E characters in X. By doing this, we finally can check if the map can
	be solved.

PARAMETERS:
	*map_data --> A pointer to a map structure with all the information about
	the original map

RETURN:
	NULL --> If the copy cannot be created.

	map_copy --> A copy of the original map.
==============================================================================*/
char	**ft_flood_fill_start(t_map_data *map_data)
{
	char	**map_copy;

	map_copy = ft_map_dup(map_data);
	if (!map_copy)
		return (NULL);
	ft_start_posit(map_data);
	ft_flood_fill(map_copy, map_data, map_data->start_x, map_data->start_y);
	return (map_copy);
}

/*==============================================================================
DESCRIPTION:
	ft_check_map_possible() checks whether the map has a solution. To do so, a
	map copy is created and the possible characters (0 - c/C - e/E) are changed
	to 'X'. If there are still special characters (collectables and exit),
	the map cannot be solved.

PARAMETERS:
	*mlx_data --> A pointer to the general structure that contains all the data
		needed in the program.

	c --> Character to be looked for.

RETURN:
	12 --> The copy cannot be created.

	11 --> The map cannot be solved.

	0 --> OK.
==============================================================================*/
int	ft_check_map_possible(t_mlx_data *mlx_data)
{
	char	**map_copy;
	int		line;
	int		col;
	int		count;

	map_copy = ft_flood_fill_start(&mlx_data->map_info);
	if (!map_copy)
		return (12);
	count = 0;
	line = -1;
	while (map_copy[++line])
	{
		col = -1;
		while (map_copy[line][++col])
		{
			if (map_copy[line][col] == 'c' || map_copy[line][col] == 'C'
				|| map_copy[line][col] == 'e' || map_copy[line][col] == 'E')
				count++;
		}
	}
	ft_free_double(map_copy);
	if (count)
		return (11);
	return (0);
}
