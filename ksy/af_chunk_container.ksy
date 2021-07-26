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
            '"MEDA"': strz # medal
            '"THRD"': u4   # one means allied, zero means axis
            '"ALMI"': u4   # allied missions
            '"AXMI"': u4   # axis missions
            '"ACKI"': u4   # air combat kills
            '"GUKI"': u4   # ground unit kills
            '"WUKI"': u4   # water unit kills
            '"FOOK"': u4   # ?
            '"FRIK"': u4   # ?
            '"DEAT"': u4   # crashes (maybe sp only)
            '"PKIL"': u4   # mp kills
            '"PDEA"': u4   # mp deaths (maybe only when shot down)
            '"SCOR"': u4   # score
            
            # *.brf "BRIF" briefing
            '"NAME"': strz
            '"OUTL"': strz
            '"TEXT"': strz
            '"PRIM"': strz
            '"SCND"': strz
            '"AIRS"': strz
            '"SELA"': strz
            
            # *.world "HOUS" world
            '"TEXU"': strz
            '"CCFF"': strz
            '"BCKD"': strz # backdrop
            '"MMSK"': strz
            '"MIMG"': strz
            '"ROOM"': room
            '"FLRY"': flry
            '"LLST"': strz
            # '"LDAT"': # NfMission data
            
            # *.object "OBJE" "MODL"
            '"TYPE"': strz
            '"CATG"': strz
            '"NAME"': strz
            '"NATY"': strz
            '"TEXU"': strz
            '"CCFF"': strz
            '"MESH"': strz
            '"GRAV"': grav
            '"HIDE"': hide
            
            # *.level "FHOU"
            '"HOUS"': strz
            '"GCCS"': u4   # same as nl_checksum console var
            '"MODL"': modl
            '"OBJE"': obje
            '"IAOB"': iaob

            # *.dat "PATH"
            # '"PPOS"':
            # '"PDAT"':
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
  room:
    -webide-representation: "floor:{floor:dec} {name_internal}"
    seq:
      - id: id
        type: u1
      - id: name_internal
        type: strz
      - id: name_localized
        type: strz
      - id: floor
        type: u1
  flry:
    -webide-representation: "{unk1} {unk2} {unk3}"
    seq:
      - id: unk1
        type: f4
      - id: unk2
        type: f4
      - id: unk3
        type: f4
  modl:
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
      
      # dunno what all that is
      - id: str1
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
  iaob:
    -webide-representation: "{s1} {s2}"
    seq:
      # dunno what all that is
      - id: s1
        type: strz
      - id: s2
        type: strz
      # might have one, two, or eight ints
      - id: int
        type: u4
        repeat: eos
  grav:
    seq:
      - id: float_1
        type: f4
      - id: float_2
        type: f4
      - id: float_3
        type: f4
  hide: {} # always empty
