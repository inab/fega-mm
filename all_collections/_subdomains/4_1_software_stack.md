---
layout: default
title: "[4.1] Software stack"
parent: "4TI"
indicators:
 - indicator: '[4.1.1] Development Best practices'
   levels:
    - level: 1
      desc: 'No specific best practices looked at.'
    - level: 2
      desc: 'Identified best practices at the FEGA.'
    - level: 3  
      desc: 'Best practices implemented internally.'
    - level: 4
      desc: 'Adoption of common practices by the community.'
    - level: 5
      desc: 'Tracked and enforced adoption of common software development best practices.'

 - indicator: '[4.1.2] Interoperability with CEGA microservices implemented (e.g. permissions API, submission API)'
   connected:
    - ind: '3.2.3'
   levels:
    - level: 1
      desc: 'None.'
    - level: 2
      desc: 'Testing communication with a subset of the CEGA services.'
    - level: 3  
      desc: 'Implementation and successful performance of minimally required communication with CEGA microservices.'
    - level: 4
      desc: 'Mature production quality implementation of communication with CEGA microservices and full integration into FEGA node services according to FEGA committees.'
    - level: 5
      desc: 'Able to update as needed, for example in response to changes in community standards (e.g. GA4GH passports) in the framework of the FEGA ecosystem.'

 - indicator: '[4.1.3] Microservices/APIs specific for FEGA node operations implemented'
   connected:
    - ind: '3.2.2'
   levels:
    - level: 1
      desc: 'None.'
    - level: 2
      desc: 'Use cases considered, API specifications drafted, implementation in progress.'
    - level: 3  
      desc: 'Minimal set of APIs/microservices in production to support core FEGA node services. Additional APIs/microservices being developed/tested.'
    - level: 4
      desc: 'All FEGA node microservices/APIs in production with documented specifications. Services have generally high uptime.'
    - level: 5
      desc: 'Periodic assessment of APIs/microservices against user needs and feedback. Proposals made for new APIs/microservices or new features for existing APIs/microservices.'
---
