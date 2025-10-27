/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_lstnew_bonus.c                                  :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joflorid <joflorid@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/09/22 16:43:09 by joflorid          #+#    #+#             */
/*   Updated: 2025/09/24 10:51:51 by joflorid         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

/*
================================================================================
DESCRIPTION
	The function ft_lstnew() creates a new node in a linked list using malloc.
	The node variable 'content' if initialize with the function's parameter
	'content'
	Prototype:
	t_list	*ft_lstnew(void *content);

PARAMETERS
	content --> Data the node stores.

RETURN VALUE
	The new created node
================================================================================
*/

t_list	*ft_lstnew(void *content)
{
	t_list	*new_node;

	new_node = malloc(sizeof(t_list));
	if (!new_node)
		return (NULL);
	new_node->content = content;
	new_node->next = NULL;
	return (new_node);
}
