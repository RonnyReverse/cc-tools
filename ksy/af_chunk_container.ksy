meta:
  id: af_chunk_container
  file-extension:
    - brf
    - dat
    - level
    - object
    - roster
    - world
  endian: le
  encoding: ascii

seq:
  - id: root
    type: af_chunk_container

types:
  af_chunk_container:
    seq:
      - id: id
        size: 4
        type: strz
      - id: size
        type: u4
      - id: chunks
        type: af_chunk::eos
  af_chunk:
    -webide-representation: "{id} {size}"
    seq:
      - id: id
        size: 4
        type: strz
      - id: size
        type: u4
      - id: data
        size: size
    types:
      eos:
        seq:
          - id: chunks
            type: af_chunk
            repeat: eos
