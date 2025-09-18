/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strtrim.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joflorid <joflorid@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/09/18 14:06:32 by joflorid          #+#    #+#             */
/*   Updated: 2025/09/18 16:15:27 by joflorid         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

/*
================================================================================
DESCRIPTION
	The ft_strtrim() function remove from the string 's1' all the characters
	that appear in 'set' string untill a character not included in 'set' is
	found. The process must be done from left to right and viceversa.

	Prototype:
	char	*ft_strtrim(char const *s1, char const *set);

PARAMETERS

	s1 --> Main string

	set --> Set of characters to be removed from 's1'.

RETURN VALUE
	The final string without the set characters.

	NULL --> If the allocation process fails.
================================================================================
*/
static int	ft_cut_left(const char *s1, const char *set)
{
	int	i;
	int	j;

	i = 0;
	while (s1[i] != '\0')
	{
		j = 0;
		while (set[j] != '\0')
		{
			if (s1[i] == set[j])
				break ;
			if (s1[i] != set[j])
				j++;
			if (set[j] == '\0')
				return (i);
		}
		i++;
	}
	return (i);
}

static int	ft_cut_right(const char *s1, const char *set)
{
	int	i;
	int	j;

	i = ft_strlen(s1) - 1;
	while (i >= 0)
	{
		j = 0;
		while (set[j] != '\0')
		{
			if (s1[i] == set[j])
				break ;
			if (s1[i] != set[j])
				j++;
			if (set[j] == '\0')
				return (i);
		}
		i--;
	}
	return (0);
}

char	*ft_strtrim(char const *s1, char const *set)
{
	int		start;
	int		end;
	int		i;
	char	*cut;

	if (!s1)
		return (NULL);
	if (!set || !set[0])
	{
		cut = (char *)s1;
		return (cut);
	}
	start = ft_cut_left(s1, set);
	end = ft_cut_right(s1, set);
	cut = malloc(sizeof(char) * (end - start + 2));
	if (!cut)
		return (NULL);
	i = 0;
	while (start <= end)
	{
		cut[i] = s1[start];
		i++;
		start++;
	}
	return (cut);
}
