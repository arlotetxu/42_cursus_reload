/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   sl_initial_checks2.c                               :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joflorid <joflorid@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/13 15:35:00 by joflorid          #+#    #+#             */
/*   Updated: 2025/11/13 16:08:10 by joflorid         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../inc/so_long.h"

/*==============================================================================
DESCRIPTION:
	ft_count_char() returns the total number of character 'c' found in the map
		included in the structure 'mlx_data'.

PARAMETERS:
	*mlx_data --> A pointer to the general structure that contains all the data
		needed in the program.

	c --> Character to be looked for.

RETURN:
	count --> The times the character 'c' is found.
==============================================================================*/
static int	ft_count_char(t_mlx_data *mlx_data, char c)
{
	int	count;
	int	i;
	int	j;

	count = 0;
	i = -1;
	while (mlx_data->map_info.map[++i])
	{
		j = -1;
		while (mlx_data->map_info.map[i][++j])
		{
			if (mlx_data->map_info.map[i][j] == c)
				count++;
		}
	}
	return (count);
}

/*==============================================================================
DESCRIPTION:
	ft_total_chars() checks the times a special character allowed in the map
	appears and evaluates if the number is ok or not.
	p / P --> only 1 time.
	e / E --> only 1 time.
	c / C --> At least, 1 time.

PARAMETERS:
	*mlx_data --> A pointer to the general structure that contains all the data
		needed in the program.

RETURN:
	10 --> In case the number is wrong per character.

	0 --> OK.
==============================================================================*/
int	ft_total_chars(t_mlx_data *mlx_data)
{
	int	count_p;
	int	count_e;
	int	count_c;

	count_p = ft_count_char(mlx_data, 'p');
	count_p += ft_count_char(mlx_data, 'P');
	count_e = ft_count_char(mlx_data, 'e');
	count_e += ft_count_char(mlx_data, 'E');
	count_c = ft_count_char(mlx_data, 'c');
	count_c += ft_count_char(mlx_data, 'C');
	if (count_p > 1 || count_e > 1 || count_c < 1)
		return (10);
	return (0);
}
