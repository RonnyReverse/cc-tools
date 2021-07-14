# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

from pkg_resources import parse_version
import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO


if parse_version(kaitaistruct.__version__) < parse_version('0.9'):
    raise Exception("Incompatible Kaitai Struct Python API: 0.9 or later is required, but you have %s" % (kaitaistruct.__version__))

class CcAnim(KaitaiStruct):
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._read()

    def _read(self):
        self.header = CcAnim.Header(self._io, self, self._root)
        self.animations = [None] * (self.header.animation_count)
        for i in range(self.header.animation_count):
            self.animations[i] = CcAnim.BlueprintAnimation(self._io, self, self._root)


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


    class CcQuaternion(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.w = self._io.read_f4le()
            self.x = self._io.read_f4le()
            self.y = self._io.read_f4le()
            self.z = self._io.read_f4le()


    class BlueprintAnimation(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.blueprint_name = (KaitaiStream.bytes_terminate(self._io.read_bytes(64), 0, False)).decode(u"ascii")
            self.frames = [None] * (self._parent.header.frame_count)
            for i in range(self._parent.header.frame_count):
                self.frames[i] = CcAnim.CcAnimFrame(self._io, self, self._root)



    class CcAnimFrame(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.position = CcAnim.CcCoord3d(self._io, self, self._root)
            self.orientation = CcAnim.CcQuaternion(self._io, self, self._root)


    class Header(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.magic = self._io.read_bytes(4)
            if not self.magic == b"\x43\x43\x41\x00":
                raise kaitaistruct.ValidationNotEqualError(b"\x43\x43\x41\x00", self.magic, self._io, u"/types/header/seq/0")
            self.looping = self._io.read_u4le()
            self.animation_count = self._io.read_u4le()
            self.frame_count = self._io.read_u4le()
            self.frame_rate = self._io.read_f4le()



