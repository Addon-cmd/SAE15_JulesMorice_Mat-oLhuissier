import parkings_velos
import time
def main(duree,periode):
    nbrboucles=duree/periode
    for i in range(int(nbrboucles)):
        parkings_velos.parking('FR_MTP_GAMB','voiture')
        parkings_velos.velo('velo')
        time.sleep(periode)
main(28800,1800)
