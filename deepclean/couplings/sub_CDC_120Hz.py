from deepclean.couplings import Coupling, SubtractionProblem


class SubO4CDC120Hz(SubtractionProblem):
    description = "Subtraction of 120Hz main noise and side bands"

    H1 = Coupling(
        110,
        130,
        [
            "PEM-CS_ACC_PSL_TABLE1_Z_DQ",
            "HPI-HAM4_BLND_L4C_Y_IN1_DQ",
        ],
    )

