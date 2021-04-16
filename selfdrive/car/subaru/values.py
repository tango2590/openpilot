# flake8: noqa

from selfdrive.car import dbc_dict
from cereal import car
Ecu = car.CarParams.Ecu

class CarControllerParams:
  STEER_MAX = 2047              # max_steer 4095
  STEER_STEP = 2                # how often we update the steer cmd
  STEER_DELTA_UP = 50           # torque increase per refresh, 0.8s to max
  STEER_DELTA_DOWN = 70         # torque decrease per refresh
  STEER_DRIVER_ALLOWANCE = 60   # allowed driver torque before start limiting
  STEER_DRIVER_MULTIPLIER = 10  # weight driver torque heavily
  STEER_DRIVER_FACTOR = 1       # from dbc

class CAR:
  ASCENT = "SUBARU ASCENT LIMITED 2019"
  IMPREZA = "SUBARU IMPREZA LIMITED 2019"
  FORESTER = "SUBARU FORESTER 2019"
  FORESTER_HYBRID = "SUBARU FORESTER HYBRID 2020"
  FORESTER_PREGLOBAL = "SUBARU FORESTER 2017 - 2018"
  LEGACY_PREGLOBAL = "SUBARU LEGACY 2015 - 2018"
  OUTBACK = "SUBARU OUTBACK 2020"
  OUTBACK_PREGLOBAL = "SUBARU OUTBACK 2015 - 2017"
  OUTBACK_PREGLOBAL_2018 = "SUBARU OUTBACK 2018 - 2019"

FINGERPRINTS = {
  CAR.OUTBACK: [{
  # OUTBACK 2020 2.5i (KingChalupa)
    2: 8, 64: 8, 72: 8, 272: 8, 273: 8, 274: 8, 280: 8, 281: 8, 282: 8, 289: 8, 290: 8, 312: 8, 313: 8, 372: 8, 552: 8, 554: 8, 801: 8, 802: 8, 803: 8, 805: 8, 808: 8, 811: 8, 912: 8, 915: 8, 940: 8, 941: 8, 1350: 8, 1361: 8, 1617: 8, 1632: 8, 1677: 8, 1713: 8, 1723: 8
  }],
}

# Use only FPv2
IGNORED_FINGERPRINTS = [CAR.IMPREZA, CAR.ASCENT, CAR.FORESTER, CAR.FORESTER_HYBRID]

FW_VERSIONS = {
  CAR.ASCENT: {
    # 2019 Ascent - UDM / @Adminiuga
    # 2019 Ascent - UDM / @tvo
    # Ecu, addr, subaddr: ROM ID
    (Ecu.esp, 0x7b0, None): [
      b'\xa5 \x19\x02\x00',
    ],
    (Ecu.eps, 0x746, None): [
      b'\x85\xc0\xd0\x00',
    ],
    (Ecu.fwdCamera, 0x787, None): [
      b'\x00\x00d\xb9\x1f@ \x10',
    ],
    (Ecu.engine, 0x7e0, None): [
      b'\xbb,\xa0t\a',
      b'\xf1\x82\xbb,\xa0t\x87',
    ],
    (Ecu.transmission, 0x7e1, None): [
      b'\x00\xfe\xf7\x00\x00',
    ],
  },
  CAR.FORESTER_HYBRID: {
    # 2020 Forester Hybrid - UDM / @jaypray
    # Ecu, addr, subaddr: ROM ID
    (Ecu.esp, 0x7b0, None): [
      b'\xa3 \x19\x14\x00',
    ],
    (Ecu.eps, 0x746, None): [
      b'\x8d\xc0\x04\x00',
    ],
    (Ecu.fwdCamera, 0x787, None): [
      b'\x00\x00e`\x1f@  ',
    ],
    (Ecu.engine, 0x7e0, None): [
      b'\xcb"`p\x07',
    ],
    (Ecu.transmission, 0x7e1, None): [
      b'\x1a\xf6F`\x00',
    ],
  },
  CAR.IMPREZA: {
    # 2018 Crosstrek - EDM / @martinl
    # 2018 Impreza - ADM / @Michael
    # 2019 Impreza Premium - UDM / @hitoryu2001
    # 2018 Crosstrek Limited - UDM / @Joey
    # 2017 Impreza - UDM / @Frye
    # 2018 Crosstrek - UDM / @rwalsh3
    # 2018 Crosstrek - UDM / @pemerick07
    # 2018 Crosstrek - UDM / @rwalsh3 (new engine fw)
    # 2019 Crosstrek - UDM / @Nooks Cranny
    # 2019 Impreza - UDM / @cheesypotato
    # 2019 Impreza - UDM / @dbzx6r
    # 2018 Impreza Sport - UDM / @gking
    # Ecu, addr, subaddr: ROM ID
    (Ecu.esp, 0x7b0, None): [
      b'\x7a\x94\x3f\x90\x00',
      b'\xa2 \x185\x00',
      b'\xa2 \x193\x00',
      b'z\x94.\x90\x00',
      b'z\x94\b\x90\x01',
      b'\xa2 \x19`\x00',
      b'z\x94\f\x90\001',
    ],
    (Ecu.eps, 0x746, None): [
      b'\x7a\xc0\x0c\x00',
      b'z\xc0\b\x00',
      b'\x8a\xc0\x00\x00',
      b'z\xc0\x04\x00',
      b'z\xc0\x00\x00',
      b'\x8a\xc0\x10\x00',
    ],
    (Ecu.fwdCamera, 0x787, None): [
      b'\x00\x00d\xb5\x1f@ \x0e',
      b'\x00\x00d\xdc\x1f@ \x0e',
      b'\x00\x00e\x1c\x1f@ \x14',
      b'\x00\x00d)\x1f@ \a',
      b'\x00\x00e+\x1f@ \x14',
      b'\000\000e+\000\000\000\000',
      b'\000\000dd\037@ \016',
    ],
    (Ecu.engine, 0x7e0, None): [
      b'\xaa\x61\x66\x73\x07',
      b'\xbeacr\a',
      b'\xc5!`r\a',
      b'\xaa!ds\a',
      b'\xaa!`u\a',
      b'\xaa!dq\a',
      b'\xaa!dt\a',
      b'\xc5!dr\a',
      b'\xc5!ar\a',
      b'\xbe!as\a',
    ],
    (Ecu.transmission, 0x7e1, None): [
      b'\xe3\xe5\x46\x31\x00',
      b'\xe4\xe5\x061\x00',
      b'\xe5\xf5\x04\x00\x00',
      b'\xe3\xf5G\x00\x00',
      b'\xe3\xf5\a\x00\x00',
      b'\xe3\xf5C\x00\x00',
      b'\xe5\xf5B\x00\x00',
      b'\xe5\xf5$\000\000',
      b'\xe4\xf5\a\000\000',
    ],
  },
  CAR.FORESTER_PREGLOBAL: {
    # 2018 Subaru Forester 2.5i Touring - UDM / @Oreo
    # 2018 Subaru Forester 2.5 Limited - Canada / @litobro
    # 2017 Subaru Forester UDM / @hitoryu2001
    # Ecu, addr, subaddr: ROM ID
    (Ecu.esp, 0x7b0, None): [
      b'\x7d\x97\x14\x40',
    ],
    (Ecu.eps, 0x746, None): [
      b'}\xc0\x10\x00',
      b'm\xc0\x10\x00',
    ],
    (Ecu.fwdCamera, 0x787, None): [
      b'\x00\x00\x64\x35\x1f\x40\x20\x09',
      b'\x00\x00c\xe9\x1f@ \x03',
    ],
    (Ecu.engine, 0x7e0, None): [
      b'\xba"@p\a',
      b'\xa7)\xa0q\a',
    ],
    (Ecu.transmission, 0x7e1, None): [
      b'\xdc\xf2\x60\x60\x00',
      b'\xdc\xf2@`\x00',
      b'\xda\xfd\xe0\x80\x00',
    ],
  },
  CAR.LEGACY_PREGLOBAL: {
    # 2018 Subaru Legacy 2.5i Premium - UDM / @kram322
    # 2016 Subaru Legacy - UDM / @nort
    # 2015 Subaru Legacy 3.6R Limited / @chrissantamaria
    # 2017 Subaru Legacy 2.5i Sport / @bonnysonnyandclyde
    # Ecu, addr, subaddr: ROM ID
    (Ecu.esp, 0x7b0, None): [
      b'\x8b\x97D\x00',
      b'k\x97D\x00',
      b'[\xba\xc4\x03',
      b'{\x97D\x00',
    ],
    (Ecu.eps, 0x746, None): [
      b'{\xb0\x00\x00',
      b'[\xb0\x00\x01',
      b'K\xb0\x00\x01',
      b'k\xb0\x00\x00',
    ],
    (Ecu.fwdCamera, 0x787, None): [
      b'\x00\x00df\x1f@ \n',
      b'\x00\x00c\xb7\x1f@\x10\x16',
      b'\x00\x00c\x94\x1f@\x10\x08',
      b'\x00\x00c\xec\x1f@ \x04',
    ],
    (Ecu.engine, 0x7e0, None): [
      b'\xb5\"@p\a',
      b'\xab*@r\a',
      b'\xa0+@p\x07',
      b'\xb4"@0\x07',
    ],
    (Ecu.transmission, 0x7e1, None): [
      b'\xbc\xf2\x00\x81\x00',
      b'\xbe\xf2\x00p\x00',
      b'\xbf\xfb\xc0\x80\x00',
      b'\xbd\xf2\x00`\x00',
    ],
  },
  CAR.OUTBACK: {
    # 2020 Outback Hybrid - UDM / @KingChalupa
    # 2020 Outback 2.5i Premium - UDM / @ursubpar
    # Ecu, addr, subaddr: ROM ID
    (Ecu.esp, 0x7b0, None): [
      b'\xa1  \x06\x01',
      b'\xa1  \a\x00',
    ],
    (Ecu.eps, 0x746, None): [
      b'\x9b\xc0\x10\x00',
    ],
    (Ecu.fwdCamera, 0x787, None): [
      b'\x00\x00eJ\x00\x1f@ \x19\x00',
    ],
    (Ecu.engine, 0x7e0, None): [
      b'\xbc,\xa0q\x07',
      b'\xbc\"`@\a',
    ],
    (Ecu.transmission, 0x7e1, None): [
      b'\xa5\xfe\xf7@\x00',
      b'\xa5\xf6D@\x00',
    ],
  },
  CAR.OUTBACK_PREGLOBAL: {
    # 2017 Outback Limited 3.6r - UDM / @Anthony
    # 2016 Outback Limited 2.5 - UDM / @aeiro
    # 2015 Outback Limited 2.5 - ADM / @Bugsy
    # 2015 Outback Premium 3.6i - UDM / @aidrive
    # 2016 Outback Premium 2.5 - UDM / @Troy
    # 2017 Subaru Outback 2.5 - UDM / @chewbaru
    # 2017 Subaru Outback - UDM / @the3seashells
    # 2016 Outback Premium 2.5i - UDM / @G-Wood
    # Ecu, addr, subaddr: ROM ID
    (Ecu.esp, 0x7b0, None): [
      b'{\x9a\xac\x00',
      b'k\x97\xac\x00',
      b'\x5b\xf7\xbc\x03',
      b'[\xf7\xac\x03',
      b'{\x97\xac\x00',
    ],
    (Ecu.eps, 0x746, None): [
      b'k\xb0\x00\x00',
      b'[\xb0\x00\x00',
      b'\x4b\xb0\x00\x02',
      b'K\xb0\x00\x00',
      b'{\xb0\x00\x01',
    ],
    (Ecu.fwdCamera, 0x787, None): [
      b'\x00\x00c\xec\x1f@ \x04',
      b'\x00\x00c\xd1\x1f@\x10\x17',
      b'\xf1\x00\xf0\xe0\x0e',
      b'\x00\x00c\x94\x00\x00\x00\x00',
      b'\x00\x00c\x94\x1f@\x10\b',
      b'\x00\x00c\xb7\x1f@\x10\x16',
    ],
    (Ecu.engine, 0x7e0, None): [
      b'\xb4+@p\a',
      b'\xab\"@@\a',
      b'\xa0\x62\x41\x71\x07',
      b'\xa0*@q\a',
      b'\xab*@@\a',
      b'\xb4"@0\a',
      b'\xb4"@p\a',
      b'\xab"@s\a',
    ],
    (Ecu.transmission, 0x7e1, None): [
      b'\xbd\xfb\xe0\x80\x00',
      b'\xbe\xf2@\x80\x00',
      b'\xbf\xe2\x40\x80\x00',
      b'\xbf\xf2@\x80\x00',
      b'\xbe\xf2@p\x00',
      b'\xbd\xf2@`\x00',
      b'\xbd\xf2@\x81\000',
    ],
  },
  # Outback with reversed driver torque signal
  CAR.OUTBACK_PREGLOBAL_2018: {
    # 2018 Outback Premium 2.5i - UDM / @zhoux260
    # 2018 Outback 3.6r UDM / @mirroregami
    # 2018 Outback 2.5i Premium UDM / @dirkmm
    # 2019 Outback UDM / @Valhalla
    # 2018 Outback 2.5 / @haak
    # 2018 Outback 3.6r USDM / @Scripty_
    # 2018 Subaru Outback 2.0d - ADM / @Richo
    # 2019 Outback 2.5i Premium / @Z-dawg Swizzlepants
    # Ecu, addr, subaddr: ROM ID
    (Ecu.esp, 0x7b0, None): [
      b'\x8b\x97\xac\x00',
      b'\x8b\x9a\xac\x00',
      b'\x9b\x97\xac\x00',
      b'\x8b\x97\xbc\x00',
      b'\x8b\x99\xac\x00',
    ],
    (Ecu.eps, 0x746, None): [
      b'{\xb0\x00\x00',
      b'{\xb0\x00\x01',
    ],
    (Ecu.fwdCamera, 0x787, None): [
      b'\x00\x00df\x1f@ \n',
      b'\x00\x00d\xfe\x1f@ \x15',
      b'\x00\x00d\x95\x00\x00\x00\x00',
      b'\x00\x00d\x95\x1f@ \x0f',
      b'\x00\x00d\xfe\x00\x00\x00\x00',
    ],
    (Ecu.engine, 0x7e0, None): [
      b'\xb5"@p\a',
      b'\xb5+@@\a',
      b'\xb5"@P\a',
      b'\xc4"@0\a',
      b'\xb5b@1\x07',
      b'\xb5q\xe0@\a',
    ],
    (Ecu.transmission, 0x7e1, None): [
      b'\xbc\xf2@\x81\x00',
      b'\xbc\xfb\xe0\x80\x00',
      b'\xbc\xf2@\x80\x00',
      b'\xbb\xf2@`\x00',
      b'\xbc\xe2@\x80\x00',
      b'\xbc\xfb\xe0`\x00',
      b'\xbc\xaf\xe0`\x00',
    ],
  },
}


STEER_THRESHOLD = {
  CAR.ASCENT: 80,
  CAR.IMPREZA: 80,
  CAR.FORESTER: 80,
  CAR.FORESTER_HYBRID: 80,
  CAR.OUTBACK: 80,
  CAR.FORESTER_PREGLOBAL: 75,
  CAR.LEGACY_PREGLOBAL: 75,
  CAR.OUTBACK_PREGLOBAL: 75,
  CAR.OUTBACK_PREGLOBAL_2018: 75,
}

DBC = {
  CAR.ASCENT: dbc_dict('subaru_global_2017_generated', None),
  CAR.IMPREZA: dbc_dict('subaru_global_2017_generated', None),
  CAR.FORESTER: dbc_dict('subaru_global_2017_generated', None),
  CAR.FORESTER_HYBRID: dbc_dict('subaru_global_2020_hybrid_generated', None),
  CAR.FORESTER_PREGLOBAL: dbc_dict('subaru_forester_2017_generated', None),
  CAR.LEGACY_PREGLOBAL: dbc_dict('subaru_outback_2015_generated', None),
  CAR.OUTBACK: dbc_dict('subaru_global_2017_generated', None),
  CAR.OUTBACK_PREGLOBAL: dbc_dict('subaru_outback_2015_generated', None),
  CAR.OUTBACK_PREGLOBAL_2018: dbc_dict('subaru_outback_2019_generated', None),
}

PREGLOBAL_CARS = [CAR.FORESTER_PREGLOBAL, CAR.LEGACY_PREGLOBAL, CAR.OUTBACK_PREGLOBAL, CAR.OUTBACK_PREGLOBAL_2018]
#SUBARU_WMI = ['JF1', 'JF2', '4S3', '4S4']
