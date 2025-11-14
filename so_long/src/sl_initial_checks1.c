/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   sl_initial_checks1.c                               :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joflorid <joflorid@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/13 11:13:01 by joflorid          #+#    #+#             */
/*   Updated: 2025/11/14 13:07:22 by joflorid         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../inc/so_long.h"

/*==============================================================================
DESCRIPTION:
	ft_check_map_ext() gets the last 4 character from the map file (extension)
	passed with argv1 parameter and checks if it is '.ber'.

PARAMETERS:
	argv1 --> map path

RETURN:
	5 --> The extension is not .ber

	0 --> OK
==============================================================================*/
int	ft_check_map_ext(char *argv1)
{
	char	*ext;
	int		len;
	int		start;
	int		i;

	ext = malloc(sizeof(char) * 5);
	if (!ext)
		return (5);
	len = ft_strlen(argv1);
	start = len - 4;
	if (!argv1[start - 1] || argv1[start - 1] == '/')
		return (free(ext), 6);
	i = -1;
	while (start < len)
		ext[++i] = argv1[start++];
	argv1[start] = '\0';
	if (ft_strncmp(ext, ".ber", 4))
		return (free(ext), 6);
	free(ext);
	return (0);
}

/*==============================================================================
DESCRIPTION:
	ft_map_rectangle() checks if all the lines of the map have the same length.

PARAMETERS:
	*mlx_data --> A pointer to the general structure that contains all the data
		needed in the program.

RETURN:
	7 --> The map lines have not the same length.

	0 --> OK
==============================================================================*/
int	ft_map_rectangle(t_mlx_data *mlx_data)
{
	int	i;

	i = 0;
	while (mlx_data->map_info.map[i])
	{
		if ((int)ft_strlen_sl(mlx_data->map_info.map[i])
			!= mlx_data->map_info.column)
			return (7);
		i++;
	}
	return (0);
}

/*==============================================================================
DESCRIPTION:
	ft_map_is_closed() checks if the map is rounded completely by '1' character.

PARAMETERS:
	*mlx_data --> A pointer to the general structure that contains all the data
		needed in the program.

RETURN:
	8 --> The map is not fully rounded by '1'.

	0 --> OK
==============================================================================*/
int	ft_map_is_closed(t_mlx_data *mlx_data)
{
	int	i;
	int	j;

	i = -1;
	while (mlx_data->map_info.map[0][++i] != '\0'
			&& mlx_data->map_info.map[0][i] != '\n')
		if (mlx_data->map_info.map[0][i] != '1')
			return (8);
	j = mlx_data->map_info.lines - 1;
	i = -1;
	while (mlx_data->map_info.map[j][++i] != '\0'
			&& mlx_data->map_info.map[j][i] != '\n')
		if (mlx_data->map_info.map[j][i] != '1')
			return (8);
	j = mlx_data->map_info.column - 1;
	i = -1;
	while (mlx_data->map_info.map[++i])
	{
		if (mlx_data->map_info.map[i][0] != '1'
			|| mlx_data->map_info.map[i][j] != '1')
			return (8);
	}
	return (0);
}

/*==============================================================================
DESCRIPTION:
	ft_check_chars() checks if the characters included in the map definition are
	the righ ones (1 / 0 / P / p / C / c / E / e).

PARAMETERS:
	*mlx_data --> A pointer to the general structure that contains all the data
		needed in the program.

RETURN:
	9 --> The map has not allowed characters.

	0 --> OK
==============================================================================*/
int	ft_check_chars(t_mlx_data *mlx_data)
{
	int	i;
	int	j;

	i = -1;
	while (++i < mlx_data->map_info.lines)
	{
		j = -1;
		while (++j < mlx_data->map_info.column - 1)
		{
			if (mlx_data->map_info.map[i][j] != '1'
				&& mlx_data->map_info.map[i][j] != '0'
				&& mlx_data->map_info.map[i][j] != 'e'
				&& mlx_data->map_info.map[i][j] != 'E'
				&& mlx_data->map_info.map[i][j] != 'p'
				&& mlx_data->map_info.map[i][j] != 'P'
				&& mlx_data->map_info.map[i][j] != 'c'
				&& mlx_data->map_info.map[i][j] != 'C')
				return (9);
		}
	}
	return (0);
}
