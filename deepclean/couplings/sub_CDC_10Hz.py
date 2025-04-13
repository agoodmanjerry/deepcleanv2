from deepclean.couplings import Coupling, SubtractionProblem


class Sub10Hz(SubtractionProblem):
    description = "Subtraction of 10Hz broadband noise"

    H1 = Coupling(
        10,
        13,
        [
            "ASC-CSOFT_P_OUT_DQ",
            "PEM-CS_MAG_LVEA_OUTPUTOPTICS_X_DQ",
            "ASC-CHARD_Y_OUT_DQ",
            "ASC-DHARD_Y_OUT_DQ",
            "ASC-DSOFT_P_OUT_DQ",
            "PEM-CS_MAG_EBAY_LSCRACK_X_DQ",
            "LSC-POP_A_RF45_I_ERR_DQ",
        ],
    )