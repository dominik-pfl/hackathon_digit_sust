# Smart energy management system
## Project Overview

This project implements a Python-based Energy Management System (EMS) that utilizes a Tkinter GUI to display energy optimization data for a specific building. The system is capable of adjusting energy allocations in real-time based on the consumption and production data retrieved from an external API. The GUI allows users to input their team name and then displays the total kilowatt-hours (kWh) optimized by the system.
The optimization takes place by retrieving the latest consumption and production data and deciding how to adjust the allocations.
The total kwH optimized are displayed in the GUI, this number refers to the amount of kwH which were allocated from production to consumption or from storage to consumption, so they didn't need to be paid for from the Grid.

## Project contributors

- dominik-pfl (https://github.com/dominik-pfl)
- JasminF (https://github.com/40412)

## Modules and Scripts

- `ems.py`: The main script that initializes the GUI and handles user interactions. It sets up the display and initiates a background thread to update the GUI periodically with energy optimization data.
- `optimization.py`: Contains functions to fetch consumption and production data, calculate necessary proportions for energy distribution, and adjust energy allocations.
- `setup.py`: Handles the registration of a new building for a specific team by sending a POST request to an API.

## Key Features

- **GUI Interface**: Allows input of a team name and displays optimization data in real-time.
- **Real-Time Data Updates**: Utilizes threading to continuously fetch and display updated energy data.
- **API Integration**: Interacts with an external API to get real-time energy consumption and production data for a specific building.
- **Energy Optimization**: Dynamically adjusts energy allocations based on current consumption, production, and storage levels.

## Installation and Setup

1. **Prerequisites**: Ensure Python 3.x is installed on your machine along with the `requests` and `tkinter` libraries.
2. **Download the Project**: Clone the repository or download the files to your local machine.
3. **API Setup**: This system requires access to a specific API endpoint for fetching building data. Ensure the API is accessible and functioning.
4. **Running the Application**:
    - Navigate to the project directory.
    - Run the `ems.py` script using Python:
      ```
      python ems.py
      ```
    - The GUI will prompt you to enter your team name, which will then fetch and display the energy data.

## How to Use

- **Start the Application**: Execute the `ems.py` script to launch the GUI.
- **Enter Team Name**: A dialog box will prompt you to enter your team name. This is crucial for fetching the correct building data.
- **View Energy Data**: The GUI will display the total kWh optimized and will update this data every few seconds based on the background thread's calculations.

## Components Explained

- `ems.py` initializes the Tkinter GUI and handles user inputs and GUI updates.
- `setup.py` sends a POST request to register a new building under the specified team name and returns a unique identifier for the building.
- `optimization.py` fetches real-time energy data, calculates the necessary adjustments in energy allocations, and updates these values through API requests.

## Limitations and Known Issues

- **Assumption**: This approach assumes that an adjustment of the allocations makes sense for the next 5 seconds. Although from looking at the patterns of energy consumption across several days, this seemed to make sense but there are few scenarios where this is not true (e.g. when the consumption rises with the start of the day).
- **Dependency on External API**: The system's performance and availability are heavily reliant on the external API.
- **Thread Management**: The background thread runs indefinitely; more robust thread management may be needed for longer runtime stability.
- **Error Handling**: Currently, minimal error handling is implemented, particularly regarding network issues or API failures.

## Future Enhancements

- Implement more comprehensive error handling and recovery mechanisms.
- Enhance the GUI to include more interactive elements and detailed energy statistics.
- Incorporating weather or time data to adjust the allocation even in a smarter way
- Use price data, to find out about times of day, where it might be useful to still buy electricity from the grid, as it is more logically viable to use the production and/or storage during extensively expensive hours.

## Support

For support, please contact the project maintainer or open an issue in the project repository.
