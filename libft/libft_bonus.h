/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   libft_bonus.h                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joflorid <joflorid@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/09/15 12:24:36 by joflorid          #+#    #+#             */
/*   Updated: 2025/09/22 17:08:21 by joflorid         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef LIBFT_BONUS_H
# define LIBFT_BONUS_H

//===========STD LIBRARIES===========
# include <stdio.h>
# include <unistd.h>
# include <string.h>
# include <stdlib.h>
# include <fcntl.h>

//=============DEFINITIONS=============
typedef struct s_list
{
	void			*content;
	struct s_list	*next;
}	t_list;

//=============PROTOTYPES=============
t_list	*ft_lstnew(void *content);

#endif
