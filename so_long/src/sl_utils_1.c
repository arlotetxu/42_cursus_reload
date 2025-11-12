/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   sl_utils_1.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joflorid <joflorid@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/10 13:40:09 by joflorid          #+#    #+#             */
/*   Updated: 2025/11/12 15:37:25 by joflorid         ###   ########.fr       */
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
		ft_printf("\x1b[41mError.\nCannot open the map file.\n\x1b[0m");
}

void	ft_double_free(char **str)
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
	free(str[i]);
	free(str);
}