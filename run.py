# runner for the python script

if __name__ == "__main__":
    # Importing the main module
    try:
        from main import main
        main()
    except ModuleNotFoundError:
        print("Could not find the 'main' module. Please ensure main.py exists in the current directory.")
    except AttributeError:
        print("The 'main' module does not have a 'main' function. Please ensure main.py defines a 'main()' function.")