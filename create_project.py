import os

# Define the directory structure
structure = {
    "DGI": {
        "contracts": ["DGI.sol"],
        "scripts": ["Deploy.s.sol"],
        "test": ["DGI.t.sol"],
        "frontend": {
            "components": ["WalletConnect.js"],
            "pages": ["index.js"],
            "utils": ["ipfs.js"],
            "public": [],
            "src": ["styles.css"],
        },
        "": ["README.md", "foundry.toml", "hardhat.config.js", ".gitignore", "LICENSE"],
    }
}

# Base path for the project
base_path = "./DGI_Project/"

def create_structure(base, structure):
    for key, value in structure.items():
        path = os.path.join(base, key)
        if isinstance(value, dict):  # It's a folder with sub-items
            os.makedirs(path, exist_ok=True)
            create_structure(path, value)
        elif isinstance(value, list):  # It's a folder with files
            os.makedirs(path, exist_ok=True)
            for file in value:
                with open(os.path.join(path, file), 'w') as f:
                    f.write("")  # Create an empty file

# Create the project structure
create_structure(base_path, structure)

print(f"Project structure created at: {base_path}")
