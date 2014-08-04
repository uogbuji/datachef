from amara3.util import coroutine
import json

ITEMS_DONE_SIGNAL = object()
NO_METADATA = None

@coroutine
def emitter(stream, indent=4, encoding='utf-8'):
    '''
    A framework for streamed output of exhibit records
    stream - the output stream for the data
    '''
    #FIXME: use the with statement to handle situations where the caller doesn't wrap up
    print('{"items": [', file=stream)
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
                print(', ', file=stream, end='')
            json.dump(item, stream, indent=indent)

    print(']', file=stream, end='')
    metadata = yield
    if metadata != NO_METADATA:
        for k, v in metadata.items():
            print(',\n    ', file=stream, end='')
            json.dump(k, stream, indent=indent)
            print(': ', file=stream, end='')
            json.dump(v, stream, indent=indent)

    print('}', file=stream)
    yield #Really just wait to be closed. Avoids StopIteration

