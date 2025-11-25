# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_plot_area.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: joflorid <joflorid@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/11/24 16:50:08 by joflorid          #+#    #+#              #
#    Updated: 2025/11/24 16:50:09 by joflorid         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_plot_area() -> None:
    """
    DEFINITION
        ft_plot_area() requests from the user the length and width of a garden
        and returns the area.

    PARAMETERS
        Nothing

    RETURN
        The area of the garden calculate as length * width.
    """
    length = int(input("Enter length: "), base=10)
    width = int(input("Enter width: "), base=10)
    print(f"Plot area: {length * width}")
    return


# if __name__ == "__main__":
#     ft_plot_area()
