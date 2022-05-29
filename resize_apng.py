import os.path

import apng_square_and_optimize
import apng


def convert(path,out_path):
    with open(path, "rb") as f:
        out = apng.APNG()
        out = apng_square_and_optimize.resize(f.read())
        out.save(out_path)

def main():
    in_path = input("Input path:\n")

    out_path = "resized/" + os.path.basename(in_path)

    try:
        os.makedirs(out_path)
    except FileExistsError:
        # directory already exists
        pass

    for file in os.listdir(in_path):

        if file.endswith(".apng"):
            # print(os.path.join(in_path, file))
            convert(os.path.join(in_path, file), os.path.join(out_path, file))

if __name__ == '__main__':
    main()