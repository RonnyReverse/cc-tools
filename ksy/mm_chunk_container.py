# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

from pkg_resources import parse_version
import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
from enum import Enum


if parse_version(kaitaistruct.__version__) < parse_version('0.9'):
    raise Exception("Incompatible Kaitai Struct Python API: 0.9 or later is required, but you have %s" % (kaitaistruct.__version__))

class MmChunkContainer(KaitaiStruct):
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._read()

    def _read(self):
        self.root = MmChunkContainer.MmChunkContainer(self._io, self, self._root)

    class Airb(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.name = (self._io.read_bytes_term(0, False, True, True)).decode(u"ascii")
            self.airp = MmChunkContainer.Airp(self._io, self, self._root)


    class MmChunkContainer(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.magic = self._io.read_bytes(4)
            if not self.magic == b"\x46\x4F\x52\x4D":
                raise kaitaistruct.ValidationNotEqualError(b"\x46\x4F\x52\x4D", self.magic, self._io, u"/types/mm_chunk_container/seq/0")
            self.size = self._io.read_u4be()
            self.id = (KaitaiStream.bytes_terminate(self._io.read_bytes(4), 0, False)).decode(u"ascii")
            self.chunks = MmChunkContainer.MmChunk.Eos(self._io, self, self._root)


    class Aira(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.id = self._io.read_u4le()
            self.airb = MmChunkContainer.Airb(self._io, self, self._root)


    class Phot(KaitaiStruct):

        class PhotoStatus(Enum):
            none = 0
            taken = 1
            developed = 2
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.enabled = self._io.read_u4le()
            self.completed = self._io.read_u4le()
            self.photos = [None] * (10)
            for i in range(10):
                self.photos[i] = MmChunkContainer.Phot.Row(self._io, self, self._root)


        class Row(KaitaiStruct):
            def __init__(self, _io, _parent=None, _root=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self._read()

            def _read(self):
                self.column = [None] * (10)
                for i in range(10):
                    self.column[i] = KaitaiStream.resolve_enum(MmChunkContainer.Phot.PhotoStatus, self._io.read_u4le())




    class Airp(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.parts = []
            i = 0
            while not self._io.is_eof():
                self.parts.append(MmChunkContainer.Airp.AirpPart(self._io, self, self._root))
                i += 1


        class AirpPart(KaitaiStruct):
            def __init__(self, _io, _parent=None, _root=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self._read()

            def _read(self):
                self.id = self._io.read_u4le()
                self.slot = self._io.read_u2le()
                self.parent = self._io.read_u2le()



    class Miss(KaitaiStruct):

        class MissionState(Enum):
            none = 0
            activate = 1
            complete = 2
            reward = 3
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.id = self._io.read_u4le()
            self.state = KaitaiStream.resolve_enum(MmChunkContainer.Miss.MissionState, self._io.read_u4le())
            self.is_random = self._io.read_u4le()
            self.dependencies = [None] * (self.dependency_count)
            for i in range(self.dependency_count):
                self.dependencies[i] = self._io.read_u4le()

            self.state_changes = [None] * (self.state_change_count)
            for i in range(self.state_change_count):
                self.state_changes[i] = MmChunkContainer.Miss.StateChange(self._io, self, self._root)


        class StateChange(KaitaiStruct):
            def __init__(self, _io, _parent=None, _root=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self._read()

            def _read(self):
                self.unknown_bool = self._io.read_u4le()
                self.success_processed = self._io.read_u4le()


        @property
        def mission_name(self):
            if hasattr(self, '_m_mission_name'):
                return self._m_mission_name if hasattr(self, '_m_mission_name') else None

            self._m_mission_name = (u"getcamera" if self.id == 1 else (u"deliver_newspaper_EE" if self.id == 2 else (u"gettent" if self.id == 3 else (u"repairtent" if self.id == 4 else (u"deliver_newspaper_TT" if self.id == 5 else (u"plant_crops" if self.id == 6 else (u"raisetent" if self.id == 7 else (u"rope" if self.id == 8 else (u"getfurniture" if self.id == 9 else (u"gettablecloth" if self.id == 10 else (u"getcookpot" if self.id == 11 else (u"deliver_newspaper_VR" if self.id == 12 else (u"worldphoto" if self.id == 13 else (u"vacuumcleaner" if self.id == 14 else (u"vacuumbags" if self.id == 15 else (u"powerplant_getup" if self.id == 16 else (u"powerplant_repair" if self.id == 17 else (u"deliver_newspaper_BB" if self.id == 18 else (u"getsupplies" if self.id == 19 else (u"blankets_BB" if self.id == 20 else (u"seismograph_partone" if self.id == 21 else (u"seismograph_parttwo" if self.id == 22 else (u"leaflets_VV_seismograph" if self.id == 23 else (u"seismograph_partthree" if self.id == 24 else (u"seismograph_getnet" if self.id == 25 else (u"getcable" if self.id == 26 else (u"researchequipment_BB" if self.id == 27 else (u"ernst_timber" if self.id == 28 else (u"ernst_timber" if self.id == 28 else (u"ernst_metalsheets" if self.id == 29 else (u"ernst_metalsheets" if self.id == 29 else (u"ernst_tools" if self.id == 30 else (u"ernst_tools" if self.id == 30 else (u"richard_book" if self.id == 31 else (u"richard_book" if self.id == 31 else (u"find_fabric" if self.id == 32 else (u"find_garlic" if self.id == 33 else (u"make_costumes" if self.id == 34 else (u"get_specialthread" if self.id == 35 else (u"erik_needhelp_thread" if self.id == 36 else (u"find_reindeer" if self.id == 38 else (u"place_antennas_1" if self.id == 39 else (u"place_antennas_2" if self.id == 40 else (u"place_antennas_3" if self.id == 41 else (u"get_cropsduster" if self.id == 42 else (u"water_crops" if self.id == 43 else (u"scare_gophers" if self.id == 44 else (u"worldphoto_part" if self.id == 45 else (u"worldphoto_finished" if self.id == 101 else (u"erzon_mobilephone" if self.id == 601 else (u"erzon_fancyclock" if self.id == 602 else (u"erzon_hangglider" if self.id == 603 else (u"erzon_sunglasses" if self.id == 604 else (u"photo_impactcraters_one" if self.id == 701 else (u"photo_impactcraters_two" if self.id == 702 else (u"photo_impactcraters_three" if self.id == 703 else (u"photo_birds_one" if self.id == 704 else (u"photo_birds_two" if self.id == 705 else (u"photo_birds_three" if self.id == 706 else (u"info_mygghanget" if self.id == 1002 else (u"info_roymccoy" if self.id == 1004 else (u"info_samscribbler" if self.id == 1005 else (u"info_varldsutstallning" if self.id == 1006 else (u"info_violawallmark" if self.id == 1007 else (u"info_atleartillerist" if self.id == 1008 else (u"info_turetapp" if self.id == 1009 else (u"info_richardrevers" if self.id == 1010 else (u"info_raymondraser" if self.id == 1011 else (u"info_fionafalk" if self.id == 1012 else (u"info_grottegrundlig" if self.id == 1013 else (u"info_gabriellagourmet" if self.id == 1014 else (u"info_brejtonbord" if self.id == 1015 else (u"info_victorvulcan" if self.id == 1016 else (u"info_vemontvrak" if self.id == 1017 else (u"info_dorisdigital" if self.id == 1018 else (u"info_ernsteremit" if self.id == 1019 else (u"info_samposanna" if self.id == 1020 else (u"mecchi_story_TT" if self.id == 2000 else (u"mecchi_story_VV" if self.id == 2001 else (u"mecchi_story_VR" if self.id == 2002 else (u"randomdoris_1" if self.id == 5001 else (u"randomdoris_2" if self.id == 5002 else (u"randomdoris_3" if self.id == 5003 else (u"randommia_1" if self.id == 6001 else (u"randommia_2" if self.id == 6002 else (u"randommia_3" if self.id == 6003 else (u"mecchifinal" if self.id == 9999 else u"ERROR")))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))
            return self._m_mission_name if hasattr(self, '_m_mission_name') else None

        @property
        def state_change_count(self):
            if hasattr(self, '_m_state_change_count'):
                return self._m_state_change_count if hasattr(self, '_m_state_change_count') else None

            self._m_state_change_count = (4 if self.id == 1 else (4 if self.id == 2 else (3 if self.id == 3 else (7 if self.id == 4 else (4 if self.id == 5 else (2 if self.id == 6 else (3 if self.id == 7 else (3 if self.id == 8 else (14 if self.id == 9 else (5 if self.id == 10 else (5 if self.id == 11 else (5 if self.id == 12 else (3 if self.id == 13 else (4 if self.id == 14 else (4 if self.id == 15 else (1 if self.id == 16 else (6 if self.id == 17 else (5 if self.id == 18 else (5 if self.id == 19 else (5 if self.id == 20 else (3 if self.id == 21 else (4 if self.id == 22 else (5 if self.id == 23 else (6 if self.id == 24 else (2 if self.id == 25 else (6 if self.id == 26 else (5 if self.id == 27 else (2 if self.id == 28 else (3 if self.id == 29 else (5 if self.id == 30 else (5 if self.id == 31 else (2 if self.id == 32 else (6 if self.id == 33 else (2 if self.id == 34 else (5 if self.id == 35 else (5 if self.id == 36 else (4 if self.id == 38 else (6 if self.id == 39 else (4 if self.id == 40 else (4 if self.id == 41 else (2 if self.id == 42 else (2 if self.id == 43 else (2 if self.id == 44 else (2 if self.id == 45 else (1 if self.id == 101 else (3 if self.id == 601 else (3 if self.id == 602 else (3 if self.id == 603 else (3 if self.id == 604 else (3 if self.id == 701 else (4 if self.id == 702 else (6 if self.id == 703 else (3 if self.id == 704 else (4 if self.id == 705 else (6 if self.id == 706 else (1 if self.id == 1002 else (1 if self.id == 1004 else (1 if self.id == 1005 else (1 if self.id == 1006 else (1 if self.id == 1007 else (1 if self.id == 1008 else (1 if self.id == 1009 else (1 if self.id == 1010 else (1 if self.id == 1011 else (1 if self.id == 1012 else (1 if self.id == 1013 else (1 if self.id == 1014 else (1 if self.id == 1015 else (1 if self.id == 1016 else (1 if self.id == 1017 else (1 if self.id == 1018 else (1 if self.id == 1019 else (1 if self.id == 1020 else (2 if self.id == 2000 else (2 if self.id == 2001 else (2 if self.id == 2002 else (2 if self.id == 5001 else (2 if self.id == 5002 else (2 if self.id == 5003 else (2 if self.id == 6001 else (2 if self.id == 6002 else (2 if self.id == 6003 else (1 if self.id == 9999 else -1)))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))
            return self._m_state_change_count if hasattr(self, '_m_state_change_count') else None

        @property
        def dependency_count(self):
            if hasattr(self, '_m_dependency_count'):
                return self._m_dependency_count if hasattr(self, '_m_dependency_count') else None

            self._m_dependency_count = (4 if self.id == 1 else (4 if self.id == 2 else (3 if self.id == 3 else (4 if self.id == 4 else (4 if self.id == 5 else (3 if self.id == 6 else (4 if self.id == 7 else (4 if self.id == 8 else (8 if self.id == 9 else (4 if self.id == 10 else (4 if self.id == 11 else (4 if self.id == 12 else (3 if self.id == 13 else (3 if self.id == 14 else (4 if self.id == 15 else (5 if self.id == 16 else (4 if self.id == 17 else (4 if self.id == 18 else (4 if self.id == 19 else (3 if self.id == 20 else (3 if self.id == 21 else (5 if self.id == 22 else (4 if self.id == 23 else (4 if self.id == 24 else (3 if self.id == 25 else (4 if self.id == 26 else (4 if self.id == 27 else (3 if self.id == 28 else (3 if self.id == 28 else (4 if self.id == 29 else (4 if self.id == 29 else (4 if self.id == 30 else (4 if self.id == 30 else (4 if self.id == 31 else (4 if self.id == 31 else (4 if self.id == 32 else (4 if self.id == 33 else (3 if self.id == 34 else (4 if self.id == 35 else (8 if self.id == 36 else (3 if self.id == 38 else (2 if self.id == 39 else (2 if self.id == 40 else (3 if self.id == 41 else (2 if self.id == 42 else (4 if self.id == 43 else (4 if self.id == 44 else (3 if self.id == 45 else (2 if self.id == 101 else (6 if self.id == 601 else (6 if self.id == 602 else (6 if self.id == 603 else (6 if self.id == 604 else (3 if self.id == 701 else (2 if self.id == 702 else (3 if self.id == 703 else (3 if self.id == 704 else (2 if self.id == 705 else (3 if self.id == 706 else (1 if self.id == 1002 else (1 if self.id == 1004 else (1 if self.id == 1005 else (1 if self.id == 1006 else (1 if self.id == 1007 else (1 if self.id == 1008 else (1 if self.id == 1009 else (1 if self.id == 1010 else (1 if self.id == 1011 else (1 if self.id == 1012 else (1 if self.id == 1013 else (1 if self.id == 1014 else (1 if self.id == 1015 else (1 if self.id == 1016 else (1 if self.id == 1017 else (1 if self.id == 1018 else (1 if self.id == 1019 else (1 if self.id == 1020 else (2 if self.id == 2000 else (2 if self.id == 2001 else (2 if self.id == 2002 else (3 if self.id == 5001 else (5 if self.id == 5002 else (5 if self.id == 5003 else (3 if self.id == 6001 else (4 if self.id == 6002 else (4 if self.id == 6003 else (30 if self.id == 9999 else -1)))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))
            return self._m_dependency_count if hasattr(self, '_m_dependency_count') else None


    class MmChunk(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.id = (KaitaiStream.bytes_terminate(self._io.read_bytes(4), 0, False)).decode(u"ascii")
            self.size = self._io.read_u4be()
            _on = self.id
            if _on == u"MISS":
                self._raw_data = self._io.read_bytes(self.size)
                _io__raw_data = KaitaiStream(BytesIO(self._raw_data))
                self.data = MmChunkContainer.Miss(_io__raw_data, self, self._root)
            elif _on == u"AIRB":
                self._raw_data = self._io.read_bytes(self.size)
                _io__raw_data = KaitaiStream(BytesIO(self._raw_data))
                self.data = MmChunkContainer.Airb(_io__raw_data, self, self._root)
            elif _on == u"PHOT":
                self._raw_data = self._io.read_bytes(self.size)
                _io__raw_data = KaitaiStream(BytesIO(self._raw_data))
                self.data = MmChunkContainer.Phot(_io__raw_data, self, self._root)
            elif _on == u"INVI":
                self.data = (KaitaiStream.bytes_terminate(self._io.read_bytes(self.size), 0, False)).decode(u"ascii")
            elif _on == u"PART":
                self._raw_data = self._io.read_bytes(self.size)
                _io__raw_data = KaitaiStream(BytesIO(self._raw_data))
                self.data = MmChunkContainer.Part(_io__raw_data, self, self._root)
            elif _on == u"BARN":
                self._raw_data = self._io.read_bytes(self.size)
                _io__raw_data = KaitaiStream(BytesIO(self._raw_data))
                self.data = MmChunkContainer.Barn(_io__raw_data, self, self._root)
            elif _on == u"NAME":
                self.data = (KaitaiStream.bytes_terminate(self._io.read_bytes(self.size), 0, False)).decode(u"ascii")
            elif _on == u"AIRA":
                self._raw_data = self._io.read_bytes(self.size)
                _io__raw_data = KaitaiStream(BytesIO(self._raw_data))
                self.data = MmChunkContainer.Aira(_io__raw_data, self, self._root)
            elif _on == u"DIPL":
                self._raw_data = self._io.read_bytes(self.size)
                _io__raw_data = KaitaiStream(BytesIO(self._raw_data))
                self.data = MmChunkContainer.Dipl(_io__raw_data, self, self._root)
            elif _on == u"AIRP":
                self._raw_data = self._io.read_bytes(self.size)
                _io__raw_data = KaitaiStream(BytesIO(self._raw_data))
                self.data = MmChunkContainer.Airp(_io__raw_data, self, self._root)
            else:
                self.data = self._io.read_bytes(self.size)

        class Eos(KaitaiStruct):
            def __init__(self, _io, _parent=None, _root=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self._read()

            def _read(self):
                self.chunks = []
                i = 0
                while not self._io.is_eof():
                    self.chunks.append(MmChunkContainer.MmChunk(self._io, self, self._root))
                    i += 1




    class Barn(KaitaiStruct):

        class BarnLocation(Enum):
            outside = 0
            barn_floor = 1
            barn_shelf_1 = 2
            barn_shelf_2 = 3
            barn_shelf_3 = 4
            barn_shelf_4 = 5
            barn_shelf_5 = 6
            barn_shelf_6 = 7
            barn_shelf_7 = 8
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.parts = []
            i = 0
            while not self._io.is_eof():
                self.parts.append(MmChunkContainer.Barn.BarnPart(self._io, self, self._root))
                i += 1


        class BarnPart(KaitaiStruct):
            def __init__(self, _io, _parent=None, _root=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self._read()

            def _read(self):
                self.location = KaitaiStream.resolve_enum(MmChunkContainer.Barn.BarnLocation, self._io.read_u4le())
                self.id = self._io.read_u4le()
                self.x = self._io.read_f4le()
                self.y = self._io.read_f4le()
                self.z = self._io.read_f4le()



    class Part(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.id = self._io.read_u4le()
            self.ccf = (self._io.read_bytes_term(0, False, True, True)).decode(u"ascii")


    class Dipl(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.water = self._io.read_u4le()
            self.snow = self._io.read_u4le()
            self.racing = self._io.read_u4le()
            self.circus = self._io.read_u4le()
            self.map = self._io.read_u4le()
            self.mecci = self._io.read_u4le()



