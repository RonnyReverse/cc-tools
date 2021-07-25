meta:
  id: mm_chunk_container
  file-extension:
    - air
    - dat
  endian: le
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
        type: u4be
      - id: id
        type: strz
        size: 4
      - id: chunks
        type: mm_chunk::eos
  mm_chunk:
    -webide-representation: "{id} {data}"
    seq:
      - id: id
        type: strz
        size: 4
      - id: size
        type: u4be
      - id: data
        size: size
        type:
          switch-on: id
          cases:
            # *.dat (save)
            '"NAME"': strz # save name
            '"MISS"': miss # mission status
            '"INVI"': strz # inventory item
            '"PHOT"': phot # map photo quest status
            '"DIPL"': dipl # diploma status
            '"BARN"': barn # loose parts in the barn and outside
            
            '"AIRP"': airp # airplane
            '"AIRA"': aira # airplane with name and id
            
            # *.air (exported airplane)
            '"AIRB"': airb # airplane with name
            
            # *.dat (parts)
            '"PART"': part # part id to ccf mapping
    types:
      eos:
        seq:
          - id: chunks
            type: mm_chunk
            repeat: eos
  aira:
    -webide-representation: "{id} {airb}"
    seq:
      - id: id
        type: u4
      - id: airb
        type: airb
  airb:
    -webide-representation: "{name}"
    seq:
      - id: name
        type: strz
      - id: airp
        type: airp
  airp:
    # -webide-representation: "{parts}"
    seq:
      - id: parts
        type: airp_part
        repeat: eos
    types:
      airp_part:
        -webide-representation: "({id} {slot} {parent})"
        seq:
          - id: id
            type: u4
          - id: slot
            type: u2
          - id: parent
            type: u2
  barn:
    # -webide-representation: "{parts}"
    seq:
      - id: parts
        type: barn_part
        repeat: eos
    types:
      barn_part:
        -webide-representation: "{id} {location}"
        seq:
          - id: location
            type: u4
            enum: barn_location
          - id: id
            type: u4
          - id: x
            type: f4
          - id: y
            type: f4
          - id: z
            type: f4
    enums:
      barn_location:
        0: outside
        1: barn_floor
        2: barn_shelf_1
        3: barn_shelf_2
        4: barn_shelf_3
        5: barn_shelf_4
        6: barn_shelf_5
        7: barn_shelf_6
        8: barn_shelf_7
  part:
    -webide-representation: "{id} {ccf}"
    seq:
      - id: id
        type: u4
      - id: ccf
        type: strz
  dipl:
    -webide-representation: "water:{water} snow:{snow} racing:{racing} circus:{circus} map:{map} mecci:{mecci}"
    seq:
      - id: water
        type: u4
      - id: snow
        type: u4
      - id: racing
        type: u4
      - id: circus
        type: u4
      - id: map
        type: u4
      - id: mecci
        type: u4
  phot:
    -webide-representation: "enabled:{enabled} completed:{completed}"
    seq:
      - id: enabled # has camera
        type: u4
      - id: completed
        type: u4
      - id: photos
        type: row
        repeat: expr
        repeat-expr: 10
    enums:
      photo_status:
        0: none
        1: taken
        2: developed
    types:
      row:
        # -webide-representation: "{column}"
        seq:
          - id: column
            type: u4
            enum: photo_status
            repeat: expr
            repeat-expr: 10
  miss:
    -webide-representation: "state:{state} is_random:{is_random} id:{id:dec} {mission_name}"
    seq:
      - id: id
        type: u4
      - id: state
        enum: mission_state
        type: u4
      - id: is_random
        type: u4
      - id: dependencies # bools
        type: u4
        repeat: expr
        repeat-expr: dependency_count
      - id: state_changes
        type: state_change
        repeat: expr
        repeat-expr: state_change_count
    types:
      state_change:
        -webide-representation: "unknown_bool:{unknown_bool} success_processed:{success_processed}"
        seq:
          - id: unknown_bool
            type: u4
          - id: success_processed
            type: u4
    enums:
      mission_state:
        0: none
        1: activate
        2: complete
        3: reward
    instances:
      mission_name:
        value: |
          id ==    1 ? "getcamera" :
          id ==    2 ? "deliver_newspaper_EE" :
          id ==    3 ? "gettent" :
          id ==    4 ? "repairtent" :
          id ==    5 ? "deliver_newspaper_TT" :
          id ==    6 ? "plant_crops" :
          id ==    7 ? "raisetent" :
          id ==    8 ? "rope" :
          id ==    9 ? "getfurniture" :
          id ==   10 ? "gettablecloth" :
          id ==   11 ? "getcookpot" :
          id ==   12 ? "deliver_newspaper_VR" :
          id ==   13 ? "worldphoto" :
          id ==   14 ? "vacuumcleaner" :
          id ==   15 ? "vacuumbags" :
          id ==   16 ? "powerplant_getup" :
          id ==   17 ? "powerplant_repair" :
          id ==   18 ? "deliver_newspaper_BB" :
          id ==   19 ? "getsupplies" :
          id ==   20 ? "blankets_BB" :
          id ==   21 ? "seismograph_partone" :
          id ==   22 ? "seismograph_parttwo" :
          id ==   23 ? "leaflets_VV_seismograph" :
          id ==   24 ? "seismograph_partthree" :
          id ==   25 ? "seismograph_getnet" :
          id ==   26 ? "getcable" :
          id ==   27 ? "researchequipment_BB" :
          id ==   28 ? "ernst_timber" :
          id ==   28 ? "ernst_timber" :
          id ==   29 ? "ernst_metalsheets" :
          id ==   29 ? "ernst_metalsheets" :
          id ==   30 ? "ernst_tools" :
          id ==   30 ? "ernst_tools" :
          id ==   31 ? "richard_book" :
          id ==   31 ? "richard_book" :
          id ==   32 ? "find_fabric" :
          id ==   33 ? "find_garlic" :
          id ==   34 ? "make_costumes" :
          id ==   35 ? "get_specialthread" :
          id ==   36 ? "erik_needhelp_thread" :
          id ==   38 ? "find_reindeer" :
          id ==   39 ? "place_antennas_1" :
          id ==   40 ? "place_antennas_2" :
          id ==   41 ? "place_antennas_3" :
          id ==   42 ? "get_cropsduster" :
          id ==   43 ? "water_crops" :
          id ==   44 ? "scare_gophers" :
          id ==   45 ? "worldphoto_part" :
          id ==  101 ? "worldphoto_finished" :
          id ==  601 ? "erzon_mobilephone" :
          id ==  602 ? "erzon_fancyclock" :
          id ==  603 ? "erzon_hangglider" :
          id ==  604 ? "erzon_sunglasses" :
          id ==  701 ? "photo_impactcraters_one" :
          id ==  702 ? "photo_impactcraters_two" :
          id ==  703 ? "photo_impactcraters_three" :
          id ==  704 ? "photo_birds_one" :
          id ==  705 ? "photo_birds_two" :
          id ==  706 ? "photo_birds_three" :
          id == 1002 ? "info_mygghanget" :
          id == 1004 ? "info_roymccoy" :
          id == 1005 ? "info_samscribbler" :
          id == 1006 ? "info_varldsutstallning" :
          id == 1007 ? "info_violawallmark" :
          id == 1008 ? "info_atleartillerist" :
          id == 1009 ? "info_turetapp" :
          id == 1010 ? "info_richardrevers" :
          id == 1011 ? "info_raymondraser" :
          id == 1012 ? "info_fionafalk" :
          id == 1013 ? "info_grottegrundlig" :
          id == 1014 ? "info_gabriellagourmet" :
          id == 1015 ? "info_brejtonbord" :
          id == 1016 ? "info_victorvulcan" :
          id == 1017 ? "info_vemontvrak" :
          id == 1018 ? "info_dorisdigital" :
          id == 1019 ? "info_ernsteremit" :
          id == 1020 ? "info_samposanna" :
          id == 2000 ? "mecchi_story_TT" :
          id == 2001 ? "mecchi_story_VV" :
          id == 2002 ? "mecchi_story_VR" :
          id == 5001 ? "randomdoris_1" :
          id == 5002 ? "randomdoris_2" :
          id == 5003 ? "randomdoris_3" :
          id == 6001 ? "randommia_1" :
          id == 6002 ? "randommia_2" :
          id == 6003 ? "randommia_3" :
          id == 9999 ? "mecchifinal" : "ERROR"
      state_change_count:
        value: |
          id ==    1 ?  4 :
          id ==    2 ?  4 :
          id ==    3 ?  3 :
          id ==    4 ?  7 :
          id ==    5 ?  4 :
          id ==    6 ?  2 :
          id ==    7 ?  3 :
          id ==    8 ?  3 :
          id ==    9 ? 14 :
          id ==   10 ?  5 :
          id ==   11 ?  5 :
          id ==   12 ?  5 :
          id ==   13 ?  3 :
          id ==   14 ?  4 :
          id ==   15 ?  4 :
          id ==   16 ?  1 :
          id ==   17 ?  6 :
          id ==   18 ?  5 :
          id ==   19 ?  5 :
          id ==   20 ?  5 :
          id ==   21 ?  3 :
          id ==   22 ?  4 :
          id ==   23 ?  5 :
          id ==   24 ?  6 :
          id ==   25 ?  2 :
          id ==   26 ?  6 :
          id ==   27 ?  5 :
          id ==   28 ?  2 :
          id ==   29 ?  3 :
          id ==   30 ?  5 :
          id ==   31 ?  5 :
          id ==   32 ?  2 :
          id ==   33 ?  6 :
          id ==   34 ?  2 :
          id ==   35 ?  5 :
          id ==   36 ?  5 :
          id ==   38 ?  4 :
          id ==   39 ?  6 :
          id ==   40 ?  4 :
          id ==   41 ?  4 :
          id ==   42 ?  2 :
          id ==   43 ?  2 :
          id ==   44 ?  2 :
          id ==   45 ?  2 :
          id ==  101 ?  1 :
          id ==  601 ?  3 :
          id ==  602 ?  3 :
          id ==  603 ?  3 :
          id ==  604 ?  3 :
          id ==  701 ?  3 :
          id ==  702 ?  4 :
          id ==  703 ?  6 :
          id ==  704 ?  3 :
          id ==  705 ?  4 :
          id ==  706 ?  6 :
          id == 1002 ?  1 :
          id == 1004 ?  1 :
          id == 1005 ?  1 :
          id == 1006 ?  1 :
          id == 1007 ?  1 :
          id == 1008 ?  1 :
          id == 1009 ?  1 :
          id == 1010 ?  1 :
          id == 1011 ?  1 :
          id == 1012 ?  1 :
          id == 1013 ?  1 :
          id == 1014 ?  1 :
          id == 1015 ?  1 :
          id == 1016 ?  1 :
          id == 1017 ?  1 :
          id == 1018 ?  1 :
          id == 1019 ?  1 :
          id == 1020 ?  1 :
          id == 2000 ?  2 :
          id == 2001 ?  2 :
          id == 2002 ?  2 :
          id == 5001 ?  2 :
          id == 5002 ?  2 :
          id == 5003 ?  2 :
          id == 6001 ?  2 :
          id == 6002 ?  2 :
          id == 6003 ?  2 :
          id == 9999 ?  1 : -1
      dependency_count:
        value: |
          id ==    1 ?  4 :
          id ==    2 ?  4 :
          id ==    3 ?  3 :
          id ==    4 ?  4 :
          id ==    5 ?  4 :
          id ==    6 ?  3 :
          id ==    7 ?  4 :
          id ==    8 ?  4 :
          id ==    9 ?  8 :
          id ==   10 ?  4 :
          id ==   11 ?  4 :
          id ==   12 ?  4 :
          id ==   13 ?  3 :
          id ==   14 ?  3 :
          id ==   15 ?  4 :
          id ==   16 ?  5 :
          id ==   17 ?  4 :
          id ==   18 ?  4 :
          id ==   19 ?  4 :
          id ==   20 ?  3 :
          id ==   21 ?  3 :
          id ==   22 ?  5 :
          id ==   23 ?  4 :
          id ==   24 ?  4 :
          id ==   25 ?  3 :
          id ==   26 ?  4 :
          id ==   27 ?  4 :
          id ==   28 ?  3 :
          id ==   28 ?  3 :
          id ==   29 ?  4 :
          id ==   29 ?  4 :
          id ==   30 ?  4 :
          id ==   30 ?  4 :
          id ==   31 ?  4 :
          id ==   31 ?  4 :
          id ==   32 ?  4 :
          id ==   33 ?  4 :
          id ==   34 ?  3 :
          id ==   35 ?  4 :
          id ==   36 ?  8 :
          id ==   38 ?  3 :
          id ==   39 ?  2 :
          id ==   40 ?  2 :
          id ==   41 ?  3 :
          id ==   42 ?  2 :
          id ==   43 ?  4 :
          id ==   44 ?  4 :
          id ==   45 ?  3 :
          id ==  101 ?  2 :
          id ==  601 ?  6 :
          id ==  602 ?  6 :
          id ==  603 ?  6 :
          id ==  604 ?  6 :
          id ==  701 ?  3 :
          id ==  702 ?  2 :
          id ==  703 ?  3 :
          id ==  704 ?  3 :
          id ==  705 ?  2 :
          id ==  706 ?  3 :
          id == 1002 ?  1 :
          id == 1004 ?  1 :
          id == 1005 ?  1 :
          id == 1006 ?  1 :
          id == 1007 ?  1 :
          id == 1008 ?  1 :
          id == 1009 ?  1 :
          id == 1010 ?  1 :
          id == 1011 ?  1 :
          id == 1012 ?  1 :
          id == 1013 ?  1 :
          id == 1014 ?  1 :
          id == 1015 ?  1 :
          id == 1016 ?  1 :
          id == 1017 ?  1 :
          id == 1018 ?  1 :
          id == 1019 ?  1 :
          id == 1020 ?  1 :
          id == 2000 ?  2 :
          id == 2001 ?  2 :
          id == 2002 ?  2 :
          id == 5001 ?  3 :
          id == 5002 ?  5 :
          id == 5003 ?  5 :
          id == 6001 ?  3 :
          id == 6002 ?  4 :
          id == 6003 ?  4 :
          id == 9999 ? 30 : -1
