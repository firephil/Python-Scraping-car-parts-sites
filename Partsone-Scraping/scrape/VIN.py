import vinlib


def info(vin):
    v = vinlib.Vin(vin)

    # print(v)

    print(v._wmidata)

    '''
    v.manufacturer
    v.wmi
    v.vds
    v.vis
    v.vsn'''
