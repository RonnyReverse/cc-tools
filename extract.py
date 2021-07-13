#!/usr/bin/env python3

import math
import sys
from pathlib import Path

from ksy.up_package import UpPackage


class DecompressionError(Exception):
    def __init__(self, message):
        super().__init__(message)


# found in UdsPack.dll UpFile::UpFile
def decompress(file_):
    if not file_.entry.is_compressed:
        return file_.data
    else:
        data_in = file_.data
        data_out = bytearray()

        chunk_type = None
        offset = 0
        while chunk_type != 0x67:
            chunk_type = data_in[offset]
            offset += 1

            if chunk_type == 0x65:
                count = math.ceil(data_in[offset] / 4)  # data_in[offset] + 3 >> 2
                offset += 1
                for _ in range(count):
                    data_out.extend(data_in[offset : offset + 4])
                offset += 4

            elif chunk_type in [0x66, 0x67]:
                size = data_in[offset]
                offset += 1
                data_out.extend(data_in[offset : offset + size])
                offset += size

            else:
                raise DecompressionError(f"unknown chunk type {data_in[offset]}")

        if len(data_out) != file_.entry.size:
            raise DecompressionError(f"expected decompressed size {file_.entry.size}, got {len(data_out)}")

        return data_out


# found in UdsPack.dll UpHashTable::Add
def up_hashtable_hash(string):
    hash_constants = [0x03, 0x05, 0x07, 0x0B, 0x0D, 0x11, 0x13, 0x17, 0x1D, 0x1F, 0x25, 0x29, 0x2B, 0x2F, 0x35, 0x3B]

    offset = len(string) - 15
    if offset < 0:
        offset = 0

    hash_ = len(string)
    index = len(string) - offset

    for char in string.lower()[offset:]:
        hash_ += ord(char) * hash_constants[index]
        index -= 1

    return hash_


def extract(uppackage_file):
    uppackage_file = Path(uppackage_file)
    package = UpPackage.from_file(uppackage_file)
    file_count = sum([len(dir_.files) for dir_ in package.dirs])
    print(f"loaded {uppackage_file} ({file_count} files)")

    extracted_count = 0
    for dir_ in package.dirs:
        # create directory
        dir_path = uppackage_file.parent / dir_.path.replace("\\", "/")
        dir_path.mkdir(parents=True, exist_ok=True)

        # extract files
        for file_ in dir_.files:
            file_path = uppackage_file.parent / file_.path.replace("\\", "/")

            extracted_count += 1
            print(f"{uppackage_file.name} {extracted_count}/{file_count}: extracting {file_path}")
            file_path.write_bytes(decompress(file_))

            # print("checking hash func")
            # expected_hash = file_.entry.name_hash
            # computed_hash = up_hashtable_hash(file_.entry.name.value)
            # if expected_hash != computed_hash:
            #     print(f"{expected_hash=} {computed_hash=}")
            #     exit(1)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Extract UpPackage (*.up) files.")
    parser.add_argument("files", metavar="file", type=str, nargs="+", help="an UpPackage (*.up) file")
    args = parser.parse_args()

    for uppackage_file in args.files:
        extract(uppackage_file)
