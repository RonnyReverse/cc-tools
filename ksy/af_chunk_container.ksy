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
  encoding: windows-1250

seq:
  - id: root
    type: af_chunk_container

types:
  af_chunk_container:
    seq:
      - id: id
        size: 4
        type: str
      - id: size
        type: u4
      - id: chunks
        type: af_chunk::eos
  af_chunk:
    -webide-representation: "{id} {data:dec}"
    seq:
      - id: id
        size: 4
        type: str
      - id: size
        type: u4
      - id: data
        size: size
        type:
          switch-on: id
          cases:
            # *.roster save
            '"NAME"': strz # name
            '"PICT"': strz # picture
            '"MEDA"': strz # earned medal
            '"THRD"': u4   # one means allied, zero means axis. last played? TODO
            '"ALMI"': u4   # allied missions
            '"AXMI"': u4   # axis missions
            '"ACKI"': u4   # air combat kills
            '"GUKI"': u4   # ground unit kills
            '"WUKI"': u4   # water unit kills
            '"FOOK"': u4   # ? TODO
            '"FRIK"': u4   # ? TODO
            '"DEAT"': u4   # crashes (maybe sp only) TODO
            '"PKIL"': u4   # mp kills TODO
            '"PDEA"': u4   # mp deaths (maybe only when shot down) TODO
            '"SCOR"': u4   # score
            
            # *.brf "BRIF" briefing
            '"NAME"': strz # mission name
            '"OUTL"': strz # quick brief
            '"OUT2"': strz # quick brief page 2
            '"TEXT"': strz # mission briefing
            '"TXT2"': strz # mission briefing page 2
            '"PRIM"': strz # primary objectives
            '"SCND"': strz # secondary objectives
            '"AIRS"': strz # airplane models
            '"SELA"': strz # default airplane model
            
            # *.world "HOUS" world
            '"TEXU"': strz # texture search path
            '"CCFF"': strz # world ccf
            '"BCKD"': strz # backdrop
            '"MMSK"': strz # floor map image alpha mask
            '"MIMG"': strz # floor map image
            '"FLRY"': flry # floor y levels
            '"ROOM"': room # room info
            '"LLST"': strz # radar room name
            '"LDAT"': ldat # radar lines
            
            # *.object "OBJE" "MODL"
            '"TYPE"': strz # house editor type
            '"CATG"': strz # house editor category
            '"NAME"': strz # house editor name
            '"NATY"': strz # airplane nationality
            '"TEXU"': strz # texture search path
            '"CCFF"': strz # model ccf
            '"MESH"': strz # mesh blueprint
            '"GRAV"': grav # gravity? always three nulls TODO
            '"HIDE"': hide # hidden in house editor, existence is used as bool
            
            # *.level "FHOU"
            '"HOUS"': strz # world file
            '"GCCS"': u4   # same as nl_checksum console var TODO
            '"OBJE"': obje # position and rotation of objects
            '"MODL"': modl # extended objects? TODO
            '"IAOB"': iaob # interactive object with state TODO

            # *.dat "PATH"
            '"PPOS"': ppos # start position and rotation
            '"PDAT"': pdat # step position and rotation TODO
    types:
      eos:
        seq:
          - id: chunks
            type: af_chunk
            repeat: eos
  xyz:
    -webide-representation: "x:{x:dec} y:{y:dec} z:{z:dec}"
    seq:
      - id: x
        type: f4
      - id: y
        type: f4
      - id: z
        type: f4
  flry:
    -webide-representation: "floor 1 y:{floor_1_y} floor 2 y:{floor_2_y} floor 3 y:{floor_3_y}"
    seq:
      - id: floor_1_y
        type: f4
      - id: floor_2_y
        type: f4
      - id: floor_3_y
        type: f4
  room:
    -webide-representation: "floor:{floor:dec} {name_internal}"
    seq:
      - id: room_id
        type: u1
      - id: name_internal
        type: strz
      - id: name_localized
        type: strz
      - id: floor
        type: u1
  ldat:
    seq:
      - id: lines
        type: line
        repeat: eos
    types:
      line:
        -webide-representation: "x_1:{x_1:dec} y_1:{y_1:dec} x_2:{x_2:dec} y_2:{y_2:dec}"
        seq:
          - id: x1
            type: f4
          - id: y1
            type: f4
          - id: x2
            type: f4
          - id: y2
            type: f4
  grav:
    seq:
      - id: float_1
        type: f4
      - id: float_2
        type: f4
      - id: float_3
        type: f4
  hide: {}
  obje:
    -webide-representation: "{room} {object}"
    seq:
      - id: position
        type: xyz
      - id: axis_rotation
        type: xyz
      - id: room
        type: strz
      - id: object
        type: strz
  modl:
    -webide-representation: "{object} {name}"
    seq:
      - id: object
        type: obje
      
      # dunno what all that is
      - id: name
        type: strz
      - id: int1
        type: u4
      - id: str2
        type: strz
      - id: int2
        type: u4
      - id: str3
        type: strz
      - id: int3
        type: u4
      
      - id: int4
        type: u4
        if: not _io.eof
  iaob:
    -webide-representation: "type:{type} name:{name}"
    seq:
      - id: type
        type: strz
      - id: name
        type: strz
      - id: bools
        type: u4
        repeat: expr
        repeat-expr: |
          type == "IaDoor"        ? 8 :
          type == "IaHatch"       ? 8 :
          type == "IaBlind"       ? 2 :
          type == "IaWindow"      ? 2 :
          type == "IaLightswitch" ? 1 : -1
  ppos:
    seq:
      - id: position
        type: xyz
      - id: rotation
        type: xyz
  pdat:
    seq:
      - id: entries
        type: buffer_entry
        repeat: eos
    types:
      # position and rotation as 16 bit floats?
      # see AfPathRecord::Record
      # and AfPathRecord::Playback
      buffer_entry:
        seq:
          - id: data
            size: 12
