/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strtrim.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joflorid <joflorid@student.42urduliz.co    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/09/18 14:06:32 by joflorid          #+#    #+#             */
/*   Updated: 2025/09/25 15:00:53 by joflorid         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"
#include <stdio.h>

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

static int	ft_check_char(char c, char const *set)
{
	int	i;

	i = 0;
	while (set[i])
	{
		if (c == set[i])
			return (1);
		i++;
	}
	return (0);
}

char	*ft_strtrim(char const *s1, char const *set)
{
	int		start;
	int		end;
	char	*s1_cut;

	if (!s1 || !set)
		return (NULL);
	start = 0;
	while (s1[start] && ft_check_char(s1[start], set))
		start++;
	end = ft_strlen(s1);
	while (end > start && ft_check_char(s1[end - 1], set))
		end--;
	s1_cut = (char *)malloc(sizeof(char) * (end - start + 1));
	if (!s1_cut)
		return (NULL);
	ft_strlcpy(s1_cut, s1 + start, end - start + 1);
	return (s1_cut);
}
