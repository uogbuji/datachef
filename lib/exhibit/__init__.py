#datachef.exhibit

#Also useful: RhinoShell  http://www.mozilla.org/rhino/  /  https://developer.mozilla.org/en/Rhino_Shell

import re

EJSON_ID_CHARS = r'a-zA-Z0-9\-\_'
EJSON_ID_PAT = re.compile('[^%s]'%EJSON_ID_CHARS)
fixup_id = lambda t: EJSON_ID_PAT.sub('_', t.strip())#.lower()


def fixup(ejson, legend=None):
    legend = legend or {}
    fixup_keys(ejson)
    for k, val in ejson.items():
        if not val: del ejson[k]
    return


def fixup_keys(ejson, legend=None):
    legend = legend or {}
    #Cannot use for k in ejson because we're mutating as we go
    for k in ejson.keys():
        new_k = fixup_id(k)
        if k != new_k:
            #Avoid collisions 
            while new_k in legend:
                if legend[new_k] != k:
                    new_k += '_'
            ejson[new_k] = ejson[k]
            del ejson[k]
    return

