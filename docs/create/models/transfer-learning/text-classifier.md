---
description: Learn how to use transfer learning to create custom text classifier models
sidebar_position: 1
toc_max_heading_level: 4
---

# Text Classifier

**Learn how to use transfer learning to create custom text classifier models**
<hr />

A text classifier is a machine learning model designed to categorize text data into predefined classes or labels.

Let's demonstrate how you can create a custom text classifier model using the [transfer learning](README.mdx) technique.


## **Via the UI**

Let's demonstrate how you can create a text classifier model that identifies whether an email message is a spam or not a spam. 

### Step 1: Create an App

[Click here](https://docs.clarifai.com/clarifai-basics/applications/create-an-application/#create-an-application-on-the-portal) to learn how to create an application on the Clarifai platform.

:::note

When creating the application, choose the Text/Document option as the primary input type.

:::

### Step 2: Create a Dataset

[Click here](https://docs.clarifai.com/portal-guide/datasets/create-get-update-delete/#create-a-new-dataset) to learn how to create a dataset that will store the text inputs. 

### Step 3: Add and Annotate Inputs

Next, you'll need to upload data to the app you've created. This input data, labeled with specific concepts, will be used to train your model. 

A concept is something that describes the content of your text input, similar to a "tag" or "keyword." The data in these concepts give the model something to "observe" about the keyword, and learn from.

For transfer learning, you can start with a small dataset. We recommend beginning with just 10 text inputs and gradually adding more as needed. 

In this example, we'll use 5 examples of spam messages and 5 examples of non-spam messages sourced from [this dataset](https://www.kaggle.com/datasets/datatattle/email-classification-nlp). You can download the dataset and follow along with this documentation.

To upload inputs, select the **Inputs** option in the collapsible left sidebar. Next, click the **Upload inputs** button.

![](/img/others/nav-to-explorer_1.png)

The small window that pops up allows you to upload your inputs.

You can use either of the following options to add text inputs to your app:

 - Upload from a `.csv` file
 - Add texts directly

#### Option 1: Upload From a `.csv` File

You can upload your text directly from a `.csv` file. This means you can work with your favorite spreadsheet software or text editor when preparing your data for upload. 

[Click here](https://docs.clarifai.com/portal-guide/advanced-topics/csv-and-tsv/) to learn how to upload your text data from a `.csv` file. 

#### Option 2: Add Texts Directly

Select the **Text** option in the input uploader window. Then, use the input field to add each of the text inputs directly to your app. 

For this illustration, let's use the second option. 

![](/img/others/text-upload-inputs-1.png)

- In the **Select or add datasets** search box, choose the dataset you previously created for storing your uploaded inputs.

- To label the inputs with the `non-spam` concept, click the plus (**+**) icon next to the **Select or add concepts** search box. Then, type the concept name in the search box. The new name will appear below the search box — click **Add new concept** to create it. The newly created concept will now be listed below the search box.

- To complete the process, click **Upload inputs** at the bottom of the pop-up window to upload your annotated input to the selected dataset. 

- Similarly, upload the examples of spam messages to the previously created dataset and label them with the `spam` concept.

![](/img/others/text-upload-inputs-2-2.png)

:::note

If you're adding text inputs directly, you'll need to repeat the process for each example message: select the dataset to which you want to add the input, choose the relevant concept, and then click the upload button.

:::

:::tip

[Click here](https://docs.clarifai.com/portal-guide/annotate/create-get-update-delete) to learn more about labeling inputs.

:::

### Step 4: Update Dataset

Next, navigate to your dataset's individual page and create a new version by clicking the **New version** button. This action bookmarks the current state of your dataset, allowing you to apply a specific version when training your custom text model.

![](/img/others/text-add-dataset.png)

### Step 5: Choose a Model Type

Once you've uploaded the example text messages containing the concepts you want to train for, you're ready to create your custom model.

Begin by selecting the **Models** option from the collapsible left sidebar. On the following page, click the **Add Model** button in the upper-right corner.

In the pop-up window, select **Build a Custom Model** and click **Continue** to proceed.

![](/img/others/text-model-mode.png)

You'll then be redirected to a page where you can choose the model type. In the **Text** section, select the **Transfer Learn** model type.

![](/img/others/select-model-type.png)

### Step 6: Create a Model

On the ensuing page, provide a unique ID and click the **Continue to Configure Model** button to create your model.

![](/img/others/text-create-model-2.png) 

### Step 7: Set Up the Model

Next, provide the details for training your text classification model.

![](/img/others/custom-transfer-text-model-1.png) 

- **Dataset selection** — Choose the dataset you want to use for training. For this example, let's select the dataset we previously created, along with its specific version.
- **Base embedding model** — You can select the base model version to use for embeddings, which has to be one of the embed models in the app workflow. This allows you to specify the specific model in case the default workflow of your app has multiple embedding models present in it. For this example, let's use the default option.
- **Define concepts** — Specify the concepts you want the model to classify. Here, let's use `spam` and `non-spam` as the two concepts.
- **Set concepts as mutually exclusive** — Enable this option to indicate that there is no overlap between the defined concepts.
- **Enrich dataset** — If set to `Automatic`, this feature will enhance the model by including additional data from pre-built datasets with negative embeddings, improving accuracy. If set to `Disabled`, it will exclude these embeddings. Let's use the default `Automatic` setting for this example.
- **Configure inference settings (optional)** — Adjust inference settings as needed for your model. This step is optional.

After configuring the settings, click on **Train Model** to start the training process. Training typically takes a few seconds.

### Step 8: Use Your Custom Model

You'll be redirected to the created model's page. Once the text classifier model is trained, you can put it to work, such as for making a [prediction](https://docs.clarifai.com/portal-guide/ppredict/).

To test it:

- Click the blue **(+)** button labeled "Try your own text."
- A window will appear where you can input a text sample.
- The model will display prediction probabilities, showing how it classifies the text input.


![](/img/others/custom-transfer-text-model-2.png) 


## **Via the API**

:::info

Before using the [Python SDK](https://docs.clarifai.com/additional-resources/api-overview/python-sdk), [Node.js SDK](https://docs.clarifai.com/additional-resources/api-overview/nodejs-sdk), or any of our [gRPC clients](https://docs.clarifai.com/additional-resources/api-overview/grpc-clients), ensure they are properly installed on your machine. Refer to their respective installation guides for instructions on how to install and initialize them.

:::

### Example 1

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';
import CodeBlock from "@theme/CodeBlock";


import CodeAC from "!!raw-loader!../../../../code_snippets/python-sdk/model_training/embedding_classifier/ac.py";
import CodeDU from "!!raw-loader!../../../../code_snippets/python-sdk/model_training/embedding_classifier/du.py";
import CodeMT from "!!raw-loader!../../../../code_snippets/python-sdk/model_training/embedding_classifier/mt.py";
import CodeMC from "!!raw-loader!../../../../code_snippets/python-sdk/model_training/embedding_classifier/mc.py";
import CodeS from "!!raw-loader!../../../../code_snippets/python-sdk/model_training/embedding_classifier/s.py";
import CodeIMT from "!!raw-loader!../../../../code_snippets/python-sdk/model_training/embedding_classifier/imt.py";
import CodeMP from "!!raw-loader!../../../../code_snippets/python-sdk/model_training/embedding_classifier/mp.py";
import CodeTrEv from "!!raw-loader!../../../../code_snippets/python-sdk/model_eval/embedding_classifier/train_eval.py";
import CodeTeEv from "!!raw-loader!../../../../code_snippets/python-sdk/model_eval/embedding_classifier/test_eval.py";
import CodeCMP from "!!raw-loader!../../../../code_snippets/python-sdk/model_eval/embedding_classifier/cmp.py";


import CodeOutputMT from "!!raw-loader!../../../../code_snippets/python-sdk/model_training/outputs/embedding_classifier/mt.txt";
import CodeOutputS from "!!raw-loader!../../../../code_snippets/python-sdk/model_training/outputs/embedding_classifier/s.txt";
import CodeOutputMP from "!!raw-loader!../../../../code_snippets/python-sdk/model_training/outputs/embedding_classifier/mp.txt";
import CodeOutputTrEv from "!!raw-loader!../../../../code_snippets/python-sdk/model_eval/embedding_classifier/outputs/train_eval.txt";
import CodeOutputTeEv from "!!raw-loader!../../../../code_snippets/python-sdk/model_eval/embedding_classifier/outputs/test_eval.txt";
import CodeOutputCMP from "!!raw-loader!../../../../code_snippets/python-sdk/model_eval/embedding_classifier/outputs/cmp.txt";


Let's demonstrate how you can create a text classifier model using our API. 

#### Step 1: App Creation

Let's start by creating an [app](https://docs.clarifai.com/create-manage/applications/create). 

<Tabs groupId="code">
<TabItem value="python" label="Python SDK">
    <CodeBlock className="language-python">{CodeAC}</CodeBlock>
</TabItem>
</Tabs>

#### Step 2: Dataset Upload

Next, let’s upload the [dataset](https://docs.clarifai.com/create-manage/datasets/upload) that will be used to train the model to the app.

You can find the dataset we used [here](https://github.com/Clarifai/examples/tree/main/datasets/upload/data).

<Tabs groupId="code">
<TabItem value="python" label="Python SDK">
    <CodeBlock className="language-python">{CodeDU}</CodeBlock>
</TabItem>
</Tabs>



#### Step 3: Model Creation

Let's list all the available trainable model types in the Clarifai platform. 

<Tabs groupId="code">
<TabItem value="python" label="Python SDK">
    <CodeBlock className="language-python">{CodeMT}</CodeBlock>
</TabItem>
</Tabs>
<details>
  <summary>Output</summary>
    <CodeBlock className="language-text">{CodeOutputMT}</CodeBlock>
</details>

Next, let's select the `embedding-classifier` model type and use it to create a model.  


<Tabs groupId="code">
<TabItem value="python" label="Python">
    <CodeBlock className="language-python">{CodeMC}</CodeBlock>
</TabItem>
</Tabs>


:::tip

[Click here](https://docs.clarifai.com/create-manage/models/deep-fine-tuning/clusterer#step-4-patch-model-optional) to learn how to patch your model. 

:::

#### Step 4: Set Up Model Parameters

You can customize the model parameters as needed before starting the training process.


<Tabs groupId="code">
<TabItem value="python" label="Python SDK">
    <CodeBlock className="language-python">{CodeS}</CodeBlock>
</TabItem>
</Tabs>
<details>
  <summary>Output</summary>
    <CodeBlock className="language-text">{CodeOutputS}</CodeBlock>
</details>

#### Step 5: Initiate Model Training

To initiate the model training process, call the `model.train()` method. The Clarifai API also provides features for monitoring training status and saving training logs to a local file.

:::note

If the training status code returns `MODEL-TRAINED`, it means the model has successfully completed training and is ready for use.

:::

<Tabs groupId="code">
<TabItem value="python" label="Python SDK">
    <CodeBlock className="language-python">{CodeIMT}</CodeBlock>
</TabItem>
</Tabs>




#### Step 6: Model Prediction

After the model is trained and ready to use, you can run some predictions with it.

<Tabs groupId="code">
<TabItem value="python" label="Python SDK">
    <CodeBlock className="language-python">{CodeMP}</CodeBlock>
</TabItem>
</Tabs>
<details>
  <summary>Output</summary>
    <CodeBlock className="language-text">{CodeOutputMP}</CodeBlock>
</details>


#### Step 7: Model Evaluation

Let’s evaluate the model using both the training and test datasets. We’ll start by reviewing the evaluation metrics for the training dataset.

<Tabs groupId="code">
<TabItem value="python" label="Python SDK">
    <CodeBlock className="language-python">{CodeTrEv}</CodeBlock>
</TabItem>
</Tabs>
<details>
  <summary>Output</summary>
    <CodeBlock className="language-text">{CodeOutputTrEv}</CodeBlock>
</details>

Before evaluating the model on the test dataset, ensure it is uploaded using the data loader. Once uploaded, proceed with the evaluation.

<Tabs groupId="code">
<TabItem value="python" label="Python SDK">
    <CodeBlock className="language-python">{CodeTeEv}</CodeBlock>
</TabItem>
</Tabs>
<details>
  <summary>Output</summary>
    <CodeBlock className="language-text">{CodeOutputTeEv}</CodeBlock>
</details>

Finally, to gain deeper insights into the model’s performance, use the `EvalResultCompare` method to compare results across multiple datasets.

<Tabs groupId="code">
<TabItem value="python" label="Python SDK">
    <CodeBlock className="language-python">{CodeCMP}</CodeBlock>
</TabItem>
</Tabs>
<details>
  <summary>Output</summary>
    <CodeBlock className="language-text">{CodeOutputCMP}</CodeBlock>
</details>

### Example 2

Let's demonstrate how you can create a custom text classifier using transfer learning. 

#### Step 1: App Creation

Let's start by creating an [app](https://docs.clarifai.com/create-manage/applications/create). 


<!--
![](https://s3.amazonaws.com/clarifai-api/img3/prod/large/e12ce254f2824b0ab2aef1b10784ff23/3e695b780f597cd263b06d0aeb30b3d1?v=001)
-->

<!--
Afterward, copy the newly-created application's _API key_ and set it in the variable below. This variable is going to be used by all Clarifai API calls for authorization purposes.
-->

import PythonAddBatchTexts from "!!raw-loader!../../../../code_snippets/api-guide/model/py/add_batch_texts.py";
import PythonWaitInputsDownload from "!!raw-loader!../../../../code_snippets/api-guide/model/py/wait_inputs_download.py";
import PythonCreateCustomModel from "!!raw-loader!../../../../code_snippets/api-guide/model/py/create_custom_text_model.py";
import PythonTrainTextModel from "!!raw-loader!../../../../code_snippets/api-guide/model/py/train_text_model.py";
import PythonWaitModelTraining from "!!raw-loader!../../../../code_snippets/api-guide/model/py/wait_model_training_complete.py";
import PythonPredictNewInputs from "!!raw-loader!../../../../code_snippets/api-guide/model/py/predict_new_inputs.py";
import PythonStartModelEvaluation from "!!raw-loader!../../../../code_snippets/api-guide/model/py/start_model_evaluation.py";
import PythonWaitModelEvaluationResults from "!!raw-loader!../../../../code_snippets/api-guide/model/py/wait_model_evaluation_results.py";

import OutputExample1 from "!!raw-loader!../../../../code_snippets/api-guide/model/code_output_examples/custom-text-model-walkthrough_1.js";
import OutputExample2 from "!!raw-loader!../../../../code_snippets/api-guide/model/code_output_examples/custom-text-model-walkthrough_2.js";

<!--
<Tabs groupId="code">
<TabItem value="grpc_python" label="gRPC Python">

```python
# Insert here the initialization code as outlined on this page:
# https://docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

api_key_metadata = (('authorization', 'Key ' + post_keys_response.keys[0].id),)
```
</TabItem>
</Tabs>
-->

#### Step 2: Add a Batch of Texts

We'll now add several text inputs that we will later use as training data in our custom model. The idea is that we'll create a model which can differentiate between positive and negative sentences \(in a grammatical sense\). 

We'll mark each input with one of the two concepts: `positive` or `negative`.

The texts can be added either directly \(it's called raw\) or from a URL.

<Tabs groupId="code">

<TabItem value="grpc_python" label="Python (gRPC)">
    <CodeBlock className="language-python">{PythonAddBatchTexts}</CodeBlock>
</TabItem>

</Tabs>

#### Step 3: Wait for Inputs to Download

Let's now wait for all the inputs to download.

<Tabs groupId="code">

<TabItem value="grpc_python" label="Python (gRPC)">
    <CodeBlock className="language-python">{PythonWaitInputsDownload}</CodeBlock>
</TabItem>

</Tabs>

#### Step 4: Create a Custom Model

Let's create a custom transfer learning model (also called an "embedding-classifier"). 

<Tabs groupId="code">

<TabItem value="grpc_python" label="Python (gRPC)">
    <CodeBlock className="language-python">{PythonCreateCustomModel}</CodeBlock>
</TabItem>

</Tabs>

#### Step 5: Train the Model

Let's train the model using the `positive` and `negative` concepts. 

All inputs \(in our application\) associated with these two concepts will be used as training data. This will make the model to learn from these inputs so that we can later predict new text examples. 

<Tabs groupId="code">

<TabItem value="grpc_python" label="Python (gRPC)">
    <CodeBlock className="language-python">{PythonTrainTextModel}</CodeBlock>
</TabItem>

</Tabs>

#### Step 6: Wait for Model Training to Complete

Let's wait for the model training to complete.

Each model training produces a new model version. Notice that on the bottom of the following code example, we placed the model version ID into its own variable.

We'll be using it later to specify which specific model version we want to use \(since a model can have multiple versions\).

<Tabs groupId="code">

<TabItem value="grpc_python" label="Python (gRPC)">
    <CodeBlock className="language-python">{PythonWaitModelTraining}</CodeBlock>
</TabItem>

</Tabs>

#### Step 7: Predict on New Inputs

Let's now use the trained custom model to predict new text examples.

<Tabs groupId="code">

<TabItem value="grpc_python" label="Python (gRPC)">
    <CodeBlock className="language-python">{PythonPredictNewInputs}</CodeBlock>
</TabItem>

</Tabs>

<details>
  <summary>Text Output Example</summary>

```text
The following concepts were predicted for the input `Butchart Gardens contains over 900 varieties of plants.`:
	positive: 0.83
	negative: 0.17
The following concepts were predicted for the input `https://samples.clarifai.com/negative_sentence_12.txt`:
	negative: 1.00
	positive: 0.00
```
</details>

#### Step 8: Start Model Evaluation

Let's now test the performance of the model by using model evaluation. Take note of the `evaluation_id` returned in the response, as you will need it for the next step. 

:::tip

See the [Evaluating Models](https://docs.clarifai.com/api-guide/evaluate/) section to learn more.

:::

<Tabs groupId="code">

<TabItem value="grpc_python" label="Python (gRPC)">
    <CodeBlock className="language-python">{PythonStartModelEvaluation}</CodeBlock>
</TabItem>

</Tabs>

<details>
  <summary>Raw Output Example</summary>
    <CodeBlock className="language-javascript">{OutputExample1}</CodeBlock>
</details>

#### Step 9: Wait for Model Evaluation Results

Model evaluation takes some time — depending on the amount of data the model has. 

Let's wait for it to complete, and print all the results that it gives us.

<Tabs groupId="code">

<TabItem value="grpc_python" label="Python (gRPC)">
    <CodeBlock className="language-python">{PythonWaitModelEvaluationResults}</CodeBlock>
</TabItem>

</Tabs>

<details>
  <summary>Raw Output Example</summary>
    <CodeBlock className="language-javascript">{OutputExample2}</CodeBlock>
</details>
