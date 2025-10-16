/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   get_next_line.h                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joflorid <joflorid@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/13 16:32:41 by joflorid          #+#    #+#             */
/*   Updated: 2025/10/16 17:08:47 by joflorid         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef GET_NEXT_LINE_H
# define GET_NEXT_LINE_H

//============DEFINITIONS===========
# ifndef BUFFER_SIZE
#  define BUFFER_SIZE 10000000
# endif

//============LIBRARIES============
# include <stdlib.h>
# include <stdio.h>
# include <fcntl.h>
# include <unistd.h>

//============PROTOTYPES============
char	*get_next_line(int fd);
char	*ft_init_gnl(char *buffer, char **stack, int fd);
char	*ft_clean_stack(char *stack);
char	*ft_fill_line(char *stack);
char	*ft_strjoin(char *s1, char *s2);
size_t	ft_strlen(char *s);
int		ft_check_char(char *str);

#endif
