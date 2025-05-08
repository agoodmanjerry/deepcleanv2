from deepclean.couplings import Coupling, SubtractionProblem


class Sub30Hz(SubtractionProblem):
    description = "Subtraction of ~30Hz line noise"

    H1 = Coupling(
        27.5,
        32.5,
        [
            "PEM-CS_MAG_EBAY_LSCRACK_X_DQ",
            "LSC-SRCL_OUT_DQ",
            "LSC-SRCL_IN1_DQ",
            "PEM-CS_MAG_LVEA_INPUTOPTICS_Y_DQ",
            "LSC-POP_A_RF45_I_ERR_DQ",
            "PEM-CS_MAG_EBAY_LSCRACK_Z_DQ",
            "PEM-CS_MAG_LVEA_INPUTOPTICS_Z_DQ",
        ],
    )
