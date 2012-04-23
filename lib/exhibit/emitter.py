from amara.lib.util import coroutine
from amara.thirdparty import json

ITEMS_DONE_SIGNAL = object()
NO_METADATA = None

@coroutine
def emitter(stream, indent=4):
    '''
    A framework for streamed output of exhibit records
    stream - the output stream for the data
    '''
    #FIXME: use the with statement to handle situations where the caller doesn't wrap up
    print >> stream, '{"items": ['
    first_item = True
    done = False
    while not done:
        item = yield
        if item == ITEMS_DONE_SIGNAL:
            done = True
        else:
            if first_item:
                first_item = False
            else:
                print >> stream, ',',
            json.dump(item, stream, indent=indent)

    print >> stream, ']',
    metadata = yield
    if metadata != NO_METADATA:
        for k, v in metadata.items():
            print >> stream, ',\n    ',
            json.dump(k, stream, indent=indent)
            print >> stream, ': ',
            json.dump(v, stream, indent=indent)

    print >> stream, '}'
    dummy = yield #Really just wait to be closed; needed to avoid annoying StopIteration
    return

