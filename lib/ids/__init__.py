#datachef.ids

import hashlib
import base64
import zlib
import struct


def create_slug(title, plain_len=None):
    '''
    Tries to create a slug from a title, trading off collision risk with readability and minimized cruft

    plain_len - the maximum charcter length preserved (from the beginning) of the title

    >>> create_slug(u"The quick brown fox jumps over the lazy dog")
    2g_cWw
    '''
    #Useful discussion of techniques here: http://stackoverflow.com/questions/1303021/shortest-hash-in-python-to-name-cache-files

    #raw_hash = hashlib.md5(title).digest() #Abandoned idea of using MD5 and truncating
    raw_hash = struct.pack('I', zlib.adler32(title))
    slug = base64.urlsafe_b64encode(raw_hash).rstrip("=")
    return slug

