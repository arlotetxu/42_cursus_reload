/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_lstmap_bonus.c                                  :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joflorid <joflorid@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/09/24 09:58:18 by joflorid          #+#    #+#             */
/*   Updated: 2025/09/24 10:51:46 by joflorid         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

/*
================================================================================
DESCRIPTION
	The function ft_lstmap() goes through the list pointed by 'lst' and applies
	the function 'f' to the content of each node crating a new list. The
	function pointed by 'del' removes the content of a node.

	Prototype:
	t_list	*ft_lstmap(t_list *lst, void *(*f)(void *),void (*del)(void *));

PARAMETERS
	lst --> Pointer to the first node of the list.

	f --> Function to apply to the content of each node.

	del --> Function to delete the node content.

RETURN VALUE
	A new list.
================================================================================
*/

t_list	*ft_lstmap(t_list *lst, void *(*f)(void *), void (*del)(void *))
{
	t_list	*new_lst;
	t_list	*new_node;

	if (!lst || !f)
		return (NULL);
	new_lst = NULL;
	while (lst != NULL)
	{
		new_node = ft_lstnew(f(lst->content));
		if (new_node == NULL)
		{
			ft_lstclear(&new_node, del);
			return (NULL);
		}
		ft_lstadd_back(&new_lst, new_node);
		lst = lst->next;
	}
	return (new_lst);
}
