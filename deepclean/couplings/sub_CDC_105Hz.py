from deepclean.couplings import Coupling, SubtractionProblem

class Sub105Hz(SubtractionProblem):
    description = "Subtraction of IMC noise around ~105Hz"

    H1 = Coupling(
        104,
        109,
        [
            "IMC-F_OUT_DQ",
            "PEM-CS_ACC_PSL_TABLE1_X_DQ",
            "PEM-CS_ACC_PSL_TABLE1_Z_DQ",
            "IMC-WFS_B_Q_PIT_OUT_DQ",
            "IMC-WFS_A_DC_PIT_OUT_DQ",
            "LSC-MCL_IN1_DQ",
            "IMC-WFS_B_DC_YAW_OUT_DQ",
            "IMC-L_OUT_DQ",
            "IMC-DOF_2_P_IN1_DQ",
            "IMC-WFS_A_DC_YAW_OUT_DQ",
            "LSC-MCL_OUT_DQ",
            "PEM-CS_ACC_PSL_PERISCOPE_X_DQ",
            "IMC-DOF_4_Y_IN1_DQ",
            "IMC-WFS_B_I_PIT_OUT_DQ",
        ],
    )