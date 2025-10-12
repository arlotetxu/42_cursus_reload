# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Makefile                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: joflorid <joflorid@student.42urduliz.co    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/09/22 11:11:03 by joflorid          #+#    #+#              #
#    Updated: 2025/10/11 11:43:58 by joflorid         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

define HEADER

 ________  _________         _______  _______     _____  ____  _____  _________  ________
|_   __  ||  _   _  |       |_   __ \|_   __ \   |_   _||_   \|_   _||  _   _  ||_   __  |
  | |_ \_||_/ | | \_|         | |__) | | |__) |    | |    |   \ | |  |_/ | | \_|  | |_ \_|
  |  _|       | |             |  ___/  |  __ /     | |    | |\ \| |      | |      |  _|
 _| |_       _| |_  _______  _| |_    _| |  \ \_  _| |_  _| |_\   |_    _| |_    _| |_
|_____|     |_____||_______||_____|  |____| |___||_____||_____|\____|  |_____|  |_____|



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
NAME = $(SRC_DIR)/libftprintf.a

SRC_DIR = .

SRC = ft_printf.c ft_prints_1.c ft_utils_1.c


OBJ_DIR = ./obj

OBJS = $(addprefix $(OBJ_DIR)/, $(SRC:.c=.o))
OBJS_BONUS = $(addprefix $(OBJ_DIR)/, $(SRC_BONUS:.c=.o))

H_FILES = ft_printf.h

#=========================TARGETS========================
all: libft $(NAME)

libft:
	cd libft && make

$(OBJ_DIR):
	mkdir -p $(OBJ_DIR)

$(OBJ_DIR)/%.o: $(SRC_DIR)/%.c $(H_FILES) | $(OBJ_DIR)
	@$(CC) $(CFLAGS) -c $< -o $@

$(NAME): $(OBJS)
	@$(AR) $(AFLAGS) $(NAME) $^
	@echo "$(YELLOW)$$HEADER$(DEF_COLOR)"
	@echo "$(GREEN) Compilation process finished successly!!$(DEF_COLOR)"

bonus: $(OBJS) $(OBJS_BONUS)
	@$(AR) $(AFLAGS) $(NAME) $^
	@echo "$$HEADER"
	@echo "$(GREEN) Compilation process finished successly!!$(DEF_COLOR)"

clean: libft_clean
	@echo "$(CYAN)Removing source files...$(DEF_COLOR)"
	rm -rf $(OBJS)
	rm -rf $(OBJ_DIR)

libft_clean:
	cd libft && make clean

fclean: libft_fclean clean
	@echo "$(CYAN)Removing $(NAME) ...file$(DEF_COLOR)"
	rm -rf $(NAME)

libft_fclean:
	cd libft && make fclean

re: fclean all

.PHONY: all libft clean libft_clean fclean libft_fclean re bonus
