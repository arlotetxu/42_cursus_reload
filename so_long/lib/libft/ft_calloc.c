/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_calloc.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joflorid <joflorid@student.42urduliz.co    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/09/18 10:41:21 by joflorid          #+#    #+#             */
/*   Updated: 2025/09/28 07:20:55 by joflorid         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

/*
================================================================================
DESCRIPTION
	The ft_calloc() allocates memory for an array of 'nmemb' with a 'size' bytes
	each one. The memory is set to zero.
	Prototype:
	void	*ft_calloc(size_t nmemb, size_t size);

PARAMETERS
	nmemb --> Number of members that compose the array.

	size --> size of each member

RETURN VALUE
	The pointer to the allocated memory.

	If nmemb or size are 0, the function returns a unique pointer that can be
	freeses later on with free().
================================================================================
*/

void	*ft_calloc(size_t nmemb, size_t size)
{
	void	*ptr;

	if (nmemb == 0 || size == 0)
	{
		ptr = malloc(1);
		if (!ptr)
			return (NULL);
		ft_bzero(ptr, 1);
		return (ptr);
	}
	if (nmemb > ((size_t)-1) / size)
		return (NULL);
	ptr = malloc(nmemb * size);
	if (!ptr)
		return (NULL);
	ft_bzero(ptr, nmemb * size);
	return (ptr);
}
