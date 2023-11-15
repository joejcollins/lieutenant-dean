import os
import json

project_path = os.path.abspath(os.path.dirname(__file__))
folders = [{"path": folder} for folder in os.listdir(project_path) if os.path.isdir(folder)]

workspace_config = {
    "folders": folders,
    "settings": {
        "python.linting.pylintEnabled": True,
        "python.linting.enabled": True,
        "python.linting.pylintArgs": ["--load-plugins", "pylint.extension"],
        # Add other shared settings here
    }
}

with open(os.path.join(project_path, "my_project.code-workspace"), "w") as workspace_file:
    json.dump(workspace_config, workspace_file, indent=2)

print("Workspace file generated successfully.")
