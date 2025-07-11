import { Model } from "clarifai-nodejs";

const model = new Model({
  url: "https://clarifai.com/openai/chat-completion/models/o4-mini",
  authConfig: {
    pat: process.env.CLARIFAI_PAT,
  },
});

const methodSignatures = await model.methodSignatures();

console.log(methodSignatures);