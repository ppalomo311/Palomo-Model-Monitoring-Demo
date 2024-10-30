# Generating monitoring data

## Context

The aim of this demo is to show how Scenario evaluation data, collected over time, can be used to create a model monitoring dashboard. The dashboard should show the following as a minimum view inot model behaviour:

1. *Predicted confidence score distrobutions over time*  
Plan is to simulate a scenario where there is a drastic drop in the frequency of secrecy 
2. *ngram histogram over time*  
This might have to be restricted to positive ngrams only for visual purposes

As a stretch, it might be valuable to show how confidence score distrobutions change in response to a pipeline change (e.g. incorrect ngram range causes bi-grams to be dropped from the inference inputs).

## Methodology

To simulate a relevant business process for monitoring material behviour of the scenario model, we will leverage the secrecy test dataset. We will control the confidence score distribution by over and under-sampling the positive language of interest in the test set. When we over-sample positives, we expect the confidence score distribution to be skewed toward higher scores, while under-sampling will have the opposite effect.

### Temporal monitoring

In the business context we will use for the demo, the hypothetical client has built a dashboard that ingests Scenario evaluations, and visualises confidence score distrobutions, along with ngram histograms. Scenario evaluations are run manually, but can be automatically ingested by the dashboard app. We will visualise the distrobutions quarterly to give a termoral angle to the monitoring.

### Scenario Eval Data Model

Below is an example response from the Scenario eval API response:

```json
{
  "classifers": [
    {
      "id": 1,
      "name": "MODEL:smarsh-rumor-en:rumor-en-lr:1.2.0",
      "labels": ["politics","economics", "sports"]
    },
    {
      "id": 2,
      "name": "MODEL:smarsh-harassment-en:harassment-en-lr:1.4.0",
      "labels": ["positive","negative"]
    }
  ],
  "results": [
    {
      "recordIdentifier": "1.1",
      "sentence": "Or was Ms. Oliphant elected for life?",
      "classifiers": [
        {
          "id": 1,
          "confidence": [0.65, 0.3, 0.05]
        },
        {
          "id": 2,
          "confidence": [0.15, 0.85]
        }
      ]
    },
    {
      "recordIdentifier": "1.2",
      "sentence": "If you know",
      "classifiers": [
        {
          "id": 1,
          "confidence": [0.01, 0.02, 0.01]
        },
        {
          "id": 2,
          "confidence": [0.01, 0.99]
        }
      ]
    },
    {
      "recordIdentifier": "1.3",
      "sentence": "please reply to this e-mail and inform me about the process.",
      "classifiers": [
        {
          "id": 1,
          "confidence": [0.01,0.01,0.01]
        },
        {
          "id": 2,
          "confidence": [0.01,0.99]
        }
      ]
    },
    {
      "recordIdentifier": "1.3",
      "sentence": "thanks for the confirmation.",
      "classifiers": [
        {
          "id": 1,
          "confidence": [0.01,0.01,0.01]
        },
        {
          "id": 2,
          "confidence": [0.01, 0.99]
        }
      ]
    }
  ]
}
```



