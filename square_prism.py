#!/usr/bin/env python3
# created by : Sereke Asfeday
# date: 12th October 2026
# This program asks the user for the side length (a or either s) and the height (h) of a square prism and
# then calculates and displays the volume, and surface area of the square prism.
def main():

    # ask the users for units
    unit = input("Enter the units of measurement (e.g. cm, m, in, etc...): ")
    # get the length of the side and height of the square prism from the user
    side_length = float(input("Enter the side length, a or either s,: "))
    height = float(input("Enter the height,: "))

    # check if the side length and height are positive values
    if side_length < 0 or height < 0:
        print("Error: Please enter positive values for side length and height.")
        return

    # Calculate the volume and surface area
    volume = (side_length**2) * height
    surface_area = (4 * side_length * height) + (2 * (side_length**2))

    # display the answers
    print(
        "The volume of the square prism is: {volume:.2f} {unit}^3".format(
            volume=volume, unit=unit
        )
    )
    print(
        "The surface area of the square prism is: {surface_area:.2f} {unit}^2".format(
            surface_area=surface_area, unit=unit
        )
    )


main()
