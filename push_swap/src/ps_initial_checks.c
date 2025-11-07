/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ps_initial_checks.c                                :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joflorid <joflorid@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/27 10:47:13 by joflorid          #+#    #+#             */
/*   Updated: 2025/11/07 10:49:45 by joflorid         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../lib/libft/libft.h"
#include "../inc/push_swap.h"

/*==============================================================================
DESCRIPTION:
	ft_check_dupli() checks if there are duplications in the input arguments. To
	do so, firstly converts the string full_args in an array of numbers with the
	function ft_load_nbr_arr()

PARAMETERS:
	*full_args --> A string with all the input arguments.

RETURN:
	1 --> If there is not the array if numbers or if there are duplications.

	0 --> OK.
==============================================================================*/
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

/*==============================================================================
DESCRIPTION:
	ft_load_nbr_arr() receives a string with all the arguments, splits it into
	different string thanks to the function ft_split_2() and converts each
	string in a number through the ft_atoi_2() function. As ft_atoi_2() function
	returns 0 in case of error, a check is done to compare if the processed
	number is 0 to avoid errors.

PARAMETERS:
	*full_args --> a pointer to the string with all the input.

	*len --> a pointer to save the string len.

RETURN:
	NULL --> in case of error in malloc or any other function

	args_arr --> the array of number comming from the input
==============================================================================*/
int	*ft_load_nbr_arr(char *full_args, int *len)
{
	char	**args_split;
	int		*args_arr;
	int		i;

	args_split = ft_split_2(full_args);
	if (!args_split)
		return (NULL);
	*len = 0;
	while (args_split[*len])
		(*len)++;
	args_arr = malloc(sizeof(int) * (*len));
	if (!args_arr)
		return (ft_free_double(args_split), NULL);
	i = -1;
	while (args_split[++i])
	{
		args_arr[i] = ft_atoi_2(args_split[i]);
		if (args_arr[i] == 0 && ft_strncmp(args_split[i], "0", 1) != 0)
			return (ft_free_double(args_split), free(args_arr), NULL);
	}
	ft_free_double(args_split);
	return (args_arr);
}

/*==============================================================================
DESCRIPTION:
	ft_input_len() calculates the size of the input adding extra space for the
	characters used as separator.

PARAMETERS:
	argc --> The number of arguments received from the terminal.

	**argv --> A pointer to the array of arguments received from the terminal.

RETURN:
	len + argc - 2 --> The size of the final string where all the arguments are
		going to be saved.
==============================================================================*/
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

/*==============================================================================
DESCRIPTION:
	ft_strjoin_2() joins all the input arguments in a single string that is used
		to evaluate possible input errors.

PARAMETERS:
	argc --> The number of arguments received from the terminal.

	**argv --> A pointer to the array of arguments received from the terminal.

RETURN:
	NULL --> If the memory book fails

	full_args --> the string that contains all the input arguments.
==============================================================================*/
char	*ft_strjoin_2(int argc, char **argv)
{
	char	*full_args;
	int		len;
	int		i;
	int		j;
	int		k;

	len = ft_input_len(argc, argv);
	full_args = malloc(sizeof(char) * (len + 1));
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

/*==============================================================================
DESCRIPTION:
	ft_check_chars_argv() checks if the characters in the input arguments are
	right. The consedered characters are:
	+ // - // spaces // tabs // digits

PARAMETERS:
	*str --> A string with all the input arguments.

RETURN:
	1 --> If there is not the str or there are any character not allowed.

	0 --> OK.
==============================================================================*/
int	ft_check_chars_argv(char *str)
{
	int		i;

	if (!str)
		return (1);
	i = -1;
	while (str[++i])
	{
		if (str[i] != '+' && str[i] != '-' && str[i] != 32 && str[i] != 9
			&& !(ft_isdigit(str[i])))
			return (1);
		if ((str[i] == '+' || str[i] == '-') && !(ft_isdigit(str[i + 1]))
			&& str[i])
			return (1);
	}
	return (0);
}
