_state={'projector':{'power':'STANDBY','input':'HDMI1'},'text':'Sistema pronto'}

def set_public_state(d): _state.update(d)

def get_public_state(): return _state.copy()
