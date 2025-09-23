/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_lstlast_bonus.c                                 :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joflorid <joflorid@student.42urduliz.co    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/09/23 11:31:45 by joflorid          #+#    #+#             */
/*   Updated: 2025/09/23 11:51:37 by joflorid         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft_bonus.h"

/*
================================================================================
DESCRIPTION
	The function ft_lstlast() returns the last node from the list 'lst'.
	Prototype:
	t_list	*ft_lstlast(t_list *lst);

PARAMETERS
	lst --> Pointer to the first node of the list.

RETURN VALUE
	The last node.
================================================================================
*/

t_list	*ft_lstlast(t_list *lst)
{
	if (!lst)
		return (NULL);
	while (lst->next != NULL)
		lst = lst->next;
	return (lst);
}
