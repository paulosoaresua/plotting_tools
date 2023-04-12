from glob import glob
import os.path as path
import matplotlib as mpl
from pathlib import Path
import shutil


def configure_environment():
    """
    This function copies all the available styles in the resources/mplstyles to the approrpiate matplolib folder in
    the environment this function is run. It can be used to configure a brand new conda environment or to update the
    styles in an existing one.
    """

    target_dir = path.join(mpl.__path__[0], "mpl-data", "stylelib")

    styles_dir = Path(__file__).parent / "resources/mplstyles"

    print(f"Coppying styles to {target_dir}.")
    for i, file in enumerate(glob(f"{styles_dir}/*.mplstyle")):
        print(f"{i+1}: {file}")
        shutil.copy(file, target_dir)
