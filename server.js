const express = require("express");
const dotenv = require("dotenv");
dotenv.config();
const multer = require("multer");
const { spawn } = require("child_process");
const path = require("path");
const cors = require("cors");
const fs = require("fs");
const openai = require("./helper/openAI");
const bodyParser = require("body-parser");

const app = express();
app.use(bodyParser.json());
const port = 3001;

app.use(cors());
// app.use(express.urlencoded({ extended: true }));

const storage = multer.memoryStorage();
const upload = multer({ storage: storage });

app.post("/upload", upload.single("pdfFile"), async (req, res) => {
  const pdfBuffer = req.file.buffer;
  const pdfFilePath = path.join(__dirname, "uploads", "uploaded.pdf");
  fs.writeFileSync(pdfFilePath, pdfBuffer);
  const password = req.body.password;
  const query = req.body.query;

  const childPy = spawn("python", [
    "./pythonScripts/main.py",
    pdfFilePath, // PDF file path
    password,
    query,
  ]);

  let content = "";

  childPy.stdout.on("data", (data) => {
    content += data.toString();
  });

  childPy.stderr.on("data", (data) => {
    console.error(`stderr: ${data}`);
  });

  const pythonProcessClosed = new Promise((resolve, reject) => {
    childPy.on("close", (code) => {
      resolve(code);
    });
  });

  pythonProcessClosed.then(async (code) => {
    // Perform additional operations on the content here
    // console.log(content);
    // const ch = await openai(content, "");
    // Send the modified content as the response
    res.json({ result: content });
  });
});

app.post("/ai", async (req, res) => {
  const data = req.body.data;
  const prompt = req.body.prompt;

  // console.log("Prompt:", prompt);
  // Now you have the prompt data from the request body
  // Perform any additional processing or calls here
  const output = await openai(data, prompt); // Assuming openai is a function that returns a promise
  // console.log(output);
  res.json({ result: output }); // Sending back a dummy response for now
});

app.listen(port, () => {
  console.log(`Server is running on http://localhost:${port}`);
});
