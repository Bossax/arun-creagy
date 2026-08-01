const fs = require("fs");
const path = require("path");
const { pathToFileURL } = require("url");
const { chromium } = require("playwright");

const [sourceArg = "layout_prototype.html", outputArg = "layout_prototype.png", selector = ".rollup"] = process.argv.slice(2);
const source = path.resolve(sourceArg);
const output = path.resolve(outputArg);

if (!fs.existsSync(source)) {
  throw new Error(`Prototype HTML not found: ${source}`);
}

(async () => {
  const browser = await chromium.launch({ headless: true });

  try {
    const page = await browser.newPage({
      viewport: { width: 1280, height: 3200 }, // set to fit stacked 16:9 slides (1280x2880px plus padding)
      deviceScaleFactor: 1,
    });

    await page.goto(pathToFileURL(source).href, { waitUntil: "load" });
    await page.locator(selector).screenshot({
      path: output,
      omitBackground: false,
    });

    console.log(`Rendered ${output}`);
  } finally {
    await browser.close();
  }
})();
