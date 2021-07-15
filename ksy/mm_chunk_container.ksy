meta:
  id: mm_chunk_container
  file-extension: mm_chunk_container
  endian: be
  encoding: ascii

seq:
  - id: root
    type: mm_chunk_container

# guessed names, based on airfix
types:
  mm_chunk_container:
    seq:
      - id: magic
        contents: FORM
      - id: size
        type: u4
      - id: id
        type: strz
        size: 4
      - id: chunks
        type: mm_chunk::eos
  mm_chunk:
    -webide-representation: "{id} {size}"
    seq:
      - id: id
        type: strz
        size: 4
      - id: size
        type: u4
      - id: data
        size: size
    types:
      eos:
        seq:
          - id: chunks
            type: mm_chunk
            repeat: eos
