import gettext
import locale
locale.setlocale(locale.LC_ALL, 'zh_CN.UTF-8')

from Honkai_Star_Rail import SRA

loc = ('zh_CN','UTF-8')
t = gettext.translation('sra', 'locale', languages=[loc[0]])
_ = t.gettext


sra = SRA()
sra.load_plugin()
sra.run_plugins()
sra.main(platform=_("模拟器"), start='2-5_1')
