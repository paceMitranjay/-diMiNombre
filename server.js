const express = require("express");
const multer = require("multer");
const { spawn } = require("child_process");
const path = require("path");
const cors = require("cors");
const { stdout } = require("process");

const app = express();
const port = 3001;

app.use(cors());

const storage = multer.memoryStorage();
const upload = multer({ storage: storage });

app.post("/upload", upload.single("pdfFile"), (req, res) => {
  const pdfBuffer = req.file.buffer;

  const pdfFilePath = path.join(__dirname, "uploads", "uploaded.pdf");
  require("fs").writeFileSync(pdfFilePath, pdfBuffer);

  const childPy = spawn("python", [
    "extract_text.py",
    "./uploads/uploaded.pdf",
    "1906@1564",
  ]);
  let content = "";

  const getContentPromise = new Promise((resolve, reject) => {
    childPy.stdout.on("data", (data) => {
      // console.log(`stdout: ${data}`);
      content += data.toString();
    });

    childPy.stderr.on("data", (data) => {
      console.error(`stderr: ${data}`);
      reject(new Error(`Error in child process: ${data}`));
    });

    childPy.on("close", (code) => {
      console.log(`child process exited with code ${code}`);
      resolve(content);
    });
  });

  getContentPromise
    .then((parsedData) => {
      console.log("Content outside the block:", parsedData);

      res.json({ result: parsedData });
    })
    .catch((error) => {
      console.error(error.message);
    });
});

app.listen(port, () => {
  console.log(`Server is running on http://localhost:${port}`);
});
