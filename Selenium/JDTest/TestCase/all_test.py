import unittest
import LoginJD
import ChArea
import HTMLTestRunner
import time
testunit = unittest.TestSuite()

testunit.addTest(unittest.makeSuite(LoginJD.Login))

testunit.addTest(unittest.makeSuite(ChArea.ChArea))

now = time.strftime('%Y-%m-%M-%H_%M_%S',time.localtime(time.time()))
fp = open('result' + '.html','wb')
runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title='Test Result',description='Result:')
runner.run(testunit)
fp.close()