# Federated EGA Maturity Model

Live version of the Federated EGA (European Genome-phenome Archive) Maturity model available at https://inab.github.io/fega-mm/

## Usage

This MM is based on a simple single page model.

### Create or Modify content

All content about Domains/Subdomains/Indicators is located at _all_collections_/_domains_ directory

#### Adding / Modifiying Domain

1. Add a new or modify an existing markdown file at _all_collection_ directory
   - This action show a new (or modify) item at the main accordion list

```
|-- all_collections
 |-- _domains
   |-- 1_governance_strategy_sustainability.md
   |-- 2_legal.md
   |-- 3_new_one.md
 |-- _subdomains
```

2. Ensure to keep the header between '---'
   - *layout*, *title* and *identifier* variables are mandatory
```md
---
layout: default
title: "[1] Governance, Strategy and Sustainability"
identifier: "1GSS"
---
```

#### Adding / Modifiying Subdomain

1. Add a new or modify an existing markdown file at _all_collection_/_subdomains_ directory
   - This action show a new (or modify) row under *domain* item at the main accordion

```
|-- all_collections
 |-- _domains
 |-- _subdomains
   |-- 1_1_governance_and_structure_of_the_federated_ega_node.md
   |-- 1_2_vision_and_strategy_of_the_federated_ega_node.md
   |-- 1_3_sustainability_model_of_the_federated_ega_node.md
   |-- 1_4_overarching_key_performance_indicators_kpis.md
   |-- 2_1_data_protection_policies_at_the_federated_ega_node.md
   |-- 2_2_new_one.md
```

2. Ensure to keep the header between '---'
   - *layout*, *title* and *parent* variables are mandatory

3. Ensure to keep spacing and the same tree structure for variables
```md
---
layout: default
title: "[1.1] Governance and structure of the Federated EGA node"
parent: "1GSS"
indicators:
 - indicator: '[1.1.1] Dedicated governance bodies and structure defined for the Federated EGA instance'
   levels:
    - level: 1
      desc: 'None existing'
    - level: 2
      desc: 'The team is assembled and proposed roles identified'
    - level: 3  
      desc: 'Overall governace body and node structure is defined, with stakeholder consultation, and formally approved including key roles, e.g. DPO'
    - level: 4
      desc: 'Governance body is fully operating with key personnel and is monitored based on work plan'
    - level: 5
      desc: 'Governance body is institutionalized, protected from organizational changes, open to novel developments and supportive of international cooperation'
---
```

### Pull Request (from the root folder):
- all_collections/_domains/<domain of interest>
- all_collections/_subdomains/<subdomain of interest>
- Create branches off of main branch, tag issue in commit statement (to close the issue automatically when PR is merged)


## Credits

- Theme is made with [jekyll](https://jekyllrb.com/).
- Look and Feel based on [B1MG project - MLM](https://b1mg-project.github.io/MLM/).

