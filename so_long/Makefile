# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Makefile                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: joflorid <joflorid@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/09/22 11:11:03 by joflorid          #+#    #+#              #
#    Updated: 2025/11/19 11:29:27 by joflorid         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

define HEADER

                                 ,--,
                              ,---.'|
  .--.--.                     |   | :
 /  /    '.                   :   : |
|  :  /`. /    ,---.          |   ' :      ,---.        ,---,
;  |  |--`    '   ,'\         ;   ; '     '   ,'\   ,-+-. /  |  ,----._,.
|  :  ;_     /   /   |        '   | |__  /   /   | ,--.'|'   | /   /  ' /
 \  \    `. .   ; ,. :        |   | :.'|.   ; ,. :|   |  ,"' ||   :     |
  `----.   \'   | |: :        '   :    ;'   | |: :|   | /  | ||   | .\  .
  __ \  \  |'   | .; :        |   |  ./ '   | .; :|   | |  | |.   ; ';  |
 /  /`--'  /|   :    |    ___ ;   : ;   |   :    ||   | |  |/ '   .   . |
'--'.     /  \   \  /  .'  .`||   ,/     \   \  / |   | |--'   `---`-'| |
  `--'---'    `----'.'  .'   :'---'       `----'  |   |/       .'__/\_: |
                 ,---, '   .'                     '---'        |   :    :
                 ;   |  .'                                      \   \  /
                 `---'                                           `--`-'



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

AFLAGS = rcs

CC = cc

CFLAGS = -Wall -Wextra -Werror

#=======================FILES======================
#NAME = $(SRC_DIR)/push_swap
NAME = so_long

SRC_DIR = ./src

SRC = sl_graphics.c sl_initial_checks1.c sl_initial_checks2.c \
sl_initial_checks3.c sl_moves.c sl_parse_map.c sl_utils_1.c sl_utils_2.c \
so_long.c


OBJ_DIR = ./src/obj

OBJS = $(addprefix $(OBJ_DIR)/, $(SRC:.c=.o))

#OBJS_BONUS = $(addprefix $(OBJ_DIR)/, $(SRC_BONUS:.c=.o))

H_FILES = ./inc/so_long.h

#=========================TARGETS========================
all: libft_make minilibx_make $(NAME)
	@echo "$(GREEN)✓ Everything is up to date!$(DEF_COLOR)"

$(OBJ_DIR):
	mkdir -p $(OBJ_DIR)

$(OBJ_DIR)/%.o: $(SRC_DIR)/%.c $(H_FILES) | $(OBJ_DIR)
	@$(CC) $(CFLAGS) -c $< -o $@

$(NAME): $(OBJS)
#	@cp ../inc/libft/libft.a $(NAME)
#	@$(AR) $(AFLAGS) $(NAME) $^
	@$(CC) $(CFLAGS) $(OBJS) -L./lib/libft -lft -L./lib/minilibx-linux \
	-lmlx_Linux -lX11 -lXext -o $(NAME)
	@echo "$(CYAN)$$HEADER$(DEF_COLOR)"
	@echo "$(GREEN) Compilation process finished successly!!$(DEF_COLOR)"

libft_make:
	cd ./lib/libft && make

minilibx_make:
	cd ./lib/minilibx-linux && make

#bonus: $(OBJS) $(OBJS_BONUS)
#	@$(AR) $(AFLAGS) $(NAME) $^
#	@echo "$$HEADER"
#	@echo "$(GREEN) Compilation process finished successly!!$(DEF_COLOR)"

clean: libft_clean minilibx_clean
	@echo "$(CYAN)Removing source files...$(DEF_COLOR)"
	rm -rf $(OBJS)
	rm -rf $(OBJ_DIR)

libft_clean:
	cd ./lib/libft && make clean

minilibx_clean:
	cd ./lib/minilibx-linux && make clean

fclean: libft_fclean clean
	@echo "$(CYAN)Removing $(NAME) ...file$(DEF_COLOR)"
	rm -rf $(NAME)

libft_fclean:
	cd ./lib/libft && make fclean

re: fclean all

.PHONY: all libft_make minilibx clean libft_clean minilibx_clean fclean \
libft_fclean re bonus
