# CC Tools

CC Tools is a collection of scripts to explore Unique Development Studio's (UDS)
CC, the 3D engine (Cc.dll, UdsPack.dll) data files.

## Tools

- [extract.py](./extract.py) to extract `UpPackage`s
- [convert.py](./convert.py) to convert `GtImage`s to PNG

## File Formats

The fully supported file formats are:

  - `UpPackage` *.up files
  - `GtImage` *.gti files

File formats with parsing support only:
  - `CcAnim` *.cca files
  - `MmChunkContainer` Mulle Meck files (container only)
    - *.air files
    - *.dat files
  - `AfChunkContainer` Airfix files (container only)
    - *.brf files
    - *.dat files
    - *.level files
    - *.object files
    - *.roster files
    - *.world files

Unsupported file formats include:

  - `CcLoadedScene` *.ccf and *.l3d files
  - Chunks inside chunk container files

### KSYs

[Kaitai Struct](https://github.com/kaitai-io/kaitai_struct), a declarative 
language for describing binary data, is used to parse files:

- [ksy/up_package.ksy](./ksy/up_package.ksy) describes `UpPackage`s (magic: `UDSP`)
- [ksy/gt_image.ksy](./ksy/gt_image.ksy) describes `GtImage`s (magic: `GtIm`)
- [ksy/cc_anim.ksy](./ksy/cc_anim.ksy) describes `CcAnim`s (magic: `CCA`)
- [ksy/mm_chunk_container.ksy](./ksy/mm_chunk_container.ksy)
  describes `MmChunkContainer`s (used as container for Mulle Meck files)
- [ksy/af_chunk_container.ksy](./ksy/af_chunk_container.ksy)
  describes `AfChunkContainer`s (used as container for Airfix files)

## Games

Only a few games are known to use the CC engine:

  - Airfix Dogfighter
  - Mulle Meck 3: Planes
    - Mulle Meck (Swedish/Danish)
    - Miel Monteur (Dutch)
    - Masa Mainion (Finnish)
    - Willy Werkel (German)
    - Mulle Mekk (Norwegian)

The Cc.dll found in Airfix Dogfighter is less optimized and better for reversing. 
