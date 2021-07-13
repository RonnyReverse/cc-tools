# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

from pkg_resources import parse_version
import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
from enum import Enum


if parse_version(kaitaistruct.__version__) < parse_version('0.9'):
    raise Exception("Incompatible Kaitai Struct Python API: 0.9 or later is required, but you have %s" % (kaitaistruct.__version__))

class GtImage(KaitaiStruct):

    class GtFmt(Enum):
        none = 0
        p4 = 1
        ap44 = 2
        p8 = 3
        ap88 = 4
        rgb565 = 5
        argb4444 = 6
        rgb888 = 7
        argb8888 = 8
        rgb332 = 9
        rgb555 = 10
        argb1555 = 11
        argb8332 = 12
        dxt1 = 13
        dxt2 = 15
        dxt3 = 16
        dxt4 = 17
        dxt5 = 18
        bgr565 = 19
        bgra4444 = 20
        bgr888 = 21
        bgra8888 = 22
        bgr233 = 23
        bgr555 = 24
        bgra5551 = 25
        bgra2338 = 26
        abgr444 = 27
        abgr888 = 28
        abgr1555 = 29
        abgr8233 = 31
        rgba4444 = 32
        rgba8888 = 33
        rgba5551 = 34
        rgba3328 = 35
        argb4565 = 36
        xrgb8888 = 37
        alpha = 38
        a8 = 39
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._read()

    def _read(self):
        self.magic = self._io.read_bytes(4)
        if not self.magic == b"\x47\x74\x49\x6D":
            raise kaitaistruct.ValidationNotEqualError(b"\x47\x74\x49\x6D", self.magic, self._io, u"/seq/0")
        self.version = self._io.read_u4le()
        self.chunks = []
        i = 0
        while not self._io.is_eof():
            self.chunks.append(GtImage.Chunk(self._io, self, self._root))
            i += 1


    class Chunk(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.tag = (self._io.read_bytes(4)).decode(u"ascii")
            self.size = self._io.read_u4le()
            _on = self.tag
            if _on == u"Imag":
                self._raw_data = self._io.read_bytes(((self._io.size() - self._io.pos()) if self.size > (self._io.size() - self._io.pos()) else self.size))
                _io__raw_data = KaitaiStream(BytesIO(self._raw_data))
                self.data = GtImage.Imag(_io__raw_data, self, self._root)
            else:
                self.data = self._io.read_bytes(((self._io.size() - self._io.pos()) if self.size > (self._io.size() - self._io.pos()) else self.size))


    class Imag(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.format = KaitaiStream.resolve_enum(GtImage.GtFmt, self._io.read_u4le())
            self.width = self._io.read_u4le()
            self.height = self._io.read_u4le()
            self.palette_size = self._io.read_u4le()
            self.mipmap_levels = self._io.read_u4le()
            self.palette = [None] * (self.palette_size)
            for i in range(self.palette_size):
                self.palette[i] = self._io.read_u4le()

            self.mipmaps = [None] * (self.mipmap_levels)
            for i in range(self.mipmap_levels):
                self.mipmaps[i] = GtImage.Imag.MipmapLevel(i, self._io, self, self._root)


        class FormatInfo(KaitaiStruct):
            def __init__(self, format, _io, _parent=None, _root=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self.format = format
                self._read()

            def _read(self):
                pass

            @property
            def pixel_size(self):
                if hasattr(self, '_m_pixel_size'):
                    return self._m_pixel_size if hasattr(self, '_m_pixel_size') else None

                self._m_pixel_size = (0 if self.format == GtImage.GtFmt.none else (0 if self.format == GtImage.GtFmt.p4 else (1 if self.format == GtImage.GtFmt.ap44 else (1 if self.format == GtImage.GtFmt.p8 else (2 if self.format == GtImage.GtFmt.ap88 else (2 if self.format == GtImage.GtFmt.rgb565 else (2 if self.format == GtImage.GtFmt.argb4444 else (3 if self.format == GtImage.GtFmt.rgb888 else (4 if self.format == GtImage.GtFmt.argb8888 else (1 if self.format == GtImage.GtFmt.rgb332 else (2 if self.format == GtImage.GtFmt.rgb555 else (2 if self.format == GtImage.GtFmt.argb1555 else (2 if self.format == GtImage.GtFmt.argb8332 else (0 if self.format == GtImage.GtFmt.dxt1 else (0 if self.format == GtImage.GtFmt.dxt2 else (0 if self.format == GtImage.GtFmt.dxt3 else (0 if self.format == GtImage.GtFmt.dxt4 else (0 if self.format == GtImage.GtFmt.dxt5 else (2 if self.format == GtImage.GtFmt.bgr565 else (2 if self.format == GtImage.GtFmt.bgra4444 else (3 if self.format == GtImage.GtFmt.bgr888 else (4 if self.format == GtImage.GtFmt.bgra8888 else (1 if self.format == GtImage.GtFmt.bgr233 else (2 if self.format == GtImage.GtFmt.bgr555 else (2 if self.format == GtImage.GtFmt.bgra5551 else (2 if self.format == GtImage.GtFmt.bgra2338 else (2 if self.format == GtImage.GtFmt.abgr444 else (4 if self.format == GtImage.GtFmt.abgr888 else (2 if self.format == GtImage.GtFmt.abgr1555 else (2 if self.format == GtImage.GtFmt.abgr8233 else (2 if self.format == GtImage.GtFmt.rgba4444 else (4 if self.format == GtImage.GtFmt.rgba8888 else (2 if self.format == GtImage.GtFmt.rgba5551 else (2 if self.format == GtImage.GtFmt.rgba3328 else (4 if self.format == GtImage.GtFmt.argb4565 else (4 if self.format == GtImage.GtFmt.xrgb8888 else (0 if self.format == GtImage.GtFmt.alpha else (1 if self.format == GtImage.GtFmt.a8 else -1))))))))))))))))))))))))))))))))))))))
                return self._m_pixel_size if hasattr(self, '_m_pixel_size') else None


        class MipmapLevel(KaitaiStruct):
            def __init__(self, level, _io, _parent=None, _root=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self.level = level
                self._read()

            def _read(self):
                self.data = self._io.read_bytes(self.size)

            @property
            def width(self):
                if hasattr(self, '_m_width'):
                    return self._m_width if hasattr(self, '_m_width') else None

                self._m_width = (self._parent.width >> self.level)
                return self._m_width if hasattr(self, '_m_width') else None

            @property
            def height(self):
                if hasattr(self, '_m_height'):
                    return self._m_height if hasattr(self, '_m_height') else None

                self._m_height = (self._parent.height >> self.level)
                return self._m_height if hasattr(self, '_m_height') else None

            @property
            def size(self):
                if hasattr(self, '_m_size'):
                    return self._m_size if hasattr(self, '_m_size') else None

                self._m_size = (((self._parent.width * self._parent.height) * self._parent.format_info.pixel_size) >> (self.level * 2))
                return self._m_size if hasattr(self, '_m_size') else None


        @property
        def format_info(self):
            if hasattr(self, '_m_format_info'):
                return self._m_format_info if hasattr(self, '_m_format_info') else None

            self._m_format_info = GtImage.Imag.FormatInfo(self.format, self._io, self, self._root)
            return self._m_format_info if hasattr(self, '_m_format_info') else None



