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
