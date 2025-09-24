/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_lstdelone_bonus.c                               :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joflorid <joflorid@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/09/23 14:52:36 by joflorid          #+#    #+#             */
/*   Updated: 2025/09/24 10:51:28 by joflorid         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

/*
================================================================================
DESCRIPTION
	The function ft_lstdelone() deletes the content of a given node passed as
	an argument 'lst' using the function 'del' passed as parameter. The node is
	freed.
	Prototype:
	void	ft_lstdelone(t_list *lst, void (*del)(void*));

PARAMETERS
	lst --> The node to be freed.

	del --> Function to delete the node content

RETURN VALUE
	Nothing.
================================================================================
*/

void	ft_lstdelone(t_list *lst, void (*del)(void*))
{
	if (!lst || !del)
		return ;
	del(lst->content);
	free(lst);
}
