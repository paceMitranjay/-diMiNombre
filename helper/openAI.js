// import OpenAI from "openai";
const OpenAI = require("openai");

const openai = new OpenAI({
  organization: process.env.OPENAPI_SPEC_PATH,
  apiKey: process.env.OPENAPI_API_KEY,
});

async function main(data, prompt) {
  // console.log("data", data);
  const completion = await openai.chat.completions.create({
    messages: [
      {
        role: "system",
        content: "You are my transaction analyser",
      },
      {
        role: "user",
        content: `currency rupees`,
      },
      {
        role: "user",
        content: `this is in string but I converted the .csv into string and it is a list of list ${data} `,
      },
      {
        role: "user",
        content: `${prompt}  `,
      },
      {
        role: "user",
        content: `give me a final answer only, I dont need any method `,
      },
      // {
      //   role: "user",
      //   content: `${query}`,
      // },
    ],
    model: "gpt-3.5-turbo-0125",
  });

  return completion.choices[0].message.content;
}

module.exports = main;
