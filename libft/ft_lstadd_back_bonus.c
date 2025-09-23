/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_lstadd_back_bonus.c                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joflorid <joflorid@student.42urduliz.co    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/09/23 11:56:27 by joflorid          #+#    #+#             */
/*   Updated: 2025/09/23 12:41:58 by joflorid         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft_bonus.h"

/*
================================================================================
DESCRIPTION
	The function ft_lstadd_back() adds the node 'new' at the end of the list
	pointed by 'lst'.
	Prototype:
	void	ft_lstadd_back(t_list **lst, t_list *new);

PARAMETERS
	lst --> Pointer to the first node of the list.
	
	new --> New node to be added at the end of the list.

RETURN VALUE
	Nothing.
================================================================================
*/

void	ft_lstadd_back(t_list **lst, t_list *new)
{
	t_list	*last;

	if (!lst || !new)
		return ;
	if (*lst == NULL)
	{
		*lst = new;
		return ;
	}
	last = ft_lstlast(*lst);
	last->next = new;
}
