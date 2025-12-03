#!/usr/bin/env python3
# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_garden_intro.py                                 :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: joflorid <joflorid@student.42urduliz.com>  +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/03 09:25:11 by joflorid          #+#    #+#              #
#    Updated: 2025/12/03 09:25:16 by joflorid         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_garden_intro() -> None:
    """Prints a static introduction to a garden."""
    name = "Rose"
    height = 25
    age = 30
    print("=== Welcome to My Garden ===")
    print(f"Plant: {name}")
    print(f"Height: {height}cm")
    print(f"Age: {age} days")
    print("\n=== End of Program ===")


if __name__ == '__main__':
    ft_garden_intro()
# ft_garden_intro()
