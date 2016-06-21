#!/usr/bin/env python
# -*- coding: utf-8 -*-


# query for load data local infile

def q_load(dirname, dbfile):
	import re
	m = re.search("(R.*_)*(\w*)(\d\d\d\d).DAT", dbfile)
	q = "USE NHIRD1M;\nLOAD DATA LOCAL INFILE "
	if m:
		dbtype = m.group(2)
		year = int(m.group(3))
		path = re.sub("\\\\", "/", os.path.join(dirname, dbfile))
		print "## NHIRD file: " + path
		q = q + "'" + path + "' INTO TABLE " + dbtype + " (@var1) "
	else:
		#print "## NOT NHIRD file: " + dbfile
		return 

	if dbtype == "HOSB":
		q1 = """SET HOSP_ID = SUBSTR(@var1, 1, 34),
			HOSP_CONT_TYPE = SUBSTR(@var1, 35, 1),
			CNT_S_DATE = str_to_date(SUBSTR(@var1, 36, 8), "%Y%m%d"),
			CNT_E_DATE = str_to_date(SUBSTR(@var1, 44, 8), "%Y%m%d"),
			HOSP_TYPE_ID = SUBSTR(@var1, 52, 2),
			TYPE_S_DATE = str_to_date(SUBSTR(@var1, 54, 8), "%Y%m%d"),
			TYPE_E_DATE = str_to_date(SUBSTR(@var1, 62, 8), "%Y%m%d"),
			HOSP_EDUC_MARK = SUBSTR(@var1, 70, 1),
			EDUC_S_DATE = str_to_date(SUBSTR(@var1, 71, 8), "%Y%m%d"),
			EDUC_E_DATE = str_to_date(SUBSTR(@var1, 79, 8), "%Y%m%d"),
			HOSP_GRAD_ID = SUBSTR(@var1, 87, 2),
			GRAD_S_DATE = str_to_date(SUBSTR(@var1, 89, 8), "%Y%m%d"),
			GRAD_E_DATE = str_to_date(SUBSTR(@var1, 97, 8), "%Y%m%d"),
			HOSP_OLD_GRAD = SUBSTR(@var1, 105, 2),
			OLDGRAD_S_DATE = str_to_date(SUBSTR(@var1, 107, 8), "%Y%m%d"),
			AREA_NO_H = SUBSTR(@var1, 115, 4),
			HOSP_OWN_ID = SUBSTR(@var1, 119, 32),
			HOSP_OPEN_DATE = str_to_date(SUBSTR(@var1, 151, 8), "%Y%m%d"),
			REVIEW_CODE = SUBSTR(@var1, 159, 1),
			CONT_S_DATE = str_to_date(SUBSTR(@var1, 160, 8), "%Y%m%d"),
			CONT_E_DATE = str_to_date(SUBSTR(@var1, 168, 8), "%Y%m%d"),
			CCNT_S_DATE = str_to_date(SUBSTR(@var1, 176, 8), "%Y%m%d"),
			CCNT_E_DATE = str_to_date(SUBSTR(@var1, 184, 8), "%Y%m%d"),
			STOP_S_DATE = str_to_date(SUBSTR(@var1, 192, 8), "%Y%m%d"),
			STOP_E_DATE = str_to_date(SUBSTR(@var1, 200, 8), "%Y%m%d"),
			REST_S_DATE = str_to_date(SUBSTR(@var1, 208, 8), "%Y%m%d"),
			REST_E_DATE = str_to_date(SUBSTR(@var1, 216, 8), "%Y%m%d"),
			OLD_HOSP_ID = SUBSTR(@var1, 224, 34);"""

	if dbtype == "HOSX":
			q1 = """SET HOSP_ID = SUBSTR(@var1, 1, 34),
			X01 = SUBSTR(@var1, 35, 1),
			X01_S_DATE = str_to_date(SUBSTR(@var1, 36, 8), "%Y%m%d"),
			X01_E_DATE = str_to_date(SUBSTR(@var1, 44, 8), "%Y%m%d"),
			X02 = SUBSTR(@var1, 52, 1),
			X02_S_DATE = str_to_date(SUBSTR(@var1, 53, 8), "%Y%m%d"),
			X02_E_DATE = str_to_date(SUBSTR(@var1, 61, 8), "%Y%m%d"),
			X03 = SUBSTR(@var1, 69, 1),
			X03_S_DATE = str_to_date(SUBSTR(@var1, 70, 8), "%Y%m%d"),
			X03_E_DATE = str_to_date(SUBSTR(@var1, 78, 8), "%Y%m%d"),
			X04 = SUBSTR(@var1, 86, 1),
			X04_S_DATE = str_to_date(SUBSTR(@var1, 87, 8), "%Y%m%d"),
			X04_E_DATE = str_to_date(SUBSTR(@var1, 95, 8), "%Y%m%d"),
			X05 = SUBSTR(@var1, 103, 1),
			X05_S_DATE = str_to_date(SUBSTR(@var1, 104, 8), "%Y%m%d"),
			X05_E_DATE = str_to_date(SUBSTR(@var1, 112, 8), "%Y%m%d"),
			X06 = SUBSTR(@var1, 120, 1),
			X06_S_DATE = str_to_date(SUBSTR(@var1, 121, 8), "%Y%m%d"),
			X06_E_DATE = str_to_date(SUBSTR(@var1, 129, 8), "%Y%m%d"),
			X07 = SUBSTR(@var1, 137, 1),
			X07_S_DATE = str_to_date(SUBSTR(@var1, 138, 8), "%Y%m%d"),
			X07_E_DATE = str_to_date(SUBSTR(@var1, 146, 8), "%Y%m%d"),
			X08 = SUBSTR(@var1, 154, 1),
			X08_S_DATE = str_to_date(SUBSTR(@var1, 155, 8), "%Y%m%d"),
			X08_E_DATE = str_to_date(SUBSTR(@var1, 163, 8), "%Y%m%d"),
			X09 = SUBSTR(@var1, 171, 1),
			X09_S_DATE = str_to_date(SUBSTR(@var1, 172, 8), "%Y%m%d"),
			X09_E_DATE = str_to_date(SUBSTR(@var1, 180, 8), "%Y%m%d"),
			X10 = SUBSTR(@var1, 188, 1),
			X10_S_DATE = str_to_date(SUBSTR(@var1, 189, 8), "%Y%m%d"),
			X10_E_DATE = str_to_date(SUBSTR(@var1, 197, 8), "%Y%m%d"),
			X11 = SUBSTR(@var1, 205, 1),
			X11_S_DATE = str_to_date(SUBSTR(@var1, 206, 8), "%Y%m%d"),
			X11_E_DATE = str_to_date(SUBSTR(@var1, 214, 8), "%Y%m%d"),
			X12 = SUBSTR(@var1, 222, 1),
			X12_S_DATE = str_to_date(SUBSTR(@var1, 223, 8), "%Y%m%d"),
			X12_E_DATE = str_to_date(SUBSTR(@var1, 231, 8), "%Y%m%d"),
			X13 = SUBSTR(@var1, 239, 1),
			X13_S_DATE = str_to_date(SUBSTR(@var1, 240, 8), "%Y%m%d"),
			X13_E_DATE = str_to_date(SUBSTR(@var1, 248, 8), "%Y%m%d");"""

	if dbtype == "HOX":
			q1 = """SET HOSP_ID = SUBSTR(@var1, 1, 34),
			HOSP_SERVICE_CODE = SUBSTR(@var1, 35, 1),
			VALID_S_DATE = str_to_date(SUBSTR(@var1, 36, 8), "%Y%m%d"),
			VALID_E_DATE = str_to_date(SUBSTR(@var1, 44, 8), "%Y%m%d");"""

	if dbtype == "DETA":
			q1 = """SET HOSP_ID = SUBSTR(@var1, 1, 34),
			FUNC_TYPE = SUBSTR(@var1, 35, 2),
			PAY_S_DATE = str_to_date(SUBSTR(@var1, 37, 8), "%Y%m%d"),
			PAY_E_DATE = str_to_date(SUBSTR(@var1, 45, 8), "%Y%m%d");"""

	if dbtype == "BED":
			q1 = """SET HOSP_ID = SUBSTR(@var1, 1, 34),
			BED_NO = SUBSTR(@var1, 35, 10),
			BED_TYPE = SUBSTR(@var1, 45, 3),
			BED_LEVEL = SUBSTR(@var1, 48, 1),
			PAY_S_DATE = str_to_date(SUBSTR(@var1, 49, 8), "%Y%m%d"),
			PAY_E_DATE = str_to_date(SUBSTR(@var1, 57, 8), "%Y%m%d"),
			UDD_MARK = SUBSTR(@var1, 65, 1),
			UDD_LEVEL = SUBSTR(@var1, 66, 1),
			UDD_S_DATE = str_to_date(SUBSTR(@var1, 67, 8), "%Y%m%d"),
			UDD_E_DATE = str_to_date(SUBSTR(@var1, 75, 8), "%Y%m%d");"""

	if dbtype == "PER":
			q1 = """SET PRSN_ID = SUBSTR(@var1, 1, 32),
			BIRTHDAY = str_to_date(SUBSTR(@var1, 33, 8), "%Y%m%d"),
			PRSN_SEX = SUBSTR(@var1, 41, 4),
			WORK_STATUS = SUBSTR(@var1, 45, 1),
			LINC_DATE = str_to_date(SUBSTR(@var1, 46, 8), "%Y%m%d"),
			WORK_PLACE = SUBSTR(@var1, 54, 34),
			PRSN_TYPE = SUBSTR(@var1, 88, 1),
			STOP_S_YM = str_to_date(SUBSTR(@var1, 89, 8), "%Y%m%d"),
			STOP_E_YM = str_to_date(SUBSTR(@var1, 97, 8), "%Y%m%d"),
			AGAIN_S_YM = str_to_date(SUBSTR(@var1, 105, 8), "%Y%m%d"),
			BRANCH_CODE = SUBSTR(@var1, 113, 1),
			VALID_S_DATE = str_to_date(SUBSTR(@var1, 114, 8), "%Y%m%d"),
			VALID_E_DATE = str_to_date(SUBSTR(@var1, 122, 8), "%Y%m%d"),
			PRSN_CNT = SUBSTR(@var1, 130, 6);"""

	if dbtype == "DOC":
			q1 = """SET PRSN_ID = SUBSTR(@var1, 1, 32),
			DOCU_LWRD_ID = SUBSTR(@var1, 33, 5),
			DOCU_LWRD_NO = SUBSTR(@var1, 38, 6),
			PROV_TPE_ID = SUBSTR(@var1, 44, 5),
			INIT_DATE = str_to_date(SUBSTR(@var1, 49, 8), "%Y%m%d"),
			VALID_S_DATE = str_to_date(SUBSTR(@var1, 57, 8), "%Y%m%d"),
			VALID_E_DATE = str_to_date(SUBSTR(@var1, 65, 8), "%Y%m%d"),
			WORK_RLACE = SUBSTR(@var1, 73, 34),
			BRANCH_CODE = SUBSTR(@var1, 107, 1),
			M_VALID_S_DATE = str_to_date(SUBSTR(@var1, 108, 8), "%Y%m%d");"""

	if dbtype == "HV":
		if year >= 1996 and year <= 2004:
			q1 = """SET ID = SUBSTR(@var1, 1, 32),
			ICD9CM_CODE = SUBSTR(@var1, 33, 5),
			HV_TYPE = SUBSTR(@var1, 38, 2),
			BIRTHDAY = str_to_date(SUBSTR(@var1, 40, 8), "%Y%m%d"),
			SEX = SUBSTR(@var1, 48, 1),
			APPL_DATE = str_to_date(SUBSTR(@var1, 49, 8), "%Y%m%d"),
			APPL_TYPE = SUBSTR(@var1, 57, 1),
			HOSP_ID = SUBSTR(@var1, 58, 34),
			DIAG_PRSN_ID = SUBSTR(@var1, 92, 32),
			RECV_DATE = str_to_date(SUBSTR(@var1, 124, 8), "%Y%m%d"),
			ACPT_NO_YYY = SUBSTR(@var1, 132, 3),
			ACPT_NO_B = SUBSTR(@var1, 135, 1),
			ACPT_NO_SEQ = SUBSTR(@var1, 136, 7),
			## DISE_DESC = SUBSTR(@var1, 143, 150),
			ICD9CM_CNAME = SUBSTR(@var1, 143, 150),
			STOP_REASON = SUBSTR(@var1, 293, 1),
			STOP_DATE = str_to_date(SUBSTR(@var1, 294, 8), "%Y%m%d"),
			REPRINT = SUBSTR(@var1, 302, 2),
			DUPRINT = SUBSTR(@var1, 304, 1),
			VALID_E_DATE = str_to_date(SUBSTR(@var1, 305, 8), "%Y%m%d");"""
		if year >= 2005 and year <= 2009:
			q1 = """SET ID = SUBSTR(@var1, 1, 32),
			ICD9CM_CODE = SUBSTR(@var1, 33, 5),
			HV_TYPE = SUBSTR(@var1, 38, 2),
			BIRTHDAY = str_to_date(SUBSTR(@var1, 40, 8), "%Y%m%d"),
			SEX = SUBSTR(@var1, 48, 1),
			APPL_DATE = str_to_date(SUBSTR(@var1, 49, 8), "%Y%m%d"),
			APPL_TYPE = SUBSTR(@var1, 57, 1),
			HOSP_ID = SUBSTR(@var1, 58, 34),
			DIAG_PRSN_ID = SUBSTR(@var1, 92, 32),
			RECV_DATE = str_to_date(SUBSTR(@var1, 124, 8), "%Y%m%d"),
			ACPT_NO = SUBSTR(@var1, 132, 11),
			ICD9CM_CNAME = SUBSTR(@var1, 143, 150),
			DEATH_MARK = SUBSTR(@var1, 293, 1),
			DEATH_DATE = str_to_date(SUBSTR(@var1, 294, 8), "%Y%m%d"),
			REISSUE_NUM = SUBSTR(@var1, 302, 2),
			CARD_MARK = SUBSTR(@var1, 304, 1),
			VALID_E_DATE = str_to_date(SUBSTR(@var1, 305, 8), "%Y%m%d"),
			ACPT_NUM = SUBSTR(@var1, 313, 5);"""
		if year >= 2010:
			q1 = """SET ID = SUBSTR(@var1, 1, 32),
			ICD9CM_CODE = SUBSTR(@var1, 33, 5),
			HV_TYPE = SUBSTR(@var1, 38, 2),
			BIRTHDAY = str_to_date(SUBSTR(@var1, 40, 8), "%Y%m%d"),
			SEX = SUBSTR(@var1, 48, 1),
			APPL_DATE = str_to_date(SUBSTR(@var1, 49, 8), "%Y%m%d"),
			APPL_TYPE = SUBSTR(@var1, 57, 1),
			HOSP_ID = SUBSTR(@var1, 58, 34),
			DIAG_PRSN_ID = SUBSTR(@var1, 92, 32),
			RECV_DATE = str_to_date(SUBSTR(@var1, 124, 8), "%Y%m%d"),
			ACPT_NO = SUBSTR(@var1, 132, 11),
			ICD9CM_CNAME = SUBSTR(@var1, 143, 150),
			DEATH_MARK = SUBSTR(@var1, 293, 1),
			DEATH_DATE = str_to_date(SUBSTR(@var1, 294, 8), "%Y%m%d"),
			REISSUE_NUM = SUBSTR(@var1, 302, 2),
			CARD_MARK = SUBSTR(@var1, 304, 1),
			VALID_E_DATE = str_to_date(SUBSTR(@var1, 305, 8), "%Y%m%d"),
			ACPT_NUM = SUBSTR(@var1, 313, 5),
			RARE_SICK_MARE = SUBSTR(@var1, 318, 1),
			RS_CODE_A = SUBSTR(@var1, 319, 15),
			RS_CODE_B = SUBSTR(@var1, 334, 15);"""

	if dbtype == "CT":
			q1 = """SET HOSP_ID = SUBSTR(@var1, 1, 34),
			FEE_YM = str_to_date(SUBSTR(@var1, 35, 6), "%Y%m"),
			APPL_TYPE = SUBSTR(@var1, 41, 1),
			APPL_DATE = str_to_date(SUBSTR(@var1, 42, 8), "%Y%m%d"),
			APPL_MODE = SUBSTR(@var1, 50, 1),
			MEDIC_GEN_QTY = SUBSTR(@var1, 51, 10),
			MEDIC_GEN_AMT = SUBSTR(@var1, 61, 10),
			MEDIC_PRO_QTY = SUBSTR(@var1, 71, 10),
			MEDIC_PRO_AMT = SUBSTR(@var1, 81, 10),
			MEDIC_ADR_QTY = SUBSTR(@var1, 91, 10),
			MEDIC_ADR_AMT = SUBSTR(@var1, 101, 10),
			MEDIC_BRN_QTY = SUBSTR(@var1, 111, 10),
			MEDIC_BRN_AMT = SUBSTR(@var1, 121, 10),
			MEDIC_TUB_QTY = SUBSTR(@var1, 131, 10),
			MEDIC_TUB_AMT = SUBSTR(@var1, 141, 10),
			MEDIC_QTY = SUBSTR(@var1, 151, 10),
			MEDIC_AMT = SUBSTR(@var1, 161, 10),
			DENT_GEN_QTY = SUBSTR(@var1, 171, 10),
			DENT_GEN_AMT = SUBSTR(@var1, 181, 10),
			DENT_PRO_QTY = SUBSTR(@var1, 191, 10),
			DENT_PRO_AMT = SUBSTR(@var1, 201, 10),
			DENT_QTY = SUBSTR(@var1, 211, 10),
			DENT_AMT = SUBSTR(@var1, 221, 10),
			HERB_GEN_QTY = SUBSTR(@var1, 231, 10),
			HERB_GEN_AMT = SUBSTR(@var1, 241, 10),
			HERB_PRO_QTY = SUBSTR(@var1, 251, 10),
			HERB_PRO_AMT = SUBSTR(@var1, 261, 10),
			HERB_QTY = SUBSTR(@var1, 271, 10),
			HERB_AMT = SUBSTR(@var1, 281, 10),
			PREV_QTY = SUBSTR(@var1, 291, 10),
			PREV_AMT = SUBSTR(@var1, 301, 10),
			PREP_QTY1 = SUBSTR(@var1, 311, 10),
			PREP_AMT1 = SUBSTR(@var1, 321, 10),
			PREP_QTY2 = SUBSTR(@var1, 331, 10),
			PREP_AMT2 = SUBSTR(@var1, 341, 10),
			T_APPL_QTY = SUBSTR(@var1, 351, 10),
			T_APPL_AMT = SUBSTR(@var1, 361, 10);"""

	if dbtype == "DT":
			q1 = """SET HOSP_ID = SUBSTR(@var1, 1, 34),
			FEE_YM = str_to_date(SUBSTR(@var1, 35, 6), "%Y%m"),
			APPL_TYPE = SUBSTR(@var1, 41, 1),
			APPL_DATE = str_to_date(SUBSTR(@var1, 42, 8), "%Y%m%d"),
			APPL_MODE = SUBSTR(@var1, 50, 1),
			CASE_GEN_QTY = SUBSTR(@var1, 51, 10),
			CASE_GEN_DAYS = SUBSTR(@var1, 61, 10),
			CASE_GEN_AMT = SUBSTR(@var1, 71, 10),
			CASE_PAY_QTY = SUBSTR(@var1, 81, 10),
			CASE_PAY_DAYS = SUBSTR(@var1, 91, 10),
			CASE_PAY_AMT = SUBSTR(@var1, 101, 10),
			CASE_SPE_QTY = SUBSTR(@var1, 111, 10),
			CASE_SPE_DAYS = SUBSTR(@var1, 121, 10),
			CASE_SPE_AMT = SUBSTR(@var1, 131, 10),
			D_TOTL_QTY = SUBSTR(@var1, 141, 10),
			D_TOTL_DAYS = SUBSTR(@var1, 151, 10),
			D_TOTL_AMT = SUBSTR(@var1, 161, 10),
			D_PART_QTY = SUBSTR(@var1, 171, 10),
			D_PART_DAYS = SUBSTR(@var1, 181, 10),
			D_PART_AMT = SUBSTR(@var1, 191, 10),
			T_CHRG_QTY = SUBSTR(@var1, 201, 10),
			T_CHRG_DAYS = SUBSTR(@var1, 211, 10),
			T_CHRG_AMT = SUBSTR(@var1, 221, 10),
			T_APPL_QTY = SUBSTR(@var1, 231, 10),
			T_APPL_DAYS = SUBSTR(@var1, 241, 10),
			T_APPL_AMT = SUBSTR(@var1, 251, 10);"""

	if dbtype == "CD":
		if year >= 1996 and year <= 2003:
			q1 = """SET FEE_YM = str_to_date(SUBSTR(@var1, 1, 6), "%Y%m"),
			APPL_TYPE = SUBSTR(@var1, 7, 1),
			HOSP_ID = SUBSTR(@var1, 8, 34),
			APPL_DATE = str_to_date(SUBSTR(@var1, 42, 8), "%Y%m%d"),
			CASE_TYPE = SUBSTR(@var1, 50, 2),
			SEQ_NO = SUBSTR(@var1, 52, 6),
			CURE_ITEM_NO1 = SUBSTR(@var1, 58, 2),
			CURE_ITEM_NO2 = SUBSTR(@var1, 60, 2),
			CURE_ITEM_NO3 = SUBSTR(@var1, 62, 2),
			CURE_ITEM_NO4 = SUBSTR(@var1, 64, 2),
			FUNC_TYPE = SUBSTR(@var1, 66, 2),
			FUNC_DATE = str_to_date(SUBSTR(@var1, 68, 8), "%Y%m%d"),
			TREAT_END_DATE = str_to_date(SUBSTR(@var1, 76, 8), "%Y%m%d"),
			ID_BIRTHDAY = str_to_date(SUBSTR(@var1, 84, 8), "%Y%m%d"),
			ID = SUBSTR(@var1, 92, 32),
			CARD_SEQ_NO = SUBSTR(@var1, 124, 2),
			GAVE_KIND = SUBSTR(@var1, 127, 1),
			PART_NO = SUBSTR(@var1, 128, 3),
			ACODE_ICD9_1 = SUBSTR(@var1, 131, 5),
			ACODE_ICD9_2 = SUBSTR(@var1, 136, 5),
			ACODE_ICD9_3 = SUBSTR(@var1, 141, 5),
			ICD_OP_CODE = SUBSTR(@var1, 146, 4),
			DRUG_DAY = SUBSTR(@var1, 150, 2),
			MED_TYPE = SUBSTR(@var1, 152, 1),
			PRSN_ID = SUBSTR(@var1, 153, 32),
			PHAR_ID = SUBSTR(@var1, 185, 32),
			DRUG_AMT = SUBSTR(@var1, 217, 8),
			TREAT_AMT = SUBSTR(@var1, 225, 8),
			TREAT_CODE = SUBSTR(@var1, 233, 12),
			DIAG_AMT = SUBSTR(@var1, 245, 8),
			DSVC_NO = SUBSTR(@var1, 253, 12),
			DSVC_AMT = SUBSTR(@var1, 265, 8),
			BY_PASS_CODE = SUBSTR(@var1, 273, 2),
			T_AMT = SUBSTR(@var1, 275, 8),
			PART_AMT = SUBSTR(@var1, 283, 8),
			T_APPL_AMT = SUBSTR(@var1, 291, 8),
			ID_SEX = SUBSTR(@var1, 299, 1);"""
		if year >= 2004:
			q1 = """SET FEE_YM = str_to_date(SUBSTR(@var1, 1, 6), "%Y%m"),
			APPL_TYPE = SUBSTR(@var1, 7, 1),
			HOSP_ID = SUBSTR(@var1, 8, 34),
			APPL_DATE = str_to_date(SUBSTR(@var1, 42, 8), "%Y%m%d"),
			CASE_TYPE = SUBSTR(@var1, 50, 2),
			SEQ_NO = SUBSTR(@var1, 52, 6),
			CURE_ITEM_NO1 = SUBSTR(@var1, 58, 2),
			CURE_ITEM_NO2 = SUBSTR(@var1, 60, 2),
			CURE_ITEM_NO3 = SUBSTR(@var1, 62, 2),
			CURE_ITEM_NO4 = SUBSTR(@var1, 64, 2),
			FUNC_TYPE = SUBSTR(@var1, 66, 2),
			FUNC_DATE = str_to_date(SUBSTR(@var1, 68, 8), "%Y%m%d"),
			TREAT_END_DATE = str_to_date(SUBSTR(@var1, 76, 8), "%Y%m%d"),
			ID_BIRTHDAY = str_to_date(SUBSTR(@var1, 84, 8), "%Y%m%d"),
			ID = SUBSTR(@var1, 92, 32),
			CARD_SEQ_NO = SUBSTR(@var1, 124, 4),
			GAVE_KIND = SUBSTR(@var1, 128, 1),
			PART_NO = SUBSTR(@var1, 129, 3),
			ACODE_ICD9_1 = SUBSTR(@var1, 132, 5),
			ACODE_ICD9_2 = SUBSTR(@var1, 137, 5),
			ACODE_ICD9_3 = SUBSTR(@var1, 142, 5),
			ICD_OP_CODE = SUBSTR(@var1, 147, 4),
			DRUG_DAY = SUBSTR(@var1, 151, 2),
			MED_TYPE = SUBSTR(@var1, 153, 1),
			PRSN_ID = SUBSTR(@var1, 154, 32),
			PHAR_ID = SUBSTR(@var1, 186, 32),
			DRUG_AMT = SUBSTR(@var1, 218, 8),
			TREAT_AMT = SUBSTR(@var1, 226, 8),
			TREAT_CODE = SUBSTR(@var1, 234, 12),
			DIAG_AMT = SUBSTR(@var1, 246, 8),
			DSVC_NO = SUBSTR(@var1, 254, 12),
			DSVC_AMT = SUBSTR(@var1, 266, 8),
			BY_PASS_CODE = SUBSTR(@var1, 274, 2),
			T_AMT = SUBSTR(@var1, 276, 8),
			PART_AMT = SUBSTR(@var1, 284, 8),
			T_APPL_AMT = SUBSTR(@var1, 292, 8),
			ID_SEX = SUBSTR(@var1, 300, 1);"""

	if dbtype == "OO":
		if year >= 1997 and year <= 2006:
			q1 = """SET FEE_YM = str_to_date(SUBSTR(@var1, 1, 6), "%Y%m"),
			APPL_TYPE = SUBSTR(@var1, 7, 1),
			HOSP_ID = SUBSTR(@var1, 8, 34),
			APPL_DATE = str_to_date(SUBSTR(@var1, 42, 8), "%Y%m%d"),
			CASE_TYPE = SUBSTR(@var1, 50, 2),
			SEQ_NO = SUBSTR(@var1, 52, 6),
			ORDER_TYPE = SUBSTR(@var1, 58, 1),
			DRUG_NO = SUBSTR(@var1, 59, 12),
			DRUG_USE = SUBSTR(@var1, 71, 6),
			DRUG_FRE = SUBSTR(@var1, 77, 18),
			UNIT_PRICE = SUBSTR(@var1, 95, 10),
			TOTAL_QTY = SUBSTR(@var1, 105, 7),
			TOTAL_AMT = SUBSTR(@var1, 112, 8);"""
		if year >= 2007:
			q1 = """SET FEE_YM = str_to_date(SUBSTR(@var1, 1, 6), "%Y%m"),
			APPL_TYPE = SUBSTR(@var1, 7, 1),
			HOSP_ID = SUBSTR(@var1, 8, 34),
			APPL_DATE = str_to_date(SUBSTR(@var1, 42, 8), "%Y%m%d"),
			CASE_TYPE = SUBSTR(@var1, 50, 2),
			SEQ_NO = SUBSTR(@var1, 52, 6),
			ORDER_TYPE = SUBSTR(@var1, 58, 1),
			DRUG_NO = SUBSTR(@var1, 59, 12),
			DRUG_USE = SUBSTR(@var1, 71, 6),
			DRUG_FRE = SUBSTR(@var1, 77, 18),
			UNIT_PRICE = SUBSTR(@var1, 95, 10),
			TOTAL_QTY = SUBSTR(@var1, 105, 7),
			TOTAL_AMT = SUBSTR(@var1, 112, 8),
			ORDER_SEQ_NO = SUBSTR(@var1, 120, 5);"""

	if dbtype == "DD":
		if year >= 1996 and year <= 2003:
			q1 = """SET FEE_YM = str_to_date(SUBSTR(@var1, 1, 6), "%Y%m"),
			APPL_TYPE = SUBSTR(@var1, 7, 1),
			HOSP_ID = SUBSTR(@var1, 8, 34),
			APPL_DATE = str_to_date(SUBSTR(@var1, 42, 8), "%Y%m%d"),
			CASE_TYPE = SUBSTR(@var1, 50, 1),
			SEQ_NO = SUBSTR(@var1, 51, 6),
			ID = SUBSTR(@var1, 57, 32),
			ID_BIRTHDAY = str_to_date(SUBSTR(@var1, 89, 8), "%Y%m%d"),
			GAVE_KIND = SUBSTR(@var1, 97, 1),
			TRAC_EVEN = SUBSTR(@var1, 98, 1),
			CARD_SEQ_NO = SUBSTR(@var1, 99, 2),
			FUNC_TYPE = SUBSTR(@var1, 102, 2),
			IN_DATE = str_to_date(SUBSTR(@var1, 104, 8), "%Y%m%d"),
			OUT_DATE = str_to_date(SUBSTR(@var1, 112, 8), "%Y%m%d"),
			APPL_BEG_DATE = str_to_date(SUBSTR(@var1, 120, 8), "%Y%m%d"),
			APPL_END_DATE = str_to_date(SUBSTR(@var1, 128, 8), "%Y%m%d"),
			E_BED_DAY = SUBSTR(@var1, 136, 3),
			S_BED_DAY = SUBSTR(@var1, 139, 3),
			PRSN_ID = SUBSTR(@var1, 142, 32),
			DRG_CODE = SUBSTR(@var1, 174, 5),
			EXT_CODE_1 = SUBSTR(@var1, 179, 5),
			EXT_CODE_2 = SUBSTR(@var1, 184, 5),
			TRAN_CODE = SUBSTR(@var1, 189, 1),
			ICD9CM_CODE = SUBSTR(@var1, 190, 5),
			ICD9CM_CODE_1 = SUBSTR(@var1, 195, 5),
			ICD9CM_CODE_2 = SUBSTR(@var1, 200, 5),
			ICD9CM_CODE_3 = SUBSTR(@var1, 205, 5),
			ICD9CM_CODE_4 = SUBSTR(@var1, 210, 5),
			ICD_OP_CODE = SUBSTR(@var1, 215, 4),
			ICD_OP_CODE_1 = SUBSTR(@var1, 219, 4),
			ICD_OP_CODE_2 = SUBSTR(@var1, 223, 4),
			ICD_OP_CODE_3 = SUBSTR(@var1, 227, 4),
			ICD_OP_CODE_4 = SUBSTR(@var1, 231, 4),
			DIAG_AMT = SUBSTR(@var1, 235, 7),
			ROOM_AMT = SUBSTR(@var1, 242, 7),
			MEAL_AMT = SUBSTR(@var1, 249, 7),
			AMIN_AMT = SUBSTR(@var1, 256, 7),
			RADO_AMT = SUBSTR(@var1, 263, 7),
			THRP_AMT = SUBSTR(@var1, 270, 7),
			SGRY_AMT = SUBSTR(@var1, 277, 7),
			PHSC_AMT = SUBSTR(@var1, 284, 7),
			BLOD_AMT = SUBSTR(@var1, 291, 7),
			HD_AMT = SUBSTR(@var1, 298, 7),
			ANE_AMT = SUBSTR(@var1, 305, 7),
			METR_AMT = SUBSTR(@var1, 312, 7),
			DRUG_AMT = SUBSTR(@var1, 319, 7),
			DSVC_AMT = SUBSTR(@var1, 326, 7),
			NRTP_AMT = SUBSTR(@var1, 333, 7),
			INJT_AMT = SUBSTR(@var1, 340, 7),
			BABY_AMT = SUBSTR(@var1, 347, 7),
			CHARG_AMT = SUBSTR(@var1, 354, 7),
			MED_AMT = SUBSTR(@var1, 361, 8),
			PART_AMT = SUBSTR(@var1, 369, 7),
			APPL_AMT = SUBSTR(@var1, 376, 8),
			EB_APPL30_AMT = SUBSTR(@var1, 384, 8),
			EB_PART30_AMT = SUBSTR(@var1, 392, 7),
			EB_APPL60_AMT = SUBSTR(@var1, 399, 8),
			EB_PART60_AMT = SUBSTR(@var1, 407, 7),
			EB_APPL61_AMT = SUBSTR(@var1, 414, 8),
			EB_PART61_AMT = SUBSTR(@var1, 422, 7),
			SB_APPL30_AMT = SUBSTR(@var1, 429, 8),
			SB_PART30_AMT = SUBSTR(@var1, 437, 7),
			SB_APPL90_AMT = SUBSTR(@var1, 444, 8),
			SB_PART90_AMT = SUBSTR(@var1, 452, 7),
			SB_APPL180_AMT = SUBSTR(@var1, 459, 8),
			SB_PART180_AMT = SUBSTR(@var1, 467, 7),
			SB_APPL181_AMT = SUBSTR(@var1, 474, 8),
			SB_PART181_AMT = SUBSTR(@var1, 482, 7),
			PART_MARK = SUBSTR(@var1, 489, 3),
			ID_SEX = SUBSTR(@var1, 492, 1);"""
		if year >= 2004 and year <= 2006:
			q1 = """SET FEE_YM = str_to_date(SUBSTR(@var1, 1, 6), "%Y%m"),
			APPL_TYPE = SUBSTR(@var1, 7, 1),
			HOSP_ID = SUBSTR(@var1, 8, 34),
			APPL_DATE = str_to_date(SUBSTR(@var1, 42, 8), "%Y%m%d"),
			CASE_TYPE = SUBSTR(@var1, 50, 1),
			SEQ_NO = SUBSTR(@var1, 51, 6),
			ID = SUBSTR(@var1, 57, 32),
			ID_BIRTHDAY = str_to_date(SUBSTR(@var1, 89, 8), "%Y%m%d"),
			GAVE_KIND = SUBSTR(@var1, 97, 1),
			TRAC_EVEN = SUBSTR(@var1, 98, 1),
			CARD_SEQ_NO = SUBSTR(@var1, 99, 4),
			FUNC_TYPE = SUBSTR(@var1, 103, 2),
			IN_DATE = str_to_date(SUBSTR(@var1, 105, 8), "%Y%m%d"),
			OUT_DATE = str_to_date(SUBSTR(@var1, 113, 8), "%Y%m%d"),
			APPL_BEG_DATE = str_to_date(SUBSTR(@var1, 121, 8), "%Y%m%d"),
			APPL_END_DATE = str_to_date(SUBSTR(@var1, 129, 8), "%Y%m%d"),
			E_BED_DAY = SUBSTR(@var1, 137, 3),
			S_BED_DAY = SUBSTR(@var1, 140, 3),
			PRSN_ID = SUBSTR(@var1, 143, 32),
			DRG_CODE = SUBSTR(@var1, 175, 5),
			EXT_CODE_1 = SUBSTR(@var1, 180, 5),
			EXT_CODE_2 = SUBSTR(@var1, 185, 5),
			TRAN_CODE = SUBSTR(@var1, 190, 1),
			ICD9CM_CODE = SUBSTR(@var1, 191, 5),
			ICD9CM_CODE_1 = SUBSTR(@var1, 196, 5),
			ICD9CM_CODE_2 = SUBSTR(@var1, 201, 5),
			ICD9CM_CODE_3 = SUBSTR(@var1, 206, 5),
			ICD9CM_CODE_4 = SUBSTR(@var1, 211, 5),
			ICD_OP_CODE = SUBSTR(@var1, 216, 4),
			ICD_OP_CODE_1 = SUBSTR(@var1, 220, 4),
			ICD_OP_CODE_2 = SUBSTR(@var1, 224, 4),
			ICD_OP_CODE_3 = SUBSTR(@var1, 228, 4),
			ICD_OP_CODE_4 = SUBSTR(@var1, 232, 4),
			DIAG_AMT = SUBSTR(@var1, 236, 7),
			ROOM_AMT = SUBSTR(@var1, 243, 7),
			MEAL_AMT = SUBSTR(@var1, 250, 7),
			AMIN_AMT = SUBSTR(@var1, 257, 7),
			RADO_AMT = SUBSTR(@var1, 264, 7),
			THRP_AMT = SUBSTR(@var1, 271, 7),
			SGRY_AMT = SUBSTR(@var1, 278, 7),
			PHSC_AMT = SUBSTR(@var1, 285, 7),
			BLOD_AMT = SUBSTR(@var1, 292, 7),
			HD_AMT = SUBSTR(@var1, 299, 7),
			ANE_AMT = SUBSTR(@var1, 306, 7),
			METR_AMT = SUBSTR(@var1, 313, 7),
			DRUG_AMT = SUBSTR(@var1, 320, 7),
			DSVC_AMT = SUBSTR(@var1, 327, 7),
			NRTP_AMT = SUBSTR(@var1, 334, 7),
			INJT_AMT = SUBSTR(@var1, 341, 7),
			BABY_AMT = SUBSTR(@var1, 348, 7),
			CHARG_AMT = SUBSTR(@var1, 355, 7),
			MED_AMT = SUBSTR(@var1, 362, 8),
			PART_AMT = SUBSTR(@var1, 370, 7),
			APPL_AMT = SUBSTR(@var1, 377, 8),
			EB_APPL30_AMT = SUBSTR(@var1, 385, 8),
			EB_PART30_AMT = SUBSTR(@var1, 393, 7),
			EB_APPL60_AMT = SUBSTR(@var1, 400, 8),
			EB_PART60_AMT = SUBSTR(@var1, 408, 7),
			EB_APPL61_AMT = SUBSTR(@var1, 415, 8),
			EB_PART61_AMT = SUBSTR(@var1, 423, 7),
			SB_APPL30_AMT = SUBSTR(@var1, 430, 8),
			SB_PART30_AMT = SUBSTR(@var1, 438, 7),
			SB_APPL90_AMT = SUBSTR(@var1, 445, 8),
			SB_PART90_AMT = SUBSTR(@var1, 453, 7),
			SB_APPL180_AMT = SUBSTR(@var1, 460, 8),
			SB_PART180_AMT = SUBSTR(@var1, 468, 7),
			SB_APPL181_AMT = SUBSTR(@var1, 475, 8),
			SB_PART181_AMT = SUBSTR(@var1, 483, 7),
			PART_MARK = SUBSTR(@var1, 490, 3),
			ID_SEX = SUBSTR(@var1, 493, 1);"""
		if year >= 2007:
			q1 = """SET FEE_YM = str_to_date(SUBSTR(@var1, 1, 6), "%Y%m"),
			APPL_TYPE = SUBSTR(@var1, 7, 1),
			HOSP_ID = SUBSTR(@var1, 8, 34),
			APPL_DATE = str_to_date(SUBSTR(@var1, 42, 8), "%Y%m%d"),
			CASE_TYPE = SUBSTR(@var1, 50, 2),
			SEQ_NO = SUBSTR(@var1, 52, 6),
			ID = SUBSTR(@var1, 58, 32),
			ID_BIRTHDAY = str_to_date(SUBSTR(@var1, 90, 8), "%Y%m%d"),
			GAVE_KIND = SUBSTR(@var1, 98, 1),
			TRAC_EVEN = SUBSTR(@var1, 99, 1),
			CARD_SEQ_NO = SUBSTR(@var1, 100, 4),
			FUNC_TYPE = SUBSTR(@var1, 104, 2),
			IN_DATE = str_to_date(SUBSTR(@var1, 106, 8), "%Y%m%d"),
			OUT_DATE = str_to_date(SUBSTR(@var1, 114, 8), "%Y%m%d"),
			APPL_BEG_DATE = str_to_date(SUBSTR(@var1, 122, 8), "%Y%m%d"),
			APPL_END_DATE = str_to_date(SUBSTR(@var1, 130, 8), "%Y%m%d"),
			E_BED_DAY = SUBSTR(@var1, 138, 3),
			S_BED_DAY = SUBSTR(@var1, 141, 3),
			PRSN_ID = SUBSTR(@var1, 144, 32),
			DRG_CODE = SUBSTR(@var1, 176, 5),
			EXT_CODE_1 = SUBSTR(@var1, 181, 5),
			EXT_CODE_2 = SUBSTR(@var1, 186, 5),
			TRAN_CODE = SUBSTR(@var1, 191, 1),
			ICD9CM_CODE = SUBSTR(@var1, 192, 5),
			ICD9CM_CODE_1 = SUBSTR(@var1, 197, 5),
			ICD9CM_CODE_2 = SUBSTR(@var1, 202, 5),
			ICD9CM_CODE_3 = SUBSTR(@var1, 207, 5),
			ICD9CM_CODE_4 = SUBSTR(@var1, 212, 5),
			ICD_OP_CODE = SUBSTR(@var1, 217, 4),
			ICD_OP_CODE_1 = SUBSTR(@var1, 221, 4),
			ICD_OP_CODE_2 = SUBSTR(@var1, 225, 4),
			ICD_OP_CODE_3 = SUBSTR(@var1, 229, 4),
			ICD_OP_CODE_4 = SUBSTR(@var1, 233, 4),
			DIAG_AMT = SUBSTR(@var1, 237, 7),
			ROOM_AMT = SUBSTR(@var1, 244, 7),
			MEAL_AMT = SUBSTR(@var1, 251, 7),
			AMIN_AMT = SUBSTR(@var1, 258, 7),
			RADO_AMT = SUBSTR(@var1, 265, 7),
			THRP_AMT = SUBSTR(@var1, 272, 7),
			SGRY_AMT = SUBSTR(@var1, 279, 7),
			PHSC_AMT = SUBSTR(@var1, 286, 7),
			BLOD_AMT = SUBSTR(@var1, 293, 7),
			HD_AMT = SUBSTR(@var1, 300, 7),
			ANE_AMT = SUBSTR(@var1, 307, 7),
			METR_AMT = SUBSTR(@var1, 314, 7),
			DRUG_AMT = SUBSTR(@var1, 321, 7),
			DSVC_AMT = SUBSTR(@var1, 328, 7),
			NRTP_AMT = SUBSTR(@var1, 335, 7),
			INJT_AMT = SUBSTR(@var1, 342, 7),
			BABY_AMT = SUBSTR(@var1, 349, 7),
			CHARG_AMT = SUBSTR(@var1, 356, 7),
			MED_AMT = SUBSTR(@var1, 363, 8),
			PART_AMT = SUBSTR(@var1, 371, 7),
			APPL_AMT = SUBSTR(@var1, 378, 8),
			EB_APPL30_AMT = SUBSTR(@var1, 386, 8),
			EB_PART30_AMT = SUBSTR(@var1, 394, 7),
			EB_APPL60_AMT = SUBSTR(@var1, 401, 8),
			EB_PART60_AMT = SUBSTR(@var1, 409, 7),
			EB_APPL61_AMT = SUBSTR(@var1, 416, 8),
			EB_PART61_AMT = SUBSTR(@var1, 424, 7),
			SB_APPL30_AMT = SUBSTR(@var1, 431, 8),
			SB_PART30_AMT = SUBSTR(@var1, 439, 7),
			SB_APPL90_AMT = SUBSTR(@var1, 446, 8),
			SB_PART90_AMT = SUBSTR(@var1, 454, 7),
			SB_APPL180_AMT = SUBSTR(@var1, 461, 8),
			SB_PART180_AMT = SUBSTR(@var1, 469, 7),
			SB_APPL181_AMT = SUBSTR(@var1, 476, 8),
			SB_PART181_AMT = SUBSTR(@var1, 484, 7),
			PART_MARK = SUBSTR(@var1, 491, 3),
			ID_SEX = SUBSTR(@var1, 494, 1);"""

	if dbtype == "DO":
		if year >= 1996 and year <= 2006:
			q1 = """SET FEE_YM = str_to_date(SUBSTR(@var1, 1, 6), "%Y%m"),
			APPL_TYPE = SUBSTR(@var1, 7, 1),
			HOSP_ID = SUBSTR(@var1, 8, 34),
			APPL_DATE = str_to_date(SUBSTR(@var1, 42, 8), "%Y%m%d"),
			CASE_TYPE = SUBSTR(@var1, 50, 1),
			SEQ_NO = SUBSTR(@var1, 51, 6),
			ORDER_SEQ_NO = SUBSTR(@var1, 57, 5),
			ORDER_TYPE = SUBSTR(@var1, 62, 1),
			ORDER_CODE = SUBSTR(@var1, 63, 12),
			RATE_TYPE = SUBSTR(@var1, 75, 4),
			ORDER_QTY = SUBSTR(@var1, 79, 7),
			ORDER_PRICE = SUBSTR(@var1, 86, 10),
			ORDER_AMT = SUBSTR(@var1, 96, 8);"""
		if year >= 2007:
			q1 = """SET FEE_YM = str_to_date(SUBSTR(@var1, 1, 6), "%Y%m"),
			APPL_TYPE = SUBSTR(@var1, 7, 1),
			HOSP_ID = SUBSTR(@var1, 8, 34),
			APPL_DATE = str_to_date(SUBSTR(@var1, 42, 8), "%Y%m%d"),
			CASE_TYPE = SUBSTR(@var1, 50, 2),
			SEQ_NO = SUBSTR(@var1, 52, 6),
			ORDER_SEQ_NO = SUBSTR(@var1, 58, 5),
			ORDER_TYPE = SUBSTR(@var1, 63, 1),
			ORDER_CODE = SUBSTR(@var1, 64, 12),
			RATE_TYPE = SUBSTR(@var1, 76, 4),
			ORDER_QTY = SUBSTR(@var1, 80, 7),
			ORDER_PRICE = SUBSTR(@var1, 87, 10),
			ICD_OP_CODE = SUBSTR(@var1, 97, 8);"""

	if dbtype == "GD":
		if year >= 1996 and year <= 1998:
			q1 = """SET FEE_YM = str_to_date(SUBSTR(@var1, 1, 6), "%Y%m"),
			APPL_TYPE = SUBSTR(@var1, 7, 1),
			HOSP_ID = SUBSTR(@var1, 8, 34),
			APPL_DATE = str_to_date(SUBSTR(@var1, 42, 8), "%Y%m%d"),
			CASE_TYPE = SUBSTR(@var1, 50, 1),
			SEQ_NO = SUBSTR(@var1, 51, 6),
			R_HOSP_ID = SUBSTR(@var1, 57, 34),
			R_CASE_TYPE = SUBSTR(@var1, 91, 2),
			FUNC_TYPE = SUBSTR(@var1, 93, 2),
			FUNC_DATE = str_to_date(SUBSTR(@var1, 95, 8), "%Y%m%d"),
			DRUG_DATE = str_to_date(SUBSTR(@var1, 103, 8), "%Y%m%d"),
			ID_BIRTHDAY = str_to_date(SUBSTR(@var1, 111, 8), "%Y%m%d"),
			ID = SUBSTR(@var1, 119, 32),
			CARD_SEQ_NO = SUBSTR(@var1, 151, 2),
			GAVE_KIND = SUBSTR(@var1, 153, 1),
			DRUG_DAY = SUBSTR(@var1, 154, 2),
			PRSN_ID = SUBSTR(@var1, 156, 32),
			PHAR_ID = SUBSTR(@var1, 188, 32),
			DRUG_AMT = SUBSTR(@var1, 220, 8),
			DSVC_AMT = SUBSTR(@var1, 228, 8),
			T_APPL_AMT = SUBSTR(@var1, 236, 8),
			SEX = SUBSTR(@var1, 244, 1);"""
		if year >= 1999 and year <= 2003:
			q1 = """SET FEE_YM = str_to_date(SUBSTR(@var1, 1, 6), "%Y%m"),
			APPL_TYPE = SUBSTR(@var1, 7, 1),
			HOSP_ID = SUBSTR(@var1, 8, 34),
			APPL_DATE = str_to_date(SUBSTR(@var1, 42, 8), "%Y%m%d"),
			CASE_TYPE = SUBSTR(@var1, 50, 1),
			SEQ_NO = SUBSTR(@var1, 51, 6),
			R_HOSP_ID = SUBSTR(@var1, 57, 34),
			R_CASE_TYPE = SUBSTR(@var1, 91, 2),
			FUNC_TYPE = SUBSTR(@var1, 93, 2),
			FUNC_DATE = str_to_date(SUBSTR(@var1, 95, 8), "%Y%m%d"),
			DRUG_DATE = str_to_date(SUBSTR(@var1, 103, 8), "%Y%m%d"),
			ID_BIRTHDAY = str_to_date(SUBSTR(@var1, 111, 8), "%Y%m%d"),
			ID = SUBSTR(@var1, 119, 32),
			CARD_SEQ_NO = SUBSTR(@var1, 151, 2),
			GAVE_KIND = SUBSTR(@var1, 153, 1),
			DRUG_DAY = SUBSTR(@var1, 154, 2),
			PRSN_ID = SUBSTR(@var1, 156, 32),
			PHAR_ID = SUBSTR(@var1, 188, 32),
			DRUG_AMT = SUBSTR(@var1, 220, 8),
			DSVC_AMT = SUBSTR(@var1, 228, 8),
			T_APPL_AMT = SUBSTR(@var1, 236, 8),
			SEX = SUBSTR(@var1, 244, 1),
			PART_NO = SUBSTR(@var1, 245, 3),
			SPE_MET_AMT = SUBSTR(@var1, 248, 7),
			PART_AMT = SUBSTR(@var1, 255, 4),
			T_AMT = SUBSTR(@var1, 259, 8);"""
		if year >= 2004 and year <= 2009:
			q1 = """SET FEE_YM = str_to_date(SUBSTR(@var1, 1, 6), "%Y%m"),
			APPL_TYPE = SUBSTR(@var1, 7, 1),
			HOSP_ID = SUBSTR(@var1, 8, 34),
			APPL_DATE = str_to_date(SUBSTR(@var1, 42, 8), "%Y%m%d"),
			CASE_TYPE = SUBSTR(@var1, 50, 1),
			SEQ_NO = SUBSTR(@var1, 51, 6),
			R_HOSP_ID = SUBSTR(@var1, 57, 34),
			R_CASE_TYPE = SUBSTR(@var1, 91, 2),
			FUNC_TYPE = SUBSTR(@var1, 93, 2),
			FUNC_DATE = str_to_date(SUBSTR(@var1, 95, 8), "%Y%m%d"),
			DRUG_DATE = str_to_date(SUBSTR(@var1, 103, 8), "%Y%m%d"),
			ID_BIRTHDAY = str_to_date(SUBSTR(@var1, 111, 8), "%Y%m%d"),
			ID = SUBSTR(@var1, 119, 32),
			CARD_SEQ_NO = SUBSTR(@var1, 151, 4),
			GAVE_KIND = SUBSTR(@var1, 155, 1),
			DRUG_DAY = SUBSTR(@var1, 156, 2),
			PRSN_ID = SUBSTR(@var1, 158, 32),
			PHAR_ID = SUBSTR(@var1, 190, 32),
			DRUG_AMT = SUBSTR(@var1, 222, 8),
			DSVC_AMT = SUBSTR(@var1, 230, 8),
			T_APPL_AMT = SUBSTR(@var1, 238, 8),
			SEX = SUBSTR(@var1, 246, 1),
			PART_NO = SUBSTR(@var1, 247, 3),
			SPE_MET_AMT = SUBSTR(@var1, 250, 7),
			PART_AMT = SUBSTR(@var1, 257, 4),
			T_AMT = SUBSTR(@var1, 261, 8);"""
			
		if year >= 2010:
			q1 = """SET FEE_YM = str_to_date(SUBSTR(@var1, 1, 6), "%Y%m"),
			APPL_TYPE = SUBSTR(@var1, 7, 1),
			HOSP_ID = SUBSTR(@var1, 8, 34),
			APPL_DATE = str_to_date(SUBSTR(@var1, 42, 8), "%Y%m%d"),
			CASE_TYPE = SUBSTR(@var1, 50, 1),
			SEQ_NO = SUBSTR(@var1, 51, 6),
			R_HOSP_ID = SUBSTR(@var1, 57, 34),
			R_CASE_TYPE = SUBSTR(@var1, 91, 2),
			FUNC_TYPE = SUBSTR(@var1, 93, 2),
			FUNC_DATE = str_to_date(SUBSTR(@var1, 95, 8), "%Y%m%d"),
			DRUG_DATE = str_to_date(SUBSTR(@var1, 103, 8), "%Y%m%d"),
			ID_BIRTHDAY = str_to_date(SUBSTR(@var1, 111, 8), "%Y%m%d"),
			ID = SUBSTR(@var1, 119, 32),
			CARD_SEQ_NO = SUBSTR(@var1, 151, 4),
			GAVE_KIND = SUBSTR(@var1, 155, 1),
			DRUG_DAY = SUBSTR(@var1, 156, 2),
			PRSN_ID = SUBSTR(@var1, 158, 32),
			PHAR_ID = SUBSTR(@var1, 190, 32),
			DRUG_AMT = SUBSTR(@var1, 222, 8),
			DSVC_AMT = SUBSTR(@var1, 230, 8),
			T_APPL_AMT = SUBSTR(@var1, 238, 8),
			SEX = SUBSTR(@var1, 246, 1),
			PART_NO = SUBSTR(@var1, 247, 3),
			SPE_MET_AMT = SUBSTR(@var1, 250, 7),
			PART_AMT = SUBSTR(@var1, 257, 4),
			T_AMT = SUBSTR(@var1, 261, 8),
			ICD9CM_CODE = SUBSTR(@var1, 269, 15),
			ICD9CM_CODE1 = SUBSTR(@var1, 284, 15);"""

	if dbtype == "GO":
		if year >= 1996 and year <= 2006:
			q1 = """SET FEE_YM = str_to_date(SUBSTR(@var1, 1, 6), "%Y%m"),
			APPL_TYPE = SUBSTR(@var1, 7, 1),
			HOSP_ID = SUBSTR(@var1, 8, 34),
			APPL_DATE = str_to_date(SUBSTR(@var1, 42, 8), "%Y%m%d"),
			CASE_TYPE = SUBSTR(@var1, 50, 1),
			SEQ_NO = SUBSTR(@var1, 51, 6),
			DRUG_NO = SUBSTR(@var1, 57, 12),
			DRUG_USE = SUBSTR(@var1, 69, 6),
			TOTAL_QTY = SUBSTR(@var1, 75, 7),
			UNIT_PRICE = SUBSTR(@var1, 82, 10),
			TOTAL_AMT = SUBSTR(@var1, 92, 8);"""
		if year >= 2007:
			q1 = """SET FEE_YM = str_to_date(SUBSTR(@var1, 1, 6), "%Y%m"),
			APPL_TYPE = SUBSTR(@var1, 7, 1),
			HOSP_ID = SUBSTR(@var1, 8, 34),
			APPL_DATE = str_to_date(SUBSTR(@var1, 42, 8), "%Y%m%d"),
			CASE_TYPE = SUBSTR(@var1, 50, 1),
			SEQ_NO = SUBSTR(@var1, 51, 6),
			DRUG_NO = SUBSTR(@var1, 57, 12),
			DRUG_USE = SUBSTR(@var1, 69, 6),
			TOTAL_QTY = SUBSTR(@var1, 75, 7),
			UNIT_PRICE = SUBSTR(@var1, 82, 10),
			TOTAL_AMT = SUBSTR(@var1, 92, 8),
			ORDER_SEQ_NO = SUBSTR(@var1, 100, 5);"""

	if dbtype == "ID":
		if year <= 1999:
			q1 = """SET ID = SUBSTR(@var1, 1, 32),
			INS_ID = SUBSTR(@var1, 33, 32),
			INS_ID_TYPE = SUBSTR(@var1, 65, 1),
			INS_AMT = SUBSTR(@var1, 66, 6),
			ID_BIRTHDAY = str_to_date(SUBSTR(@var1, 72, 8), "%Y%m%d"),
			ID_SEX = SUBSTR(@var1, 80, 1),
			INS_RELATION = SUBSTR(@var1, 81, 1),
			UNIT_INS_TYPE = SUBSTR(@var1, 82, 3),
			REG_ZIP_CODE = SUBSTR(@var1, 85, 4),
			ID_IN_TYPE = SUBSTR(@var1, 89, 1),
			ID_IN_DATE = str_to_date(SUBSTR(@var1, 90, 8), "%Y%m%d"),
			ID_OUT_TYPE = SUBSTR(@var1, 98, 1),
			ID_OUT_DATE = str_to_date(SUBSTR(@var1, 99, 8), "%Y%m%d");"""
		if year >= 2000:
			q1 = """SET ID = SUBSTR(@var1, 1, 32),
			INS_ID = SUBSTR(@var1, 33, 32),
			INS_ID_TYPE = SUBSTR(@var1, 65, 1),
			INS_AMT = SUBSTR(@var1, 66, 6),
			ID_BIRTHDAY = str_to_date(SUBSTR(@var1, 72, 8), "%Y%m%d"),
			ID_SEX = SUBSTR(@var1, 80, 1),
			INS_RELATION = SUBSTR(@var1, 81, 1),
			UNIT_INS_TYPE = SUBSTR(@var1, 82, 3),
			REG_ZIP_CODE = SUBSTR(@var1, 85, 4),
			TX_CODE = SUBSTR(@var1, 89, 2),
			ID_IN_DATE = str_to_date(SUBSTR(@var1, 91, 8), "%Y%m%d"),
			ID_OUT_DATE = str_to_date(SUBSTR(@var1, 99, 8), "%Y%m%d");"""

	if dbtype == "DRUG":
			q1 = """SET DRUG_ID = SUBSTR(@var1, 1, 10),
			DRUG_NAME = SUBSTR(@var1, 11, 120),
			DRCON_NAME = SUBSTR(@var1, 131, 50),
			DRUG_ITEM = SUBSTR(@var1, 181, 6),
			ITEM_C_NAME = SUBSTR(@var1, 187, 50),
			ITEM_E_NAME = SUBSTR(@var1, 237, 50),
			DOSE_NAME = SUBSTR(@var1, 287, 50),
			TYPE_NAME = SUBSTR(@var1, 337, 10),
			TYPEUNIT_NAME = SUBSTR(@var1, 347, 50),
			DRCON_QTY = SUBSTR(@var1, 397, 12),
			DRCON_DRUGTYPE = SUBSTR(@var1, 409, 50),
			DRUG_MULTI = SUBSTR(@var1, 459, 11),
			DRGIST_NAME = SUBSTR(@var1, 470, 50),
			DRUG_NOUSE_DATE = str_to_date(SUBSTR(@var1, 520, 8), "%Y%m%d"),
			DRUG_PRICE = SUBSTR(@var1, 528, 11);"""
	
	return q + q1

import os
root_dir = os.getcwd()

#import MySQLdb
 
# �s���� MySQL
#db = MySQLdb.connect(host="localhost", user="root", passwd="", db="NHIRD1M")
#cursor = db.cursor()
 
for dirname, dirnames, filenames in os.walk(root_dir):
#    for subdirname in dirnames:
#        print os.path.join(dirname, subdirname)
    for filename in filenames:
#		print os.path.join(dirname, filename)
		sql = q_load(dirname, filename)
		if sql:
			print sql
			# cursor.execute(sql)
			# result = cursor.fetchall()
			# for record in result:
				# print record[0]

				