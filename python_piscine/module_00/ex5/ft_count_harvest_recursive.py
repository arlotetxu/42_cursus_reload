#!/usr/bin/env python3

def ft_count_harvest_recursive() -> None:
    days = int(input("Days until harvest: "))

    def ft_count_harvest_r(current_day: int) -> None:
        if current_day > days:
            print("Harvest time!")
            return

        print(f"Day {current_day}")
        ft_count_harvest_r(current_day + 1)
    ft_count_harvest_r(current_day=1)


# if __name__ == '__main__':
#     ft_count_harvest_recursive()
