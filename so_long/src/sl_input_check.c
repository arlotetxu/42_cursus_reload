/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   sl_input_check.c                                   :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joflorid <joflorid@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/12 12:11:08 by joflorid          #+#    #+#             */
/*   Updated: 2025/11/12 15:53:46 by joflorid         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../inc/so_long.h"

int	ft_feed_map_line(int fd, char **map_line)
{
	char	*gnl_line;


	gnl_line = get_next_line(fd);
	if (!gnl_line)
		return (1);
	//printf("strlen: %zu\n", ft_strlen(gnl_line));
	*map_line= ft_strdup(gnl_line);
	free(gnl_line);
	if (!(*map_line))
		return (1);
	//close(fd);
	return (0);
}

int	ft_ber2map(int fd, char *map_path, t_mlx_data *mlx_data)
{
	int	lines;
	int	i;
	int	ret;

	mlx_data->map_info.map = NULL;
	lines = 0;
	while(get_next_line(fd))
		lines++;
	close(fd);

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
			return(mlx_data->map_info.map[i] = NULL, close(fd), ft_double_free(mlx_data->map_info.map), 25);
	}
	mlx_data->map_info.map[i] = NULL;
	close(fd);
	mlx_data->map_info.lines = lines;
	mlx_data->map_info.column = ft_strlen(mlx_data->map_info.map[0]);
	return (0);
}
