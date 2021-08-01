#!/usr/bin/env python3

import base64
import json
from pathlib import Path

from ksy.af_chunk_container import AfChunkContainer
from ksy.mm_chunk_container import MmChunkContainer


class ChunkContainer:
    def __init__(self, filename):
        self.container = None
        for chunk_container_format in [AfChunkContainer, MmChunkContainer]:
            try:
                self.container = chunk_container_format.from_file(filename)
                break
            except:
                pass
        if not self.container:
            raise ValueError("unknown chunk container format")

    @staticmethod
    def to_serializable(value):
        serializable = None

        if type(value) in [str, int, float, bool, type(None)]:
            serializable = value

        elif type(value) == bytes:
            serializable = base64.b64encode(value).decode("utf-8")

        elif type(value) == list:
            serializable = [ChunkContainer.to_serializable(e) for e in value]

        else:
            serializable = dict()
            for key, value in value.__dict__.items():
                if key.startswith("_"):
                    continue
                serializable[key] = ChunkContainer.to_serializable(value)

        return serializable

    def to_dict(self):
        return {
            "type": self.container.__class__.__name__,
            "id": self.container.root.id,
            "chunks": [
                {
                    "id": chunk.id,
                    "data": ChunkContainer.to_serializable(chunk.data),
                }
                for chunk in self.container.root.chunks.chunks
            ],
        }


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Dump ChunkContainer files to JSON.")
    parser.add_argument(
        "files",
        metavar="file",
        type=str,
        nargs="+",
        help="a ChunkContainer file relative to the current directory or a glob",
    )
    args = parser.parse_args()

    cc_files = list()
    for glob in args.files:
        cc_files += Path(".").glob(glob)
    for i, cc_file in enumerate(cc_files, start=1):
        print(f"{i}/{len(cc_files)} {cc_file}")
        json.dump(ChunkContainer(cc_file).to_dict(), Path(f"{cc_file}.json").open("w"), indent=2)
