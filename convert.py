#!/usr/bin/env python3

from pathlib import Path

from PIL import Image

from ksy.gt_image import GtImage


PIXEL_SIZE = dict()
for format_ in GtImage.GtFmt:
    PIXEL_SIZE[format_] = GtImage.Imag.FormatInfo(format_, None).pixel_size


def convert(gti_file, game):
    gti_file = Path(gti_file)
    gti = GtImage.from_file(gti_file)
    # print(f"loaded {gti_file}")

    # find highest quality image, determined by pixel size
    hq = None
    for chunk in gti.chunks:
        if chunk.tag == "Imag":
            if not hq:
                hq = chunk.data
            elif PIXEL_SIZE[chunk.data.format] > PIXEL_SIZE[hq.format]:
                hq = chunk.data
    # print(f"{hq.format} {hq.width}x{hq.height}")

    # reorder channels based on game
    if hq.format == GtImage.GtFmt.rgb888:
        im = Image.frombytes("RGB", (hq.width, hq.height), hq.mipmaps[0].data)
        if game != "airfix":
            b, g, r = im.split()
            im = Image.merge("RGB", [r, g, b])

    elif hq.format == GtImage.GtFmt.rgb565:
        im = Image.frombytes("RGB", (hq.width, hq.height), hq.mipmaps[0].data, "raw", "RGB;16")
        b, g, r = im.split()
        im = Image.merge("RGB", [r, g, b])

    elif hq.format == GtImage.GtFmt.argb8888:
        im = Image.frombytes("RGBA", (hq.width, hq.height), hq.mipmaps[0].data)
        b, g, r, a = im.split()
        im = Image.merge("RGBA", [r, g, b, a])

    elif hq.format == GtImage.GtFmt.argb4444:
        im = Image.frombytes("RGBA", (hq.width, hq.height), hq.mipmaps[0].data, "raw", "RGBA;4B")
        b, g, r, a = im.split()
        im = Image.merge("RGBA", [r, g, b, a])

    else:
        raise NotImplementedError(f"{hq.format} loading not implemented")

    # out = f"img/{hq.format}.{gti_file}.png".replace("/", "-")
    out = f"{gti_file}.png"
    # print(f"saving to {out}")
    im.save(out, "PNG")


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Convert GtImage (*.gti) files to PNG files.",
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
        help="a GtImage (*.gti) file relative to the current directory or a glob",
    )
    args = parser.parse_args()

    gti_files = list()
    for glob in args.files:
        gti_files += Path(".").glob(glob)
    for i, gti_file in enumerate(gti_files, start=1):
        print(f"{i}/{len(gti_files)} {gti_file}")
        convert(gti_file, args.game)
