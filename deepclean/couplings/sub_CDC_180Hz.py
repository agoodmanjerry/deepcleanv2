from deepclean.couplings import Coupling, SubtractionProblem


class Sub180Hz(SubtractionProblem):
    description = "Subtraction of 180Hz main noise and side bands"

    H1 = Coupling(
        176,
        184,
        [
            "PEM-CS_MAG_LVEA_OUTPUTOPTICS_Z_DQ",
            "LSC-REFL_A_LF_OUT_DQ",
            "IMC-F_OUT_DQ",
            "IMC-WFS_B_Q_YAW_OUT_DQ",
            "IMC-WFS_A_Q_YAW_OUT_DQ",
            "PEM-EX_MAG_VEA_FLOOR_X_DQ",
            "PEM-CS_ACC_PSL_PERISCOPE_Y_DQ",
            "ISI-ITMY_ST2_BLND_RZ_GS13_CUR_IN1_DQ",
            "IMC-WFS_A_DC_YAW_OUT_DQ",
            "IMC-WFS_B_DC_YAW_OUT_DQ",
            "ISI-HAM6_BLND_GS13Z_IN1_DQ",
            "PEM-EY_VMON_ETMY_ESDPOWERMINUS18_DQ",
            "ISI-HAM2_BLND_GS13RZ_IN1_DQ",
            "IMC-L_OUT_DQ",
            "PEM-CS_ACC_PSL_PERISCOPE_X_DQ",
            "PEM-CS_MAG_EBAY_LSCRACK_Z_DQ",
            "IMC-DOF_4_Y_IN1_DQ",
            "IMC-WFS_B_I_YAW_OUT_DQ",
        ],
    )
