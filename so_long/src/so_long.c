/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   so_long.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joflorid <joflorid@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/12 11:50:56 by joflorid          #+#    #+#             */
/*   Updated: 2025/11/17 16:30:02 by joflorid         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../inc/so_long.h"


/*
CHECK LIST INPUT VALIDATION

* Numero de argumentos correctos //?OK
* Argumento con extension .ber //?OK
* El fichero existe fd != -1 //?OK
* Parsear el mapa con gnl //?OK
* El mapa es rectangular //?OK
* El mapa esta cerrado //?OK
* Caracteres validos en el mapa (Ojo mayusculas - minusculas).//?OK
* Al menos 1 coleccionable (C), 1 salida(E) y 1 posicion inicial de personaje(P).
	0 y 1 para paredes y espacios abiertos //?OK
* El mapa es valido. Se llega a la salida sin dejarse ningun coleccionable //?OK
	flood_fill()
En caso de fallos de configuración de cualquier tipo encontrados en el archivo, el
programa debe terminar correctamente y devolver “Error\n” seguido de un mensaje
explícito de tu elección.
*/

int	ft_intial_checks(char *map_path, t_mlx_data *mlx_data)
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


int	ft_launcher(int fd, char *map_path, t_mlx_data *mlx_data)
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
	//!INICIALIZAR VENTANA
	ret = ft_graphics_init(mlx_data);

	return (ret);
}
/*
ERROR CODES
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
		return (1);
	mlx_data->mlx_ptr = NULL;
	mlx_data->map_info.map = NULL;
	ret = 0;
	ret = ft_launcher(fd, argv[1], mlx_data);

	mlx_destroy_window(mlx_data->mlx_ptr, mlx_data->win_info.win_ptr);
	mlx_destroy_display(mlx_data->mlx_ptr);

	if (mlx_data->map_info.map)
		ft_freeing(mlx_data->map_info.map, mlx_data);
	// if (mlx_data->mlx_ptr)
	// 	free(mlx_data->mlx_ptr);
	//free(mlx_data);
	return (ret);
}
