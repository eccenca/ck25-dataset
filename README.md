<!-- markdownlint-disable MD012 MD013 MD024 MD033 -->
# The CK25 Corporate Knowledge Reference Dataset for Benchmarking Text 2 SPARQL Question Answering Approaches

Text to SPARQL is a task that aims to automatically generate SPARQL queries which retrieve answers from RDF-based Knowledge Graphs.
As pointed out in [Strappazon  et al.](https://hal.science/hal-04918564) ...

> ... the task of parsing natural language questions into structured queries is even more prevalent now, given the high potential that Large Language Models (LLMs) offer in Retrieval-Augmented conversational agents and the problems they face with using the correct information as context.

In order to support researchers of RAG-based systems with reference questions and queries for a Knowledge Graph with an industrial background, we provide this dataset repository, which was created for the [First International TEXT2SPARQL Challenge](https://text2sparql.aksw.org/), which we organized as part of the [4th International Workshop on LLM-Integrated Knowledge Graph Generation from Text (Text2KG)](https://aiisc.ai/text2kg2025) at the [22th European Semantic Web Conference (ESWC2025)](https://2025.eswc-conferences.org/).

## Important Files

- `questions.yml`
  - This YAML file is the curated list of 50 questions together with a working reference SAPRQL query
- `graphs/`
  - This directory contains Turtle files (one for the ontology, one for the instance data)
  - The `*.graph` files contain the named graph IRI we use

## How to use this repository?

In order to test your own Text to SPARQL approach, provide it as a TEXT2SPARQL endpoint as described [here](https://text2sparql.aksw.org/challenge/#process).
Then you can use the [text2sparql](https://pypi.org/project/text2sparql-client/) command line client like this:

``` shell-session
$ text2sparql ask questions.yml [YOUR ENDPOINT] --output result.json
2025-05-05 09:47:45.049 | INFO     | text2sparql_client.commands.ask:ask_command:72 - Asking questions about dataset https://text2sparql.aksw.org/2025/corporate/ on endpoint [YOUR ENDPOINT].
2025-05-05 09:47:45.049 | INFO     | text2sparql_client.commands.ask:ask_command:77 - In which department is Ms. Brant? (en) ...
2025-05-05 09:47:45.064 | INFO     | text2sparql_client.commands.ask:ask_command:77 - What is the telephone of Baldwin Dirksen? (en) ...
2025-05-05 09:47:45.069 | INFO     | text2sparql_client.commands.ask:ask_command:77 - Who is the manager of Heinrich Hoch? (en) ...
... more questions
2025-05-05 09:49:43.421 | INFO     | text2sparql_client.commands.ask:ask_command:100 - Writing 50 responses to result.json.
```

The new file result.json contains a structure like this:

``` JSON
[
  {
    "dataset": "https://text2sparql.aksw.org/2025/corporate/",
    "question": "In which department is Ms. Brant?",
    "query": "...",
    "endpoint": "[YOUR ENDPOINT]",
    "qname": "ck25:1-en",
    "uri": "https://text2sparql.aksw.org/2025/corporate/1-en"
  },
...
]
```

This file can be used with the same CLI for analysis:


``` shell-session
$ text2sparql evaluate API_NAME questions.yml result.json
```

