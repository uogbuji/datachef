#datachef.squaredata

def dict_from_xls(f, sheet_index=0, start_row=1):
    '''
    >>> from datachef.squaredata import dict_from_xls
    >>> with open('spam.xlsx') as f:
    >>> with open('spam.xlsx') as f:
    ...     d = dict_from_xls(f)
    
    '''
    import mmap
    import xlrd # pip install xlrd
    data = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
    book = xlrd.open_workbook(file_contents=data)
    sheet = book.sheet_by_index(sheet_index)

    def item(i, j):
        return (sheet.cell_value(0, j), sheet.cell_value(i, j))

    return ( dict(item(i, j) for j in range(sheet.ncols)) \
                 for i in range(start_row, sheet.nrows) )


