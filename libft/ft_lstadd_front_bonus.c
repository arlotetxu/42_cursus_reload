/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_lstadd_front_bonus.c                            :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joflorid <joflorid@student.42urduliz.co    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/09/23 08:34:03 by joflorid          #+#    #+#             */
/*   Updated: 2025/09/23 11:50:24 by joflorid         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft_bonus.h"

/*
================================================================================
DESCRIPTION
	The function ft_lstnew() adds the node 'new' at the beginning of the list
	(lst).
	Prototype:
	void	ft_lstadd_front(t_list **lst, t_list *new);

PARAMETERS
	lst --> Pointer to the first node of the list.

	new --> New node to be added at the beginning of the list.

RETURN VALUE
	Nothing
================================================================================
*/

void	ft_lstadd_front(t_list **lst, t_list *new)
{
	if (!lst || !new)
		return ;
	new->next = *lst;
	*lst = new;
}
