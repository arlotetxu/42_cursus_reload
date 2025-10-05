/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   printf.h                                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joflorid <joflorid@student.42urduliz.co    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/05 10:15:22 by joflorid          #+#    #+#             */
/*   Updated: 2025/10/05 12:44:16 by joflorid         ###   ########.fr       */
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
int		ft_distributor(int c, va_list *args);
int		ft_print_string(char *str);
int		ft_print_char(int c);

#endif