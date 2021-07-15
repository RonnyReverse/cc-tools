# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

from pkg_resources import parse_version
import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO


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


    class MmChunk(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.id = (KaitaiStream.bytes_terminate(self._io.read_bytes(4), 0, False)).decode(u"ascii")
            self.size = self._io.read_u4be()
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





