from util.cell import Cell


def check_existance(cells, cell):
    for c in cells:
        if c.hash_value == cell.hash_value:
            return True

    return False
