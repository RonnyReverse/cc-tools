# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

from pkg_resources import parse_version
import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO


if parse_version(kaitaistruct.__version__) < parse_version('0.9'):
    raise Exception("Incompatible Kaitai Struct Python API: 0.9 or later is required, but you have %s" % (kaitaistruct.__version__))

class AfChunkContainer(KaitaiStruct):
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._read()

    def _read(self):
        self.root = AfChunkContainer.AfChunkContainer(self._io, self, self._root)

    class AfChunkContainer(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.id = (self._io.read_bytes(4)).decode(u"windows-1250")
            self.size = self._io.read_u4le()
            self.chunks = AfChunkContainer.AfChunk.Eos(self._io, self, self._root)


    class Ppos(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.position = AfChunkContainer.Xyz(self._io, self, self._root)
            self.rotation = AfChunkContainer.Xyz(self._io, self, self._root)


    class Hide(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            pass


    class Ldat(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.lines = []
            i = 0
            while not self._io.is_eof():
                self.lines.append(AfChunkContainer.Ldat.Line(self._io, self, self._root))
                i += 1


        class Line(KaitaiStruct):
            def __init__(self, _io, _parent=None, _root=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self._read()

            def _read(self):
                self.x1 = self._io.read_f4le()
                self.y1 = self._io.read_f4le()
                self.x2 = self._io.read_f4le()
                self.y2 = self._io.read_f4le()



    class Xyz(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.x = self._io.read_f4le()
            self.y = self._io.read_f4le()
            self.z = self._io.read_f4le()


    class Iaob(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.type = (self._io.read_bytes_term(0, False, True, True)).decode(u"windows-1250")
            self.name = (self._io.read_bytes_term(0, False, True, True)).decode(u"windows-1250")
            self.bools = [None] * ((8 if self.type == u"IaDoor" else (8 if self.type == u"IaHatch" else (2 if self.type == u"IaBlind" else (2 if self.type == u"IaWindow" else (1 if self.type == u"IaLightswitch" else -1))))))
            for i in range((8 if self.type == u"IaDoor" else (8 if self.type == u"IaHatch" else (2 if self.type == u"IaBlind" else (2 if self.type == u"IaWindow" else (1 if self.type == u"IaLightswitch" else -1)))))):
                self.bools[i] = self._io.read_u4le()



    class Grav(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.float_1 = self._io.read_f4le()
            self.float_2 = self._io.read_f4le()
            self.float_3 = self._io.read_f4le()


    class AfChunk(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.id = (self._io.read_bytes(4)).decode(u"windows-1250")
            self.size = self._io.read_u4le()
            _on = self.id
            if _on == u"DEAT":
                self.data = self._io.read_u4le()
            elif _on == u"AXMI":
                self.data = self._io.read_u4le()
            elif _on == u"BCKD":
                self.data = (KaitaiStream.bytes_terminate(self._io.read_bytes(self.size), 0, False)).decode(u"windows-1250")
            elif _on == u"PPOS":
                self._raw_data = self._io.read_bytes(self.size)
                _io__raw_data = KaitaiStream(BytesIO(self._raw_data))
                self.data = AfChunkContainer.Ppos(_io__raw_data, self, self._root)
            elif _on == u"ALMI":
                self.data = self._io.read_u4le()
            elif _on == u"OBJE":
                self._raw_data = self._io.read_bytes(self.size)
                _io__raw_data = KaitaiStream(BytesIO(self._raw_data))
                self.data = AfChunkContainer.Obje(_io__raw_data, self, self._root)
            elif _on == u"HOUS":
                self.data = (KaitaiStream.bytes_terminate(self._io.read_bytes(self.size), 0, False)).decode(u"windows-1250")
            elif _on == u"PDEA":
                self.data = self._io.read_u4le()
            elif _on == u"ACKI":
                self.data = self._io.read_u4le()
            elif _on == u"MMSK":
                self.data = (KaitaiStream.bytes_terminate(self._io.read_bytes(self.size), 0, False)).decode(u"windows-1250")
            elif _on == u"IAOB":
                self._raw_data = self._io.read_bytes(self.size)
                _io__raw_data = KaitaiStream(BytesIO(self._raw_data))
                self.data = AfChunkContainer.Iaob(_io__raw_data, self, self._root)
            elif _on == u"SCOR":
                self.data = self._io.read_u4le()
            elif _on == u"FRIK":
                self.data = self._io.read_u4le()
            elif _on == u"OUT2":
                self.data = (KaitaiStream.bytes_terminate(self._io.read_bytes(self.size), 0, False)).decode(u"windows-1250")
            elif _on == u"MEDA":
                self.data = (KaitaiStream.bytes_terminate(self._io.read_bytes(self.size), 0, False)).decode(u"windows-1250")
            elif _on == u"LDAT":
                self._raw_data = self._io.read_bytes(self.size)
                _io__raw_data = KaitaiStream(BytesIO(self._raw_data))
                self.data = AfChunkContainer.Ldat(_io__raw_data, self, self._root)
            elif _on == u"PICT":
                self.data = (KaitaiStream.bytes_terminate(self._io.read_bytes(self.size), 0, False)).decode(u"windows-1250")
            elif _on == u"GUKI":
                self.data = self._io.read_u4le()
            elif _on == u"PRIM":
                self.data = (KaitaiStream.bytes_terminate(self._io.read_bytes(self.size), 0, False)).decode(u"windows-1250")
            elif _on == u"SELA":
                self.data = (KaitaiStream.bytes_terminate(self._io.read_bytes(self.size), 0, False)).decode(u"windows-1250")
            elif _on == u"TEXT":
                self.data = (KaitaiStream.bytes_terminate(self._io.read_bytes(self.size), 0, False)).decode(u"windows-1250")
            elif _on == u"HIDE":
                self._raw_data = self._io.read_bytes(self.size)
                _io__raw_data = KaitaiStream(BytesIO(self._raw_data))
                self.data = AfChunkContainer.Hide(_io__raw_data, self, self._root)
            elif _on == u"NATY":
                self.data = (KaitaiStream.bytes_terminate(self._io.read_bytes(self.size), 0, False)).decode(u"windows-1250")
            elif _on == u"TEXU":
                self.data = (KaitaiStream.bytes_terminate(self._io.read_bytes(self.size), 0, False)).decode(u"windows-1250")
            elif _on == u"GCCS":
                self.data = self._io.read_u4le()
            elif _on == u"FLRY":
                self._raw_data = self._io.read_bytes(self.size)
                _io__raw_data = KaitaiStream(BytesIO(self._raw_data))
                self.data = AfChunkContainer.Flry(_io__raw_data, self, self._root)
            elif _on == u"FOOK":
                self.data = self._io.read_u4le()
            elif _on == u"GRAV":
                self._raw_data = self._io.read_bytes(self.size)
                _io__raw_data = KaitaiStream(BytesIO(self._raw_data))
                self.data = AfChunkContainer.Grav(_io__raw_data, self, self._root)
            elif _on == u"PDAT":
                self._raw_data = self._io.read_bytes(self.size)
                _io__raw_data = KaitaiStream(BytesIO(self._raw_data))
                self.data = AfChunkContainer.Pdat(_io__raw_data, self, self._root)
            elif _on == u"LLST":
                self.data = (KaitaiStream.bytes_terminate(self._io.read_bytes(self.size), 0, False)).decode(u"windows-1250")
            elif _on == u"NAME":
                self.data = (KaitaiStream.bytes_terminate(self._io.read_bytes(self.size), 0, False)).decode(u"windows-1250")
            elif _on == u"AIRS":
                self.data = (KaitaiStream.bytes_terminate(self._io.read_bytes(self.size), 0, False)).decode(u"windows-1250")
            elif _on == u"THRD":
                self.data = self._io.read_u4le()
            elif _on == u"OUTL":
                self.data = (KaitaiStream.bytes_terminate(self._io.read_bytes(self.size), 0, False)).decode(u"windows-1250")
            elif _on == u"CCFF":
                self.data = (KaitaiStream.bytes_terminate(self._io.read_bytes(self.size), 0, False)).decode(u"windows-1250")
            elif _on == u"MESH":
                self.data = (KaitaiStream.bytes_terminate(self._io.read_bytes(self.size), 0, False)).decode(u"windows-1250")
            elif _on == u"WUKI":
                self.data = self._io.read_u4le()
            elif _on == u"MIMG":
                self.data = (KaitaiStream.bytes_terminate(self._io.read_bytes(self.size), 0, False)).decode(u"windows-1250")
            elif _on == u"TYPE":
                self.data = (KaitaiStream.bytes_terminate(self._io.read_bytes(self.size), 0, False)).decode(u"windows-1250")
            elif _on == u"PKIL":
                self.data = self._io.read_u4le()
            elif _on == u"CATG":
                self.data = (KaitaiStream.bytes_terminate(self._io.read_bytes(self.size), 0, False)).decode(u"windows-1250")
            elif _on == u"MODL":
                self._raw_data = self._io.read_bytes(self.size)
                _io__raw_data = KaitaiStream(BytesIO(self._raw_data))
                self.data = AfChunkContainer.Modl(_io__raw_data, self, self._root)
            elif _on == u"SCND":
                self.data = (KaitaiStream.bytes_terminate(self._io.read_bytes(self.size), 0, False)).decode(u"windows-1250")
            elif _on == u"TXT2":
                self.data = (KaitaiStream.bytes_terminate(self._io.read_bytes(self.size), 0, False)).decode(u"windows-1250")
            elif _on == u"ROOM":
                self._raw_data = self._io.read_bytes(self.size)
                _io__raw_data = KaitaiStream(BytesIO(self._raw_data))
                self.data = AfChunkContainer.Room(_io__raw_data, self, self._root)
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
                    self.chunks.append(AfChunkContainer.AfChunk(self._io, self, self._root))
                    i += 1




    class Pdat(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.entries = []
            i = 0
            while not self._io.is_eof():
                self.entries.append(AfChunkContainer.Pdat.BufferEntry(self._io, self, self._root))
                i += 1


        class BufferEntry(KaitaiStruct):
            def __init__(self, _io, _parent=None, _root=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self._read()

            def _read(self):
                self.data = self._io.read_bytes(12)



    class Modl(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.object = AfChunkContainer.Obje(self._io, self, self._root)
            self.name = (self._io.read_bytes_term(0, False, True, True)).decode(u"windows-1250")
            self.int1 = self._io.read_u4le()
            self.str2 = (self._io.read_bytes_term(0, False, True, True)).decode(u"windows-1250")
            self.int2 = self._io.read_u4le()
            self.str3 = (self._io.read_bytes_term(0, False, True, True)).decode(u"windows-1250")
            self.int3 = self._io.read_u4le()
            if not (self._io.is_eof()):
                self.int4 = self._io.read_u4le()



    class Flry(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.floor_1_y = self._io.read_f4le()
            self.floor_2_y = self._io.read_f4le()
            self.floor_3_y = self._io.read_f4le()


    class Room(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.room_id = self._io.read_u1()
            self.name_internal = (self._io.read_bytes_term(0, False, True, True)).decode(u"windows-1250")
            self.name_localized = (self._io.read_bytes_term(0, False, True, True)).decode(u"windows-1250")
            self.floor = self._io.read_u1()


    class Obje(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.position = AfChunkContainer.Xyz(self._io, self, self._root)
            self.axis_rotation = AfChunkContainer.Xyz(self._io, self, self._root)
            self.room = (self._io.read_bytes_term(0, False, True, True)).decode(u"windows-1250")
            self.object = (self._io.read_bytes_term(0, False, True, True)).decode(u"windows-1250")



