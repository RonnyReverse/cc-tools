meta:
  id: gt_image
  file-extension: gti
  endian: le
  encoding: ascii

enums:
  gt_fmt:
    0x00: none
    0x01: p4
    0x02: ap44
    0x03: p8
    0x04: ap88
    0x05: rgb565
    0x06: argb4444
    0x07: rgb888
    0x08: argb8888
    0x09: rgb332
    0x0a: rgb555
    0x0b: argb1555
    0x0c: argb8332
    0x0d: dxt1
    0x0f: dxt2
    0x10: dxt3
    0x11: dxt4
    0x12: dxt5
    0x13: bgr565
    0x14: bgra4444
    0x15: bgr888
    0x16: bgra8888
    0x17: bgr233
    0x18: bgr555
    0x19: bgra5551
    0x1a: bgra2338
    0x1b: abgr444
    0x1c: abgr888
    0x1d: abgr1555
    0x1f: abgr8233
    0x20: rgba4444
    0x21: rgba8888
    0x22: rgba5551
    0x23: rgba3328
    0x24: argb4565
    0x25: xrgb8888
    0x26: alpha
    0x27: a8

seq:
  - id: magic
    contents: GtIm
  - id: version
    type: u4
  - id: chunks
    type: chunk
    repeat: eos

types:
  chunk:
    -webide-representation: "{tag}"
    seq:
      - id: tag
        type: str
        size: 4
      - id: size
        type: u4
      - id: data
        # trailing zeroes may be truncated, see airfix Graphics/Fonts/system12.gti
        size: |
          size > _io.size - _io.pos
          ? _io.size - _io.pos
          : size
        type:
          switch-on: tag
          cases:
            '"Imag"': imag
  imag:
    seq:
      - id: format
        type: u4
        enum: gt_fmt
      - id: width
        type: u4
      - id: height
        type: u4
      - id: palette_size
        type: u4
      - id: mipmap_levels
        type: u4
      - id: palette
        type: u4
        repeat: expr
        repeat-expr: palette_size
      - id: mipmaps
        type: mipmap_level(_index)
        repeat: expr
        repeat-expr: mipmap_levels
    instances:
      format_info:
        type: format_info(format)
    types:
      format_info:
        params:
          - id: format
            type: u4
            enum: gt_fmt
        instances:
          pixel_size:
            value: |
              format == gt_fmt::none     ? 0 :
              format == gt_fmt::p4       ? 0 :
              format == gt_fmt::ap44     ? 1 :
              format == gt_fmt::p8       ? 1 :
              format == gt_fmt::ap88     ? 2 :
              format == gt_fmt::rgb565   ? 2 :
              format == gt_fmt::argb4444 ? 2 :
              format == gt_fmt::rgb888   ? 3 :
              format == gt_fmt::argb8888 ? 4 :
              format == gt_fmt::rgb332   ? 1 :
              format == gt_fmt::rgb555   ? 2 :
              format == gt_fmt::argb1555 ? 2 :
              format == gt_fmt::argb8332 ? 2 :
              format == gt_fmt::dxt1     ? 0 :
              format == gt_fmt::dxt2     ? 0 :
              format == gt_fmt::dxt3     ? 0 :
              format == gt_fmt::dxt4     ? 0 :
              format == gt_fmt::dxt5     ? 0 :
              format == gt_fmt::bgr565   ? 2 :
              format == gt_fmt::bgra4444 ? 2 :
              format == gt_fmt::bgr888   ? 3 :
              format == gt_fmt::bgra8888 ? 4 :
              format == gt_fmt::bgr233   ? 1 :
              format == gt_fmt::bgr555   ? 2 :
              format == gt_fmt::bgra5551 ? 2 :
              format == gt_fmt::bgra2338 ? 2 :
              format == gt_fmt::abgr444  ? 2 :
              format == gt_fmt::abgr888  ? 4 :
              format == gt_fmt::abgr1555 ? 2 :
              format == gt_fmt::abgr8233 ? 2 :
              format == gt_fmt::rgba4444 ? 2 :
              format == gt_fmt::rgba8888 ? 4 :
              format == gt_fmt::rgba5551 ? 2 :
              format == gt_fmt::rgba3328 ? 2 :
              format == gt_fmt::argb4565 ? 4 :
              format == gt_fmt::xrgb8888 ? 4 :
              format == gt_fmt::alpha    ? 0 :
              format == gt_fmt::a8       ? 1 : -1
      mipmap_level:
        params:
          - id: level
            type: u4
        instances:
          width:
            value: _parent.width >> level # shift instead of division for level 0
          height:
            value: _parent.height >> level
          size:
            # value: width * height * _parent.format_info.pixel_size # is technically wrong for width/height of 0
            value: (_parent.width * _parent.height * _parent.format_info.pixel_size) >> (level * 2)
        seq:
          - id: data
            size: size
