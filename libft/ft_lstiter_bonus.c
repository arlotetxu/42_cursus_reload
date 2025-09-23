/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_lstiter_bonus.c                                 :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joflorid <joflorid@student.42urduliz.co    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/09/23 16:27:17 by joflorid          #+#    #+#             */
/*   Updated: 2025/09/23 17:03:40 by joflorid         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft_bonus.h"

/*
================================================================================
DESCRIPTION
	The function ft_lstiter() applies the function 'f' passed as an argument
	to all the nodes content of the list 'lst'
	Prototype:
	void	ft_lstiter(t_list *lst, void (*f)(void *));

PARAMETERS
	lst --> A pointer to the list.

	(*f) --> A pointer to a function to apply to all nodes content.

RETURN VALUE
	Nothing.
================================================================================
*/

void	ft_lstiter(t_list *lst, void (*f)(void *))
{
	if (!lst || !f)
		return ;
	while (lst != NULL)
	{
		f(lst->content);
		lst = lst->next;
	}
}
