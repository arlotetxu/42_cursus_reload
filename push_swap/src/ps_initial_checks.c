/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ps_initial_checks.c                                :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joflorid <joflorid@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/27 10:47:13 by joflorid          #+#    #+#             */
/*   Updated: 2025/10/27 17:14:52 by joflorid         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../inc/libft/libft.h"
#include "push_swap.h"

int	*ft_load_nbr_arr(char **argv, int *len)
{
	char	**args_stack;
	int		*nbr_list;
	int		i;

	args_stack = ft_split_2(argv[1]); //!cUIDADOO. COMPROBAR SPLIT
	if (!args_stack)
		return (NULL);
	*len = 0;
	while (args_stack[*len])
		(*len)++;
	nbr_list = malloc(sizeof(int) * (*len));
	if (!nbr_list)
		return (ft_free_double(args_stack), NULL);
	i = -1;
	while (++i < *len)
	{
		nbr_list[i] = ft_atoi(args_stack[i]);
		if (nbr_list[i] == 0 && ft_strncmp(args_stack[i], "0", 1) != 0)
		//!ft_atoi devuelve 0 si hay error por lo que compruebo que el caracter a covertir no era 0
			return (free(nbr_list), ft_free_double(args_stack), NULL);
	}
	ft_free_double(args_stack);
	return (nbr_list);
}

int	ft_check_duplicates(char **argv)
{
	int	*nbr_list;
	int	len;
	int	i;
	int	j;

	nbr_list = ft_load_nbr_arr(argv, &len);
	if (!nbr_list)
		return (1); //!Error
	//printf("Valor de len: %i\n", len); //!PRINTF
	i = -1;
	while (++i < len)
	{
		j = i;
		while (++j < len)
		{
			if (nbr_list[i] == nbr_list[j])
			{
				//printf("Hay duplicados\n"); //!PRINTF
				return (1); //!Error
			}
		}
	}
	return (0);
}

int	ft_check_chars_argv(int argc, char **argv)
{
	char	*str;
	int		i;

	i = 1;
	while (i < argc)
	{
		str = argv[i];
		if (!str)
			return (1); //!Error
		while (*str)
		{
			if (*str != '+' && *str != '-' && *str != 32 && *str != 9
				&& !(ft_isdigit(*str)))
				return (1); ///!Error
			str++;
		}
		i++;
	}
	return (0);
}
