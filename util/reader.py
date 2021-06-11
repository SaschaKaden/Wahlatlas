from util.cell import Cell


def create_cell(lon, lat, bt, extra):
    cell = Cell(lon, lat)
    if bt is None or extra is None:
        return cell

    try:
        bt_json = bt.json()
        cell.gru_bt = bt_json['p_zs_gru_percent']
        pixel = bt_json['wahlberechtigte']
        if pixel is not None:
            cell.pixel = pixel

        extra_json = extra.json()
        sinus = extra_json['sinus'][0].get('sinus_sn')
        if sinus is not None:
            cell.sinus = sinus
        potential = extra_json['pot_21'][0].get('bt_21_potential')
        if potential is not None:
            cell.potential = potential
        potential_scale = extra_json['pot_21'][0].get('bt_21_pot_scale')
        if potential_scale is not None:
            cell.potential_scale = potential_scale
        potential_scale_wk = extra_json['pot_21'][0].get('bt_21_pot_scale_wk')
        if potential_scale_wk is not None:
            cell.potential_scale = potential_scale_wk
    except:
        pass
    return cell


