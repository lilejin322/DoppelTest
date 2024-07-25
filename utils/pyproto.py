import os
import subprocess
from config import APOLLO_ROOT, DT_ROOT

def compile_proto_files() -> None:
    """
    Compile all .proto files in the APOLLO_ROOT to .py files in DT_ROOT, using the protoc compiler.
    """

    # Check the correct protoc compiler is used, here protoc==3.19.0
    result1 = subprocess.run(['which', 'protoc'], capture_output=True, text=True)
    print(result1.stdout)
    result2 = subprocess.run(['protoc', '--version'], capture_output=True, text=True)
    print(result2.stdout)

    for dirpath, _, filenames in os.walk(APOLLO_ROOT):
        for filename in filenames:
            if filename.endswith('.proto'):
                proto_file = os.path.join(dirpath, filename)
                # Note that the output directory should be the root, otherwise it will create a cyclic dir struct
                try:
                    # Compile the dirpath/filename.proto file to .py file in the same directory
                    subprocess.run(['protoc', f'--proto_path={APOLLO_ROOT}', f'--python_out={DT_ROOT}', proto_file],\
                                    stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                except subprocess.CalledProcessError as _:
                    pass
    print("Protoc compilation complete.")
