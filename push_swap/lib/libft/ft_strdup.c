/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strdup.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joflorid <joflorid@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/09/18 11:48:28 by joflorid          #+#    #+#             */
/*   Updated: 2025/09/18 12:23:10 by joflorid         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

/*
================================================================================
DESCRIPTION
	The ft_strdup() duplicates a string allocating memory with malloc().
	Prototype:
	char	*ft_strdup(const char *s);

PARAMETERS
	s --> String to be duplicated.

RETURN VALUE
	The pointer to the duplicated string.

	NULL --> If the memory allocation fails.
================================================================================
*/

char	*ft_strdup(const char *s)
{
	char	*s_dup;

	if (!s)
		return (NULL);
	s_dup = malloc(ft_strlen(s) + 1);
	if (!s_dup)
		return (NULL);
	ft_memcpy(s_dup, s, ft_strlen(s) + 1);
	return (s_dup);
}
