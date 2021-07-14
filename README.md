# CC Tools

CC Tools is a collection of scripts to explore Unique Development Studio's (UDS) CC, the 3D engine (Cc.dll, UdsPack.dll) files.

## Tools

- [extract.py](./extract.py) to extract `UpPackage`s
- [convert.py](./convert.py) to convert `GtImage`s to PNG

## File Formats

The supported file formats are:

  - `UpPackage` *.up files
  - `GtImage` *.gti files
  - `CcAnim` *.cca files (parser only)

Unsupported file formats include:

  - `CcRoom` (aka scene) *.ccf and *.l3d files
  - various game-specific IFF-based file formats

### KSYs

[Kaitai Struct](https://github.com/kaitai-io/kaitai_struct), a declarative language used for describing binary data, is used to parse files:

- [ksy/up_package.ksy](./ksy/up_package.ksy) describes `UpPackage`s (magic: `UDSP`)
- [ksy/gt_image.ksy](./ksy/gt_image.ksy) describes `GtImage`s (magic: `GtIm`)
- [ksy/cc_anim.ksy](./ksy/cc_anim.ksy) describes `CcAnim`s (magic: `CCA`)

## Games

Only a few game are known to use the CC engine:

  - Airfix Dogfighter
  - Mulle Meck 3: Planes
    - Mulle Meck (Swedish/Danish)
    - Miel Monteur (Dutch)
    - Masa Mainion (Finnish)
    - Willy Werkel (German)
    - Mulle Mekk (Norwegian)

The Cc.dll found in Airfix Dogfighter is less optimized and better for reversing. 
