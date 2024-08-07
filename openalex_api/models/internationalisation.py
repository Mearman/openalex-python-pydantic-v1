# coding: utf-8

"""
    OpenAlex

    ![](https://raw.githubusercontent.com/ourresearch/openalex-docs/main/.gitbook/assets/OpenAlex-logo-5.png)  **OpenAlex** is a fully open catalog of the global research system.  It's named after the [ancient Library of Alexandria](https://en.wikipedia.org/wiki/Library_of_Alexandria) and made by the nonprofit [OurResearch](https://ourresearch.org/).  ## OpenAPI Specification  [Mearman/openalex-api-spec](https://github.com/Mearman/openalex-api-spec)  This OpenAPI specification is reverse-engineered and derived from spec generated by [openapi-devtools](https://github.com/AndrewWalsh/openapi-devtools).  The specification document itself is OpenAPI version 3.1 and is generated from TypeScript source code.  [![Open in](https://img.shields.io/badge/Open%20in-Swagger%20UI-85EA2D?style=for-the-badge&logo=Swagger&link=https://mearman.github.io/openalex-swagger-ui-react/)](https://mearman.github.io/openalex-swagger-ui-react/)  **[Releases](https://github.com/Mearman/openalex-api-spec/releases)**  ## Clients  [![TypeScript](https://img.shields.io/badge/TypeScript-3178C6?style=for-the-badge&logo=TypeScript&logoColor=white&link=https://github.com/Mearman/openalex-typescript)](https://github.com/Mearman/openalex-typescript)  [![TypeScript Fetch](https://img.shields.io/badge/TypeScript%20Fetch-3178C6?style=for-the-badge&logo=TypeScript&logoColor=white&link=https://github.com/Mearman/openalex-typescript-fetch)](https://github.com/Mearman/openalex-typescript-fetch)  [![TypeScript Node](https://img.shields.io/badge/TypeScript%20Node-339933?style=for-the-badge&logo=Node.js&logoColor=white&link=https://github.com/Mearman/openalex-typescript-node)](https://github.com/Mearman/openalex-typescript-node)  [![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=Python&logoColor=white&link=https://github.com/Mearman/openalex-python)](https://github.com/Mearman/openalex-python) [![Open in](https://img.shields.io/badge/Open%20in-CodeSpaces-181717?style=for-the-badge&logo=GitHub&link=https://codespaces.new/Mearman/openalex-python)](https://codespaces.new/Mearman/openalex-python) [![Open in](https://img.shields.io/badge/Open%20in-Colab-F9AB00?style=for-the-badge&logo=Google%20Colab&link=https://colab.research.google.com/github/Mearman/openalex-python/blob/main/README.ipynb)](https://colab.research.google.com/github/Mearman/openalex-python/blob/main/README.ipynb)  ---

    The version of the OpenAPI document: 0.3.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional
from pydantic import BaseModel, Field, StrictStr

class Internationalisation(BaseModel):
    """
    Internationalisation
    """
    ab: Optional[StrictStr] = None
    ace: Optional[StrictStr] = None
    aeb_arab: Optional[StrictStr] = Field(default=None, alias="aeb-arab")
    af: Optional[StrictStr] = None
    ak: Optional[StrictStr] = None
    alt: Optional[StrictStr] = None
    am: Optional[StrictStr] = None
    an: Optional[StrictStr] = None
    ang: Optional[StrictStr] = None
    ar: Optional[StrictStr] = None
    arc: Optional[StrictStr] = None
    ary: Optional[StrictStr] = None
    arz: Optional[StrictStr] = None
    var_as: Optional[StrictStr] = Field(default=None, alias="as")
    ast: Optional[StrictStr] = None
    atj: Optional[StrictStr] = None
    ay: Optional[StrictStr] = None
    az: Optional[StrictStr] = None
    azb: Optional[StrictStr] = None
    ba: Optional[StrictStr] = None
    ban: Optional[StrictStr] = None
    bar: Optional[StrictStr] = None
    bcl: Optional[StrictStr] = None
    be: Optional[StrictStr] = None
    be_tarask: Optional[StrictStr] = Field(default=None, alias="be-tarask")
    bg: Optional[StrictStr] = None
    bho: Optional[StrictStr] = None
    bi: Optional[StrictStr] = None
    bm: Optional[StrictStr] = None
    bn: Optional[StrictStr] = None
    bo: Optional[StrictStr] = None
    bpy: Optional[StrictStr] = None
    br: Optional[StrictStr] = None
    bs: Optional[StrictStr] = None
    bxr: Optional[StrictStr] = None
    ca: Optional[StrictStr] = None
    cbk_zam: Optional[StrictStr] = Field(default=None, alias="cbk-zam")
    cdo: Optional[StrictStr] = None
    ce: Optional[StrictStr] = None
    ceb: Optional[StrictStr] = None
    chr: Optional[StrictStr] = None
    ckb: Optional[StrictStr] = None
    co: Optional[StrictStr] = None
    crh: Optional[StrictStr] = None
    crh_latn: Optional[StrictStr] = Field(default=None, alias="crh-latn")
    cs: Optional[StrictStr] = None
    csb: Optional[StrictStr] = None
    cv: Optional[StrictStr] = None
    cy: Optional[StrictStr] = None
    da: Optional[StrictStr] = None
    de: Optional[StrictStr] = None
    de_at: Optional[StrictStr] = Field(default=None, alias="de-at")
    de_ch: Optional[StrictStr] = Field(default=None, alias="de-ch")
    diq: Optional[StrictStr] = None
    dv: Optional[StrictStr] = None
    el: Optional[StrictStr] = None
    eml: Optional[StrictStr] = None
    en: StrictStr = Field(...)
    en_ca: Optional[StrictStr] = Field(default=None, alias="en-ca")
    en_gb: Optional[StrictStr] = Field(default=None, alias="en-gb")
    en_us: Optional[StrictStr] = Field(default=None, alias="en-us")
    eo: Optional[StrictStr] = None
    es: Optional[StrictStr] = None
    et: Optional[StrictStr] = None
    eu: Optional[StrictStr] = None
    ext: Optional[StrictStr] = None
    fa: Optional[StrictStr] = None
    fi: Optional[StrictStr] = None
    fo: Optional[StrictStr] = None
    fr: Optional[StrictStr] = None
    frc: Optional[StrictStr] = None
    frp: Optional[StrictStr] = None
    frr: Optional[StrictStr] = None
    fur: Optional[StrictStr] = None
    fy: Optional[StrictStr] = None
    ga: Optional[StrictStr] = None
    gan: Optional[StrictStr] = None
    gan_hans: Optional[StrictStr] = Field(default=None, alias="gan-hans")
    gan_hant: Optional[StrictStr] = Field(default=None, alias="gan-hant")
    gcr: Optional[StrictStr] = None
    gd: Optional[StrictStr] = None
    gl: Optional[StrictStr] = None
    gn: Optional[StrictStr] = None
    gpe: Optional[StrictStr] = None
    gsw: Optional[StrictStr] = None
    gu: Optional[StrictStr] = None
    gv: Optional[StrictStr] = None
    ha: Optional[StrictStr] = None
    hak: Optional[StrictStr] = None
    he: Optional[StrictStr] = None
    hi: Optional[StrictStr] = None
    hif: Optional[StrictStr] = None
    hr: Optional[StrictStr] = None
    hsb: Optional[StrictStr] = None
    ht: Optional[StrictStr] = None
    hu: Optional[StrictStr] = None
    hy: Optional[StrictStr] = None
    hyw: Optional[StrictStr] = None
    ia: Optional[StrictStr] = None
    id: Optional[StrictStr] = None
    ie: Optional[StrictStr] = None
    ig: Optional[StrictStr] = None
    ilo: Optional[StrictStr] = None
    inh: Optional[StrictStr] = None
    io: Optional[StrictStr] = None
    var_is: Optional[StrictStr] = Field(default=None, alias="is")
    it: Optional[StrictStr] = None
    iu: Optional[StrictStr] = None
    ja: Optional[StrictStr] = None
    jam: Optional[StrictStr] = None
    jv: Optional[StrictStr] = None
    ka: Optional[StrictStr] = None
    kaa: Optional[StrictStr] = None
    kab: Optional[StrictStr] = None
    kbp: Optional[StrictStr] = None
    kg: Optional[StrictStr] = None
    kk: Optional[StrictStr] = None
    kk_arab: Optional[StrictStr] = Field(default=None, alias="kk-arab")
    kk_cn: Optional[StrictStr] = Field(default=None, alias="kk-cn")
    kk_cyrl: Optional[StrictStr] = Field(default=None, alias="kk-cyrl")
    kk_kz: Optional[StrictStr] = Field(default=None, alias="kk-kz")
    kk_latn: Optional[StrictStr] = Field(default=None, alias="kk-latn")
    kk_tr: Optional[StrictStr] = Field(default=None, alias="kk-tr")
    kl: Optional[StrictStr] = None
    km: Optional[StrictStr] = None
    kn: Optional[StrictStr] = None
    ko: Optional[StrictStr] = None
    ko_kp: Optional[StrictStr] = Field(default=None, alias="ko-kp")
    krc: Optional[StrictStr] = None
    ks: Optional[StrictStr] = None
    ksh: Optional[StrictStr] = None
    ku: Optional[StrictStr] = None
    ku_latn: Optional[StrictStr] = Field(default=None, alias="ku-latn")
    kw: Optional[StrictStr] = None
    ky: Optional[StrictStr] = None
    la: Optional[StrictStr] = None
    lad: Optional[StrictStr] = None
    lb: Optional[StrictStr] = None
    lfn: Optional[StrictStr] = None
    li: Optional[StrictStr] = None
    lij: Optional[StrictStr] = None
    lld: Optional[StrictStr] = None
    lmo: Optional[StrictStr] = None
    lo: Optional[StrictStr] = None
    lt: Optional[StrictStr] = None
    lv: Optional[StrictStr] = None
    lzh: Optional[StrictStr] = None
    mai: Optional[StrictStr] = None
    mg: Optional[StrictStr] = None
    min: Optional[StrictStr] = None
    mk: Optional[StrictStr] = None
    ml: Optional[StrictStr] = None
    mn: Optional[StrictStr] = None
    mni: Optional[StrictStr] = None
    mr: Optional[StrictStr] = None
    ms: Optional[StrictStr] = None
    ms_arab: Optional[StrictStr] = Field(default=None, alias="ms-arab")
    mt: Optional[StrictStr] = None
    mwl: Optional[StrictStr] = None
    my: Optional[StrictStr] = None
    mzn: Optional[StrictStr] = None
    nah: Optional[StrictStr] = None
    nan: Optional[StrictStr] = None
    nap: Optional[StrictStr] = None
    nb: Optional[StrictStr] = None
    nds: Optional[StrictStr] = None
    nds_nl: Optional[StrictStr] = Field(default=None, alias="nds-nl")
    ne: Optional[StrictStr] = None
    new: Optional[StrictStr] = None
    nia: Optional[StrictStr] = None
    nl: Optional[StrictStr] = None
    nn: Optional[StrictStr] = None
    nov: Optional[StrictStr] = None
    nqo: Optional[StrictStr] = None
    nrm: Optional[StrictStr] = None
    oc: Optional[StrictStr] = None
    var_or: Optional[StrictStr] = Field(default=None, alias="or")
    os: Optional[StrictStr] = None
    pa: Optional[StrictStr] = None
    pam: Optional[StrictStr] = None
    pap: Optional[StrictStr] = None
    pcd: Optional[StrictStr] = None
    pdc: Optional[StrictStr] = None
    pih: Optional[StrictStr] = None
    pl: Optional[StrictStr] = None
    pms: Optional[StrictStr] = None
    pnb: Optional[StrictStr] = None
    ps: Optional[StrictStr] = None
    pt: Optional[StrictStr] = None
    pt_br: Optional[StrictStr] = Field(default=None, alias="pt-br")
    qu: Optional[StrictStr] = None
    rm: Optional[StrictStr] = None
    ro: Optional[StrictStr] = None
    ru: Optional[StrictStr] = None
    rue: Optional[StrictStr] = None
    rw: Optional[StrictStr] = None
    sa: Optional[StrictStr] = None
    sah: Optional[StrictStr] = None
    sat: Optional[StrictStr] = None
    sc: Optional[StrictStr] = None
    scn: Optional[StrictStr] = None
    sco: Optional[StrictStr] = None
    sd: Optional[StrictStr] = None
    se: Optional[StrictStr] = None
    sgs: Optional[StrictStr] = None
    sh: Optional[StrictStr] = None
    shi: Optional[StrictStr] = None
    si: Optional[StrictStr] = None
    sk: Optional[StrictStr] = None
    sl: Optional[StrictStr] = None
    smn: Optional[StrictStr] = None
    sms: Optional[StrictStr] = None
    so: Optional[StrictStr] = None
    sq: Optional[StrictStr] = None
    sr: Optional[StrictStr] = None
    sr_ec: Optional[StrictStr] = Field(default=None, alias="sr-ec")
    sr_el: Optional[StrictStr] = Field(default=None, alias="sr-el")
    stq: Optional[StrictStr] = None
    su: Optional[StrictStr] = None
    sv: Optional[StrictStr] = None
    sw: Optional[StrictStr] = None
    syl: Optional[StrictStr] = None
    szl: Optional[StrictStr] = None
    ta: Optional[StrictStr] = None
    te: Optional[StrictStr] = None
    tg: Optional[StrictStr] = None
    tg_latn: Optional[StrictStr] = Field(default=None, alias="tg-latn")
    th: Optional[StrictStr] = None
    ti: Optional[StrictStr] = None
    tk: Optional[StrictStr] = None
    tl: Optional[StrictStr] = None
    tr: Optional[StrictStr] = None
    ts: Optional[StrictStr] = None
    tt: Optional[StrictStr] = None
    tt_cyrl: Optional[StrictStr] = Field(default=None, alias="tt-cyrl")
    tw: Optional[StrictStr] = None
    ug: Optional[StrictStr] = None
    uk: Optional[StrictStr] = None
    ur: Optional[StrictStr] = None
    uz: Optional[StrictStr] = None
    vec: Optional[StrictStr] = None
    vi: Optional[StrictStr] = None
    vls: Optional[StrictStr] = None
    vo: Optional[StrictStr] = None
    vro: Optional[StrictStr] = None
    wa: Optional[StrictStr] = None
    war: Optional[StrictStr] = None
    wo: Optional[StrictStr] = None
    wuu: Optional[StrictStr] = None
    xmf: Optional[StrictStr] = None
    yi: Optional[StrictStr] = None
    yo: Optional[StrictStr] = None
    yue: Optional[StrictStr] = None
    za: Optional[StrictStr] = None
    zh: Optional[StrictStr] = None
    zh_cn: Optional[StrictStr] = Field(default=None, alias="zh-cn")
    zh_hans: Optional[StrictStr] = Field(default=None, alias="zh-hans")
    zh_hant: Optional[StrictStr] = Field(default=None, alias="zh-hant")
    zh_hk: Optional[StrictStr] = Field(default=None, alias="zh-hk")
    zh_mo: Optional[StrictStr] = Field(default=None, alias="zh-mo")
    zh_my: Optional[StrictStr] = Field(default=None, alias="zh-my")
    zh_sg: Optional[StrictStr] = Field(default=None, alias="zh-sg")
    zh_tw: Optional[StrictStr] = Field(default=None, alias="zh-tw")
    zu: Optional[StrictStr] = None
    __properties = ["ab", "ace", "aeb-arab", "af", "ak", "alt", "am", "an", "ang", "ar", "arc", "ary", "arz", "as", "ast", "atj", "ay", "az", "azb", "ba", "ban", "bar", "bcl", "be", "be-tarask", "bg", "bho", "bi", "bm", "bn", "bo", "bpy", "br", "bs", "bxr", "ca", "cbk-zam", "cdo", "ce", "ceb", "chr", "ckb", "co", "crh", "crh-latn", "cs", "csb", "cv", "cy", "da", "de", "de-at", "de-ch", "diq", "dv", "el", "eml", "en", "en-ca", "en-gb", "en-us", "eo", "es", "et", "eu", "ext", "fa", "fi", "fo", "fr", "frc", "frp", "frr", "fur", "fy", "ga", "gan", "gan-hans", "gan-hant", "gcr", "gd", "gl", "gn", "gpe", "gsw", "gu", "gv", "ha", "hak", "he", "hi", "hif", "hr", "hsb", "ht", "hu", "hy", "hyw", "ia", "id", "ie", "ig", "ilo", "inh", "io", "is", "it", "iu", "ja", "jam", "jv", "ka", "kaa", "kab", "kbp", "kg", "kk", "kk-arab", "kk-cn", "kk-cyrl", "kk-kz", "kk-latn", "kk-tr", "kl", "km", "kn", "ko", "ko-kp", "krc", "ks", "ksh", "ku", "ku-latn", "kw", "ky", "la", "lad", "lb", "lfn", "li", "lij", "lld", "lmo", "lo", "lt", "lv", "lzh", "mai", "mg", "min", "mk", "ml", "mn", "mni", "mr", "ms", "ms-arab", "mt", "mwl", "my", "mzn", "nah", "nan", "nap", "nb", "nds", "nds-nl", "ne", "new", "nia", "nl", "nn", "nov", "nqo", "nrm", "oc", "or", "os", "pa", "pam", "pap", "pcd", "pdc", "pih", "pl", "pms", "pnb", "ps", "pt", "pt-br", "qu", "rm", "ro", "ru", "rue", "rw", "sa", "sah", "sat", "sc", "scn", "sco", "sd", "se", "sgs", "sh", "shi", "si", "sk", "sl", "smn", "sms", "so", "sq", "sr", "sr-ec", "sr-el", "stq", "su", "sv", "sw", "syl", "szl", "ta", "te", "tg", "tg-latn", "th", "ti", "tk", "tl", "tr", "ts", "tt", "tt-cyrl", "tw", "ug", "uk", "ur", "uz", "vec", "vi", "vls", "vo", "vro", "wa", "war", "wo", "wuu", "xmf", "yi", "yo", "yue", "za", "zh", "zh-cn", "zh-hans", "zh-hant", "zh-hk", "zh-mo", "zh-my", "zh-sg", "zh-tw", "zu"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Internationalisation:
        """Create an instance of Internationalisation from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Internationalisation:
        """Create an instance of Internationalisation from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Internationalisation.parse_obj(obj)

        _obj = Internationalisation.parse_obj({
            "ab": obj.get("ab"),
            "ace": obj.get("ace"),
            "aeb_arab": obj.get("aeb-arab"),
            "af": obj.get("af"),
            "ak": obj.get("ak"),
            "alt": obj.get("alt"),
            "am": obj.get("am"),
            "an": obj.get("an"),
            "ang": obj.get("ang"),
            "ar": obj.get("ar"),
            "arc": obj.get("arc"),
            "ary": obj.get("ary"),
            "arz": obj.get("arz"),
            "var_as": obj.get("as"),
            "ast": obj.get("ast"),
            "atj": obj.get("atj"),
            "ay": obj.get("ay"),
            "az": obj.get("az"),
            "azb": obj.get("azb"),
            "ba": obj.get("ba"),
            "ban": obj.get("ban"),
            "bar": obj.get("bar"),
            "bcl": obj.get("bcl"),
            "be": obj.get("be"),
            "be_tarask": obj.get("be-tarask"),
            "bg": obj.get("bg"),
            "bho": obj.get("bho"),
            "bi": obj.get("bi"),
            "bm": obj.get("bm"),
            "bn": obj.get("bn"),
            "bo": obj.get("bo"),
            "bpy": obj.get("bpy"),
            "br": obj.get("br"),
            "bs": obj.get("bs"),
            "bxr": obj.get("bxr"),
            "ca": obj.get("ca"),
            "cbk_zam": obj.get("cbk-zam"),
            "cdo": obj.get("cdo"),
            "ce": obj.get("ce"),
            "ceb": obj.get("ceb"),
            "chr": obj.get("chr"),
            "ckb": obj.get("ckb"),
            "co": obj.get("co"),
            "crh": obj.get("crh"),
            "crh_latn": obj.get("crh-latn"),
            "cs": obj.get("cs"),
            "csb": obj.get("csb"),
            "cv": obj.get("cv"),
            "cy": obj.get("cy"),
            "da": obj.get("da"),
            "de": obj.get("de"),
            "de_at": obj.get("de-at"),
            "de_ch": obj.get("de-ch"),
            "diq": obj.get("diq"),
            "dv": obj.get("dv"),
            "el": obj.get("el"),
            "eml": obj.get("eml"),
            "en": obj.get("en"),
            "en_ca": obj.get("en-ca"),
            "en_gb": obj.get("en-gb"),
            "en_us": obj.get("en-us"),
            "eo": obj.get("eo"),
            "es": obj.get("es"),
            "et": obj.get("et"),
            "eu": obj.get("eu"),
            "ext": obj.get("ext"),
            "fa": obj.get("fa"),
            "fi": obj.get("fi"),
            "fo": obj.get("fo"),
            "fr": obj.get("fr"),
            "frc": obj.get("frc"),
            "frp": obj.get("frp"),
            "frr": obj.get("frr"),
            "fur": obj.get("fur"),
            "fy": obj.get("fy"),
            "ga": obj.get("ga"),
            "gan": obj.get("gan"),
            "gan_hans": obj.get("gan-hans"),
            "gan_hant": obj.get("gan-hant"),
            "gcr": obj.get("gcr"),
            "gd": obj.get("gd"),
            "gl": obj.get("gl"),
            "gn": obj.get("gn"),
            "gpe": obj.get("gpe"),
            "gsw": obj.get("gsw"),
            "gu": obj.get("gu"),
            "gv": obj.get("gv"),
            "ha": obj.get("ha"),
            "hak": obj.get("hak"),
            "he": obj.get("he"),
            "hi": obj.get("hi"),
            "hif": obj.get("hif"),
            "hr": obj.get("hr"),
            "hsb": obj.get("hsb"),
            "ht": obj.get("ht"),
            "hu": obj.get("hu"),
            "hy": obj.get("hy"),
            "hyw": obj.get("hyw"),
            "ia": obj.get("ia"),
            "id": obj.get("id"),
            "ie": obj.get("ie"),
            "ig": obj.get("ig"),
            "ilo": obj.get("ilo"),
            "inh": obj.get("inh"),
            "io": obj.get("io"),
            "var_is": obj.get("is"),
            "it": obj.get("it"),
            "iu": obj.get("iu"),
            "ja": obj.get("ja"),
            "jam": obj.get("jam"),
            "jv": obj.get("jv"),
            "ka": obj.get("ka"),
            "kaa": obj.get("kaa"),
            "kab": obj.get("kab"),
            "kbp": obj.get("kbp"),
            "kg": obj.get("kg"),
            "kk": obj.get("kk"),
            "kk_arab": obj.get("kk-arab"),
            "kk_cn": obj.get("kk-cn"),
            "kk_cyrl": obj.get("kk-cyrl"),
            "kk_kz": obj.get("kk-kz"),
            "kk_latn": obj.get("kk-latn"),
            "kk_tr": obj.get("kk-tr"),
            "kl": obj.get("kl"),
            "km": obj.get("km"),
            "kn": obj.get("kn"),
            "ko": obj.get("ko"),
            "ko_kp": obj.get("ko-kp"),
            "krc": obj.get("krc"),
            "ks": obj.get("ks"),
            "ksh": obj.get("ksh"),
            "ku": obj.get("ku"),
            "ku_latn": obj.get("ku-latn"),
            "kw": obj.get("kw"),
            "ky": obj.get("ky"),
            "la": obj.get("la"),
            "lad": obj.get("lad"),
            "lb": obj.get("lb"),
            "lfn": obj.get("lfn"),
            "li": obj.get("li"),
            "lij": obj.get("lij"),
            "lld": obj.get("lld"),
            "lmo": obj.get("lmo"),
            "lo": obj.get("lo"),
            "lt": obj.get("lt"),
            "lv": obj.get("lv"),
            "lzh": obj.get("lzh"),
            "mai": obj.get("mai"),
            "mg": obj.get("mg"),
            "min": obj.get("min"),
            "mk": obj.get("mk"),
            "ml": obj.get("ml"),
            "mn": obj.get("mn"),
            "mni": obj.get("mni"),
            "mr": obj.get("mr"),
            "ms": obj.get("ms"),
            "ms_arab": obj.get("ms-arab"),
            "mt": obj.get("mt"),
            "mwl": obj.get("mwl"),
            "my": obj.get("my"),
            "mzn": obj.get("mzn"),
            "nah": obj.get("nah"),
            "nan": obj.get("nan"),
            "nap": obj.get("nap"),
            "nb": obj.get("nb"),
            "nds": obj.get("nds"),
            "nds_nl": obj.get("nds-nl"),
            "ne": obj.get("ne"),
            "new": obj.get("new"),
            "nia": obj.get("nia"),
            "nl": obj.get("nl"),
            "nn": obj.get("nn"),
            "nov": obj.get("nov"),
            "nqo": obj.get("nqo"),
            "nrm": obj.get("nrm"),
            "oc": obj.get("oc"),
            "var_or": obj.get("or"),
            "os": obj.get("os"),
            "pa": obj.get("pa"),
            "pam": obj.get("pam"),
            "pap": obj.get("pap"),
            "pcd": obj.get("pcd"),
            "pdc": obj.get("pdc"),
            "pih": obj.get("pih"),
            "pl": obj.get("pl"),
            "pms": obj.get("pms"),
            "pnb": obj.get("pnb"),
            "ps": obj.get("ps"),
            "pt": obj.get("pt"),
            "pt_br": obj.get("pt-br"),
            "qu": obj.get("qu"),
            "rm": obj.get("rm"),
            "ro": obj.get("ro"),
            "ru": obj.get("ru"),
            "rue": obj.get("rue"),
            "rw": obj.get("rw"),
            "sa": obj.get("sa"),
            "sah": obj.get("sah"),
            "sat": obj.get("sat"),
            "sc": obj.get("sc"),
            "scn": obj.get("scn"),
            "sco": obj.get("sco"),
            "sd": obj.get("sd"),
            "se": obj.get("se"),
            "sgs": obj.get("sgs"),
            "sh": obj.get("sh"),
            "shi": obj.get("shi"),
            "si": obj.get("si"),
            "sk": obj.get("sk"),
            "sl": obj.get("sl"),
            "smn": obj.get("smn"),
            "sms": obj.get("sms"),
            "so": obj.get("so"),
            "sq": obj.get("sq"),
            "sr": obj.get("sr"),
            "sr_ec": obj.get("sr-ec"),
            "sr_el": obj.get("sr-el"),
            "stq": obj.get("stq"),
            "su": obj.get("su"),
            "sv": obj.get("sv"),
            "sw": obj.get("sw"),
            "syl": obj.get("syl"),
            "szl": obj.get("szl"),
            "ta": obj.get("ta"),
            "te": obj.get("te"),
            "tg": obj.get("tg"),
            "tg_latn": obj.get("tg-latn"),
            "th": obj.get("th"),
            "ti": obj.get("ti"),
            "tk": obj.get("tk"),
            "tl": obj.get("tl"),
            "tr": obj.get("tr"),
            "ts": obj.get("ts"),
            "tt": obj.get("tt"),
            "tt_cyrl": obj.get("tt-cyrl"),
            "tw": obj.get("tw"),
            "ug": obj.get("ug"),
            "uk": obj.get("uk"),
            "ur": obj.get("ur"),
            "uz": obj.get("uz"),
            "vec": obj.get("vec"),
            "vi": obj.get("vi"),
            "vls": obj.get("vls"),
            "vo": obj.get("vo"),
            "vro": obj.get("vro"),
            "wa": obj.get("wa"),
            "war": obj.get("war"),
            "wo": obj.get("wo"),
            "wuu": obj.get("wuu"),
            "xmf": obj.get("xmf"),
            "yi": obj.get("yi"),
            "yo": obj.get("yo"),
            "yue": obj.get("yue"),
            "za": obj.get("za"),
            "zh": obj.get("zh"),
            "zh_cn": obj.get("zh-cn"),
            "zh_hans": obj.get("zh-hans"),
            "zh_hant": obj.get("zh-hant"),
            "zh_hk": obj.get("zh-hk"),
            "zh_mo": obj.get("zh-mo"),
            "zh_my": obj.get("zh-my"),
            "zh_sg": obj.get("zh-sg"),
            "zh_tw": obj.get("zh-tw"),
            "zu": obj.get("zu")
        })
        return _obj


