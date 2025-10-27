/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_split_2.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joflorid <joflorid@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/09/19 10:25:16 by joflorid          #+#    #+#             */
/*   Updated: 2025/10/27 17:01:26 by joflorid         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

/*
================================================================================
DESCRIPTION
	The function ft_split() takes a string and split it into words. The 'c'
	parameter acts as delimiter between words. The words are saved in a new
	array that it is returned with a null pointer at the end.
	Prototype:
	char	**ft_split(const char *str)

PARAMETERS
	str --> The main string.

RETURN VALUE
	A pointer to the strings array.
================================================================================
*/

static void	ft_free_split(char **split, int words)
{
	int	i;

	i = 0;
	while (i < words)
	{
		free(split[i]);
		i++;
	}
	free(split);
}

static int	ft_count_words(const char *str)
{
	int	i;
	int	flag;
	int	count;

	i = 0;
	while (str[i] && (str[i] == 32 || str[i] == 9))
		i++;
	count = 0;
	flag = 0;
	while (str[i])
	{
		if (str[i] != 32 && str[i]!= 9)
			flag = 1;
		if ((str[i] == 32 || str[i] == 9) && flag == 1)
		{
			count++;
			flag = 0;
		}
		i++;
	}
	if (flag == 1)
		count++;
	return (count);
}

char	*ft_get_word(const char *str, int *pos)
{
	char	*word;
	int		start;
	int		i;

	while (str[*pos] && (str[*pos] == 32 || str[*pos] == 9))
		(*pos)++;
	start = *pos;
	i = 0;
	while (str[*pos] && str[*pos] != 32 && str[*pos] != 9)
		(*pos)++;
	word = ft_substr(str, start, *pos - start);
	if (!word)
		return (NULL);
	return (word);
}

char	**ft_split_2(const char *str)
{
	char	**w_stack;
	int		i;
	int		pos;
	int		words;

	words = ft_count_words(str);
	w_stack = malloc(sizeof(char *) * (words + 1));
	if (!w_stack)
		return (NULL);
	i = -1;
	pos = 0;
	while (++i < words)
	{
		w_stack[i] = ft_get_word(str, &pos);
		if (!w_stack[i])
			return (ft_free_split(w_stack, i), NULL);
	}
	w_stack[i] = NULL;
	return (w_stack);
}
