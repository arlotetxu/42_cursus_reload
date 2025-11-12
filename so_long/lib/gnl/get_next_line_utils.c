/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   get_next_line_utils.c                              :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joflorid <joflorid@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/13 16:32:50 by joflorid          #+#    #+#             */
/*   Updated: 2025/11/12 12:46:39 by joflorid         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "get_next_line.h"

/*
================================================================================
DESCRIPTION
	The  ft_strlen() function return the length of the string pointed by 's'.
	Prototype:
	size_t	ft_strlen(const char *s)

PARAMETERS
	s --> String to be evaluated.

RETURN VALUE
	1 --> The length of the 's' string..
================================================================================
*/

size_t	ft_strlen_gnl(char *s)
{
	size_t	len;

	len = 0;
	while (s[len] != '\0')
		len++;
	return (len);
}

/*
================================================================================
DESCRIPTION
	The ft_strjoin() concatenates 2 strings in a new one. s1 corrresponds to
	stack and s2 to buffer. The functions checks initially if 's1' exists and
	books memory if not to proceed with the process

PARAMETERS
	s1 --> String 1.

	s2 --> String 2 to be added to s1.

RETURN VALUE
	The new string created.

	NULL --> If the memory allocation fails.
================================================================================
*/

char	*ft_strjoin_gnl(char *s1, char *s2)
{
	char	*s3;
	int		i;
	int		j;

	if (!s1)
	{
		s1 = malloc(1);
		if (!s1)
			return (NULL);
		s1[0] = '\0';
	}
	if (!s2)
		return (free(s1), NULL);
	s3 = malloc(sizeof(char) * (ft_strlen_gnl(s1) + ft_strlen_gnl(s2) + 1));
	if (!s3)
		return (free(s1), NULL);
	i = -1;
	while (s1[++i] != '\0')
		s3[i] = s1[i];
	j = -1;
	while (s2[++j] != '\0')
		s3[i + j] = s2[j];
	s3[i + j] = '\0';
	free(s1);
	return (s3);
}

/*
================================================================================
DESCRIPTION
	The ft_check_char() checks if the special character '\n' is in a string.
	Prototype:
	int	ft_check_char(char *str);

PARAMETERS
	str --> String to search for the character in.

RETURN VALUE
	1 --> If the character is found.

	0 --> If the character is NOT found.
================================================================================
*/
int	ft_check_char(char *str)
{
	if (!str)
		return (0);
	while (*str)
	{
		if (*str == '\n')
			return (1);
		str++;
	}
	return (0);
}

/*==============================================================================
DESCRIPTION
	The function ft_fill_line() fills and return the first line the 'stack'
	string contains.

PARAMETERS
	stack --> The string in which to get the line if there is a line in it.

RETURN
	line --> The line found in the 'stack' string null terminated.
==============================================================================*/
char	*ft_fill_line(char *stack)
{
	char	*line;
	int		len;

	if (!stack)
		return (NULL);
	len = 0;
	while (stack[len] != '\n')
		len++;
	line = malloc(sizeof(char) * (len + 2));
	if (!line)
		return (NULL);
	len = -1;
	while (stack[++len] != '\n' && stack[len])
		line[len] = stack[len];
	if (stack[len] == '\n')
		line[len++] = '\n';
	line[len] = '\0';
	return (line);
}

/*==============================================================================
DESCRIPTION
	The function ft_clean_stack() removes from the 'stack' string the first line
	found on it. //!If the string only contains '\n' or if the string is
	//!empty ('\0), there is nothing to be returned.

PARAMETERS
	stack --> The string in which the line has to be removed.

RETURN
	new_stack --> A string cleaned. This string will be asigned to the 'stack'
		string later on.
==============================================================================*/
char	*ft_clean_stack(char *stack)
{
	int		i;
	int		j;
	char	*new_stack;

	if (!stack)
		return (NULL);
	i = 0;
	while (stack[i] && stack[i] != '\n')
		i++;
	if (!stack[i] || !stack[++i])
		return (free(stack), NULL);
	new_stack = malloc(sizeof(char) * (ft_strlen_gnl(stack) - i + 1));
	if (!new_stack)
		return (free(stack), NULL);
	j = 0;
	while (stack[i])
		new_stack[j++] = stack[i++];
	new_stack[j] = '\0';
	free(stack);
	stack = NULL;
	return (new_stack);
}
