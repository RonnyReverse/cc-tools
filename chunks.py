#!/usr/bin/env python3

import json
from pathlib import Path

from ksy.af_chunk_container import AfChunkContainer
from ksy.mm_chunk_container import MmChunkContainer


def dump_mm(cc_file):
    cc_file = Path(cc_file)
    cc = MmChunkContainer.from_file(cc_file)
    # print(f"loaded {cc_file}")

    result = dict()
    for chunk in cc.root.chunks.chunks:
        if chunk.id == "NAME":
            result["name"] = chunk.data
        elif chunk.id == "MISS":
            if "missions" not in result:
                result["missions"] = list()
            result["missions"].append(
                {
                    "name": chunk.data.mission_name,
                    "id": chunk.data.id,
                    "state": chunk.data.state.name.upper(),
                    "is_random": chunk.data.is_random != 0,
                    "dependencies": [e != 0 for e in chunk.data.dependencies],
                    "state_changes": [[e.bool_1 != 0, e.bool_2 != 0] for e in chunk.data.state_changes],
                }
            )
        elif chunk.id == "INVI":
            if "inventory" not in result:
                result["inventory"] = list()
            result["inventory"].append(chunk.data)
        elif chunk.id == "PHOT":
            result["map_photos"] = {
                "enabled": chunk.data.enabled != 0,
                "completed": chunk.data.completed != 0,
                "photos": [[e.name.upper() for e in row.column] for row in chunk.data.photos],
            }
        elif chunk.id == "DIPL":
            result["diplomas"] = {
                "water": chunk.data.water != 0,
                "snow": chunk.data.snow != 0,
                "racing": chunk.data.racing != 0,
                "circus": chunk.data.circus != 0,
                "map": chunk.data.map != 0,
                "mecci": chunk.data.mecci != 0,
            }
        elif chunk.id == "BARN":
            result["barn"] = list()
            for part in chunk.data.parts:
                result["barn"].append(
                    {
                        "id": part.id,
                        "location": part.location.name.upper(),
                        "x": part.x,
                        "y": part.y,
                        "z": part.z,
                    }
                )
        elif chunk.id.startswith("AIR"):
            real_chunk_id = chunk.id
            airplane = dict()
            if chunk.id == "AIRA":
                airplane["id"] = chunk.data.id
                chunk.id = "AIRB"
                chunk.data = chunk.data.airb
            if chunk.id == "AIRB":
                airplane["name"] = chunk.data.name
                chunk.id = "AIRP"
                chunk.data = chunk.data.airp
            if chunk.id == "AIRP":
                airplane["parts"] = list()
                for part in chunk.data.parts:
                    airplane["parts"].append(
                        {
                            "id": part.id,
                            "slot": part.slot,
                            "parent": part.parent,
                        }
                    )
            if real_chunk_id in ["AIRA", "AIRP"]:
                if "airplanes" not in result:
                    result["airplanes"] = dict()
                if real_chunk_id == "AIRP":
                    result["airplanes"]["active"] = airplane
                else:
                    if "saved" not in result["airplanes"]:
                        result["airplanes"]["saved"] = list()
                    result["airplanes"]["saved"].append(airplane)
            else:
                result["airplane"] = airplane
        elif chunk.id == "PART":
            if "parts" not in result:
                result["parts"] = list()
            result["parts"].append({"id": chunk.data.id, "ccf": chunk.data.ccf})

    # print(json.dumps(result, indent=2))
    json.dump(result, Path(f"{cc_file}.json").open("w"), indent=2)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Dump ChunkContainer files to JSON.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        "-g",
        "--game",
        default="mulle",
        const="mulle",
        nargs="?",
        choices=["mulle", "airfix"],
        help="what game the files are from",
    )
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
        if args.game == "mulle":
            dump_mm(cc_file)
        else:
            raise NotImplemented(f"{args.game} is not implemented")
