# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

from pkg_resources import parse_version
import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO


if parse_version(kaitaistruct.__version__) < parse_version('0.9'):
    raise Exception("Incompatible Kaitai Struct Python API: 0.9 or later is required, but you have %s" % (kaitaistruct.__version__))

class UpPackage(KaitaiStruct):
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._read()

    def _read(self):
        self.header = UpPackage.Header(self._io, self, self._root)

    class Header(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.magic = self._io.read_bytes(4)
            if not self.magic == b"\x55\x44\x53\x50":
                raise kaitaistruct.ValidationNotEqualError(b"\x55\x44\x53\x50", self.magic, self._io, u"/types/header/seq/0")
            self.version = self._io.read_u4le()
            self.dirs = UpPackage.Header.Block(self._io, self, self._root)
            self.strings = UpPackage.Header.Block(self._io, self, self._root)
            self.files = UpPackage.Header.Block(self._io, self, self._root)

        class Empty(KaitaiStruct):
            def __init__(self, _io, _parent=None, _root=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self._read()

            def _read(self):
                pass


        class Block(KaitaiStruct):
            def __init__(self, _io, _parent=None, _root=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self._read()

            def _read(self):
                self.size = self._io.read_u4le()
                self.pos = self._io.read_u4le()

            @property
            def data(self):
                if hasattr(self, '_m_data'):
                    return self._m_data if hasattr(self, '_m_data') else None

                _pos = self._io.pos()
                self._io.seek(self.pos)
                self._raw__m_data = self._io.read_bytes(self.size)
                _io__raw__m_data = KaitaiStream(BytesIO(self._raw__m_data))
                self._m_data = UpPackage.Header.Empty(_io__raw__m_data, self, self._root)
                self._io.seek(_pos)
                return self._m_data if hasattr(self, '_m_data') else None



    class UpHashEntry(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.name_hash = self._io.read_u4le()
            self.name = UpPackage.UpHashEntry.String(self._io, self, self._root)
            self.is_compressed = self._io.read_u4le()
            self.size = self._io.read_u4le()
            self.size_compressed = self._io.read_u4le()
            self.offset = self._io.read_u4le()

        class String(KaitaiStruct):
            def __init__(self, _io, _parent=None, _root=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self._read()

            def _read(self):
                self.offset = self._io.read_u4le()

            @property
            def value(self):
                if hasattr(self, '_m_value'):
                    return self._m_value if hasattr(self, '_m_value') else None

                io = self._root.header.strings.data._io
                _pos = io.pos()
                io.seek(self.offset)
                self._m_value = (io.read_bytes_term(0, False, True, True)).decode(u"ascii")
                io.seek(_pos)
                return self._m_value if hasattr(self, '_m_value') else None


        class Dir(KaitaiStruct):
            def __init__(self, _io, _parent=None, _root=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self._read()

            def _read(self):
                self.entry = UpPackage.UpHashEntry(self._io, self, self._root)

            @property
            def path(self):
                if hasattr(self, '_m_path'):
                    return self._m_path if hasattr(self, '_m_path') else None

                self._m_path = self.entry.name.value
                return self._m_path if hasattr(self, '_m_path') else None

            @property
            def files(self):
                if hasattr(self, '_m_files'):
                    return self._m_files if hasattr(self, '_m_files') else None

                io = self._root.header.files.data._io
                _pos = io.pos()
                io.seek(self.entry.offset)
                self._m_files = [None] * (self.entry.size_compressed)
                for i in range(self.entry.size_compressed):
                    self._m_files[i] = UpPackage.UpHashEntry.File(io, self, self._root)

                io.seek(_pos)
                return self._m_files if hasattr(self, '_m_files') else None


        class File(KaitaiStruct):
            def __init__(self, _io, _parent=None, _root=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self._read()

            def _read(self):
                self.entry = UpPackage.UpHashEntry(self._io, self, self._root)

            @property
            def path(self):
                if hasattr(self, '_m_path'):
                    return self._m_path if hasattr(self, '_m_path') else None

                self._m_path = self._parent.entry.name.value + u"\\" + self.entry.name.value
                return self._m_path if hasattr(self, '_m_path') else None

            @property
            def data(self):
                if hasattr(self, '_m_data'):
                    return self._m_data if hasattr(self, '_m_data') else None

                io = self._root._io
                _pos = io.pos()
                io.seek(self.entry.offset)
                self._m_data = io.read_bytes(self.entry.size_compressed)
                io.seek(_pos)
                return self._m_data if hasattr(self, '_m_data') else None



    @property
    def dirs(self):
        if hasattr(self, '_m_dirs'):
            return self._m_dirs if hasattr(self, '_m_dirs') else None

        io = self.header.dirs.data._io
        self._m_dirs = []
        i = 0
        while not io.is_eof():
            self._m_dirs.append(UpPackage.UpHashEntry.Dir(io, self, self._root))
            i += 1

        return self._m_dirs if hasattr(self, '_m_dirs') else None


