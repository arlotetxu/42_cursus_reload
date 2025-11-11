/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   toy_program.c                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joflorid <joflorid@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/08 19:47:14 by joflorid          #+#    #+#             */
/*   Updated: 2025/11/11 16:17:56 by joflorid         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../inc/so_long.h"

int	ft_close_window(t_mlx_data *mlx_data)
{

	mlx_destroy_window(mlx_data->mlx_ptr, mlx_data->win_info.win_ptr);
	mlx_destroy_display(mlx_data->mlx_ptr);
	free(mlx_data->mlx_ptr);
	free(mlx_data);
	exit(0);
}


int	ft_print_key(int keycode, t_mlx_data *mlx_data)
{
	ft_printf("Pressed key: %i\n", keycode);
	//sleep to apreciate loop_hook stopping
	//sleep(1);
	if (keycode == XK_Escape)
	{
		ft_printf("Closing the window...\n");
		ft_close_window(mlx_data);
	}
	return (1);
}

int	ft_mouse_posit(int button, int x, int y, t_mlx_data *mlx_data)
{
	ft_printf("Posicion X: %i  -- Posicion Y: %i\n", x, y);
	return (1);
}

int	main(void)
{
	t_mlx_data	*mlx_data;

	mlx_data = malloc(sizeof(t_mlx_data));
	if (!mlx_data)
		return (1);

	//Inicializamos el servidor grafico
	mlx_data->mlx_ptr = mlx_init();
	if (!mlx_data->mlx_ptr)
		return (1);

	// Creamos una ventana
	mlx_data->win_info.win_ptr = mlx_new_window(mlx_data->mlx_ptr, WIN_L, WIN_H, "JFLORID");
	if (!mlx_data->win_info.win_ptr)
	{
		mlx_destroy_display(mlx_data->mlx_ptr);
		free(mlx_data->mlx_ptr);
		free(mlx_data);
		return (2);
	}

	//Leemos la tecla pulsada e imprimimos el su codigo en terminal
	//Realmente, mlx_key_hook() es un alias de mlx_hook() para el event 02
	mlx_key_hook(mlx_data->win_info.win_ptr, ft_print_key, mlx_data);
	//Alternativa. En este caso se usa mlx_hook(). Para este caso concreto, se
	//necesitan mascaras ((1L<<0)) para el evento 02 (KeyPress)
	//mlx_hook(mlx_data->win_ptr, 02, (1L<<0), ft_print_key, mlx_data);

	//Creamos hook para cerrar la ventana con el boton X
	mlx_hook(mlx_data->win_info.win_ptr, 17, 0, ft_close_window, mlx_data);

	//Creamos hook para evento de click en raton
	mlx_hook(mlx_data->win_info.win_ptr, 04, (1L<<2), ft_mouse_posit, mlx_data);

	//Lanzamos el bucle para mantener el display y la ventana?
	mlx_loop(mlx_data->mlx_ptr);

	//Salimos liberando todo
	// mlx_destroy_window(mlx_data->mlx_ptr, mlx_data->win_ptr);
	// mlx_destroy_display(mlx_data->mlx_ptr);
	// free(mlx_data->mlx_ptr);
	// free(mlx_data);
	return (0);
}
