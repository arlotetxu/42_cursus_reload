# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_harvest_total.py                                :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: joflorid <joflorid@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/11/24 16:49:47 by joflorid          #+#    #+#              #
#    Updated: 2025/11/24 16:58:44 by joflorid         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_harvest_total() -> None:
    harvest = []
    for day in range(1, 4):
        harvest.append(int(input(f"Day {day} harvest: ")))
    total_harvest = sum(harvest)
    print(f"Total harvest: {total_harvest}")
    return


# if __name__ == '__main__':
#     ft_harvest_total()
