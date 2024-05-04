import tkinter as tk
from tkinter import simpledialog
import threading
import time
import setup as set
import optimization as opt

def main():
    """
        Main function to set up and run the tkinter GUI for the energy management system. This function initializes
        the GUI, prompts for user input, and updates the display with the latest energy optimization data.

        The GUI prompts for a team name, sets up labels to display energy optimization data, and runs a background
        thread that updates the GUI periodically with the latest data from the optimization functions.
        """
    # Setup the main GUI window
    root = tk.Tk()
    root.title("Energy Management System Display")

    # Prompt for team name using a dialog
    team_name = simpledialog.askstring("Input", "Please enter your team name:", parent=root)
    if not team_name:
        print("No team name provided. Exiting.")
        return  # Exit if no name is provided

    # Label for the text description
    description_label = tk.Label(root, text="Total kwh optimized by your energy management system", font=('Arial', 14))
    description_label.pack(pady=(20, 0))  # add some padding only at the top

    # Label for displaying the total kWh covered, in a larger font
    total_kwh_label = tk.Label(root, text="0", font=('Arial', 24), fg='blue')  # making the number blue and larger
    total_kwh_label.pack(pady=(0, 20))  # add some padding only at the bottom

    # Get the initial setup ID using the provided team name
    id = set.setup(team_name)

    # Function to update the GUI with new data
    def update_gui(id):
        """
        Function running in a separate thread that continuously updates the GUI with the latest
        total kWh covered as optimized by the energy management system. This function fetches updates
        every 2 seconds.

        Parameters:
            id (int): The unique identifier for the building obtained from the setup process.
        """
        while True:
            time.sleep(2)  # Delay to mimic your existing sleep
            opt.adjust_energy_allocations(id)
            # Update the GUI from the optimization results
            total_kwh_label.config(text=f"{opt.total_kwH_covered}")
            root.update_idletasks()  # Update GUI elements


    # Start the energy management routine in a separate thread
    thread = threading.Thread(target=update_gui, args=(id,))
    thread.daemon = True
    thread.start()

    root.mainloop()

if __name__ == '__main__':
    main()
