---
layout: default
title: "[3.2] Incoming and outgoing data and metadata flow"
parent: "3DMM"
indicators:
 - indicator: '[3.2.1] Incoming Data flow in the FEGA node is established'
   connected:
    - ind: '1.2.1'
    - ind: '3.3.1'
    - ind: '3.3.2'
   levels:
    - level: 1
      desc: 'None.'
    - level: 2
      desc: 'First mechanisms for receiving and processing data submissions are designed.'
    - level: 3  
      desc: 'Ad-hoc incoming data flow into the FEGA node. This is a largely automated process.'
    - level: 4
      desc: 'Accept data only in formats agreed using standard data reception services in a more automated manner. Accepted formats follow the general agreement reached at the FEGA ecosystem.'
    - level: 5
      desc: 'Periodic review of existing incoming data mechanisms to guarantee up-to-date implementations and the opportunity to incorporate newly accepted data-types and developed data transfer protocols for accepted data-types.'

 - indicator: '[3.2.2] Outgoing Data flow in the FEGA node is established'
   levels:
    - level: 1
      desc: 'None.'
    - level: 2
      desc: 'First methods are drafted and proposed for the data distribution out of the FEGA node.'
    - level: 3  
      desc: 'Ad-hoc distribution of data out of the FEGA node to approved users using labour intensive protocols.'
    - level: 4
      desc: 'Data can flow out of node in a semi-automated or self-service way for approved users using secure protocols. Majority of data distribution scenarios agreed by the FEGA ecosystem are supported by the node.'
    - level: 5
      desc: 'Periodic review of existing data distribution mechanisms to guarantee up-to-date implementations and the opportunity to incorporate newly accepted data-types, developed data transfer protocols as well as to scale-up the service to cope with increasing use, including the use of standards for partial data retrieval.'

 - indicator: '[3.2.3] Mechanisms for sharing metadata and other operations-oriented information are established between the FEGA node and Central EGA'
   levels:
    - level: 1
      desc: 'None.'
    - level: 2
      desc: 'Information to be exchanged between the FEGA and Central EGA is drafted.'
    - level: 3  
      desc: 'Communication interfaces are well defined. Information, operations-oriented and public metadata, e.g. study metadata, accessions, can be exchanged between the FEGA node and Central EGA in a manual way.'
    - level: 4
      desc: 'Information, operations-oriented and public metadata, e.g. study metadata, accessions, is exchanged between the FEGA node and Central EGA in an automated or scheduled way.'
    - level: 5
      desc: 'Periodic review of exchange information to ensure up-to-date implementations as well as to facilitate the adoption of new standards and newly developed technologies. This periodic review can facilitate the redefinition of exchanged information.'
---
