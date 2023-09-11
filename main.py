from starbot.core.bot import StarBot
from starbot.core.datasource import JsonDataSource
from starbot.utils import config

config.set_credential(sessdata="ad73905a%2C1705516727%2C3badc%2A72DyP6picfqBeGUyU15hQV5l37XlN-R8KsCZh-xm3tQHNXGPJgDrP4dUGKSv5JpxYzPx4lXgAALQA", bili_jct="fd1301495788cf2560641b752eff2369", buvid3="00AF01DA-011A-4EAE-BDCA-582FDC8048B4167628infoc")
config.set("MASTER_QQ", 2461942798)
datasource = JsonDataSource("推送配置.json")
bot = StarBot(datasource)
bot.run()