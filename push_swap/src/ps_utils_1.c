/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ps_utils_1.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joflorid <joflorid@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/27 10:56:12 by joflorid          #+#    #+#             */
/*   Updated: 2025/10/27 13:22:19 by joflorid         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../inc/libft/libft.h"
#include "push_swap.h"

void	ft_free_double(char **d_pointer)
{
	int	i;

	if (!d_pointer)
		return ;
	i = 0;
	while (d_pointer[i])
	{
		free(d_pointer[i]);
		i++;
	}
	free(d_pointer);
}

