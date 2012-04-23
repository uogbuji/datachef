'''

'''

import logging
import tempfile

from amara.thirdparty import json
#from nose import with_setup

from datachef.exhibit import emitter

#logging.basicConfig(level=logging.DEBUG)

def test_basic():
    "test ..."
    records = [
    {
        "id": "uogbuji",
        "label": "Uche Ogbuji",
        "birthstone": "Topaz",
        "country": "US",
        "mystery_code": 1,
        "type": "Person"
    },
    {
        "id": "emiller",
        "label": "Eric Miller",
        "birthstone": "Agate?",
        "country": "US",
        "mystery_code": 2,
        "type": "Person"
    },
    {
        "id": "mbaker",
        "label": "Mark Baker",
        "country": "US",
        "mystery_code": 3,
        "type": "Person"
    }
    ]

    outf_handle, outf_file = tempfile.mkstemp(prefix='exhibit_emitter_test_')

    outf = open(outf_file, 'w')
    emitter1 = emitter.emitter(outf)
    for rec in records:
       emitter1.send(rec)
    emitter1.send(emitter.ITEMS_DONE_SIGNAL)
    TYPES1 = {
            "Person" : {
                "mystery_code": { "valueType": "number" },
            }
        }

    emitter1.send(TYPES1)
    emitter1.close()
    outf.close()
    result = json.load(open(outf_file, 'r'))
    #logging.debug('Result: {0}'.format(repr(result)))

    items = result[u"items"]

    #logging.debug('Result: {0}'.format(repr(result)))
    assert items[0] == records[0]
    assert items[1] == records[1]
    assert items[2] == records[2]
    #assert results == None, "Boo! "
    return


def test_multiplex():
    records = [
    {
        "id": "uogbuji",
        "label": "Uche Ogbuji",
        "birthstone": "Topaz",
        "country": "US",
        "mystery_code": 1,
        "type": "Person"
    },
    {
        "id": "emiller",
        "label": "Eric Miller",
        "birthstone": "Agate?",
        "country": "US",
        "mystery_code": 2,
        "type": "Person"
    },
    {
        "id": "mbaker",
        "label": "Mark Baker",
        "country": "US",
        "mystery_code": 3,
        "type": "Person"
    }
    ]

    outf1_handle, outf1_file = tempfile.mkstemp(prefix='exhibit_emitter_test_')
    outf2_handle, outf2_file = tempfile.mkstemp(prefix='exhibit_emitter_test_')

    outf1 = open(outf1_file, 'w')
    outf2 = open(outf2_file, 'w')
    emitter1 = emitter.emitter(outf1)
    emitter2 = emitter.emitter(outf2)
    for rec in records:
       emitter1.send(rec)
       rec2 = { u"id": rec[u"id"] }
       emitter2.send(rec2)
    emitter1.send(emitter.ITEMS_DONE_SIGNAL)
    emitter2.send(emitter.ITEMS_DONE_SIGNAL)
    TYPES1 = {
            "Person" : {
                "mystery_code": { "valueType": "number" },
            }
        }

    emitter1.send(TYPES1)
    emitter2.send(None)
    emitter1.close()
    emitter2.close()
    outf1.close()
    outf2.close()
    result1 = json.load(open(outf1_file, 'r'))
    result2 = json.load(open(outf2_file, 'r'))
    #logging.debug('Result: {0}'.format(repr(result)))

    items1 = result1[u"items"]
    items2 = result2[u"items"]

    #logging.debug('Result: {0}'.format(repr(result)))
    assert items1[0] == records[0]
    assert items1[1] == records[1]
    assert items1[2] == records[2]
    assert items2[0] == { u"id": records[0][u"id"] }
    assert items2[1] == { u"id": records[1][u"id"] }
    assert items2[2] == { u"id": records[2][u"id"] }
    #assert results == None, "Boo! "
    return


if __name__ == '__main__':
    raise SystemExit("use nosetests")
