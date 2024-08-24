import os
import subprocess

def generate_requirements_txt(venv_path, output_file='requirements.txt'):
    # Activate the virtual environment
    activate_script = os.path.join(venv_path, 'Scripts', 'activate')
    
    if not os.path.isfile(activate_script):
        print(f"Activation script not found at {activate_script}")
        return

    # Run pip freeze to get the list of installed packages
    try:
        # For Windows
        command = f'"{activate_script}" && pip freeze'
        result = subprocess.run(command, shell=True, check=True, text=True, capture_output=True)
    except subprocess.CalledProcessError as e:
        print(f"Error while running pip freeze: {e}")
        return

    # Write the output to requirements.txt
    with open(output_file, 'w') as file:
        file.write(result.stdout)

    print(f"requirements.txt has been generated successfully at {output_file}")

# Example usage:
venv_path = 'path_to_your_venv'  # Replace with the path to your virtual environment
generate_requirements_txt(venv_path)
