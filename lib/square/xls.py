import sys
import mmap
import xlrd #http://pypi.python.org/pypi/xlrd
try:
    from openpyxl.reader.excel import load_workbook
     #http://pypi.python.org/pypi/openpyxl/
    OPENPYCL_PRESENT = True
except ImportError:
    OPENPYCL_PRESENT = False

def dict_from_xls_sheet(f, sheet=0, header_row=0, start_row=-1):
    '''
    >>> from datachef.square import dict_from_xls_sheet
    >>> with open('spam.xlsx') as f:
    >>> with open('spam.xlsx') as f:
    ...     d = dict_from_xls(f)
    '''
    if start_row == -1: start_row = header_row + 1

    data = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
    book = xlrd.open_workbook(file_contents=data)
    if isinstance(sheet, int):
        sheet = book.sheet_by_index(sheet)
    else:
        sheet = book.sheet_by_name(str(sheet))

    def item(i, j):
        return (sheet.cell_value(header_row, j), sheet.cell_value(i, j))

    book.release_resources()
    resultgen = ( dict(item(i, j) for j in range(sheet.ncols)) \
                 for i in range(start_row, sheet.nrows) )

    return resultgen


def dict_from_xls(f, header_row=0, start_row=-1):
    '''
    >>> from datachef.square import dict_from_xls
    >>> sheets = dict_from_xls(open('test/resource/most-borrowed-uk-books.xlsx'), 1)
    >>> sheets.keys()
    dict_keys(['AUTHORS', 'BOOKS'])
    >>> books = sheets['BOOKS']
    >>> book = next(books)
    >>> book.keys()
    dict_keys(['Lending band (Min loans, 2009-10)', 'Author', 'Genre - Adultdult, Childrenhildren', 'ORDER'])
    '''
    if start_row == -1: start_row = header_row + 1

    data = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
    book = xlrd.open_workbook(file_contents=data)

    sheet_names = book.sheet_names()

    resultgen = {}
    for sname in sheet_names:
        sheet = book.sheet_by_name(sname)
        #FWIW could also set scope by using functools.partial
        def sheetgen(sheet=sheet):
            nrows = sheet.nrows
            ncols = sheet.ncols
            for i in range(start_row, nrows):
                yield dict( (sheet.cell_value(header_row, j), sheet.cell_value(i, j))
                            for j in range(ncols) )

        resultgen[sname] = sheetgen()

    book.release_resources()

    return resultgen


def xlsx2csv(fname, outf):
    if not OPENPYCL_PRESENT:
        raise ImportError('openpyxl required (pip install openpyxl)')
    wb = load_workbook(fname)
    for sheet in wb.worksheets:
        for row in sheet.rows:
            values=[]
            for cell in row:
                value=cell.value
                if value is None:
                    value=''
                if not isinstance(value, unicode):
                    value=unicode(value)
                value=value.encode('utf8')
                values.append(value)
            #FIXME: Replace with csv module output
            outf.write('\t'.join(values))
            outf.write('\n')
        outf.close()
    return


if __name__=='__main__':
    #filename=sys.argv[1]
    #csv_file='%s.csv' % sheet.title
    #print 'Creating %s' % csv_file
    #fd=open(csv_file, 'wt')
    main()
