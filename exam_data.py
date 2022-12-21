
# Grame Negative Tests:
EMB = {
    'dark_with_green _metallic_sheen' : 'imeges/dark_with_green _metallic_sheen.jpg',
    'dark_colonies' : 'imeges/dark_colonies.jpg',
    'colorless_colonies' : 'imeges/colorless_colonies.jpg'
}
MACCONKEY_AGAR = {
    '+' : 'imeges/rose_pink_colonies.jpg',
    '-' : 'imeges/pale-yellow_colonies.jpg'
}
IMVIC_TEST = {
    '++--' : 'imeges/imvic++--.jpg',
    '-+-+' : 'imeges/imvic-+-+.jpg',
    '--++' : 'imeges/imvic--++.jpg',
    '-+--' : 'imeges/imvic-+--.jpg',
    '++-+' : 'imeges/imvic++-+.jpg',
}
TSI = {
    'A/A+CO2' : 'imeges/A|A+CO2.jpg',
    'K/A+H2S' : 'imeges/K|A+H2S.jpg',
    'K/A' : 'imeges/K|A.jpg',
    'K/K' : 'imeges/K|K.jpg'
}
MOTILITY_TEST = {
    'motile'     : 'imeges/motile.jpg',
    'non-motile' : 'imeges/non-motile.jpg'
}
UREASE_TEST = {
    '+' : 'imeges/urease_positive.jpg',
    '-' : 'imeges/urease_negative.jpg'   
}

# Grame Positive Tests:
CATALASE_TEST = {
    '+' : 'imeges/catalase_positive.jpg',
    '-' : 'imeges/catalase_negative.jpg'
}
COAGULASE_TEST = {
    '+' : 'imeges/coagulase_positive.jpg',
    '-' : 'imeges/coagulase_negative.jpg'
}
GELATINASE_TEST = {
    '+' : 'imeges/gelatinase_positive.jpg',
    '-' : 'imeges/gelatinase_negative.jpg'
}
BLOOD_AGAR = {
    'alpha': 'imeges/alpha_hemolytic.jpg',
    'beta' : 'imeges/beta_hemolytic.jpg',
    'gamma' : 'imeges/gamma_hemolytic.jpg',
}
NITRATE_REDUCTION_TEST = {
    '+' : 'imeges/nitrate_reduction_positive.jpg',
    '-' : 'imeges/nitrate_reduction_negative.jpg'
}
OXIDASE_TEST = {
    '+' : 'imeges/oxidase_positve.jpg',
    '-' : 'imeges/oxidase_negative.jpg'
}
NUTRIENT_AGAR = {
    # staph
    'golden_yellow_colonies' : 'imeges/golden_yellow_colonies.jpg',
    'lemon_yellow_colonies' : 'imeges/lemon_yellow_colonies.jpg',
    'whitish_colonies' : 'imeges/whitish_colonies.jpg',

    # serriea
    'brick_red_colonies' : 'imeges/brick_red_colonies.jpg',

    # gram postive
    'green_colonies' : 'imeges/green_colonies.jpg',
    'no_pigment' : 'imeges/no_pigment.jpg'
}
MANNITOL_TEST = {
    '+' : 'imeges/mannitol_fermentor.jpg',
    '-' : 'imeges/mannitol_non_fermentor.jpg'
}
BILE_SOLUBLITIY_TEST = {
    'soluble' : 'imeges/bile_soluble.jpg',
    'insoluble' : 'imeges/bile_insoluble.jpg'
}
OPTICHIN_SENSITIVITY_TEST = {
    'sensitive' : 'imeges/optichin_sensitive.jpg',
    'resistant' : 'imeges/optichin_resistant.jpg'
}
BACITRACIN_SENSITIVITY_TEST = {
    'sensitive' : 'imeges/bacitracin_sensitive.jpg',
    'resistant' : 'imeges/bacitracin_resistant.jpg'
}
PENICILLIN_SENSITIVITY_TEST = {
    'sensitive' : 'imeges/penicillin_sensitive.jpg',
    'resistant' : 'imeges/penicillin_resistant.jpg'
}
NaCl_SENSITIVE = {
    'sensitive' : 'imeges/NaCl_sensitive.jpg',
    'resistant' : 'imeges/NaCl_resistant.jpg'    
}


class GramPositive():
    def __init__(self, name, catalase_test=None, blood_agar=None, coagulase_test=None,
                    gelatinase_test=None, mannitol_test=None, nutrient_agar=None, 
                    nitrate_reduction_test=None, urease_test=None,bile_solublitiy_test=None,
                    optichin_sensitivity_test=None,bacitracin_sensitivity_test=None,
                    penicillin_sensitivity_test=None,NaCl_sensitive=None, is_Gram_postive=True,
                    is_staph=False, is_strepto=False, MacConkey_agar=None):
        self.__name = name
        self.__catalase_test = catalase_test
        self.__blood_agar = blood_agar
        self.__coagulase_test = coagulase_test
        self.__gelatinase_test = gelatinase_test
        self.__mannitol_test = mannitol_test
        self.__nutrient_agar = nutrient_agar
        self.__nitrate_reduction_test = nitrate_reduction_test
        self.__urease_test = urease_test
        self.__bile_solublitiy_test = bile_solublitiy_test
        self.__optichin_sensitivity_test = optichin_sensitivity_test
        self.__bacitracin_sensitivity_test = bacitracin_sensitivity_test
        self.__penicillin_sensitivity_test = penicillin_sensitivity_test
        self.__NaCl_sensitive = NaCl_sensitive
        self.is_Gram_postive = is_Gram_postive
        self.is_staph = is_staph
        self.is_strepto = is_strepto
        self.__MacConkey_agar = MacConkey_agar

    def get_name(self):
        return self.__name

    def get_catalase_test(self):
        return self.__catalase_test

    def get_blood_agar(self):
        return self.__blood_agar
        
    def get_coagulase_test(self):
        return self.__coagulase_test

    def get_gelatinase_test(self):
        return self.__gelatinase_test
    
    def get_mannitol_test(self):
        return self.__mannitol_test
        
    def get_nutrient_agar(self):
        return self.__nutrient_agar

    def get_nitrate_reduction_test(self):
        return self.__nitrate_reduction_test
        
    def get_urease_test(self):
        return self.__urease_test

    def get_bile_solublitiy_test(self):
        return self.__bile_solublitiy_test

    def get_optichin_sensitivity_test(self):
        return self.__optichin_sensitivity_test

    def get_bacitracin_sensitivity_test(self):
        return self.__bacitracin_sensitivity_test

    def get_penicillin_sensitivity_test(self):
        return self.__penicillin_sensitivity_test

    def get_NaCl_sensitive(self):
        return self.__NaCl_sensitive

    def get_MacConkey_agar(self):
        return self.__MacConkey_agar


class GramNegative():
    def __init__(self, name, MacConkey_agar=None, EMB=None, TSI=None, IMViC_test=None, 
                    motility_test=None, urease_test=None, 
                    O_F_test=None, oxidase_test=None, is_Gram_postive=False):

        self.__name = name
        self.__MacConkey_agar = MacConkey_agar
        self.__EMB = EMB
        self.__TSI = TSI
        self.__IMViC_test = IMViC_test
        self.__motility_test = motility_test
        self.__urease_test = urease_test
        self.__O_F_test = O_F_test
        self.__oxidase_test = oxidase_test
        self.is_Gram_postive = is_Gram_postive

    def get_name(self):
        return self.__name

    def get_MacConkey_agar(self):
        return self.__MacConkey_agar

    def get_EMB(self):
        return self.__EMB

    def get_TSI(self):
        return self.__TSI

    def get_IMViC_test(self):
        return self.__IMViC_test

    def get_motility_test(self):
        return self.__motility_test

    def get_urease_test(self):
        return self.__urease_test

    def get_O_F_test(self):
        return self.__O_F_test

    def get_oxidase_test(self):
        return self.__oxidase_test
          

####################### Gram Negative Bacteria #######################
# Lactose fermentor
E_Coli = GramNegative('E Coli', MACCONKEY_AGAR['+'], EMB['dark_with_green _metallic_sheen'], TSI['A/A+CO2'],IMVIC_TEST['++--'], MOTILITY_TEST['motile'])
Citrobacter = GramNegative('Citrobacter spp', MACCONKEY_AGAR['+'], EMB['dark_colonies'], TSI['A/A+CO2'], IMVIC_TEST['-+-+'], MOTILITY_TEST['motile'])
Klebsiella = GramNegative('Klebsilla pneumonia', MACCONKEY_AGAR['+'], EMB['dark_colonies'], TSI['A/A+CO2'], IMVIC_TEST['--++'], MOTILITY_TEST['non-motile'])
Enterobacter = GramNegative('Enterobacter spp', MACCONKEY_AGAR['+'], EMB['dark_colonies'], TSI['A/A+CO2'], IMVIC_TEST['--++'], MOTILITY_TEST['motile'])

# Lactose non fermentor
Shigella = GramNegative('Shigella', MACCONKEY_AGAR['-'], EMB['colorless_colonies'], TSI['K/A'], IMVIC_TEST['-+--'], MOTILITY_TEST['non-motile'], UREASE_TEST['-'])
Salmonella = GramNegative('Salmonella spp', MACCONKEY_AGAR['-'], EMB['colorless_colonies'], TSI['K/A+H2S'], IMVIC_TEST['-+-+'], MOTILITY_TEST['motile'], UREASE_TEST['-'])
Proteus = GramNegative('Proteus spp', MACCONKEY_AGAR['-'], EMB['colorless_colonies'], TSI['K/A+H2S'], IMVIC_TEST['++-+'], MOTILITY_TEST['motile'], UREASE_TEST['+'])
Serratia = GramNegative('Serratia', MACCONKEY_AGAR['-'], EMB['colorless_colonies'], TSI['K/A'], IMVIC_TEST['--++'], MOTILITY_TEST['motile'], UREASE_TEST['-'])



####################### Gram Negative Bacteria #######################
Staph_aureus = GramPositive('staph aureus', CATALASE_TEST['+'], BLOOD_AGAR['beta'], COAGULASE_TEST['+'],GELATINASE_TEST['+'], MANNITOL_TEST['+'], NUTRIENT_AGAR['golden_yellow_colonies'], is_staph=True)
Staph_epidermidis = GramPositive('staph epidermidis', CATALASE_TEST['+'], BLOOD_AGAR['gamma'], COAGULASE_TEST['-'],GELATINASE_TEST['-'], MANNITOL_TEST['-'], NUTRIENT_AGAR['whitish_colonies'], is_staph=True)
Staph_saprophyticus = GramPositive('staph saprophyticus', CATALASE_TEST['+'], BLOOD_AGAR['gamma'], COAGULASE_TEST['-'],GELATINASE_TEST['-'], MANNITOL_TEST['-'], NUTRIENT_AGAR['lemon_yellow_colonies'], is_staph=True)

Literia = GramPositive('Literia monocytogenes', CATALASE_TEST['+'], BLOOD_AGAR['beta'],nitrate_reduction_test=NITRATE_REDUCTION_TEST['-'], urease_test=UREASE_TEST['-'])

Bacillus = GramPositive('Bacillus spp', CATALASE_TEST['+'], BLOOD_AGAR['beta'],nitrate_reduction_test=NITRATE_REDUCTION_TEST['+'], urease_test=UREASE_TEST['-'], gelatinase_test=GELATINASE_TEST['+'])

Corynbacterium = GramPositive('Corynbacterium diphteria', CATALASE_TEST['+'], BLOOD_AGAR['gamma'], nitrate_reduction_test=NITRATE_REDUCTION_TEST['+'], urease_test=UREASE_TEST['+'])

strepto_pyogens = GramPositive('strepto pyogens', CATALASE_TEST['-'], BLOOD_AGAR['beta'], bacitracin_sensitivity_test= BACITRACIN_SENSITIVITY_TEST['sensitive'], is_strepto=True)
strepto_aglactiae = GramPositive('strepto aglactiae', CATALASE_TEST['-'], BLOOD_AGAR['beta'], bacitracin_sensitivity_test= BACITRACIN_SENSITIVITY_TEST['resistant'], is_strepto=True)
strepto_pneumonia = GramPositive('strepto pneumonia', CATALASE_TEST['-'], BLOOD_AGAR['alpha'], optichin_sensitivity_test= OPTICHIN_SENSITIVITY_TEST['sensitive'], bile_solublitiy_test= BILE_SOLUBLITIY_TEST['soluble'], is_strepto=True)
strepto_viridans = GramPositive('strepto viridans', CATALASE_TEST['-'], BLOOD_AGAR['alpha'], optichin_sensitivity_test= OPTICHIN_SENSITIVITY_TEST['resistant'], bile_solublitiy_test= BILE_SOLUBLITIY_TEST['insoluble'], is_strepto=True)
strepto_enterococci = GramPositive('strepto enterococci', CATALASE_TEST['-'], BLOOD_AGAR['gamma'], penicillin_sensitivity_test= PENICILLIN_SENSITIVITY_TEST['resistant'], NaCl_sensitive= NaCl_SENSITIVE['resistant'], is_strepto=True, MacConkey_agar=MACCONKEY_AGAR['+'])
strepto_non_enterococci = GramPositive('strepto non-enterococci', CATALASE_TEST['-'], BLOOD_AGAR['gamma'], penicillin_sensitivity_test= PENICILLIN_SENSITIVITY_TEST['sensitive'], NaCl_sensitive= NaCl_SENSITIVE['sensitive'], is_strepto=True, MacConkey_agar=MACCONKEY_AGAR['+'])

######### list of bacteria
BACTERIA_LIST = [E_Coli, Citrobacter, Klebsiella, Enterobacter, Shigella, Salmonella, Proteus, Serratia, 
                    Staph_aureus, Staph_epidermidis, Staph_saprophyticus, Literia, Bacillus,Corynbacterium,
                    strepto_non_enterococci,strepto_enterococci,strepto_viridans,strepto_pneumonia,
                    strepto_aglactiae,strepto_pyogens]
