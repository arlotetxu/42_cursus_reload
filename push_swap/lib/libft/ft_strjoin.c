/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strjoin.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joflorid <joflorid@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/09/18 13:21:21 by joflorid          #+#    #+#             */
/*   Updated: 2025/09/18 13:52:53 by joflorid         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

/*
================================================================================
DESCRIPTION
	The ft_strjoin() concatenates 2 strings in a new one.
	Prototype:
	char	*ft_strjoin(char const *s1, char const *s2);

PARAMETERS
	s1 --> String 1.

	s2 --> String 2 to be added to s1.

RETURN VALUE
	The new string created.

	NULL --> If the memory allocation fails.
================================================================================
*/

char	*ft_strjoin(char const *s1, char const *s2)
{
	char	*s3;
	int		s3_len;

	if (!s1 || !s2)
		return (NULL);
	s3_len = ft_strlen(s1) + ft_strlen(s2);
	s3 = malloc(sizeof(char) * (s3_len + 1));
	if (!s3)
		return (NULL);
	ft_strlcpy(s3, s1, ft_strlen(s1) + 1);
	ft_strlcat(s3, s2, s3_len + 1);
	return (s3);
}
