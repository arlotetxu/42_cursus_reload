/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   printf.h                                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joflorid <joflorid@student.42urduliz.co    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/05 10:15:22 by joflorid          #+#    #+#             */
/*   Updated: 2025/10/05 10:31:08 by joflorid         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef PRINTF_H
# define PRINTF_H

//===============LIBRARIES===============
#include <stdarg.h>
#include <stdio.h>
#include <unistd.h>

//===============PROTOTYPES===============
int		ft_printf(char const *str, ...);
void	ft_distributor(int c, va_list *args);
void	ft_print_string(char *str);
void	ft_print_char(int c);

#endif