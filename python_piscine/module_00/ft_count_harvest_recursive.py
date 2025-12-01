def ft_count_harvest_r(current_day: int, total_days: int) -> None:
    if current_day > total_days:
        print("Harvest time!")
        return

    print(f"Day {current_day}")
    ft_count_harvest_r(current_day + 1, total_days)


def ft_count_harvest_recursive() -> None:
    days = int(input("Days until harvest: "))
    ft_count_harvest_r(1, days)


# if __name__ == '__main__':
#     ft_count_harvest_recursive()
