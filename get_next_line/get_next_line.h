/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   get_next_line.h                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joflorid <joflorid@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/13 16:32:41 by joflorid          #+#    #+#             */
/*   Updated: 2025/10/13 17:06:22 by joflorid         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef GET_NEXT_LINE_H
# define GET_NEXT_LINE_H

//============DEFINITIONS============
#define BUFFER_SIZE 42

//============LIBRARIES============
#include <stdlib.h>
#include <stdio.h>
#include <fcntl.h>
#include <unistd.h>

//============PROTOTYPES============
char	*get_next_line(int fd);

#endif
