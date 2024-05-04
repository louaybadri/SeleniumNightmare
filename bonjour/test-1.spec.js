// Generated by Selenium IDE
const { Builder, By, Key, until } = require('selenium-webdriver')
const assert = require('assert')

const { describe, it, beforeEach, afterEach } = require('mocha')

describe('test1', function () {
  this.timeout(30000)
  let driver
  let vars

  beforeEach(async function () {
    driver = await new Builder().forBrowser('chrome').build()
    vars = {}
  })
  afterEach(async function () {
    await driver.quit();
  })
  it('test1', async function () {
    await driver.get("https://safatelli.github.io/tp-test-logiciel/assets/hello.html")
    await driver.manage().window().setRect({ width: 1534, height: 605 })
    await driver.findElement(By.id("username")).click()
    await driver.findElement(By.id("username")).sendKeys("Louay \\n")
    await driver.findElement(By.css("button")).click()
    assert.equal(await driver.findElement(By.id("message")).getText(), "Bonjour, Louay !")
    await driver.findElement(By.id("username")).click()
    await driver.findElement(By.id("username")).sendKeys("Badri \\n\\n\\n\\n\\n")
    await driver.findElement(By.css("button")).click()
    assert.equal(await driver.findElement(By.id("message")).getText(), "Bonjour, Badrsi !")
  })
})