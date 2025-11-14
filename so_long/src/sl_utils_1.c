/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   sl_utils_1.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joflorid <joflorid@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/10 13:40:09 by joflorid          #+#    #+#             */
/*   Updated: 2025/11/14 13:08:24 by joflorid         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../inc/so_long.h"

/*==============================================================================
DESCRIPTION:
	ft_print_error() shows an error message in the terminal with the proper
	explanation about the error.

PARAMETERS:
	**stack --> A pointer to the stack in which the movement has to be applied.

	stack_id --> Stack identification

RETURN:
	Nothing.
==============================================================================*/
void	ft_print_error(int err_n)
{
	if (err_n == 1)
		ft_printf("\x1b[41mError.\nInvalid number of arguments.\n\x1b[0m");
	else if (err_n == 2)
		ft_printf("\x1b[41mError.\nMap file couldn't be found.\n\x1b[0m");
	else if (err_n == 6)
		ft_printf("\x1b[41mError.\nWrong map file.\n\x1b[0m");
	else if (err_n == 7)
		ft_printf("\x1b[41mError.\nThe map is not a rectangle.\n\x1b[0m");
	else if (err_n == 8)
		ft_printf("\x1b[41mError.\nMap with different line's length.\n\x1b[0m");
	else if (err_n == 9)
		ft_printf("\x1b[41mError.\nWrong character type in the map.\n\x1b[0m");
	else if (err_n == 10)
		ft_printf("\x1b[41mError.\nWrong characters number.\n\x1b[0m");
	else if (err_n == 11)
		ft_printf("\x1b[41mError.\nMap with no solution.\n\x1b[0m");
}

/*==============================================================================
DESCRIPTION:
	ft_double_free() frees a double pointer char variable.

PARAMETERS:
	**str --> A pointer to the data to be freed.

RETURN:
	Nothing.
==============================================================================*/
void	ft_freeing(char **str, t_mlx_data *mlx_data)
{
	int	i;

	if (!str)
		return ;
	i = 0;
	while (str[i])
	{
		free(str[i]);
		i++;
	}
	free(str);
	if (mlx_data->mlx_ptr)
		free(mlx_data->mlx_ptr);
	free(mlx_data);
}

/*==============================================================================
DESCRIPTION:
	ft_strlen_sl() calculates the length of a string until a '\0' or '\n' is
	found.

PARAMETERS:
	*str --> A pointer to the string to be measured.

RETURN:
	count --> The length of the string.
==============================================================================*/
int	ft_strlen_sl(char *str)
{
	int	count;

	count = 0;
	while (*str && *str != '\n' && *str != '\0')
	{
		count++;
		str++;
	}
	return (count);
}

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
