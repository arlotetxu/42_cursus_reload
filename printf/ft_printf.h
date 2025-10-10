/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_printf.h                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joflorid <joflorid@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/05 10:15:22 by joflorid          #+#    #+#             */
/*   Updated: 2025/10/10 16:30:56 by joflorid         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef PRINTF_H
# define PRINTF_H

//===============LIBRARIES===============
#include <stdarg.h>
#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include "libft/libft.h"

//===============PROTOTYPES===============
int	ft_printf(char const *str, ...);
int	ft_distributor(int c, va_list *args);
int	ft_print_string(char *str);
int	ft_print_char(int c);

int	ft_print_hexa(unsigned long n, char c);
int	ft_print_int(int n);

int	ft_hex_len(unsigned long n);

#endif
