# Robot_Soccer

## Project Structure

    ```
    robot_soccer/
    │
    ├── main.py
    ├── gui/
    │   ├── __init__.py
    │   ├── main_window.py
    │   ├── tabs/
    │       ├── __init__.py
    │       ├── data_acquisition_tab.py
    │       ├── control_tab.py
    ├── data_acquisition/
    │   ├── __init__.py
    │   ├── camera.py
    │   ├── image_processing.py
    ├── control/
    │   ├── __init__.py
    │   ├── strategy.py
    │   ├── communication.py
    ├── models/
    │   ├── __init__.py
    │   ├── robot.py
    │   ├── ball.py
    ├── utils/
    │   ├── __init__.py
    │   ├── config.py
    │   ├── logger.py
    └── tests/
        ├── __init__.py
        ├── test_camera.py
        ├── test_image_processing.py
        ├── test_strategy.py
        ├── test_communication.py
    ```
