import zlib, base64
exec(zlib.decompress(base64.b64decode('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')))
# Created by pyminifier (https://github.com/liftoff/pyminifier)
