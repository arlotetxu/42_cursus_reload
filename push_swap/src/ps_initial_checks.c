/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ps_initial_checks.c                                :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joflorid <joflorid@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/27 10:47:13 by joflorid          #+#    #+#             */
/*   Updated: 2025/10/31 15:31:08 by joflorid         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../inc/libft/libft.h"
#include "push_swap.h"

int	ft_check_dupli(char *full_args)
{
	int	*args_arr;
	int	len;
	int	i;
	int	j;

	args_arr = ft_load_nbr_arr(full_args, &len);
	if (!args_arr)
		return (1);
	i = -1;
	while (++i < len)
	{
		j = i;
		while (++j < len)
		{
			if (args_arr[i] == args_arr[j])
			{
				free(args_arr);
				return (1);
			}
		}
	}
	free(args_arr);
	return (0);
}

int	*ft_load_nbr_arr(char *full_args, int *len)
{
	char	**args_split;
	int		*args_arr;
	int		i;

	args_split = ft_split_2(full_args);
	if (!args_split)
		return (NULL); //!Error
	*len = 0;
	while (args_split[*len])
		(*len)++;
	args_arr = malloc(sizeof(int) * (*len)); //!MALLOC
	if (!args_arr)
		return (ft_free_double(args_split), NULL);
	i = -1;
	while (args_split[++i])
	{
		args_arr[i] = ft_atoi_2(args_split[i]);
		if (args_arr[i] == 0 && ft_strncmp(args_split[i], "0", 1) != 0)
			return (ft_free_double(args_split), NULL); //!Error. Ft_atoi devuelve 0 en caso de error
	}
	ft_free_double(args_split);
	return (args_arr);
}

static int	ft_input_len(int argc, char **argv)
{
	int	i;
	int	j;
	int	len;

	len = 0;
	i = 0;
	while (argv[++i] != NULL)
	{
		j = -1;
		while (argv[i][++j])
			len++;
	}
	return (len + argc - 2);
}

char	*ft_strjoin_2(int argc, char **argv)
{
	char	*full_args;
	int		len;
	int		i;
	int		j;
	int		k;

	len = ft_input_len(argc, argv);
	full_args = malloc(sizeof(char) * (len + 1)); //!MALLOC
	if (!full_args)
		return (NULL);
	k = 0;
	i = 0;
	while (argv[++i] != NULL)
	{
		j = -1;
		while (argv[i][++j])
		{
			full_args[k] = argv[i][j];
			k++;
		}
		if (i < argc - 1)
			full_args[k++] = 32;
	}
	full_args[k] = '\0';
	return (full_args);
}

int	ft_check_chars_argv(char *str)
{
	int		i;

	if (!str)
		return (1); //!Error
	i = -1;
	while (str[++i])
	{
		if (str[i] != '+' && str[i] != '-' && str[i] != 32 && str[i] != 9
			&& !(ft_isdigit(str[i])))
			return (1); //!Error
		if ((str[i] == '+' || str[i] == '-') && !(ft_isdigit(str[i + 1]))
			&& str[i])
			return (1); //!Error
	}
	return (0);
}
