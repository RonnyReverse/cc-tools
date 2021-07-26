# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

from pkg_resources import parse_version
import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
from enum import Enum


if parse_version(kaitaistruct.__version__) < parse_version('0.9'):
    raise Exception("Incompatible Kaitai Struct Python API: 0.9 or later is required, but you have %s" % (kaitaistruct.__version__))

class CcLoadedScene(KaitaiStruct):
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._read()

    def _read(self):
        self.magic = self._io.read_bytes(8)
        if not self.magic == b"\x43\x63\x46\x66\x01\x29\x09\x98":
            raise kaitaistruct.ValidationNotEqualError(b"\x43\x63\x46\x66\x01\x29\x09\x98", self.magic, self._io, u"/seq/0")
        self.root = CcLoadedScene.Chunk(self._io, self, self._root)

    class CcMaterialSetTexture(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.name = CcLoadedScene.Chunk(self._io, self, self._root)


    class CcPolygon(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.unknwon_int_1 = self._io.read_u4le()
            self.unknwon_int_2 = self._io.read_u4le()
            self.unknwon_int_3 = self._io.read_u4le()
            self.material_reference = self._io.read_u4le()
            self.chunks = []
            i = 0
            while not self._io.is_eof():
                self.chunks.append(CcLoadedScene.Chunk(self._io, self, self._root))
                i += 1



    class CcObject(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.name = CcLoadedScene.Chunk(self._io, self, self._root)
            self.world_maybe = self._io.read_u4le()
            self.mesh = self._io.read_u4le()
            self.room = self._io.read_u4le()
            self.some_address = self._io.read_u4le()
            self.some_bool = self._io.read_u1()
            self.portal_type = self._io.read_s4le()
            self.portal_room = self._io.read_u4le()
            self.coord = CcLoadedScene.Chunk(self._io, self, self._root)
            self.float = self._io.read_f4le()
            self.unknown_chunk = CcLoadedScene.Chunk(self._io, self, self._root)
            self.chunks = []
            i = 0
            while not self._io.is_eof():
                self.chunks.append(CcLoadedScene.Chunk(self._io, self, self._root))
                i += 1



    class CcMaterial(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.name = CcLoadedScene.Chunk(self._io, self, self._root)
            self.some_int = self._io.read_u4le()
            self.chunks = []
            i = 0
            while not self._io.is_eof():
                self.chunks.append(CcLoadedScene.Chunk(self._io, self, self._root))
                i += 1



    class CcLensFlare(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.float_1 = self._io.read_f4le()
            self.float_2 = self._io.read_f4le()
            self.float_3 = self._io.read_f4le()
            self.float_4 = self._io.read_f4le()
            if not (self._io.is_eof()):
                self.texture_name_1 = CcLoadedScene.Chunk(self._io, self, self._root)

            if not (self._io.is_eof()):
                self.texture_name_2 = CcLoadedScene.Chunk(self._io, self, self._root)



    class Chunk(KaitaiStruct):

        class ChunkType(Enum):
            root = 1
            root_rooms = 4096
            cc_room = 4352
            cc_fog = 4353
            static_bsp = 4608
            portal_bsp = 4609
            root_materials = 8192
            cc_material = 8448
            cc_material__set_texture = 8464
            cc_material__set_texture_2 = 8465
            cc_material__set_env_map = 8480
            cc_material__some_colors_and_a_float = 8512
            cc_material__a_char_a_bool_and_an_int = 8528
            cc_material__single_bool = 8529
            cc_material__an_int_and_two_floats = 8530
            cc_material__an_int_and_three_floats = 8531
            root_blueprints = 12288
            cc_mesh = 12544
            cc_vertex = 12560
            cc_polygon = 12576
            cc_null_1 = 12800
            root_instances = 16384
            cc_object = 16640
            cc_object__some_bsp = 16641
            cc_null_2 = 16896
            cc_null_2__data = 16912
            cc_light = 17152
            cc_light__set_lightmap = 17168
            cc_light__set_lightmap_new = 17169
            cc_lens_flare = 17184
            cc_light__coord_and_two_floats = 17200
            cc_object__some_int = 17664
            cc_object__some_int_2 = 17665
            cc_name = 61456
            cc_name__string = 61472
            cc_color_flt = 61488
            cc_coord_3d = 61504
            cc_coord_3d_but_three_times = 61520
            cc_polygon__mapping_coord = 61536
            cc_coord_3d_wrapped = 61552
            cc_poly_paint = 61584
            vampire_mode = 61600
            cc_object__bool_1 = 61616
            cc_object__bool_2 = 61617
            cc_polygon__bool_3 = 61618
            cc_bsp_node = 61632
            cc_bsp_node_poly = 61633
            cc_polygon__a_bool_and_two_floats = 61648
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.type = KaitaiStream.resolve_enum(CcLoadedScene.Chunk.ChunkType, self._io.read_u2le())
            self.size = self._io.read_u4le()
            _on = self.type
            if _on == CcLoadedScene.Chunk.ChunkType.cc_material__a_char_a_bool_and_an_int:
                self._raw_data = self._io.read_bytes((self.size - 6))
                _io__raw_data = KaitaiStream(BytesIO(self._raw_data))
                self.data = CcLoadedScene.CcMaterialACharABoolAndAnInt(_io__raw_data, self, self._root)
            elif _on == CcLoadedScene.Chunk.ChunkType.cc_name:
                self._raw_data = self._io.read_bytes((self.size - 6))
                _io__raw_data = KaitaiStream(BytesIO(self._raw_data))
                self.data = CcLoadedScene.CcName(_io__raw_data, self, self._root)
            elif _on == CcLoadedScene.Chunk.ChunkType.cc_color_flt:
                self._raw_data = self._io.read_bytes((self.size - 6))
                _io__raw_data = KaitaiStream(BytesIO(self._raw_data))
                self.data = CcLoadedScene.CcColorFlt(_io__raw_data, self, self._root)
            elif _on == CcLoadedScene.Chunk.ChunkType.cc_material__set_env_map:
                self._raw_data = self._io.read_bytes((self.size - 6))
                _io__raw_data = KaitaiStream(BytesIO(self._raw_data))
                self.data = CcLoadedScene.CcMaterialSetEnvMap(_io__raw_data, self, self._root)
            elif _on == CcLoadedScene.Chunk.ChunkType.cc_coord_3d:
                self._raw_data = self._io.read_bytes((self.size - 6))
                _io__raw_data = KaitaiStream(BytesIO(self._raw_data))
                self.data = CcLoadedScene.CcCoord3d(_io__raw_data, self, self._root)
            elif _on == CcLoadedScene.Chunk.ChunkType.root_rooms:
                self._raw_data = self._io.read_bytes((self.size - 6))
                _io__raw_data = KaitaiStream(BytesIO(self._raw_data))
                self.data = CcLoadedScene.RootRooms(_io__raw_data, self, self._root)
            elif _on == CcLoadedScene.Chunk.ChunkType.root_instances:
                self._raw_data = self._io.read_bytes((self.size - 6))
                _io__raw_data = KaitaiStream(BytesIO(self._raw_data))
                self.data = CcLoadedScene.RootInstances(_io__raw_data, self, self._root)
            elif _on == CcLoadedScene.Chunk.ChunkType.cc_light:
                self._raw_data = self._io.read_bytes((self.size - 6))
                _io__raw_data = KaitaiStream(BytesIO(self._raw_data))
                self.data = CcLoadedScene.CcLight(_io__raw_data, self, self._root)
            elif _on == CcLoadedScene.Chunk.ChunkType.cc_object__some_bsp:
                self._raw_data = self._io.read_bytes((self.size - 6))
                _io__raw_data = KaitaiStream(BytesIO(self._raw_data))
                self.data = CcLoadedScene.CcObjectSomeBsp(_io__raw_data, self, self._root)
            elif _on == CcLoadedScene.Chunk.ChunkType.cc_polygon:
                self._raw_data = self._io.read_bytes((self.size - 6))
                _io__raw_data = KaitaiStream(BytesIO(self._raw_data))
                self.data = CcLoadedScene.CcPolygon(_io__raw_data, self, self._root)
            elif _on == CcLoadedScene.Chunk.ChunkType.cc_bsp_node:
                self._raw_data = self._io.read_bytes((self.size - 6))
                _io__raw_data = KaitaiStream(BytesIO(self._raw_data))
                self.data = CcLoadedScene.CcBspNode(_io__raw_data, self, self._root)
            elif _on == CcLoadedScene.Chunk.ChunkType.static_bsp:
                self._raw_data = self._io.read_bytes((self.size - 6))
                _io__raw_data = KaitaiStream(BytesIO(self._raw_data))
                self.data = CcLoadedScene.CcBspTree(_io__raw_data, self, self._root)
            elif _on == CcLoadedScene.Chunk.ChunkType.cc_bsp_node_poly:
                self._raw_data = self._io.read_bytes((self.size - 6))
                _io__raw_data = KaitaiStream(BytesIO(self._raw_data))
                self.data = CcLoadedScene.CcBspNodePoly(_io__raw_data, self, self._root)
            elif _on == CcLoadedScene.Chunk.ChunkType.cc_object__bool_2:
                self._raw_data = self._io.read_bytes((self.size - 6))
                _io__raw_data = KaitaiStream(BytesIO(self._raw_data))
                self.data = CcLoadedScene.CcObjectBool2(_io__raw_data, self, self._root)
            elif _on == CcLoadedScene.Chunk.ChunkType.vampire_mode:
                self._raw_data = self._io.read_bytes((self.size - 6))
                _io__raw_data = KaitaiStream(BytesIO(self._raw_data))
                self.data = CcLoadedScene.VampireMode(_io__raw_data, self, self._root)
            elif _on == CcLoadedScene.Chunk.ChunkType.cc_coord_3d_but_three_times:
                self._raw_data = self._io.read_bytes((self.size - 6))
                _io__raw_data = KaitaiStream(BytesIO(self._raw_data))
                self.data = CcLoadedScene.CcCoord3dButThreeTimes(_io__raw_data, self, self._root)
            elif _on == CcLoadedScene.Chunk.ChunkType.root_blueprints:
                self._raw_data = self._io.read_bytes((self.size - 6))
                _io__raw_data = KaitaiStream(BytesIO(self._raw_data))
                self.data = CcLoadedScene.RootBlueprints(_io__raw_data, self, self._root)
            elif _on == CcLoadedScene.Chunk.ChunkType.cc_object:
                self._raw_data = self._io.read_bytes((self.size - 6))
                _io__raw_data = KaitaiStream(BytesIO(self._raw_data))
                self.data = CcLoadedScene.CcObject(_io__raw_data, self, self._root)
            elif _on == CcLoadedScene.Chunk.ChunkType.cc_null_2__data:
                self._raw_data = self._io.read_bytes((self.size - 6))
                _io__raw_data = KaitaiStream(BytesIO(self._raw_data))
                self.data = CcLoadedScene.CcNull2Data(_io__raw_data, self, self._root)
            elif _on == CcLoadedScene.Chunk.ChunkType.cc_material__set_texture:
                self._raw_data = self._io.read_bytes((self.size - 6))
                _io__raw_data = KaitaiStream(BytesIO(self._raw_data))
                self.data = CcLoadedScene.CcMaterialSetTexture(_io__raw_data, self, self._root)
            elif _on == CcLoadedScene.Chunk.ChunkType.root:
                self._raw_data = self._io.read_bytes((self.size - 6))
                _io__raw_data = KaitaiStream(BytesIO(self._raw_data))
                self.data = CcLoadedScene.Root(_io__raw_data, self, self._root)
            elif _on == CcLoadedScene.Chunk.ChunkType.cc_polygon__mapping_coord:
                self._raw_data = self._io.read_bytes((self.size - 6))
                _io__raw_data = KaitaiStream(BytesIO(self._raw_data))
                self.data = CcLoadedScene.CcPolygonMappingCoord(_io__raw_data, self, self._root)
            elif _on == CcLoadedScene.Chunk.ChunkType.root_materials:
                self._raw_data = self._io.read_bytes((self.size - 6))
                _io__raw_data = KaitaiStream(BytesIO(self._raw_data))
                self.data = CcLoadedScene.RootMaterials(_io__raw_data, self, self._root)
            elif _on == CcLoadedScene.Chunk.ChunkType.cc_material:
                self._raw_data = self._io.read_bytes((self.size - 6))
                _io__raw_data = KaitaiStream(BytesIO(self._raw_data))
                self.data = CcLoadedScene.CcMaterial(_io__raw_data, self, self._root)
            elif _on == CcLoadedScene.Chunk.ChunkType.cc_name__string:
                self.data = (self._io.read_bytes((self.size - 6))).decode(u"ascii")
            elif _on == CcLoadedScene.Chunk.ChunkType.cc_null_1:
                self._raw_data = self._io.read_bytes((self.size - 6))
                _io__raw_data = KaitaiStream(BytesIO(self._raw_data))
                self.data = CcLoadedScene.CcNull1(_io__raw_data, self, self._root)
            elif _on == CcLoadedScene.Chunk.ChunkType.cc_vertex:
                self._raw_data = self._io.read_bytes((self.size - 6))
                _io__raw_data = KaitaiStream(BytesIO(self._raw_data))
                self.data = CcLoadedScene.CcVertex(_io__raw_data, self, self._root)
            elif _on == CcLoadedScene.Chunk.ChunkType.portal_bsp:
                self._raw_data = self._io.read_bytes((self.size - 6))
                _io__raw_data = KaitaiStream(BytesIO(self._raw_data))
                self.data = CcLoadedScene.CcBspTree(_io__raw_data, self, self._root)
            elif _on == CcLoadedScene.Chunk.ChunkType.cc_fog:
                self._raw_data = self._io.read_bytes((self.size - 6))
                _io__raw_data = KaitaiStream(BytesIO(self._raw_data))
                self.data = CcLoadedScene.CcFog(_io__raw_data, self, self._root)
            elif _on == CcLoadedScene.Chunk.ChunkType.cc_object__bool_1:
                self._raw_data = self._io.read_bytes((self.size - 6))
                _io__raw_data = KaitaiStream(BytesIO(self._raw_data))
                self.data = CcLoadedScene.CcObjectBool1(_io__raw_data, self, self._root)
            elif _on == CcLoadedScene.Chunk.ChunkType.cc_room:
                self._raw_data = self._io.read_bytes((self.size - 6))
                _io__raw_data = KaitaiStream(BytesIO(self._raw_data))
                self.data = CcLoadedScene.CcRoom(_io__raw_data, self, self._root)
            elif _on == CcLoadedScene.Chunk.ChunkType.cc_material__some_colors_and_a_float:
                self._raw_data = self._io.read_bytes((self.size - 6))
                _io__raw_data = KaitaiStream(BytesIO(self._raw_data))
                self.data = CcLoadedScene.CcMaterialSomeColorsAndAFloat(_io__raw_data, self, self._root)
            elif _on == CcLoadedScene.Chunk.ChunkType.cc_material__an_int_and_two_floats:
                self._raw_data = self._io.read_bytes((self.size - 6))
                _io__raw_data = KaitaiStream(BytesIO(self._raw_data))
                self.data = CcLoadedScene.CcMaterialAnIntAndTwoFloats(_io__raw_data, self, self._root)
            elif _on == CcLoadedScene.Chunk.ChunkType.cc_material__set_texture_2:
                self._raw_data = self._io.read_bytes((self.size - 6))
                _io__raw_data = KaitaiStream(BytesIO(self._raw_data))
                self.data = CcLoadedScene.CcMaterialSetTexture2(_io__raw_data, self, self._root)
            elif _on == CcLoadedScene.Chunk.ChunkType.cc_lens_flare:
                self._raw_data = self._io.read_bytes((self.size - 6))
                _io__raw_data = KaitaiStream(BytesIO(self._raw_data))
                self.data = CcLoadedScene.CcLensFlare(_io__raw_data, self, self._root)
            elif _on == CcLoadedScene.Chunk.ChunkType.cc_coord_3d_wrapped:
                self._raw_data = self._io.read_bytes((self.size - 6))
                _io__raw_data = KaitaiStream(BytesIO(self._raw_data))
                self.data = CcLoadedScene.CcCoord3dWrapped(_io__raw_data, self, self._root)
            elif _on == CcLoadedScene.Chunk.ChunkType.cc_light__set_lightmap:
                self._raw_data = self._io.read_bytes((self.size - 6))
                _io__raw_data = KaitaiStream(BytesIO(self._raw_data))
                self.data = CcLoadedScene.CcLightSetLightmap(_io__raw_data, self, self._root)
            elif _on == CcLoadedScene.Chunk.ChunkType.cc_polygon__a_bool_and_two_floats:
                self._raw_data = self._io.read_bytes((self.size - 6))
                _io__raw_data = KaitaiStream(BytesIO(self._raw_data))
                self.data = CcLoadedScene.CcPolygonABoolAndTwoFloats(_io__raw_data, self, self._root)
            elif _on == CcLoadedScene.Chunk.ChunkType.cc_material__single_bool:
                self._raw_data = self._io.read_bytes((self.size - 6))
                _io__raw_data = KaitaiStream(BytesIO(self._raw_data))
                self.data = CcLoadedScene.CcMaterialSingleBool(_io__raw_data, self, self._root)
            elif _on == CcLoadedScene.Chunk.ChunkType.cc_poly_paint:
                self._raw_data = self._io.read_bytes((self.size - 6))
                _io__raw_data = KaitaiStream(BytesIO(self._raw_data))
                self.data = CcLoadedScene.CcPolyPaint(_io__raw_data, self, self._root)
            elif _on == CcLoadedScene.Chunk.ChunkType.cc_object__some_int:
                self._raw_data = self._io.read_bytes((self.size - 6))
                _io__raw_data = KaitaiStream(BytesIO(self._raw_data))
                self.data = CcLoadedScene.CcObjectSomeInt(_io__raw_data, self, self._root)
            elif _on == CcLoadedScene.Chunk.ChunkType.cc_object__some_int_2:
                self._raw_data = self._io.read_bytes((self.size - 6))
                _io__raw_data = KaitaiStream(BytesIO(self._raw_data))
                self.data = CcLoadedScene.CcObjectSomeInt2(_io__raw_data, self, self._root)
            elif _on == CcLoadedScene.Chunk.ChunkType.cc_material__an_int_and_three_floats:
                self._raw_data = self._io.read_bytes((self.size - 6))
                _io__raw_data = KaitaiStream(BytesIO(self._raw_data))
                self.data = CcLoadedScene.CcMaterialAnIntAndThreeFloats(_io__raw_data, self, self._root)
            elif _on == CcLoadedScene.Chunk.ChunkType.cc_light__coord_and_two_floats:
                self._raw_data = self._io.read_bytes((self.size - 6))
                _io__raw_data = KaitaiStream(BytesIO(self._raw_data))
                self.data = CcLoadedScene.CcLightCoordAndTwoFloats(_io__raw_data, self, self._root)
            elif _on == CcLoadedScene.Chunk.ChunkType.cc_null_2:
                self._raw_data = self._io.read_bytes((self.size - 6))
                _io__raw_data = KaitaiStream(BytesIO(self._raw_data))
                self.data = CcLoadedScene.CcNull2(_io__raw_data, self, self._root)
            elif _on == CcLoadedScene.Chunk.ChunkType.cc_light__set_lightmap_new:
                self._raw_data = self._io.read_bytes((self.size - 6))
                _io__raw_data = KaitaiStream(BytesIO(self._raw_data))
                self.data = CcLoadedScene.CcLightSetLightmapNew(_io__raw_data, self, self._root)
            elif _on == CcLoadedScene.Chunk.ChunkType.cc_mesh:
                self._raw_data = self._io.read_bytes((self.size - 6))
                _io__raw_data = KaitaiStream(BytesIO(self._raw_data))
                self.data = CcLoadedScene.CcMesh(_io__raw_data, self, self._root)
            else:
                self.data = self._io.read_bytes((self.size - 6))


    class CcBspTree(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.nodes = []
            i = 0
            while not self._io.is_eof():
                self.nodes.append(CcLoadedScene.Chunk(self._io, self, self._root))
                i += 1



    class CcMesh(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.name = CcLoadedScene.Chunk(self._io, self, self._root)
            self.int = self._io.read_u4le()
            self.bool_1 = self._io.read_u1()
            self.bool_2 = self._io.read_u1()
            self.int_2 = self._io.read_u4le()
            self.coord = CcLoadedScene.Chunk(self._io, self, self._root)
            self.float = self._io.read_f4le()
            self.something = CcLoadedScene.Chunk(self._io, self, self._root)
            self.chunks = []
            i = 0
            while not self._io.is_eof():
                self.chunks.append(CcLoadedScene.Chunk(self._io, self, self._root))
                i += 1



    class CcFog(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.fog_bool = self._io.read_u4le()
            self.float_1 = self._io.read_f4le()
            self.float_2 = self._io.read_f4le()
            self.color = CcLoadedScene.Chunk(self._io, self, self._root)


    class CcCoord3d(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.x = self._io.read_f4le()
            self.y = self._io.read_f4le()
            self.z = self._io.read_f4le()


    class CcMaterialSomeColorsAndAFloat(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.color_1 = CcLoadedScene.Chunk(self._io, self, self._root)
            self.color_2 = CcLoadedScene.Chunk(self._io, self, self._root)
            self.float = self._io.read_f4le()


    class Root(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.chunks = []
            i = 0
            while not self._io.is_eof():
                self.chunks.append(CcLoadedScene.Chunk(self._io, self, self._root))
                i += 1



    class CcBspNode(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.has_node_1 = self._io.read_u4le()
            if self.has_node_1 != 0:
                self.node_1 = CcLoadedScene.Chunk(self._io, self, self._root)

            self.has_node_2 = self._io.read_u4le()
            if self.has_node_2 != 0:
                self.node_2 = CcLoadedScene.Chunk(self._io, self, self._root)

            self.coord_1 = CcLoadedScene.Chunk(self._io, self, self._root)
            self.coord_2 = CcLoadedScene.Chunk(self._io, self, self._root)
            self.poly_nodes = []
            i = 0
            while not self._io.is_eof():
                self.poly_nodes.append(CcLoadedScene.Chunk(self._io, self, self._root))
                i += 1



    class CcMaterialSingleBool(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.bool_char = self._io.read_u1()


    class CcName(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.prefix = CcLoadedScene.Chunk(self._io, self, self._root)
            self.name = CcLoadedScene.Chunk(self._io, self, self._root)


    class RootMaterials(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.materials = []
            i = 0
            while not self._io.is_eof():
                self.materials.append(CcLoadedScene.Chunk(self._io, self, self._root))
                i += 1



    class CcPolygonBool3(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.char = self._io.read_u1()


    class CcNull1(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.name = CcLoadedScene.Chunk(self._io, self, self._root)


    class CcBspNodePoly(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.coords = [None] * (5)
            for i in range(5):
                self.coords[i] = CcLoadedScene.Chunk(self._io, self, self._root)

            self.int_1 = self._io.read_u4le()
            self.int_2 = self._io.read_u4le()


    class CcMaterialSetTexture2(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.name = CcLoadedScene.Chunk(self._io, self, self._root)


    class RootRooms(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.world = CcLoadedScene.Chunk(self._io, self, self._root)
            self.rooms = []
            i = 0
            while not self._io.is_eof():
                self.rooms.append(CcLoadedScene.Chunk(self._io, self, self._root))
                i += 1



    class CcPolygonABoolAndTwoFloats(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.bool = self._io.read_u4le()
            self.float_1 = self._io.read_f4le()
            self.float_2 = self._io.read_f4le()


    class VampireMode(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.value = self._io.read_u4le()


    class CcMaterialAnIntAndThreeFloats(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.int = self._io.read_u4le()
            self.float_1 = self._io.read_f4le()
            self.float_2 = self._io.read_f4le()
            self.float_3 = self._io.read_f4le()


    class CcCoord3dWrapped(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.data = CcLoadedScene.Chunk(self._io, self, self._root)


    class CcMaterialACharABoolAndAnInt(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.char = self._io.read_u1()
            self.bool_char = self._io.read_u1()
            self.int = self._io.read_u4le()


    class CcMaterialSetEnvMap(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.name = CcLoadedScene.Chunk(self._io, self, self._root)


    class CcLight(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.name = CcLoadedScene.Chunk(self._io, self, self._root)
            self.something = self._io.read_u4le()
            self.room_reference = self._io.read_u4le()
            self.some_int = self._io.read_u4le()
            self.coord = CcLoadedScene.Chunk(self._io, self, self._root)
            self.float_1 = self._io.read_f4le()
            self.rotation_maybe = CcLoadedScene.Chunk(self._io, self, self._root)
            self.chunks = []
            i = 0
            while not self._io.is_eof():
                self.chunks.append(CcLoadedScene.Chunk(self._io, self, self._root))
                i += 1



    class CcPolygonMappingCoord(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.coord_1_float_1 = self._io.read_f4le()
            self.coord_1_float_2 = self._io.read_f4le()
            self.coord_2_float_1 = self._io.read_f4le()
            self.coord_2_float_2 = self._io.read_f4le()
            self.coord_3_float_1 = self._io.read_f4le()
            self.coord_3_float_2 = self._io.read_f4le()


    class RootInstances(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.chunks = []
            i = 0
            while not self._io.is_eof():
                self.chunks.append(CcLoadedScene.Chunk(self._io, self, self._root))
                i += 1



    class CcPolyPaint(KaitaiStruct):

        class ColorType(Enum):
            cc_poly_paint_flat = 1
            cc_poly_paint_tri = 3
            cc_poly_paint_tri_f = 4
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.color_type = KaitaiStream.resolve_enum(CcLoadedScene.CcPolyPaint.ColorType, self._io.read_u4le())
            self.colors = [None] * ((1 if self.color_type == CcLoadedScene.CcPolyPaint.ColorType.cc_poly_paint_flat else (3 if self.color_type == CcLoadedScene.CcPolyPaint.ColorType.cc_poly_paint_tri else (4 if self.color_type == CcLoadedScene.CcPolyPaint.ColorType.cc_poly_paint_tri_f else -1))))
            for i in range((1 if self.color_type == CcLoadedScene.CcPolyPaint.ColorType.cc_poly_paint_flat else (3 if self.color_type == CcLoadedScene.CcPolyPaint.ColorType.cc_poly_paint_tri else (4 if self.color_type == CcLoadedScene.CcPolyPaint.ColorType.cc_poly_paint_tri_f else -1)))):
                self.colors[i] = CcLoadedScene.Chunk(self._io, self, self._root)



    class CcVertex(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.chunk = CcLoadedScene.Chunk(self._io, self, self._root)
            self.chunks = []
            i = 0
            while not self._io.is_eof():
                self.chunks.append(CcLoadedScene.Chunk(self._io, self, self._root))
                i += 1



    class CcNull2Data(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.size = self._io.read_u4le()
            self.data = self._io.read_bytes(self.size)


    class CcLightCoordAndTwoFloats(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.coord = CcLoadedScene.Chunk(self._io, self, self._root)
            self.float_1 = self._io.read_f4le()
            self.float_2 = self._io.read_f4le()


    class CcObjectSomeBsp(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.chunks = []
            i = 0
            while not self._io.is_eof():
                self.chunks.append(CcLoadedScene.Chunk(self._io, self, self._root))
                i += 1



    class CcNull2(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.name = CcLoadedScene.Chunk(self._io, self, self._root)
            self.world_maybe = self._io.read_u4le()
            self.room = self._io.read_u4le()
            self.some_address = self._io.read_u4le()
            self.coord = CcLoadedScene.Chunk(self._io, self, self._root)
            self.float = self._io.read_f4le()
            self.unknown_chunk = CcLoadedScene.Chunk(self._io, self, self._root)
            self.chunks = []
            i = 0
            while not self._io.is_eof():
                self.chunks.append(CcLoadedScene.Chunk(self._io, self, self._root))
                i += 1



    class CcRoom(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.name = CcLoadedScene.Chunk(self._io, self, self._root)
            self.room_pointer = self._io.read_u4le()
            self.chunks = []
            i = 0
            while not self._io.is_eof():
                self.chunks.append(CcLoadedScene.Chunk(self._io, self, self._root))
                i += 1



    class CcObjectBool1(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.bool = self._io.read_u4le()


    class CcColorFlt(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.red = self._io.read_f4le()
            self.green = self._io.read_f4le()
            self.blue = self._io.read_f4le()


    class CcLightSetLightmapNew(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.bool = self._io.read_u1()
            self.float_1 = self._io.read_f4le()
            self.color = CcLoadedScene.Chunk(self._io, self, self._root)
            self.float_2 = self._io.read_f4le()
            self.float_3 = self._io.read_f4le()
            if not (self._io.is_eof()):
                self.texture_name = CcLoadedScene.Chunk(self._io, self, self._root)



    class RootBlueprints(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.chunks = []
            i = 0
            while not self._io.is_eof():
                self.chunks.append(CcLoadedScene.Chunk(self._io, self, self._root))
                i += 1



    class CcObjectBool2(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.bool = self._io.read_u4le()


    class CcObjectSomeInt(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.int = self._io.read_u4le()


    class CcCoord3dButThreeTimes(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.coords = [None] * (3)
            for i in range(3):
                self.coords[i] = CcLoadedScene.Chunk(self._io, self, self._root)



    class CcMaterialAnIntAndTwoFloats(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.int = self._io.read_u4le()
            self.float_1 = self._io.read_f4le()
            self.float_2 = self._io.read_f4le()


    class CcObjectSomeInt2(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.int = self._io.read_u4le()


    class CcLightSetLightmap(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.float_1 = self._io.read_f4le()
            self.color = CcLoadedScene.Chunk(self._io, self, self._root)
            self.float_2 = self._io.read_f4le()
            self.float_3 = self._io.read_f4le()
            if not (self._io.is_eof()):
                self.texture_name = CcLoadedScene.Chunk(self._io, self, self._root)




