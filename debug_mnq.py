import gettext
import locale

from Honkai_Star_Rail import SRA
from utils.config import get_folder

loc = locale.getdefaultlocale()
if loc[0] not in get_folder("locale"):
    loc[0] = "zh_CN"
t = gettext.translation('sra', 'locale', languages=[loc[0]])
_ = t.gettext


sra = SRA()
sra.load_plugin()
sra.run_plugins()
sra.main_start()
sra.main(platform=_("模拟器"), start='1-3_1')
