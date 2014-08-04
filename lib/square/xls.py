import sys
import xlrd #http://pypi.python.org/pypi/xlrd
from openpyxl.reader.excel import load_workbook #http://pypi.python.org/pypi/openpyxl/


def dict_from_xls(f, sheet_index=0, start_row=1):
    import mmap
    data = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
    book = xlrd.open_workbook(file_contents=data)
    sheet = book.sheet_by_index(sheet_index)

    def item(i, j):
        return (sheet.cell_value(0, j), sheet.cell_value(i, j))

    return ( dict(item(i, j) for j in range(sheet.ncols)) \
                 for i in xrange(start_row, sheet.nrows) )


def xlsx2csv(fname, outf):
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
