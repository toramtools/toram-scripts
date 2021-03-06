# pylint: skip-file
from Build_Playground import target
from Data import *
import sys
sys.path.append("../data")


skill1 = ddict({
    'constant': lambda s: 300,
    'multiplier': lambda s: 1*(4+(s['total str']+s['total dex']+s['total agi'])*0.2/100),
    'resistance': 'pres%',
    'defense': 'def',
    'distance': 'srd%',
    'unsheathe': 'not_unsheathe',
    'crit': True,
    'others': 1.1*1.2,
    'combo': 1.5,
    'proration': 2.5
})

skills = [skill1]

character_base = ddict({
    'main': ddict({
        #'type': '2h sword',
        #'base attack': 2,
        #'base stability': 100,
        #'refine': 0,
        #'cd+': 99
    }),
    'sub': ddict({
        'type': '1h sword',
        'base attack': 380,
        'base stability': 80,
        'refine': 15
    }),
    'light armor': ddict({
        'aspd%': 50
    }),
    'food': ddict({
        'str+': 30,
        'cr+': 30,
        'mp': 1000+100,
        'ampr+': 30,
        'dte%': 11
    }),
    'masteries': ddict({
        'watk%': 30,
        'atk%': 3,
        'aspd+': 500,
        'cr%': 10,
        'agi+': 15,
        'unsheathe%': 25
    }),
    'quick slash': ddict({
        'aspd+': 50,
        'aspd%': 50
    }),
    'battle skills': ddict({
        'atk+': 116,
        'cd%': 5,
        'cr+': 5
    }),
    'registlet': ddict({
        'atk+': 30,
        'mp': 100,
        'hp+': 1000,
        'aspd+': 100
    }),
    'bushido': ddict({
        'mp': 50,
        'hp+': 50
    }),
    'warcry': ddict({
        'atk%': 10
    }),
    'consumables': ddict({
        'dte%': 5,
        'mp': 300,
        'aspd+': 100
    }),
    'flash blast': ddict({
        'main watk%': 25
    }),
    'brave aura': ddict({
        'main watk%': 30
    }),
    'quick aura': ddict({
        'aspd+': 500,
        'aspd%': 25
    }),
    'gsw': ddict({
        'motion%': 30,
        'aspd+': 900
    }),
    'matching ele': ddict({
        'dte%': 25
    }),
    'kakiri': ddict({
        'atk+': 100
    })
})

STR_OHS = UPDATE_STATS(OHS_ASCDCDCR_SCD, {'cd+': 21})
AGI_OHS = UPDATE_STATS(OHS_ASCDCDCR_SCD, {'atk%': 10, 'agi%': 5, 'cd%': 10, 'cd+': 21, 'str%': 0})
CDS_OHS = UPDATE_STATS(STR_OHS, {'str%': 5, 'atk%': 10, 'cd%': 10})

CLASSIC_ARMOR = UPDATE_STATS(ARMOR_ACDCDCR, {'atk%': 11, 'cd+': 21})
NEWEST_ARMOR = UPDATE_STATS(ARMOR_ASCDCR, {'cd+': 21, 'atk%': 11})

DTE = ddict({
    'type': '1h sword',
    'base attack': 390,
    'base stability': 80,
    'refine': 15,
    'dte%': 21,
    'atk%': 10,
    'str%': 5,
    'cd+': 21,
    'cr+': 24
})

items = ddict({
    'base stats': [BASE_STATS('str', 'agi')],
    'main': [OHS_PCR, OHS_QUEEN_BEE, OHS_ASCDCDCR_SCD],
    'armor': [ARMOR_DTESCDCR, ARMOR_DTECDCDCR],
    'add': [ADD_XMAS_TREE, ADD_KITTY_TAIL],
    'ring': [RING_GLOWING_SEA_TALISMAN, RING_HALLUCINATION_SPORE],
    'avatar 1': [AVATAR_ACC_SRD, AVATAR_ACC_PP_AMPR],
    'avatar 2': [AVATAR_TOP_SRD, AVATAR_TOP_PPIERCE],
    'avatar 3': [AVATAR_BOT_SRD, AVATAR_BOT_PPIERCE],
    'attack buff': [POTION_PEN_OIL],
    'berserk': [SKILL_ACTIVE_BERSERK_OHS, ddict({})]
    #'cp': [ddict({'atk%': 10, 'aspd%': 100})]
})

xtals = ddict({
    'main xtal': {'choices': [XTAL_W_HEXTER, XTAL_W_DEVIL_DANGO, XTAL_W_VLAM], 'slots': 2},
    'armor xtal': {'choices': [XTAL_ARM_DOC_POM, XTAL_ARM_DX_FIGHTER, XTAL_ARM_YUVERIA, XTAL_ARM_ARACHNIDEMON, XTAL_ANY_BLACK_SHADOW], 'slots': 2},
    'add xtal': {'choices': [XTAL_ADD_ROYAL_OX_KING, XTAL_ADD_JUNIOR, XTAL_ADD_DARK_LORD, XTAL_ADD_ALFENIX], 'slots': 2},
    'ring xtal': {'choices': [XTAL_ANY_BLACK_SHADOW, XTAL_ANY_GRAVICEP, XTAL_ANY_AGELADANIOS], 'slots': 2},
    #'food choice': {'choices': [ddict({'str+': 30}), ddict({'agi+': 30})], 'slots': 1}
})
