meta:
  id: cc_anim
  file-extension: cc_anim
  endian: le
  encoding: ascii

seq:
  - id: header
    type: header
  - id: animations
    type: blueprint_animation
    repeat: expr
    repeat-expr: header.animation_count

types:
  header:
    seq:
      - id: magic
        contents: [CCA, 0x0]
      - id: looping
        type: u4
      - id: animation_count
        type: u4
      - id: frame_count
        type: u4
      - id: frame_rate
        type: f4
  blueprint_animation:
    -webide-representation: "{blueprint_name}"
    seq:
      - id: blueprint_name
        size: 0x40
        type: strz
      - id: frames
        type: cc_anim_frame
        repeat: expr
        repeat-expr: _parent.header.frame_count
  cc_anim_frame:
    -webide-representation: "position:({position}) orientation:({orientation})"
    seq:
      - id: position
        type: cc_coord_3d
      - id: orientation
        type: cc_quaternion
  cc_coord_3d:
    -webide-representation: "x:{x} y:{y} z:{z}"
    seq:
      - id: x
        type: f4
      - id: y
        type: f4
      - id: z
        type: f4
  cc_quaternion:
    -webide-representation: "w:{w} x:{x} y:{y} z:{z}"
    seq:
      - id: w
        type: f4
      - id: x
        type: f4
      - id: y
        type: f4
      - id: z
        type: f4
