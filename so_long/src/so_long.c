/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   so_long.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joflorid <joflorid@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/12 11:50:56 by joflorid          #+#    #+#             */
/*   Updated: 2025/11/12 15:38:49 by joflorid         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../inc/so_long.h"


/*
CHECK LIST INPUT VALIDATION

* Numero de argumentos correctos //?OK
* Argumento con extension .ber
* El fichero existe fd != -1
* Parsear el mapa con gnl
* El mapa es rectangular
* El mapa esta cerrado
* Caracteres validos en el mapa (Ojo mayusculas - minusculas).
	Al menos 1 coleccionable (C), 1 salida(E) y 1 posicion inicial de personaje(P).
	0 y 1 para paredes y espacios abiertos
* El mapa es valido. Se llega a la salida sin dejarse ningun coleccionable
	flood_fill()
En caso de fallos de configuración de cualquier tipo encontrados en el archivo, el
programa debe terminar correctamente y devolver “Error\n” seguido de un mensaje
explícito de tu elección.
*/

/*
ERROR CODES
1 - Invalid number of arguments
2 - Cannot open the map file.
3 - Cannot load the map. Memory issues.
*/
int	main(int argc, char **argv)
{
	int	fd;
	t_mlx_data	*mlx_data;

	if (argc != 2)
		return (ft_print_error(1), 1);
	fd = open(argv[1], O_RDONLY);
	if (fd == -1)
		return (ft_print_error(2), 2);
	mlx_data = malloc(sizeof(t_mlx_data));
	if (!mlx_data)
		return (1);
	ft_ber2map(fd, argv[1], mlx_data);
	close(fd);
	ft_double_free(mlx_data->map_info.map);
	free(mlx_data->mlx_ptr);
	free(mlx_data);
	return (0);
}