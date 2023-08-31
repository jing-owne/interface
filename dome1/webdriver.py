

"""
https://www.jianshu.com/p/1b63c5f3c98e
#从selenium里面导入webdriver
from selenium import webdriver
http://chromedriver.storage.googleapis.com/index.html chrome://version/查看版本   chromedriver下载
#指定chrom的驱动
#执行到这里的时候Selenium会到指定的路径将chrome driver程序运行起来
driver = webdriver.Chrome('E:\ChromDriver\chromedriver.exe')
#driver = webdriver.Firefox()#这里是火狐的浏览器运行方法

#get 方法 打开指定网址
driver.get('http://www.baidu.com')

#选择网页元素
element_keyword = driver.find_element_by_id('kw')

#输入字符
element_keyword.send_keys('宋曲')

#找到搜索按钮
element_search_button = driver.find_element_by_id('su')


下面是对搜索结果的验证：
import time

#注意这里必须要等待时间，因为代码运行过快，代码运行完的时候页面还没加载出来就会找不到元素

time.sleep(2)

ret = driver.find_element_by_id('1')
print(ret.text)

if ret.text.startswith('宋曲'):#是不是已宋曲开头
    print('测试通过')
else:
    print('不通过')
#最后，driver.quit()让浏览器和驱动进程一起退出，不然桌面会有好多窗口
driver.quit()
下面是对代码的详细分析：

driver = webdriver.Chrome('E:\ChromDriver\chromedriver.exe')
执行到这里的时候Selenium会到指定的路径将chrom driver程序运行起来，chrome driver会将浏览器运行起来。成功后会返回一个WebDriver实例对象，通过它的方法，可以控制浏览器，我们可以把它想象成浏览器的遥控器一样。

浏览器运行起来后，通常第一件事情就是打开网址了。一般我们通过控制对象的get方法来控制浏览器打开指定网址
driver.get('http://www.baidu.com')
这一行执行后，web浏览器将会访问http://www.baidu.com这个网址。Selenium的官方文档说，不同的WebDriver和浏览器行为可能会有所不同。有的浏览器不一定等web页面完全加载完成，就返回了。当然通常我们希望的是加载完毕，再返回，不然可能页面上有的元素还没有出现，后续的操作可能有问题。这样还需要加入一些其他的代码等待某个关键的页面元素出现再进行后续操作。个人测试的情况看，Selenium 3的Chrom WebDriver驱动相应的chrom浏览器是会等待页面完全加载完成才返回的。所以我们可以放心。

接下来我们要查找到那个搜索输入栏网页元素，这里是根据该网页元素的id来选择的。

element_keyword = driver.find_element_by_id('kw')
网页元素的信息可以通过浏览器的debug功能来查看。怎么寻找网页元素，可以说是web自动化最重要的东西之一。下一节会讲到。

driver找到该元素的话，就会返回一个该元素的WebElement对象。我们接着就可以对其进行操作了，这个例子里面的操作，就是在这个输入框里面输入字符。
element_keyword.send_keys('宋曲')
后面就是在进行一次元素的选择和操作，找到搜索按钮，点击它。最后，执行下面的代码让浏览器和驱动进程一起退出

driver.quit()

"""
"""
安装Chromedriver 调用
from selenium import webdriver
import time
#coding:utf-8
 
chrome_path = "C:\webdriver\chromedriver.exe"
browser = webdriver.Chrome(executable_path=chrome_path)
browser.get("https://www.meituan.com/jiankangliren/2513304/")
 
time.sleep(5)
 
element = browser.find_element_by_class_name("toggle-btn").click()


# 查找标签
>>> label = chrome_obj.find_element_by_id("kw")
>>> label = chrome_obj.find_element_by_name("wd")
>>> label = chrome_obj.find_element_by_class_name("s_ipt")
>>> label = chrome_obj.find_element_by_tag_name("imput")
 
>>> label = chrome_obj.find_element_by_link_text("a标签中的内容 准确定位")  
>>> label = chrome_obj.find_element_by_partial_link_text("a标签中的内容 模糊定位 ")
 
>>> label = chrome_obj.find_element_by_xpath(“放入 copy 标签中的常css路径”)
>>> label = chrome_obj.find_element_by_css_selector(“input=[id='id_name'/name='name_name'/……/]")
"""
"""
# selenium 主要提供了8种定位元素方法：
find_element_by_id

find_element_by_name

find_element_by_link_text

find_element_by_partial_link_text

find_element_by_tag_name

find_element_by_class_name

find_element_by_css_selector

find_element_by_xpath

find_element_by_id("kw")
find_element_by_link_text('新闻')
find_element_by_partial_link_text("产品")
find_element_by_xpath('//*[@id="kw"]')
find_element_by_xpath('//*[@class="s_ipt"]')
find_element_by_xpath('//*input[@maxlength="255"]')
find_element_by_xpath('//*[@id="kw"]')
find_element_by_xpath("//span[@class='bg']/input") 往上级找，依次为爸爸、我
find_element_by_xpath("//form[@id='form']/span[@class='bg']/input") 往上级找，依次为爷爷、爸爸、我
find_element_by_xpath("//*[@id='kw' and @name='wd']") 使用条件组合
#css
find_element_by_css_selector("#kw") #号表示id
find_element_by_css_selector("[name=kw]") #号表示id
find_element_by_css_selector(".s_ipt") .表示class属性
find_element_by_css_selector("span.bg > input#kw") 父亲叫span,类为bg，我是input，id是kw，即往上找"""




"""
from selenium import webdriver  ##从selenium模块里面导入webdriver
import time  #导入时间模块

#driver = webdriver.Firefox()#这里是火狐的浏览器运行方法
driver = webdriver.Chrome()  #指定chrom的驱动执行这次访问
driver.get('http://www.baidu.com')  #get 方法 打开指定网址
element_keyword = driver.find_element_by_id('kw')  #定位网页元素
element_keyword.send_keys('python')  #输入搜索字符
element_search_button = driver.find_element_by_id('su').click()  #找到搜索按钮 点击
time.sleep(2)

ret = driver.find_element_by_id('1')   #定位元素id=1的地址
print(ret.text)   #输出搜索到的文本内容

if ret.text.startswith('python'):#验证是不是python开头  实际是Welcome开头哦
    print('pass')
else:
    print('fail')

driver.quit()  #让浏览器和驱动进程一起退出，不然桌面会有好多窗口

"""

# 一个页面最基本组成单元是元素，想要定位一个元素，我们需要特定的信息来说明这个元素的唯一特征。
"""
class SearchTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(15)
        self.driver.maximize_window()
        self.driver.get('http://www.baidu.com')
 
    def test_search_by_category(self):
        self.search_field = self.driver.find_element_by_id("kw")
        self.search_field.clear()
        self.search_field.send_keys('python')
        self.search_field.submit()

        products = self.driver.find_elements_by_xpath("//div[contains(@class, 'c-abstract')]")
        # 在webelement对象里面使用查找Xpath 查找时，必须使用.指明当前节点
        # food = driver.find_element_by_id('food')
        # eles = food.find_elements_by_xpath(".//p")    .指明当前节点
        # eles = food.find_elements_by_xpath("..")   查找当前节点的父节点
        self.assertEqual(11, len(products))
        #1. 如果两者一致, 程序继续往下运行
        #2. 如果两者不一致, 中断测试方法, 抛出异常信息 AssertionFailedError

    def test_search_by_cat(self):
        self.search_field = self.driver.find_element_by_id("kw")
        self.search_field.clear()
        self.search_field.send_keys('python')
        self.search_field.submit()
        products = self.driver.find_elements_by_xpath("//div[contains(@class, 'c-abstract')]")
        self.assertEqual(13, len(products))


    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)

"""
 
 ##############################################################################
"""
import unittest
from selenium import webdriver


class SearchTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(15)
        cls.driver.maximize_window()

        cls.driver.get('http://www.baidu.com')

    def test_search_by_category(self):
        self.search_field = self.driver.find_element_by_id("kw")
        self.search_field.clear()
        self.search_field.send_keys('python')
        self.search_field.submit()

        products = self.driver.find_elements_by_xpath("//div[contains(@class, 'c-abstract')]")

        self.assertEqual(13, len(products))

    def test_search_by_cat(self):
        self.search_field = self.driver.find_element_by_id("kw")
        self.search_field.clear()
        self.search_field.send_keys('python')
        self.search_field.submit()

        products = self.driver.find_elements_by_xpath("//div[contains(@class, 'c-abstract')]")

        self.assertEqual(10, len(products))

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)
"""

from time import sleep
from selenium import webdriver

driver = webdriver.Chrome()  #指定chrom的驱动执行这次访问
driver.get('http://www.baidu.com')  #get 方法 打开指定网址
element_keyword = driver.find_element_by_id('kw')  #定位网页元素
element_keyword.send_keys('python')  #输入搜索字符
element_search_button = driver.find_element_by_id('su').click()  #找到搜索按钮 点击

sleep(5) # 等待5秒
driver.quit()# 退出




from time import sleep
from selenium import webdriver

driver = webdriver.Chrome()  #指定chrom的驱动执行这次访问
driver.get('http://www.baidu.com')  #get 方法 打开指定网址
element_keyword = driver.find_element_by_name('wd')  #定位网页元素
element_keyword.send_keys('python')  #输入搜索字符
element_search_button = driver.find_element_by_id('su').click()  #找到搜索按钮 点击

sleep(5) # 等待5秒
driver.quit()# 退出


from time import sleep
from selenium import webdriver

driver = webdriver.Chrome()  #指定chrom的驱动执行这次访问
driver.get('http://www.baidu.com')  #get 方法 打开指定网址
element_keyword = driver.find_element_by_class_name('s_ipt')  #定位网页元素
element_keyword.send_keys('python')  #输入搜索字符
element_search_button = driver.find_element_by_id('su').click()  #找到搜索按钮 点击

sleep(5) # 等待5秒
driver.quit()# 退出


from time import sleep
from selenium import webdriver

driver = webdriver.Chrome()  #指定chrom的驱动执行这次访问
driver.get('http://www.baidu.com')  #get 方法 打开指定网址
element_keyword = driver.find_element_by_tag_name('input')  #定位网页元素
element_keyword.send_keys('python')  #输入搜索字符
element_search_button = driver.find_element_by_id('su').click()  #找到搜索按钮 点击

sleep(5) # 等待5秒
driver.quit()# 退出

from time import sleep
from selenium import webdriver

driver = webdriver.Chrome()  #指定chrom的驱动执行这次访问
driver.get('http://www.baidu.com')  #get 方法 打开指定网址
element_keyword = driver.find_element_by_link_text('贴吧').click()  #定位网页元素 点击
# element_keyword.send_keys('python')  #输入搜索字符
# element_search_button = driver.find_element_by_id('su').click()  #找到搜索按钮 点击

sleep(5) # 等待5秒
driver.quit()# 退出


from time import sleep
from selenium import webdriver

driver = webdriver.Chrome()  #指定chrom的驱动执行这次访问
driver.get('http://www.baidu.com')  #get 方法 打开指定网址
element_keyword = driver.find_element_by_link_text('贴吧').click()  #定位网页元素 点击
# element_keyword.send_keys('python')  #输入搜索字符
# element_search_button = driver.find_element_by_id('su').click()  #找到搜索按钮 点击

sleep(5) # 等待5秒
driver.quit()# 退出

# XPath定位：find_element_by_xpath()
from time import sleep
from selenium import webdriver

driver = webdriver.Chrome()  #指定chrom的驱动执行这次访问
driver.get('http://www.baidu.com')  #get 方法 打开指定网址
element_keyword = driver.find_element_by_xpath("//*[@id='kw']")  #定位网页元素 点击
element_keyword.send_keys('python')  #输入搜索字符
element_search_button = driver.find_element_by_id('su').click()  #找到搜索按钮 点击

sleep(5) # 等待
driver.quit()# 退出


# CSS定位  通过class、id 定位
from time import sleep
from selenium import webdriver

driver = webdriver.Chrome()  #指定chrom的驱动执行这次访问
driver.get('http://www.baidu.com')  #get 方法 打开指定网址
element_keyword = driver.find_element_by_css_selector('#kw')  #定位网页元素 点击
element_keyword.send_keys('python')  #输入搜索字符
element_search_button = driver.find_element_by_id('su').click()  #找到搜索按钮 点击

sleep(5) # 等待
driver.quit()# 退出

# CSS定位：find_element_by_css_selector()
# css相对xpath来说，语法更简洁、定位速度更快
from time import sleep
from selenium import webdriver

driver = webdriver.Chrome()  #指定chrom的驱动执行这次访问
driver.get('http://www.baidu.com')  #get 方法 打开指定网址
#class属性定位网页元素
element_keyword = driver.find_element_by_css_selector(".s_ipt")
#id属性定位网页元素
element_keyword = driver.find_element_by_css_selector("#kw")
#maxlength属性定位网页元素
element_keyword = driver.find_element_by_css_selector("input[maxlength='100']")
#autocomplete属性定位网页元素
element_keyword = driver.find_element_by_css_selector("input[autocomplete='off']")
#层级关系定位网页元素
element_keyword = driver.find_element_by_css_selector('form>span>input#kw')
#通过id和class组合定位定位网页元素 点击
element_keyword = driver.find_element_by_css_selector("input[id='kw'][class='s_ipt']")

element_keyword.send_keys('Selenium元素定位')  #输入搜索字符
#找到搜索按钮 点击
element_search_button = driver.find_element_by_id('su').click()
sleep(5) # 等待
driver.quit()# 退出

