from indic_transliteration import sanscript


def test_fix_lazy_anusvaara_itrans():
    assert sanscript.SCHEMES[sanscript.ITRANS].fix_lazy_anusvaara("shaMkara") == "sha~Nkara"
    assert sanscript.SCHEMES[sanscript.ITRANS].fix_lazy_anusvaara("saMchara") == "sa~nchara"
    assert sanscript.SCHEMES[sanscript.ITRANS].fix_lazy_anusvaara("ShaMDa") == "ShaNDa"
    assert sanscript.SCHEMES[sanscript.ITRANS].fix_lazy_anusvaara("shAMta") == "shAnta"
    assert sanscript.SCHEMES[sanscript.ITRANS].fix_lazy_anusvaara("sAMba") == "sAmba"
    assert sanscript.SCHEMES[sanscript.ITRANS].fix_lazy_anusvaara("saMvara") == "sav.Nvara"
    assert sanscript.SCHEMES[sanscript.ITRANS].fix_lazy_anusvaara("saMyukta") == "say.Nyukta"
    assert sanscript.SCHEMES[sanscript.ITRANS].fix_lazy_anusvaara("saMyukta", omit_yrl=True) == "saMyukta"
    assert sanscript.SCHEMES[sanscript.ITRANS].fix_lazy_anusvaara("saMyukta", omit_sam=True) == "saMyukta"
    assert sanscript.SCHEMES[sanscript.ITRANS].fix_lazy_anusvaara("saMlagna") == "sal.Nlagna"
    assert sanscript.SCHEMES[sanscript.ITRANS].fix_lazy_anusvaara("saMlagna", omit_sam=True) == "saMlagna"
    assert sanscript.SCHEMES[sanscript.ITRANS].fix_lazy_anusvaara("taM jitvA") == "ta~n jitvA"


def test_fix_lazy_anusvaara_slp():
    assert sanscript.SCHEMES[sanscript.SLP1].fix_lazy_anusvaara("aham") == "aham"
    assert sanscript.SCHEMES[sanscript.SLP1].fix_lazy_anusvaara("saMga") == "saNga"
    assert sanscript.SCHEMES[sanscript.SLP1].fix_lazy_anusvaara("saMga", omit_sam=True) == "saMga"


def test_optitrans_to_lay_indian():
    assert sanscript.SCHEMES[sanscript.OPTITRANS].to_lay_indian("taM jitvA") == "tam jitva"
    assert sanscript.SCHEMES[sanscript.OPTITRANS].to_lay_indian("kRShNa") == "krishna"

def test_get_standard_form():
    assert sanscript.SCHEMES[sanscript.IAST].get_standard_form("dŕ̥ṃhasva") == "dṛ́ṃhasva"
    assert sanscript.SCHEMES[sanscript.IAST].get_standard_form("pitŕ̥̄ṃs") == "pitṝ́ṃs"

def test_to_double_lettered():
    assert sanscript.SCHEMES[sanscript.OPTITRANS].get_double_lettered("taM jitvA pUraya") == "taM jitvaa puuraya"

def test_mark_off_non_indic_in_line():
    text = '05 The Śaivas’ Inclusivist View of Their Own and the Vaidikas’ Religion'
    assert sanscript.SCHEMES[sanscript.IAST].mark_off_non_indic_in_line(text) == "<05> <The> Śaivas’ <Inclusivist> <View> <of> <Their> <Own> <and> <the> <Vaidikas’> <Religion>"