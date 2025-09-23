/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_lstclear_bonus.c                                :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joflorid <joflorid@student.42urduliz.co    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/09/23 15:38:47 by joflorid          #+#    #+#             */
/*   Updated: 2025/09/23 16:25:10 by joflorid         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft_bonus.h"

/*
================================================================================
DESCRIPTION
	The function ft_lstclear() deletes from a given node pointer on. The content
	is deleted using the function given as parameter 'del' and the node is 
	freed with free().
	Prototype:
	void	ft_lstclear(t_list **lst, void (*del)(void*));

PARAMETERS
	lst --> A pointer to the node from the deletion process must start.

	del --> Function to delete the node content

RETURN VALUE
	Nothing.
================================================================================
*/

void	ft_lstclear(t_list **lst, void (*del)(void*))
{
	t_list	*current;
	t_list	*next_node;

	if (!lst || !del)
		return ;
	current = *lst;
	while (current != NULL)
	{
		next_node = current->next;
		del(current->content);
		free(current);
		current = next_node;
	}
	*lst = NULL;
}
