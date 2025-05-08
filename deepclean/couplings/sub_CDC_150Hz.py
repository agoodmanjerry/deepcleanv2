from deepclean.couplings import Coupling, SubtractionProblem


class Sub150Hz(SubtractionProblem):
    description = "Subtraction of 150Hz IMC noise"

    H1 = Coupling(
        150,
        155,
        [
            "IMC-WFS_A_DC_YAW_OUT_DQ",
            "IMC-WFS_B_Q_YAW_OUT_DQ",
            "IMC-WFS_B_Q_PIT_OUT_DQ",
            "PEM-CS_ACC_PSL_PERISCOPE_X_DQ",
            "IMC-WFS_B_DC_YAW_OUT_DQ",
            "IMC-DOF_4_Y_IN1_DQ",
        ],
    )
