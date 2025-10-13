# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Makefile                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: joflorid <joflorid@student.42urduliz.co    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/09/22 11:11:03 by joflorid          #+#    #+#              #
#    Updated: 2025/10/05 09:50:27 by joflorid         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

define HEADER

 _     ___ ____  _____ _____
| |   |_ _| __ )|  ___|_   _|
| |    | ||  _ \| |_    | |
| |___ | || |_) |  _|   | |
|_____|___|____/|_|     |_|


endef
export HEADER

#=======================DEFINITIONS======================
DEF_COLOR 	= \033[0;39m
GRAY 		= \033[0;90m
RED 		= \033[0;31m
GREEN 		= \033[0;92m
YELLOW 		= \033[0;93m
BLUE 		= \033[0;94m
MAGENTA 	= \033[0;95m
CYAN 		= \033[0;96m
WHITE 		= \033[0;97m

AR = ar

AFLAGS = -rc

CC = cc

CFLAGS = -Wall -Wextra -Werror

#=======================FILES======================
NAME = $(SRC_DIR)/libft.a

SRC_DIR = .

SRC = ft_atoi.c ft_bzero.c ft_calloc.c ft_isalnum.c ft_isalpha.c \
ft_isascii.c ft_isdigit.c ft_isprint.c ft_itoa.c ft_memchr.c ft_memcmp.c \
ft_memcpy.c ft_memmove.c ft_memset.c ft_putchar_fd.c ft_putendl_fd.c \
ft_putnbr_fd.c ft_putstr_fd.c ft_split.c ft_strchr.c ft_strdup.c ft_striteri.c \
ft_strjoin.c ft_strlcat.c ft_strlcpy.c ft_strlen.c ft_strmapi.c ft_strncmp.c \
ft_strnstr.c ft_strrchr.c ft_strtrim.c ft_substr.c ft_tolower.c ft_toupper.c

SRC_BONUS = ft_lstadd_back_bonus.c ft_lstadd_front_bonus.c ft_lstclear_bonus.c \
ft_lstdelone_bonus.c ft_lstiter_bonus.c ft_lstlast_bonus.c ft_lstmap_bonus.c \
ft_lstnew_bonus.c ft_lstsize_bonus.c

OBJ_DIR = ./obj

OBJS = $(addprefix $(OBJ_DIR)/, $(SRC:.c=.o))
OBJS_BONUS = $(addprefix $(OBJ_DIR)/, $(SRC_BONUS:.c=.o))

H_FILES = libft.h

#=========================TARGETS========================
all: $(NAME)

$(OBJ_DIR):
	mkdir -p $(OBJ_DIR)

$(OBJ_DIR)/%.o: $(SRC_DIR)/%.c $(H_FILES) | $(OBJ_DIR)
	@$(CC) $(CFLAGS) -c $< -o $@

$(NAME): $(OBJS)
	@$(AR) $(AFLAGS) $(NAME) $^
	@echo "$$HEADER"
	@echo "$(GREEN) Compilation process finished successly!!$(DEF_COLOR)"

bonus: $(OBJS) $(OBJS_BONUS)
	@$(AR) $(AFLAGS) $(NAME) $^
	@echo "$$HEADER"
	@echo "$(GREEN) Compilation process finished successly!!$(DEF_COLOR)"

clean:
	@echo "$(CYAN)Removing source files...$(DEF_COLOR)"
	rm -rf $(OBJS) $(OBJS_BONUS)
	rm -rf $(OBJ_DIR)

fclean: clean
	@echo "$(CYAN)Removing $(NAME) file...$(DEF_COLOR)"
	rm -rf $(NAME)

re: fclean all

.PHONY: all clean fclean re bonus
