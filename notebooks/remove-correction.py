from pathlib import Path
from argparse import ArgumentParser

import nbformat
import jupytext

def remove_correction(filecorr):
    filecorr = Path(filecorr)
    with filecorr.open() as f:
        notebook = jupytext.read(f)
    filestud = filecorr.name.replace("+corr", "")
    if filestud == filecorr.name:
        print(f"cowardly refusing to overwrite {filecorr}")
        return
    len_before = len(notebook['cells'])
    def is_correction(cell):
        source = cell['source']
        return (not source 
                or source.startswith('# correction')
                or source.startswith('#correction'))
    notebook['cells'] = [cell for cell in notebook['cells']
                         if not is_correction(cell)]
    len_after = len(notebook['cells'])
    # hard-code py-percent format
    text = jupytext.writes(notebook, fmt='py:percent')
    with Path(filestud).open('w') as writer:
        writer.write(text)
        writer.write("\n")
    if len_before == len_after:
        print(f"{filecorr}[{len_before}] == no change")
    else:
        print(f"{filecorr}[{len_before}] -> {filestud}[{len_after}]")


def main():
    parser = ArgumentParser()
    parser.add_argument("files", nargs="*")
    args = parser.parse_args()

    if not args.files:
        files = Path('.').glob('*+corr.py')
    else:
        files = [Path(file) for file in  args.files]

    for file in files:
        remove_correction(file)

if __name__ == '__main__':
    main()
