/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   get_next_line.h                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joflorid <joflorid@student.42urduliz.co    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/13 16:32:41 by joflorid          #+#    #+#             */
/*   Updated: 2025/10/14 20:00:24 by joflorid         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef GET_NEXT_LINE_H
# define GET_NEXT_LINE_H

//============DEFINITIONS============
#define BUFFER_SIZE 8

//============LIBRARIES============
#include <stdlib.h>
#include <stdio.h>
#include <fcntl.h>
#include <unistd.h>

//============PROTOTYPES============
char	*get_next_line(int fd);
char	*ft_strjoin(char *s1, char *s2);
size_t	ft_strlen(const char *s);
int		ft_check_char(char *str);

#endif
