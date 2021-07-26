meta:
  id: cc_loaded_scene
  file-extension: ccf
  endian: le
  encoding: ascii

seq:
  - id: magic
    contents: ["CcFf", 0x01, 0x29, 0x09, 0x98]
  - id: root
    type: chunk

types:
  chunk:
    -webide-representation: "{type} {data}"
    seq:
      - id: type
        type: u2
        enum: chunk_type
      - id: size
        type: u4
      - id: data
        size: size - 6
        type:
          switch-on: type
          cases:
            chunk_type::root: root
            
            chunk_type::root_rooms: root_rooms
            chunk_type::cc_room: cc_room
            chunk_type::cc_fog: cc_fog
            chunk_type::static_bsp: cc_bsp_tree
            chunk_type::portal_bsp: cc_bsp_tree
            
            chunk_type::root_materials: root_materials
            chunk_type::cc_material: cc_material
            chunk_type::cc_material__set_texture: cc_material__set_texture
            chunk_type::cc_material__set_texture_2: cc_material__set_texture_2
            chunk_type::cc_material__set_env_map: cc_material__set_env_map
            chunk_type::cc_material__some_colors_and_a_float: cc_material__some_colors_and_a_float
            chunk_type::cc_material__a_char_a_bool_and_an_int: cc_material__a_char_a_bool_and_an_int
            chunk_type::cc_material__single_bool: cc_material__single_bool
            chunk_type::cc_material__an_int_and_two_floats: cc_material__an_int_and_two_floats
            chunk_type::cc_material__an_int_and_three_floats: cc_material__an_int_and_three_floats
            
            chunk_type::root_blueprints: root_blueprints
            chunk_type::cc_mesh: cc_mesh
            chunk_type::cc_vertex: cc_vertex
            chunk_type::cc_polygon: cc_polygon
            chunk_type::cc_null_1: cc_null_1
            
            chunk_type::root_instances: root_instances
            chunk_type::cc_object: cc_object
            chunk_type::cc_object__some_bsp: cc_object__some_bsp
            chunk_type::cc_null_2: cc_null_2 # might be blueprint
            chunk_type::cc_null_2__data: cc_null_2__data
            chunk_type::cc_light: cc_light
            chunk_type::cc_light__set_lightmap: cc_light__set_lightmap
            chunk_type::cc_light__set_lightmap_new: cc_light__set_lightmap_new
            chunk_type::cc_lens_flare: cc_lens_flare
            chunk_type::cc_light__coord_and_two_floats: cc_light__coord_and_two_floats
            chunk_type::cc_object__some_int: cc_object__some_int
            chunk_type::cc_object__some_int_2: cc_object__some_int_2
            
            chunk_type::cc_name: cc_name
            chunk_type::cc_name__string: str
            chunk_type::cc_color_flt: cc_color_flt
            chunk_type::cc_coord_3d: cc_coord_3d
            chunk_type::cc_coord_3d_but_three_times: cc_coord_3d_but_three_times
            chunk_type::cc_polygon__mapping_coord: cc_polygon__mapping_coord
            chunk_type::cc_coord_3d_wrapped: cc_coord_3d_wrapped
            
            chunk_type::cc_poly_paint: cc_poly_paint
            chunk_type::vampire_mode: vampire_mode
            chunk_type::cc_object__bool_1: cc_object__bool_1
            chunk_type::cc_object__bool_2: cc_object__bool_2
            chunk_type::cc_bsp_node: cc_bsp_node
            chunk_type::cc_bsp_node_poly: cc_bsp_node_poly
            chunk_type::cc_polygon__a_bool_and_two_floats: cc_polygon__a_bool_and_two_floats
    enums:
      chunk_type:
        0x0001: root
        
        0x1000: root_rooms
        0x1100: cc_room
        0x1101: cc_fog
        0x1200: static_bsp
        0x1201: portal_bsp
        
        0x2000: root_materials
        0x2100: cc_material
        0x2110: cc_material__set_texture
        0x2111: cc_material__set_texture_2
        0x2120: cc_material__set_env_map
        0x2140: cc_material__some_colors_and_a_float
        0x2150: cc_material__a_char_a_bool_and_an_int
        0x2151: cc_material__single_bool
        0x2152: cc_material__an_int_and_two_floats
        0x2153: cc_material__an_int_and_three_floats
        
        0x3000: root_blueprints
        0x3100: cc_mesh
        0x3110: cc_vertex
        0x3120: cc_polygon
        0x3200: cc_null_1
        
        0x4000: root_instances
        0x4100: cc_object
        0x4101: cc_object__some_bsp
        0x4200: cc_null_2
        0x4210: cc_null_2__data
        0x4300: cc_light
        0x4310: cc_light__set_lightmap
        0x4311: cc_light__set_lightmap_new
        0x4320: cc_lens_flare
        0x4330: cc_light__coord_and_two_floats
        0x4500: cc_object__some_int
        0x4501: cc_object__some_int_2
        
        0xf010: cc_name
        0xf020: cc_name__string
        0xf030: cc_color_flt
        0xf040: cc_coord_3d
        0xf050: cc_coord_3d_but_three_times
        0xf060: cc_polygon__mapping_coord
        0xf070: cc_coord_3d_wrapped
        
        0xf090: cc_poly_paint
        0xf0a0: vampire_mode
        0xf0b0: cc_object__bool_1
        0xf0b1: cc_object__bool_2
        0xf0b2: cc_polygon__bool_3
        0xf0c0: cc_bsp_node
        0xf0c1: cc_bsp_node_poly
        0xf0d0: cc_polygon__a_bool_and_two_floats
  root:
    seq:
      - id: chunks
        type: chunk
        repeat: eos
  cc_name:
    -webide-representation: "{prefix.data} {name.data}"
    seq:
      - id: prefix
        type: chunk
      - id: name
        type: chunk
  cc_color_flt:
    seq:
      - id: red
        type: f4
      - id: green
        type: f4
      - id: blue
        type: f4
  root_rooms:
    seq:
      - id: world
        type: chunk
      - id: rooms
        type: chunk
        repeat: eos
  cc_room:
    -webide-representation: "{name.data}"
    seq:
      - id: name
        type: chunk
      - id: room_pointer
        type: u4
      - id: chunks
        type: chunk
        repeat: eos
  cc_fog:
    seq:
      - id: fog_bool
        type: u4
      - id: float_1
        type: f4
      - id: float_2
        type: f4
      - id: color
        type: chunk
  cc_bsp_tree:
    seq:
      - id: nodes
        type: chunk
        repeat: eos
  cc_bsp_node:
    seq:
      - id: has_node_1
        type: u4
      - id: node_1
        type: chunk
        if: has_node_1 != 0
      - id: has_node_2
        type: u4
      - id: node_2
        type: chunk
        if: has_node_2 != 0
      - id: coord_1
        type: chunk
      - id: coord_2
        type: chunk
      - id: poly_nodes
        type: chunk
        repeat: eos
  cc_coord_3d:
    seq:
      - id: x
        type: f4
      - id: y
        type: f4
      - id: z
        type: f4
  cc_coord_3d_but_three_times:
    seq:
      - id: coords
        type: chunk
        repeat: expr
        repeat-expr: 3
  cc_coord_3d_wrapped:
    seq:
      - id: data
        type: chunk
  cc_bsp_node_poly:
    seq:
      - id: coords
        type: chunk
        repeat: expr
        repeat-expr: 5
      - id: int_1
        type: u4
      - id: int_2
        type: u4
  root_materials:
    seq:
      - id: materials
        type: chunk
        repeat: eos
  cc_material:
    -webide-representation: "{name.data}"
    seq:
      - id: name
        type: chunk
      - id: some_int
        type: u4
      - id: chunks
        type: chunk
        repeat: eos
  cc_material__set_texture:
    seq:
      - id: name
        type: chunk
  cc_material__set_texture_2:
    seq:
      - id: name
        type: chunk
  cc_material__set_env_map:
    seq:
      - id: name
        type: chunk
  cc_material__some_colors_and_a_float:
    seq:
      - id: color_1
        type: chunk
      - id: color_2
        type: chunk
      - id: float
        type: f4
  cc_material__a_char_a_bool_and_an_int:
    seq:
      - id: char
        type: u1
      - id: bool_char
        type: u1
      - id: int
        type: u4
  cc_material__single_bool:
    seq:
      - id: bool_char
        type: u1
  cc_material__an_int_and_two_floats:
    seq:
      - id: int
        type: u4
      - id: float_1
        type: f4
      - id: float_2
        type: f4
  cc_material__an_int_and_three_floats:
    seq:
      - id: int
        type: u4
      - id: float_1
        type: f4
      - id: float_2
        type: f4
      - id: float_3
        type: f4
  root_blueprints:
    seq:
      - id: chunks
        type: chunk
        repeat: eos
  root_instances:
    seq:
      - id: chunks
        type: chunk
        repeat: eos
  cc_mesh:
    -webide-representation: "{name.data}"
    seq:
      - id: name
        type: chunk
      - id: int
        type: u4
      - id: bool_1
        type: u1
      - id: bool_2
        type: u1
      - id: int_2
        type: u4
      - id: coord
        type: chunk
      - id: float
        type: f4
      - id: something
        type: chunk
      - id: chunks
        type: chunk
        repeat: eos
  cc_null_1:
    -webide-representation: "{name.data}"
    seq:
      - id: name
        type: chunk
  cc_object:
    -webide-representation: "{name.data}"
    seq:
      - id: name
        type: chunk
      - id: world_maybe
        type: u4
      - id: mesh
        type: u4
      - id: room
        type: u4
      - id: some_address
        type: u4
      - id: some_bool
        type: u1
      - id: portal_type
        type: s4
      - id: portal_room
        type: u4
      - id: coord
        type: chunk
      - id: float
        type: f4
      - id: unknown_chunk
        type: chunk
      - id: chunks
        type: chunk
        repeat: eos
  cc_null_2:
    -webide-representation: "{name.data}"
    seq:
      - id: name
        type: chunk
      - id: world_maybe
        type: u4
      - id: room
        type: u4
      - id: some_address
        type: u4
      - id: coord
        type: chunk
      - id: float
        type: f4
      - id: unknown_chunk
        type: chunk
      - id: chunks
        type: chunk
        repeat: eos
  cc_null_2__data:
    seq:
      - id: size
        type: u4
      - id: data
        size: size
  vampire_mode:
    seq:
      - id: value
        type: u4
  cc_light:
    -webide-representation: "{name.data}"
    seq:
      - id: name
        type: chunk
      - id: something
        type: u4
      - id: room_reference
        type: u4
      - id: some_int
        type: u4
      - id: coord
        type: chunk
      - id: float_1
        type: f4
      - id: rotation_maybe
        type: chunk
      - id: chunks
        type: chunk
        repeat: eos
  cc_light__set_lightmap:
    seq:
      - id: float_1
        type: f4
      - id: color
        type: chunk
      - id: float_2
        type: f4
      - id: float_3
        type: f4
      - id: texture_name
        type: chunk
        if: not _io.eof
  cc_light__set_lightmap_new:
    seq:
      - id: bool
        type: u1
      - id: float_1
        type: f4
      - id: color
        type: chunk
      - id: float_2
        type: f4
      - id: float_3
        type: f4
      - id: texture_name
        type: chunk
        if: not _io.eof
  cc_lens_flare:
    seq:
      - id: float_1
        type: f4
      - id: float_2
        type: f4
      - id: float_3
        type: f4
      - id: float_4
        type: f4
      - id: texture_name_1
        type: chunk
        if: not _io.eof
      - id: texture_name_2
        type: chunk
        if: not _io.eof
  cc_light__coord_and_two_floats:
    seq:
      - id: coord
        type: chunk
      - id: float_1
        type: f4
      - id: float_2
        type: f4
  cc_object__bool_1:
    seq:
      - id: bool
        type: u4
  cc_object__bool_2:
    seq:
      - id: bool
        type: u4
  cc_object__some_bsp:
    seq:
      - id: chunks
        type: chunk
        repeat: eos
  cc_object__some_int:
    seq:
      - id: int
        type: u4
  cc_object__some_int_2:
    seq:
      - id: int
        type: u4
  cc_vertex:
    seq:
      - id: chunk
        type: chunk
      - id: chunks
        type: chunk
        repeat: eos
  cc_polygon:
    seq:
      - id: unknwon_int_1
        type: u4
      - id: unknwon_int_2
        type: u4
      - id: unknwon_int_3
        type: u4
      - id: material_reference
        type: u4
      - id: chunks
        type: chunk
        repeat: eos
  cc_polygon__mapping_coord:
    seq:
      - id: coord_1_float_1
        type: f4
      - id: coord_1_float_2
        type: f4
      - id: coord_2_float_1
        type: f4
      - id: coord_2_float_2
        type: f4
      - id: coord_3_float_1
        type: f4
      - id: coord_3_float_2
        type: f4
  cc_poly_paint:
    seq:
      - id: color_type
        type: u4
        enum: color_type
      - id: colors
        type: chunk
        repeat: expr
        repeat-expr: |
          color_type == color_type::cc_poly_paint_flat  ? 1 :
          color_type == color_type::cc_poly_paint_tri   ? 3 :
          color_type == color_type::cc_poly_paint_tri_f ? 4 : -1
    enums:
      color_type:
        1: cc_poly_paint_flat
        3: cc_poly_paint_tri
        4: cc_poly_paint_tri_f
  cc_polygon__bool_3:
    seq:
      - id: char
        type: u1
  cc_polygon__a_bool_and_two_floats:
    seq:
      - id: bool
        type: u4
      - id: float_1
        type: f4
      - id: float_2
        type: f4
