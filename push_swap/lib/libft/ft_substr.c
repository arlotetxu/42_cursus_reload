/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_substr.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joflorid <joflorid@student.42urduliz.co    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/09/18 12:27:48 by joflorid          #+#    #+#             */
/*   Updated: 2025/09/25 10:59:25 by joflorid         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

/*
================================================================================
DESCRIPTION
	The ft_substr() gets a substring from the 's' string.
	Prototype:
	char	*ft_substr(char const *s, unsigned int start,size_t len);

PARAMETERS
	s --> Main string.

	start --> Position in the 's' string to start the substring.

	len --> substring max length.

RETURN VALUE
	The substring.

	NULL --> If the memory allocation fails.
================================================================================
*/

char	*ft_substr(char const *s, unsigned int start, size_t len)
{
	char	*sub_s;
	size_t	s_len;
	size_t	i;

	if (!s)
		return (NULL);
	s_len = ft_strlen(s);
	if (start >= s_len)
		return (ft_strdup(""));
	if (s_len - start < len)
		len = s_len - start;
	sub_s = malloc(sizeof(char) * (len + 1));
	if (!sub_s)
		return (NULL);
	i = 0;
	while (i < len)
	{
		sub_s[i] = s[start];
		i++;
		start++;
	}
	sub_s[i] = '\0';
	return (sub_s);
}
