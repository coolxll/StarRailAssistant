import gettext
import locale
from utils.map import Map

locale.setlocale(locale.LC_ALL, 'zh_CN.UTF-8')

from Honkai_Star_Rail import SRA

loc = ('zh_CN','UTF-8')
t = gettext.translation('sra', 'locale', languages=[loc[0]])
_ = t.gettext

''
sra = SRA()
sra.load_plugin()
sra.run_plugins()

map_instance = Map(_("崩坏：星穹铁道"), _("模拟器"), "12a8d6de", "/usr/local/bin/adb")
map_instance.start_map('3-3_4')