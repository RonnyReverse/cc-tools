# CC Tools

CC Tools is a collection of scripts to explore Unique Development Studio's (UDS)
CC, the 3D engine (Cc.dll, UdsPack.dll) data files.

## Tools

- [extract.py](./extract.py) to extract `UpPackage`s
- [extract_mesh.py](./extract_mesh.py) to extract objs from *.ccf
- [convert.py](./convert.py) to convert `GtImage`s to PNG
- [chunks.py](./chunks.py) to dump `MmChunkContainer`s and `AfChunkContainer`s to JSON

## File Formats

### Supported

  - `UpPackage` *.up files
  - `GtImage` *.gti files
  - `CcAnim` *.cca files
  - `CcLoadedScene` *.ccf files (mostly just the shape of the data without meaning)
  - `MmChunkContainer` Mulle Meck binary files
    - *.air files
    - *.dat files
  - `AfChunkContainer` Airfix binary files (excluding some chunks, see below)
    - path.dat
    - *.brf files
    - *.level files
    - *.object files
    - *.roster files
    - *.world files

### Unsupported

  - Unused `CcLoadedScene` *.l3d files
  - Unused `MmChunkContainer` chunks
    - `DTBS` (database) chunks
    - `CMND` (command) chunks
    - `DATA` chunks
  - `MmChunkContainer` missions.dat file
    - mission state data size is hardcoded but isn't included in this file
  - Some `AfChunkContainer` chunks
    - path.dat file
      - `PDAT` chunks: recorded path steps
    - *.level
      - `MODL` chunks: named `OBJE`cts with additional data
      - `IAOB` chunks: interactive objects with state
    - *.object
      - `GRAV` gravity chunks?

### KSYs

[Kaitai Struct](https://github.com/kaitai-io/kaitai_struct), a declarative
language for describing binary data, is used to parse files:

  - [ksy/up_package.ksy](./ksy/up_package.ksy) describes `UpPackage`s (magic: `UDSP`)
  - [ksy/gt_image.ksy](./ksy/gt_image.ksy) describes `GtImage`s (magic: `GtIm`)
  - [ksy/cc_anim.ksy](./ksy/cc_anim.ksy) describes `CcAnim`s (magic: `CCA`)
  - [ksy/cc_loaded_scene.ksy](./ksy/cc_loaded_scene.ksy)
    describes `CcLoadedScene`s (magic: `CcFf`)
  - [ksy/mm_chunk_container.ksy](./ksy/mm_chunk_container.ksy)
    describes `MmChunkContainer`s (Mulle Meck binary files) and their chunks
  - [ksy/af_chunk_container.ksy](./ksy/af_chunk_container.ksy)
    describes `AfChunkContainer`s (Airfix binary files) and their chunks

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
