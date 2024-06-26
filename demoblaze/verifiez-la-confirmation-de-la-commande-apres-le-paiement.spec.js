// Generated by Selenium IDE
const { Builder, By, Key, until } = require('selenium-webdriver')
const assert = require('assert')


const { describe, it, beforeEach, afterEach } = require('mocha')
describe('Vérifiez la confirmation de la commande après le paiement.   ', function () {
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
  it('Vérifiez la confirmation de la commande après le paiement.   ', async function () {
    await driver.get("https://www.demoblaze.com/")
    await driver.manage().window().setRect({ width: 1051, height: 797 })
    await driver.findElement(By.linkText("Samsung galaxy s6")).click()
    await driver.findElement(By.linkText("Add to cart")).click()
    assert(await driver.switchTo().alert().getText() == "Product added")
    await driver.findElement(By.id("cartur")).click()
    await driver.findElement(By.css(".btn-success")).click()
    await driver.findElement(By.id("name")).click()
    await driver.findElement(By.id("name")).click()
    await driver.findElement(By.id("name")).sendKeys("Leslie Holden")
    await driver.findElement(By.id("country")).sendKeys("Commodi esse quidem")
    await driver.findElement(By.id("city")).sendKeys("Voluptatem qui offic")
    await driver.findElement(By.id("card")).sendKeys("Perferendis reprehen")
    await driver.findElement(By.id("month")).sendKeys("8")
    await driver.findElement(By.id("year")).sendKeys("2004")
    await driver.findElement(By.css("#orderModal .btn-primary")).click()
    await driver.findElement(By.css(".form-group:nth-child(6)")).click()
    await driver.findElement(By.css("#orderModal .btn-primary")).click()
    await driver.findElement(By.css("h2:nth-child(6)")).click()
    assert.equal(await driver.findElement(By.css("h2:nth-child(6)")).getText(), "Thank you for your purchase!")
  })
})
