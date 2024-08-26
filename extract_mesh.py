#!/usr/bin/env python3

from pathlib import Path

from ksy.cc_loaded_scene import CcLoadedScene
from ksy.gt_image import GtImage
from PIL import Image


def extract_mesh(file):
    file = Path(file)

    try:
        scene = CcLoadedScene.from_file(file)
    except Exception as err:
        print(f"Could not read {file}, exception : {err}")
    
    for chunk in scene.root.data.chunks:
        if chunk.type == CcLoadedScene.Chunk.ChunkType.root_blueprints:
            for blueprint in chunk.data.chunks:
                if blueprint.type == CcLoadedScene.Chunk.ChunkType.cc_mesh:
                    mesh = blueprint.data

                    prefix = mesh.name.data.prefix.data.encode('utf-8')[4:][:-1].decode('utf-8')
                    name = mesh.name.data.name.data.encode('utf-8')[4:][:-1].decode('utf-8')
                    print(f"Found {prefix}")

                    obj_vert = ""
                    obj_face = ""

                    for content in mesh.chunks:
                        if content.type == CcLoadedScene.Chunk.ChunkType.cc_vertex:
                            obj_vert += f"v {content.data.chunk.data.x} {content.data.chunk.data.y} {content.data.chunk.data.z}\n"
                        elif content.type == CcLoadedScene.Chunk.ChunkType.cc_polygon:
                            # Add +1 as obj files are from 1-n, not 0-n 
                            obj_face += f"f {content.data.unknwon_int_1 + 1} {content.data.unknwon_int_2 + 1} {content.data.unknwon_int_3 + 1}\n"
                    
                    with open(f"./outputs/{prefix}-{name}.obj", "w") as file:
                        file.write(f"g {name}\n")
                        file.write(obj_vert)
                        file.write(obj_face)
                        file.close()

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Convert CcLoadedScene (*.ccf) files to OBJ files.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        "files",
        metavar="file",
        type=str,
        nargs="+",
        help="a CcLoadedScene (*.ccf) file relative to the current directory or a glob",
    )
    args = parser.parse_args()

    import os
    if not os.path.exists("./outputs"):
        os.makedirs("./outputs")

    for folder in args.files:   
        for file in Path(folder).glob("*.ccf"):
            extract_mesh(file)