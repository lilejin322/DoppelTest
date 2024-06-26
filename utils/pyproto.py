import os
import subprocess
from config import APOLLO_ROOT

def compile_proto_files(root_dir=APOLLO_ROOT) -> None:
    """
    Compile all .proto files in the given root directory to .py files, using the protoc compiler.

    :param str root_dir: The apollo root directory to search for .proto files. Default is APOLLO_ROOT.
    """
    for dirpath, _, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename.endswith('.proto'):
                proto_file = os.path.join(dirpath, filename)
                # Note that the output directory should be the root, otherwise it will create a cyclic dir struct
                try:
                    # Compile the dirpath/filename.proto file to .py file in the same directory
                    subprocess.run(['protoc', f'--proto_path={root_dir}', f'--python_out={root_dir}', proto_file], check=True)
                except subprocess.CalledProcessError as e:
                    print(f"Failed to compile {proto_file}: {e}")
    print("Protoc compilation complete.")
