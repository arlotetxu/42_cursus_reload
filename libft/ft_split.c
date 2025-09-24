/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_split.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joflorid <joflorid@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/09/19 10:25:16 by joflorid          #+#    #+#             */
/*   Updated: 2025/09/24 13:54:52 by joflorid         ###   ########.fr       */
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
	char	**ft_split(char const *s, char c);

PARAMETERS
	s --> The main string.

	c --> Delimiter character.

RETURN VALUE
	A pointer to the strings array.
================================================================================
*/

static int	ft_count_words(char const *s, char c)
{
	int	flag;
	int	count_w;
	int	i;

	count_w = 0;
	i = 0;
	while (s[i] && s[i] == c)
		i++;
	while (s[i])
	{
		flag = 0;
		while (s[i] && s[i] != c)
		{
			flag = 1;
			i++;
		}
		if (flag == 1)
			count_w += 1;
		if (!s[i])
			return (count_w);
		i++;
	}
	return (count_w);
}

static char	*ft_load_word(const char **ptr, int c)
{
	char	*word;
	int		i;
	int		len;

	while (**ptr && **ptr == c)
		(*ptr)++;
	len = 0;
	while ((*ptr)[len] && (*ptr)[len] != c)
		len++;
	if (len == 0)
		return (NULL);
	word = malloc(sizeof(char) * (len + 1));
	if (!word)
		return (NULL);
	i = 0;
	while (i < len)
	{
		word[i] = (*ptr)[i];
		i++;
	}
	word[i] = '\0';
	*ptr += len;
	return (word);
}

char	**ft_split(char const *s, char c)
{
	char	**ptr_w;
	int		n_words;
	int		i;

	n_words = ft_count_words(s, c);
	ptr_w = malloc(sizeof(char *) * (n_words + 1));
	if (!ptr_w)
		return (NULL);
	i = 0;
	while (i < n_words)
	{
		ptr_w[i] = ft_load_word(&s, c);
		i++;
	}
	ptr_w[i] = NULL;
	return (ptr_w);
}
