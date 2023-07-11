---
layout: default
title: "[4.3] Storage System"
parent: "4TI"
indicators:
 - indicator: '[4.3.1] Storage Capacity'
   connected:
    - ind: '1.3.1'
    - ind: '1.3.2'
   levels:
    - level: 1
      desc: 'No storage capacity.'
    - level: 2
      desc: 'Storage capacity needs are not planned but it is addressed ad hoc if the node has no more storage to provide.'
    - level: 3  
      desc: 'A plan to maintain or increase storage capacity in case of being necessary is drafted considering the policies by the hosting institution.'
    - level: 4
      desc: 'The Federated EGA Node has a complete and implemented plan to maintain or increase its capacity when required.'
    - level: 5
      desc: "Periodic revision of the Storage Capacity Planning according to utilization KPI's of the Federated EGA Node updating it whenever necessary."

 - indicator: '[4.3.2] Storage Robustness'
   levels:
    - level: 1
      desc: 'Data is generated and stored locally only.'
    - level: 2
      desc: 'Data is stored in duplicate (locally and remotely), but there are no systems or guidelines in place to ensure service robustness.'
    - level: 3  
      desc: 'Node has a system to prevent data loss.'
    - level: 4
      desc: 'Node follow the FEGA guidelines for data storage, redundancy and access to avoid data loss.'
    - level: 5
      desc: 'Annual auditing and revision of the storage system is established to guarantee the alignment with the FEGA guidelines for data storage.'
---
