meta:
  id: up_package
  file-extension: up
  endian: le
  encoding: ascii

seq:
  - id: header
    type: header
instances:
  dirs:
    io: header.dirs.data._io
    type: up_hash_entry::dir
    repeat: eos

types:
  header:
    seq:
      - id: magic
        contents: UDSP
      - id: version
        type: u4
      - id: dirs
        type: block
      - id: strings
        type: block
      - id: files
        type: block
    types:
      empty: {}
      block:
        seq:
          - id: size
            type: u4
          - id: pos
            type: u4
        instances:
          data:
            pos: pos
            size: size
            type: empty
  up_hash_entry:
    -webide-representation: "{name}"
    seq:
      - id: name_hash
        type: u4
      - id: name
        type: string
      - id: is_compressed
        type: u4
      - id: size
        type: u4
      - id: size_compressed
        type: u4
      - id: offset
        type: u4
    types:
      string:
        -webide-representation: "{value}"
        seq:
          - id: offset
            type: u4
        instances:
          value:
            -webide-parse-mode: eager
            io: _root.header.strings.data.as<header::empty>._io
            pos: offset
            type: strz
      dir:
        -webide-representation: "{path}"
        seq:
          - id: entry
            type: up_hash_entry
        instances:
          path:
            value: entry.name.value
          files:
            io: _root.header.files.data.as<header::empty>._io
            pos: entry.offset
            type: file
            repeat: expr
            repeat-expr: entry.size_compressed
      file:
        -webide-representation: "{path}"
        seq:
          - id: entry
            type: up_hash_entry
        instances:
          path:
            value: _parent.entry.name.value + "\\" + entry.name.value
          data:
            io: _root._io
            pos: entry.offset
            size: entry.size_compressed
