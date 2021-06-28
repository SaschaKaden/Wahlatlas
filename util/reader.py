from util.cell import Cell


def create_cell(lon, lat, bt, extra):
    cell = Cell(lon, lat)
    if bt is None or extra is None:
        return cell

    try:
        bt_json = bt.json()
        cell.gru_bt = bt_json['p_zs_gru_percent']
        cell.pixel = bt_json['wahlberechtigte']
        cell.id = bt_json['id']

        extra_json = extra.json()
        sinus = extra_json['sinus'][0].get('sinus_sn')
        if sinus is not None:
            cell.sinus = sinus
        potential_scale_wk = extra_json['pot_21'][0].get('bt_21_pot_scale_wk')
        if potential_scale_wk is not None:
            cell.potential_scale_wk = potential_scale_wk
    except:
        pass
    return cell


