/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_lstsize_bonus.c                                 :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joflorid <joflorid@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/09/23 10:45:01 by joflorid          #+#    #+#             */
/*   Updated: 2025/09/24 10:51:57 by joflorid         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

/*
================================================================================
DESCRIPTION
	The function ft_lstsize() returns the length of the list (quantity of nodes).
	Prototype:
	int	ft_lstsize(t_list *lst);

PARAMETERS
	lst --> Pointer to the first node of the list.

RETURN VALUE
	The list size.
================================================================================
*/

int	ft_lstsize(t_list *lst)
{
	int	count;

	count = 0;
	while (lst != NULL)
	{
		count += 1;
		lst = lst->next;
	}
	return (count);
}
