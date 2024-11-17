from colorama import Fore, init

# Initialize colorama for cross-platform colored terminal text
init(autoreset=True)

MENU_ITEMS = [
    "Menu:",
    "0. Exit",
    "1. List movies",
    "2. Add movie",
    "3. Delete movie",
    "4. Update movie",
    "5. Stats",
    "6. Random movie",
    "7. Search movie",
    "8. Movies sorted by rating",
    "9. Create Rating Histogram",
]


def display_menu():
    """
    Display the main menu of the application.

    This function prints out all available options for users to interact with
    within the application.

    Args:
        None

    Returns:
        None: This function prints menu items to the console.
    """
    print("********** My Movies Database **********")
    print()
    print(f"{Fore.BLUE}\n".join(MENU_ITEMS))
    print(Fore.RESET)
