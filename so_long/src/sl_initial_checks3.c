/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   sl_initial_checks3.c                               :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joflorid <joflorid@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/13 16:28:05 by joflorid          #+#    #+#             */
/*   Updated: 2025/11/13 17:28:50 by joflorid         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../inc/so_long.h"

void	ft_free_double(char **str)
{
	int	i;

	if (!str)
		return ;
	i = -1;
	while (str[++i])
		free(str[i]);
	free(str);
}

char	**ft_map_dup(t_map_data *map_data)
{
	char	**map_dup;
	int		i;

	map_dup = malloc (sizeof(char *) * (map_data->lines + 1)); //!MALLOC
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

// char	**ft_flood_fill(char **map)
// {
// 	char	**map_copy;
// 	t_coord	map_size; //!son lines y colums de la estructura de mapa
// 	t_coord	start_p; //!Calcular. Necesitaremos 2 funciones para saber la
					//!posicion de inicio en x e y. Guardarlas en las variables
					//!creadas en la estructura del mapa.

// 	map_copy = ft_dupli_map(map, ft_map_size(map));
// 	map_size = ft_map_size(map_copy); //!No necesario
// 	start_p = ft_start_posit(map_copy);
// 	ft_fill_map(map_copy, map_size, start_p);
// 	return (map_copy);
// }